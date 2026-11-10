# Unity / Hyper+T

The generated `deliverator.toml` maps the canonical palette to Unity's thirteen supported color roles. The decorative web `line` role has no desktop equivalent.

Copy this file to `themes/palettes/deliverator.toml` in your Unity checkout, then refresh its installed theme catalogue using Unity's runtime catalogue generator. Hyper+T reads that catalogue and its generated preview; copying a TOML alone does not refresh an already-installed picker.

Updating the catalogue does not apply the theme. Select **The Deliverator** in Hyper+T and press Enter when you want to switch. Existing wallpaper images are separate assets and are not automatically recolored.

The November 10, 2026 Windows refresh verified all thirteen installed roles against this export while preserving the active theme. Other desktop surfaces and editor ports require their own application checks.
