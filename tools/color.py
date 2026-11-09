"""Reproducible Deliverator Signal study. Standard Oklab matrices; no palette sampling.

Only the existing #171922 ground is fixed as an RGB input. All other colors
are generated from OKLCH coordinates and constrained to the sRGB gamut by
reducing chroma while preserving lightness and hue.
"""
from pathlib import Path
import json
import math

GROUND = '#171922'

def linear(v):
    return v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4

def encoded(v):
    return 12.92*v if v <= .0031308 else 1.055*v**(1/2.4)-.055

def rgb(value):
    return tuple(int(value[i:i+2],16)/255 for i in (1,3,5))

def to_oklch(value):
    r,g,b=map(linear,rgb(value))
    l=(.4122214708*r+.5363325363*g+.0514459929*b)**(1/3)
    m=(.2119034982*r+.6806995451*g+.1073969566*b)**(1/3)
    s=(.0883024619*r+.2817188376*g+.6299787005*b)**(1/3)
    L=.2104542553*l+.793617785*m-.0040720468*s
    a=1.9779984951*l-2.428592205*m+.4505937099*s
    b=.0259040371*l+.7827717662*m-.808675766*s
    return L,math.hypot(a,b),math.degrees(math.atan2(b,a))%360

def from_oklch(L,C,h):
    a=C*math.cos(math.radians(h));b=C*math.sin(math.radians(h))
    l=(L+.3963377774*a+.2158037573*b)**3
    m=(L-.1055613458*a-.0638541728*b)**3
    s=(L-.0894841775*a-1.291485548*b)**3
    return (4.0767416621*l-3.3077115913*m+.2309699292*s,
            -1.2684380046*l+2.6097574011*m-.3413193965*s,
            -.0041960863*l-.7034186147*m+1.707614701*s)

def generate(L,C,h):
    h%=360
    lo,hi=0.,C
    for _ in range(48):
        mid=(lo+hi)/2
        if all(0<=c<=1 for c in from_oklch(L,mid,h)):lo=mid
        else:hi=mid
    C=lo
    channels=[round(255*encoded(v)) for v in from_oklch(L,C,h)]
    assert all(0<=v<=255 for v in channels)
    return '#'+''.join(f'{v:02x}' for v in channels),C,h

def luminance(value):
    return sum(v*w for v,w in zip(map(linear,rgb(value)),(.2126,.7152,.0722)))

def contrast(a,b):
    lo,hi=sorted((luminance(a),luminance(b)))
    return (hi+.05)/(lo+.05)

def blend(a,b,fraction):
    return '#'+''.join(f'{round(255*(x*fraction+y*(1-fraction))):02x}' for x,y in zip(rgb(a),rgb(b)))

def build():
    L,C,h=to_oklch(GROUND)
    signal=(h-160)%360
    step=.045
    specs={
      'bg-alt':(L+step,C*(1-.08),h),
      'bg-hl':(L+2*step,C*(1-.08*2),h),
      'line':(L+4*step,C*(1-.08*4),h),
      'fg':(.935,.006,h),
      'muted':(.720,.018,h),
      'accent':(.880,.200,signal),
      'red':(.740,.170,signal-90),
      'orange':(.790,.155,signal-55),
      'yellow':(.860,.155,signal-20),
      'green':(.780,.160,signal+30),
      'cyan':(.800,.105,signal+90),
      'blue':(.760,.130,signal+150),
      'magenta':(.760,.130,signal+210)
    }
    colors={'bg':GROUND};records={}
    for role,(lightness,chroma,hue) in specs.items():
        value,mapped,hue=generate(lightness,chroma,hue)
        colors[role]=value
        records[role]={'hex':value,'L':lightness,'C_requested':chroma,'C_srgb':mapped,'h':hue}
    for role in ('fg','muted','accent','red','orange','yellow','green','cyan','blue','magenta'):
        records[role]['contrast_panel']=contrast(colors[role],colors['bg-alt'])
        assert records[role]['contrast_panel']>=4.5,(role,records[role])
    for role in ('accent','orange','cyan'):
        selected=blend(colors[role],GROUND,.17)
        assert contrast(colors[role],selected)>=4.5,(role,'pill contrast')
        row=blend(colors[role],colors['bg-alt'],.12)
        assert contrast(colors['fg'],row)>=7,(role,'selected row text')
    assert contrast(colors['bg'],colors['accent'])>=7
    token_ratios=[]
    for wash in ('accent','red','orange','yellow','green','cyan','blue','magenta'):
        row=blend(colors[wash],colors['bg-alt'],.05)
        token_background=blend(colors[wash],row,.13)
        for ink in ('fg','accent','orange','cyan'):
            token_ratios.append(contrast(colors[ink],token_background))
    assert min(token_ratios)>=4.5, min(token_ratios)
    document={
      'id':'deliverator-signal','name':'Deliverator · Signal study',
      'status':'candidate; yellow-green direction selected by Matt; full palette pending review',
      'ground':{'hex':GROUND,'L':L,'C':C,'h':h},
      'signal_hue':signal,'tokens':colors,'derivation':records,
      'semantic_roles':{'identity':'accent','focus':'accent','action':'blue','constructor':'accent','keyword':'magenta','function':'cyan','literal':'orange'},
      'minimum_selected_syntax_contrast':min(token_ratios),
      'method':'Oklab/OKLCH, chroma reduction at fixed L/h into sRGB, then 8-bit rounding; contrast measured after rounding.'
    }
    return document
