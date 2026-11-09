# WezTerm

Add the scheme directory and select its metadata name in your existing Lua configuration:

```lua
config.color_scheme_dirs = {
  '/path/to/the-deliverator/ports/wezterm',
}
config.color_scheme = 'The Deliverator — Signal study'
```

Merge the directory with existing scheme directories instead of replacing them. Restore the previous `color_scheme` and directory list to switch back.

The TOML and all 16 ANSI values are checked against the shared palette. Full WezTerm loading and visual acceptance remain open.
