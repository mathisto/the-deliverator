from pathlib import Path
import hashlib
import importlib.util
import json
import plistlib
import re
import sys
import tomllib
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import build as generator
import color

class ExportTests(unittest.TestCase):
    def setUp(self):
        self.doc=color.build();self.c=self.doc['tokens']

    def test_recipe_and_measured_contrast(self):
        self.assertEqual(self.c['bg'],'#171922')
        self.assertEqual(self.c['accent'],'#d5e500')
        self.assertEqual(len(self.c),14)
        self.assertGreaterEqual(self.doc['minimum_selected_syntax_contrast'],4.5)
        for record in self.doc['derivation'].values():
            if 'contrast_panel' in record:self.assertGreaterEqual(record['contrast_panel'],4.5)
            self.assertLessEqual(record['C_srgb'],record['C_requested']+1e-12)

    def test_deterministic_generation_and_committed_artifacts(self):
        self.assertEqual(generator.outputs(),generator.outputs())
        for name,data in generator.outputs().items():self.assertEqual((ROOT/name).read_bytes(),data,name)

    def test_manifest_covers_generated_files(self):
        manifest=json.loads((ROOT/'palette/manifest.json').read_text())['files']
        expected=set(generator.outputs())-{'palette/manifest.json'}
        self.assertEqual(set(manifest),expected)
        for name,digest in manifest.items():self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest)

    def test_json_and_toml_formats(self):
        for path in list((ROOT/'palette').glob('*.json'))+list((ROOT/'ports').rglob('*.json')):json.loads(path.read_text(encoding='utf-8'))
        for path in list((ROOT/'palette').glob('*.toml'))+list((ROOT/'ports').rglob('*.toml')):tomllib.loads(path.read_text(encoding='utf-8'))
        portable=tomllib.loads((ROOT/'palette/signal.toml').read_text())['colors']
        self.assertEqual(len(portable),13)
        for role,value in portable.items():self.assertEqual(value,self.c[role.replace('_','-')])

    def test_vscode_workbench_and_contribution(self):
        base=ROOT/'ports/vscode';manifest=json.loads((base/'package.json').read_text(encoding='utf-8'))
        item=manifest['contributes']['themes'][0];theme=json.loads((base/item['path']).read_text(encoding='utf-8'))
        self.assertEqual(theme['colors']['editor.background'],self.c['bg'])
        self.assertEqual(theme['colors']['editorCursor.foreground'],self.c['accent'])
        self.assertEqual(theme['semanticTokenColors']['function'],self.c['cyan'])
        self.assertEqual(theme['semanticTokenColors']['keyword'],self.c[self.doc['semantic_roles']['keyword']])
        self.assertTrue(theme['semanticHighlighting'])
        for value in theme['colors'].values():self.assertRegex(value,r'^#[0-9a-f]{6}([0-9a-f]{2})?$')

    def test_textmate_and_bat_are_identical_valid_plists(self):
        textmate=(ROOT/'ports/textmate/Deliverator-Signal.tmTheme').read_bytes()
        self.assertEqual(textmate,(ROOT/'ports/bat/Deliverator-Signal.tmTheme').read_bytes())
        data=plistlib.loads(textmate)
        self.assertEqual(data['settings'][0]['settings']['background'],self.c['bg'])
        self.assertEqual(len(data['settings']),12)

    def test_ansi_consistency_across_terminals(self):
        ansi=json.loads((ROOT/'palette/ansi.json').read_text())
        wt=json.loads((ROOT/'ports/windows-terminal/deliverator-signal.json').read_text(encoding='utf-8'))
        al=tomllib.loads((ROOT/'ports/alacritty/deliverator-signal.toml').read_text())['colors']
        wez=tomllib.loads((ROOT/'ports/wezterm/deliverator-signal.toml').read_text(encoding='utf-8'))['colors']
        self.assertEqual(len(ansi['ansi']),16)
        for k,v in ansi['normal'].items():self.assertEqual(wt[k],v);self.assertEqual(al['normal'][k],v)
        for k,v in ansi['bright'].items():self.assertEqual(wt['bright'+k.title()],v);self.assertEqual(al['bright'][k],v)
        self.assertEqual(wez['ansi']+wez['brights'],ansi['ansi'])
        kitty=(ROOT/'ports/kitty/deliverator-signal.conf').read_text()
        for i,v in enumerate(ansi['ansi']):self.assertIn('color'+str(i)+' '+v,kitty)

    def test_neovim_has_core_diagnostics_and_ansi(self):
        lua=(ROOT/'ports/neovim/colors/deliverator-signal.lua').read_text()
        for name in ['Normal','Keyword','Function','String','DiagnosticError','DiagnosticWarn','@function.call']:
            self.assertIn('nvim_set_hl(0, '+json.dumps(name),lua)
        for i in range(16):self.assertIn('terminal_color_'+str(i)+' = ',lua)

    def test_svg_specimens_are_valid_and_have_no_remote_dependencies(self):
        for path in (ROOT/'assets').glob('*.svg'):
            root=ET.parse(path).getroot();self.assertIn('svg',root.tag)
            self.assertNotIn('href=',path.read_text())

if __name__=='__main__':unittest.main()
