# The Deliverator

This public repository owns the generative palette and application exports. Keep private paths, credentials and infrastructure configuration out of source, docs and screenshots.

The current Signal study is a candidate. Matt chose the blue-black ground and charged yellow-green direction; the complete palette has not been accepted as final. Do not claim a stable release, marketplace publication, installed application support, or a completed desktop migration without evidence.

`tools/color.py` is the source of truth. Change the recipe, run `python tools/build.py`, then `python tools/build.py --check` and `python -m unittest discover -s tests -v`. Never hand-edit generated palette, port, or swatch files. Keep import instructions beside ports. Clearly separate format validation, actual application loading, and subjective acceptance.

The public GitHub repository is `mathisto/the-deliverator`; Matt explicitly authorized creating and publishing it. Do not alter the portfolio, Unity HUD or HyperT configuration until Matt accepts the palette and requests or confirms that rollout.

UI icons use Phosphor exclusively; see `docs/icons.md`. Add glyphs to `ui/icon-map.json` and regenerate with `tools/build-icons.mjs`, never draw replacement paths or mix icon families. Regular for general UI, fill for media transport. Link destinations use the app-window symbol, not a diagonal arrow. Shared controls and segmented choices use the same radius token.
