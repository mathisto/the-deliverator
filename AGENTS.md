# The Deliverator

This public repository owns the generative palette and application exports. Keep private paths, credentials and infrastructure configuration out of source, docs and screenshots.

For component/design work, start at `docs/agent-entry.md` and `docs/design-system.md`. The reusable workflow is maintained in `skills/deliverator-ui/SKILL.md`; its presence here is not evidence of a global installation.

The current Signal study is a candidate. Matt chose the blue-black ground and charged yellow-green direction; the complete palette has not been accepted as final. Do not claim a stable release, marketplace publication, installed application support, or a completed desktop migration without evidence.

`tools/color.py` is the source of truth. Change the recipe, run `python tools/build.py`, then `python tools/build.py --check` and `python -m unittest discover -s tests -v`. Never hand-edit generated palette, port, or swatch files. Keep import instructions beside ports. Clearly separate format validation, actual application loading, and subjective acceptance.

The public GitHub repository is `mathisto/the-deliverator`; Matt explicitly authorized creating and publishing it. Do not alter the portfolio, Unity HUD or HyperT configuration until Matt accepts the palette and requests or confirms that rollout.

UI icons use Phosphor exclusively; see `docs/icons.md`. Add glyphs to `ui/icon-map.json` and regenerate with `tools/build-icons.mjs`, never draw replacement paths or mix icon families. Regular for general UI, fill for media transport. Link destinations use the app-window symbol, not a diagonal arrow. Shared controls and segmented choices use the same radius token.

The restrained motion grammar is accepted and on by default. Read `docs/motion.md`; use shared motion tokens/rules instead of per-component timing inventions. Respect reduced motion, avoid layout movement and default bounce, and keep UI feedback separate from project simulations.

Typography is accepted: Iosevka Etoile headings, Iosevka Aile reading and controls, Iosevka Mono breadcrumbs and code. Read `docs/typography.md`; use the semantic role tokens and bundled font declarations. Do not silently replace these with JetBrains, Fira or another family.
