# Typography

Matt selected this recipe from the real-project workbench and supplied a screenshot confirming all five roles.

| Role | Family | Token |
| --- | --- | --- |
| Headings | Iosevka Etoile | `--dv-heading-font` |
| Body / reading | Iosevka Aile | `--dv-reading-font` |
| Breadcrumbs / small metadata | Iosevka Mono | `--dv-breadcrumb-font` |
| Code / technical readouts | Iosevka Mono | `--dv-code` |
| Controls | Iosevka Aile | `--dv-font` |

All five use the regular face. The accepted reference has 18px reading text, 16px control labels and 24px exhibit headings. These are semantic roles, not permission to force project content such as music notation or game artwork into the UI typeface. Keep the established palette and Phosphor family; restrained motion is on by default under `docs/motion.md`.

Load `ui/fonts.css` with the tokens and controls. Its relative font URLs require `assets/fonts` alongside `ui`; bundled consumers resolve those URLs at build time. The reference implementation self-hosts upstream Iosevka v34.9.1 WOFF2 files unchanged. `assets/fonts/iosevka-source.json` records provenance and hashes; keep `LICENSE-IOSEVKA.md` with redistributed fonts. These are full glyph-set reference assets, not a claim of a final production font-download budget.

Fira, JetBrains and DM Sans remain comparison options in the private/local workbench. They are not alternative defaults. New components inherit the roles instead of hard-coding a family.

Acceptance is for the shared library and its consumers. Existing applications migrate deliberately; no production deployment or desktop-font installation is implied.
