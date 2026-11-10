"""Copyable color reference derived from the same RGB tokens used by every port."""
from pathlib import Path
import colorsys
import re
import color


def outputs(doc, root):
    tokens=doc['tokens']; out={}; rows=[]; detailed=[]
    for role,hex_value in tokens.items():
        r,g,b=(int(hex_value[i:i+2],16) for i in (1,3,5))
        L,C,h=color.to_oklch(hex_value)
        H,l,s=colorsys.rgb_to_hls(r/255,g/255,b/255)
        ratio=color.contrast(hex_value,tokens['bg'])
        oklch=f'{L*100:.2f}% {C:.4f} {h:.2f}'
        chip=f'assets/color-chips/{role}.svg'
        out[chip]=f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><rect x="1" y="1" width="22" height="22" rx="3" fill="{hex_value}" stroke="{tokens["muted"]}" stroke-width="1"/></svg>\n'
        rows.append(f'| <img src="{chip}" width="18" height="18" alt=""> `{role}` | `{hex_value.upper()}` | `{r}, {g}, {b}` | `{oklch}` | {ratio:.2f}:1 |')
        detailed.append(f'| `{role}` | `{hex_value.upper()}` | `rgb({r} {g} {b})` | `hsl({H*360:.2f} {s*100:.2f}% {l*100:.2f}%)` | `oklch({oklch})` | {ratio:.2f}:1 |')
    table='| Role | Hex | RGB · 0–255 | OKLCH · L C h | Contrast / ground |\n| --- | --- | --- | --- | --- |\n'+'\n'.join(rows)
    readme=(root/'README.md').read_text(encoding='utf-8')
    start='<!-- colors:start -->';end='<!-- colors:end -->'
    if start not in readme or end not in readme:raise ValueError('README color-reference markers missing')
    out['README.md']=readme.split(start)[0]+start+'\n'+table+'\n'+end+readme.split(end,1)[1]
    out['docs/colors.md']='# Color reference\n\nGenerated from the canonical Signal RGB tokens. Copyable CSS forms below; the README includes swatches. HSL and OKLCH are computed from the final gamut-mapped RGB exports, not the requested recipe coordinates. Contrast is WCAG relative luminance against `bg`; it is not a claim that every color is suitable for text.\n\n| Role | Hex | RGB | HSL | OKLCH | Contrast / ground |\n| --- | --- | --- | --- | --- | --- |\n'+'\n'.join(detailed)+'\n\nUse semantic aliases for UI. Ground, panels and decorative rules are not text inks. Keep the CSS, JSON and application ports generated from `tools/color.py`.\n'
    return out
