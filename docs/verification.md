# What has been verified

The local Python checks cover deterministic generation, manifest hashes, JSON/XML-plist/TOML parsing, role agreement across exports, the VS Code contribution path, Neovim group coverage, and measured palette contrast after rounding.

The CI workflow also loads the colorscheme in an isolated Neovim session and imports/renders the tmTheme in bat. Check the [actual workflow result](https://github.com/mathisto/the-deliverator/actions) before treating a particular revision as runtime-verified. Neither application smoke check establishes broad plugin coverage or visual acceptance.

The Lisp preview has been inspected in Chromium at desktop, 390px and 320px widths, with working semantic selections and timed playback. It is an actual consumer of the palette, not a simulated editor screenshot.

VS Code, TextMate, Windows Terminal, Alacritty, Kitty and WezTerm exports are format-checked preview files. Their full UI rendering and platform-specific installation remain an acceptance queue. No marketplace publication, automatic installation, or deployment to a personal desktop is claimed.

All exports use sRGB values. Different displays, terminal contrast features, font rendering, OS color management and application backgrounds can change the result. Palette checks do not certify every application combination.
