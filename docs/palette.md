# The Signal recipe

The palette source is [`tools/color.py`](../tools/color.py). The complete coordinates, requested and mapped chroma, hex values and contrast measurements are in [`palette/signal.json`](../palette/signal.json).

## The authored decision

Keep the exact blue-black ground **#171922**. Give the system one urgent yellow-green signature instead of making a whole pastel spectrum compete for attention. Most of the interface remains quiet, low-chroma material.

This is a design interpretation of the charcoal uniform, engineered protection, electrical equipment, speed and courier work in the novel’s opening. The yellow-green is our choice, not a claim about a canonical color named in the book. [Primary-text excerpt](https://chnm.gmu.edu/exploring/20thcentury/consumerism/pop_stephenson1.html).

## The derivation

Use [Oklab and its cylindrical OKLCH representation](https://bottosson.github.io/posts/oklab/), also defined in [CSS Color 4](https://www.w3.org/TR/css-color-4/#ok-lab).

```text
retained ground = #171922
OKLCH ground   = (0.2155431614, 0.0179811372, 275.0149674663°)
signal hue     = (ground hue - 180° + 20°) mod 360°
               = 115.0149674663°
signal request = OKLCH(0.88, 0.20, signal hue)
sRGB result    = #D5E500
```

Neutral levels use a step of 0.045 in lightness. For level n, `L = L_ground + n*0.045`, `C = C_ground*(1 - 0.08*n)`, and hue stays fixed. Panel uses n=1, highlight n=2, divider n=4.

Supporting hue offsets from the signal are red -90°, orange -55°, yellow -20°, green +30°, cyan +90°, blue +150°, and magenta +210°. Each role has a deliberate lightness and chroma budget. The exact values live in the recipe, rather than scattered hex constants in each application.

At each requested L and h, binary search reduces chroma until all three linear-sRGB channels fit 0–1. The generator then encodes sRGB and rounds once to 8-bit channels. This avoids per-channel clipping that can shift hue. The method is a simple reproducible gamut constraint, not a claim to implement CSS’s complete gamut-mapping algorithm.

## Contrast and hierarchy

The current ten text/status inks exceed 6.2:1 on the panel. The three principal selected pills and the checked highlighted-code combinations meet 4.5:1; body ink on selected rows exceeds 7:1. Contrast is measured from final rounded values. These results do not certify arbitrary foreground/background combinations or a whole application’s accessibility.

Signal now marks identity, focus and the narrow construction role: the Lisp consumer uses it for `cons` and its pill. Action buttons use blue. Generic keywords and quotation remain magenta, ordinary functions cyan, and literals amber-orange. The source JSON records separate `action` and `constructor` roles so a bright identity accent does not automatically become a button fill. No desktop installation is implied by these preview mappings.

ANSI bright inks use `L + 0.07`, `C * 0.88`, and the same hue, followed by the same gamut constraint. Bright black is the muted ink; bright white uses L=.98 and C=.003. The normal ANSI palette preserves the system’s semantic ink colors, so some tools may show a subtler normal/bright distinction than older terminal themes.

No color space proves that a design is beautiful, and no claim is made that every generated hex is unused elsewhere. Originality lies in this system’s decisions and relationships.
