"""Generate all ports from the recipe. Python 3.11+, standard library only."""
from pathlib import Path
import argparse
import hashlib
import html
import json
import plistlib
import uuid

from color import build, generate, to_oklch

ROOT=Path(__file__).resolve().parents[1]
NAME='The Deliverator — Signal study'
SLUG='deliverator-signal'

def json_text(value):return json.dumps(value,indent=2,ensure_ascii=False)+'\n'

def outputs():
    doc=build();c=doc['tokens'];out={};keyword=c[doc['semantic_roles']['keyword']]
    out['palette/signal.json']=json_text(doc)
    out['palette/signal.css']='/* Generated: Signal study, not a stable release. */\n:root{'+''.join('--'+k+':'+v+';' for k,v in c.items())+'}\n'
    out['palette/signal.toml']='family = "The Deliverator"\nvariant = "Signal study"\n\n[colors]\n'+'\n'.join(f'{k.replace("-","_")} = "{v}"' for k,v in c.items() if k!='line')+'\n'

    normal={k:c[k] for k in ('red','green','yellow','blue','magenta','cyan')}
    normal={'black':c['bg-hl'],**normal,'white':c['fg']}
    bright={}
    for k,v in normal.items():
        if k=='black':bright[k]=c['muted']
        elif k=='white':bright[k]=generate(.98,.003,doc['ground']['h'])[0]
        else:
            L,C,h=to_oklch(v);bright[k]=generate(min(.95,L+.07),C*.88,h)[0]
    ansi_names=('black','red','green','yellow','blue','magenta','cyan','white')
    ansi=[normal[k] for k in ansi_names]+[bright[k] for k in ansi_names]
    out['palette/ansi.json']=json_text({'name':NAME,'normal':normal,'bright':bright,'ansi':ansi,'method':'Bright inks: OKLCH L + 0.07, C * 0.88, fixed h, gamut mapped. Black uses muted; white uses L=.98 C=.003.'})

    scopes=[
      ('Comments','comment',c['muted']),
      ('Keywords','keyword, storage.type, storage.modifier',keyword),
      ('Functions','entity.name.function, support.function',c['cyan']),
      ('Strings','string, constant.other.symbol',c['orange']),
      ('Numbers and constants','constant.numeric, constant.language',c['yellow']),
      ('Types','entity.name.type, support.type, support.class',c['blue']),
      ('Variables','variable',c['fg']),
      ('Punctuation','punctuation',c['muted']),
      ('Errors','invalid',c['red']),
      ('Inserted','markup.inserted',c['green']),
      ('Deleted','markup.deleted',c['red'])]
    token_colors=[{'name':name,'scope':scope,'settings':{'foreground':color}} for name,scope,color in scopes]
    ui={
      'focusBorder':c['accent'],'foreground':c['fg'],'descriptionForeground':c['muted'],
      'editor.background':c['bg'],'editor.foreground':c['fg'],
      'editorCursor.foreground':c['accent'],'editor.selectionBackground':c['accent']+'33',
      'editor.inactiveSelectionBackground':c['bg-hl'],'editor.lineHighlightBackground':c['bg-alt'],
      'editorLineNumber.foreground':c['muted'],'editorLineNumber.activeForeground':c['accent'],
      'editorIndentGuide.background1':c['line'],'editorIndentGuide.activeBackground1':c['muted'],
      'sideBar.background':c['bg-alt'],'sideBar.foreground':c['fg'],
      'activityBar.background':c['bg'],'activityBar.foreground':c['accent'],
      'statusBar.background':c['bg-alt'],'statusBar.foreground':c['fg'],
      'titleBar.activeBackground':c['bg-alt'],'titleBar.activeForeground':c['fg'],
      'tab.activeBackground':c['bg'],'tab.activeForeground':c['fg'],
      'tab.inactiveBackground':c['bg-alt'],'tab.inactiveForeground':c['muted'],
      'panel.background':c['bg'],'panel.border':c['line'],
      'input.background':c['bg-alt'],'input.foreground':c['fg'],'input.border':c['line'],
      'button.background':c['accent'],'button.foreground':c['bg'],
      'list.activeSelectionBackground':c['bg-hl'],'list.activeSelectionForeground':c['fg'],
      'list.hoverBackground':c['bg-alt'],
      'terminal.background':c['bg'],'terminal.foreground':c['fg'],
      'editorError.foreground':c['red'],'editorWarning.foreground':c['yellow'],
      'editorInfo.foreground':c['cyan'],'editorHint.foreground':c['green']}
    for k,v in normal.items():ui['terminal.ansi'+k.title()]=v
    for k,v in bright.items():ui['terminal.ansiBright'+k.title()]=v
    theme={'name':NAME,'type':'dark','semanticHighlighting':True,'colors':ui,
      'tokenColors':token_colors,'semanticTokenColors':{
        'keyword':keyword,'function':c['cyan'],'method':c['cyan'],
        'type':c['blue'],'class':c['blue'],'variable':c['fg'],
        'parameter':c['fg'],'property':c['fg'],'string':c['orange'],
        'number':c['yellow'],'comment':c['muted']}}
    out['ports/vscode/themes/deliverator-signal-color-theme.json']=json_text(theme)
    out['ports/vscode/package.json']=json_text({
      'name':'the-deliverator','displayName':'The Deliverator — Signal study',
      'description':'A blue-black and charged yellow-green theme. Preview palette; not a stable release.',
      'version':'0.1.0-dev','publisher':'mathisto','engines':{'vscode':'^1.85.0'},
      'categories':['Themes'],'license':'MIT',
      'repository':{'type':'git','url':'https://github.com/mathisto/the-deliverator.git'},
      'contributes':{'themes':[{'label':NAME,'uiTheme':'vs-dark','path':'./themes/deliverator-signal-color-theme.json'}]}})

    tm={'name':NAME,'uuid':str(uuid.uuid5(uuid.NAMESPACE_URL,'https://github.com/mathisto/the-deliverator/'+SLUG)).upper(),
      'settings':[{'settings':{'background':c['bg'],'foreground':c['fg'],
        'caret':c['accent'],'selection':c['accent']+'33','lineHighlight':c['bg-alt'],
        'gutter':c['bg-alt'],'gutterForeground':c['muted'],'invisibles':c['line']}}]+token_colors}
    theme_bytes=plistlib.dumps(tm,fmt=plistlib.FMT_XML,sort_keys=False)
    out['ports/textmate/Deliverator-Signal.tmTheme']=theme_bytes
    out['ports/bat/Deliverator-Signal.tmTheme']=theme_bytes

    groups={
      'Normal':{'fg':c['fg'],'bg':c['bg']},'NormalFloat':{'fg':c['fg'],'bg':c['bg-alt']},
      'FloatBorder':{'fg':c['line'],'bg':c['bg-alt']},'Comment':{'fg':c['muted']},
      'Constant':{'fg':c['yellow']},'String':{'fg':c['orange']},'Character':{'fg':c['orange']},
      'Number':{'fg':c['yellow']},'Boolean':{'fg':c['yellow']},'Identifier':{'fg':c['fg']},
      'Function':{'fg':c['cyan']},'Statement':{'fg':keyword},'Keyword':{'fg':keyword},
      'Conditional':{'fg':keyword},'Repeat':{'fg':keyword},'Operator':{'fg':c['cyan']},
      'PreProc':{'fg':keyword},'Type':{'fg':c['blue']},'Special':{'fg':c['cyan']},
      'Delimiter':{'fg':c['muted']},'Error':{'fg':c['red']},'Todo':{'fg':c['bg'],'bg':c['accent'],'bold':True},
      'LineNr':{'fg':c['muted']},'CursorLineNr':{'fg':c['accent']},'CursorLine':{'bg':c['bg-alt']},
      'ColorColumn':{'bg':c['bg-alt']},'Visual':{'bg':c['bg-hl']},
      'Search':{'fg':c['bg'],'bg':c['yellow']},'IncSearch':{'fg':c['bg'],'bg':c['accent']},
      'StatusLine':{'fg':c['fg'],'bg':c['bg-alt']},'StatusLineNC':{'fg':c['muted'],'bg':c['bg-alt']},
      'Pmenu':{'fg':c['fg'],'bg':c['bg-alt']},'PmenuSel':{'fg':c['bg'],'bg':c['accent']},
      'WinSeparator':{'fg':c['line']},'SignColumn':{'bg':c['bg']},'EndOfBuffer':{'fg':c['line']},
      'DiffAdd':{'fg':c['green']},'DiffChange':{'fg':c['yellow']},'DiffDelete':{'fg':c['red']},
      'DiagnosticError':{'fg':c['red']},'DiagnosticWarn':{'fg':c['yellow']},
      'DiagnosticInfo':{'fg':c['cyan']},'DiagnosticHint':{'fg':c['green']},
      '@keyword':{'link':'Keyword'},'@function':{'link':'Function'},'@function.call':{'link':'Function'},
      '@variable':{'link':'Identifier'},'@string':{'link':'String'},'@type':{'link':'Type'},
      '@number':{'link':'Number'},'@comment':{'link':'Comment'},
      '@lsp.type.function':{'link':'Function'},'@lsp.type.method':{'link':'Function'},
      '@lsp.type.class':{'link':'Type'},'@lsp.type.parameter':{'link':'Identifier'}}
    lua=['-- Generated Signal study. Requires Neovim 0.9+.','vim.cmd("highlight clear")',
      'vim.o.background = "dark"','vim.o.termguicolors = true','vim.g.colors_name = "deliverator-signal"']
    for name,settings in groups.items():
        fields=', '.join(k+' = '+('true' if v is True else json.dumps(v)) for k,v in settings.items())
        lua.append('vim.api.nvim_set_hl(0, '+json.dumps(name)+', { '+fields+' })')
    for i,v in enumerate(ansi):lua.append('vim.g.terminal_color_'+str(i)+' = '+json.dumps(v))
    out['ports/neovim/colors/deliverator-signal.lua']='\n'.join(lua)+'\n'

    wt={'name':NAME,'background':c['bg'],'foreground':c['fg'],'cursorColor':c['accent'],'selectionBackground':c['bg-hl']}
    wt.update(normal);wt.update({'bright'+k.title():v for k,v in bright.items()})
    out['ports/windows-terminal/deliverator-signal.json']=json_text(wt)
    al=['# Generated Signal study. Import as an Alacritty color configuration.','[colors.primary]',f'background = "{c["bg"]}"',f'foreground = "{c["fg"]}"','\n[colors.cursor]',f'text = "{c["bg"]}"',f'cursor = "{c["accent"]}"','\n[colors.selection]',f'text = "{c["fg"]}"',f'background = "{c["bg-hl"]}"']
    for name,palette in [('normal',normal),('bright',bright)]:
        al.append('\n[colors.'+name+']');al.extend(k+' = "'+v+'"' for k,v in palette.items())
    out['ports/alacritty/deliverator-signal.toml']='\n'.join(al)+'\n'
    kitty=[f'background {c["bg"]}',f'foreground {c["fg"]}',f'cursor {c["accent"]}',f'cursor_text_color {c["bg"]}',f'selection_background {c["bg-hl"]}',f'selection_foreground {c["fg"]}']
    kitty.extend('color'+str(i)+' '+v for i,v in enumerate(ansi))
    out['ports/kitty/deliverator-signal.conf']='# Generated Signal study.\n'+'\n'.join(kitty)+'\n'
    out['ports/wezterm/deliverator-signal.toml']='[colors]\nforeground = "'+c['fg']+'"\nbackground = "'+c['bg']+'"\ncursor_bg = "'+c['accent']+'"\ncursor_fg = "'+c['bg']+'"\ncursor_border = "'+c['accent']+'"\nselection_bg = "'+c['bg-hl']+'"\nselection_fg = "'+c['fg']+'"\nansi = '+json.dumps([normal[k] for k in ansi_names])+'\nbrights = '+json.dumps([bright[k] for k in ansi_names])+'\n\n[metadata]\nname = "'+NAME+'"\nauthor = "Matt Kelly"\n'

    swatches=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title desc">',
      '<title id="title">The Deliverator — Signal study palette</title>',
      '<desc id="desc">Generated color roles on the retained blue-black ground. Candidate palette, not a stable release.</desc>',
      f'<rect width="1200" height="360" fill="{c["bg"]}"/>']
    for i,(name,value) in enumerate(c.items()):
        x=30+(i%7)*167;y=28+(i//7)*168
        swatches.append(f'<rect x="{x}" y="{y}" width="145" height="88" rx="5" fill="{value}"/>')
        swatches.append(f'<text x="{x}" y="{y+112}" font-family="monospace" font-size="16" fill="{c["fg"]}">{html.escape(name)}</text>')
        swatches.append(f'<text x="{x}" y="{y+137}" font-family="monospace" font-size="14" fill="{c["muted"]}">{value.upper()}</text>')
    swatches.append('</svg>');out['assets/palette.svg']='\n'.join(swatches)+'\n'
    # A restrained type specimen, not an invented mascot or faux screenshot.
    out['assets/header.svg']=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="The Deliverator. Blue-black. Charged signal. Signal study.">
<rect width="1200" height="300" fill="{c['bg']}"/>
<rect x="36" y="36" width="1128" height="3" fill="{c['accent']}"/>
<text x="36" y="150" font-family="sans-serif" font-size="78" font-weight="500" letter-spacing="-2" fill="{c['fg']}">The Deliverator.</text>
<text x="39" y="218" font-family="sans-serif" font-size="25" fill="{c['accent']}">Blue-black. Charged signal.</text>
<text x="1163" y="266" text-anchor="end" font-family="monospace" font-size="14" fill="{c['muted']}">SIGNAL STUDY / PREVIEW</text>
</svg>\n'''
    serialized={k:(v if isinstance(v,bytes) else v.encode('utf-8')) for k,v in out.items()}
    serialized['palette/manifest.json']=json_text({'status':'preview','files':{k:hashlib.sha256(v).hexdigest() for k,v in sorted(serialized.items())}}).encode()
    return serialized

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    expected=outputs();drift=[]
    for name,data in expected.items():
        path=ROOT/name
        if args.check:
            if not path.is_file() or path.read_bytes()!=data:drift.append(name)
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    if drift:raise SystemExit('Regenerate stale files:\n'+'\n'.join(drift))
    print(('Verified' if args.check else 'Generated')+' '+str(len(expected))+' deterministic files.')

if __name__=='__main__':main()
