# Make a port

1. Start with the semantic roles from `tools/color.py`, not a copied list of hex values. State the target application and supported format/version.
2. Add a generator in `tools/build.py`. Generated files must have stable paths, stable identifiers and deterministic contents. Do not include timestamps or machine paths.
3. Include UI, syntax, selection, cursor and diagnostics where the application exposes them. Map ANSI roles consistently; do not silently equate the UI signal with terminal yellow or green.
4. Add `ports/<application>/README.md` with import steps and rollback/removal guidance. State whether validation is structural, a smoke test, or visual acceptance.
5. Add format or cross-export assertions, regenerate, run the checks, then load it in the actual application when available. Keep subjective visual acceptance distinct from parsing success.

The 13-role TOML is a portable interchange file, not a promise that every application accepts it. The web system adds a 14th divider role. An adapter must explicitly map those roles to the application’s own schema.

Never edit generated files by hand. Palette refinements should update every port in the same change. Keep the candidate/stable status visible in documentation and package metadata.
