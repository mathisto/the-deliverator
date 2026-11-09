# Alacritty

Import this file from your current Alacritty TOML configuration. For current Alacritty versions:

```toml
[general]
import = ["/path/to/the-deliverator/ports/alacritty/deliverator-signal.toml"]
```

Merge this path into an existing import list rather than replacing other imports. Older Alacritty versions may place `import` at the top level; follow the documentation for your version. Remove the import to switch back.

TOML, normal and bright ANSI maps, selection and cursor values are generated and format-checked. Application rendering remains an acceptance task.
