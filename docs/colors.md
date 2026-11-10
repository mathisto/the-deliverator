# Color reference

Generated from the canonical Signal RGB tokens. Copyable CSS forms below; the README includes swatches. HSL and OKLCH are computed from the final gamut-mapped RGB exports, not the requested recipe coordinates. Contrast is WCAG relative luminance against `bg`; it is not a claim that every color is suitable for text.

| Role | Hex | RGB | HSL | OKLCH | Contrast / ground |
| --- | --- | --- | --- | --- | --- |
| `bg` | `#171922` | `rgb(23 25 34)` | `hsl(229.09 19.30% 11.18%)` | `oklch(21.55% 0.0180 275.01)` | 1.00:1 |
| `bg-alt` | `#22242C` | `rgb(34 36 44)` | `hsl(228.00 12.82% 15.29%)` | `oklch(26.17% 0.0152 274.24)` | 1.13:1 |
| `bg-hl` | `#2D2F37` | `rgb(45 47 55)` | `hsl(228.00 10.00% 19.61%)` | `oklch(30.65% 0.0146 274.40)` | 1.31:1 |
| `line` | `#44464D` | `rgb(68 70 77)` | `hsl(226.67 6.21% 28.43%)` | `oklch(39.49% 0.0120 273.11)` | 1.86:1 |
| `fg` | `#E8E9EE` | `rgb(232 233 238)` | `hsl(230.00 15.00% 92.16%)` | `oklch(93.47% 0.0068 277.16)` | 14.45:1 |
| `muted` | `#A1A4B0` | `rgb(161 164 176)` | `hsl(228.00 8.67% 66.08%)` | `oklch(72.01% 0.0176 274.72)` | 7.05:1 |
| `accent` | `#D5E500` | `rgb(213 229 0)` | `hsl(64.19 100.00% 44.90%)` | `oklch(87.97% 0.1990 114.78)` | 12.55:1 |
| `red` | `#FF7E77` | `rgb(255 126 119)` | `hsl(3.09 100.00% 73.33%)` | `oklch(73.97% 0.1585 24.83)` | 7.09:1 |
| `orange` | `#FFA14C` | `rgb(255 161 76)` | `hsl(28.49 100.00% 64.90%)` | `oklch(78.93% 0.1488 59.83)` | 8.72:1 |
| `yellow` | `#F1CF44` | `rgb(241 207 68)` | `hsl(48.21 86.07% 60.59%)` | `oklch(85.99% 0.1549 94.90)` | 11.47:1 |
| `green` | `#6ED274` | `rgb(110 210 116)` | `hsl(123.60 52.63% 62.75%)` | `oklch(78.06% 0.1608 145.05)` | 9.29:1 |
| `cyan` | `#5ED1DE` | `rgb(94 209 222)` | `hsl(186.09 65.98% 61.96%)` | `oklch(79.95% 0.1049 205.39)` | 9.72:1 |
| `blue` | `#8BAFFF` | `rgb(139 175 255)` | `hsl(221.38 100.00% 77.25%)` | `oklch(75.96% 0.1223 265.13)` | 8.07:1 |
| `magenta` | `#DB93DE` | `rgb(219 147 222)` | `hsl(297.60 53.19% 72.35%)` | `oklch(75.97% 0.1303 325.39)` | 7.71:1 |

Use semantic aliases for UI. Ground, panels and decorative rules are not text inks. Keep the CSS, JSON and application ports generated from `tools/color.py`.
