# Kitty

Include the generated file from your existing `kitty.conf`:

```text
include /path/to/the-deliverator/ports/kitty/deliverator-signal.conf
```

Keep the previous theme include available so you can switch back. The file supplies the foreground/background, cursor, selection and ANSI 16 palette. Remove this include to restore your previous setup.

ANSI values are checked against the shared palette. Kitty parsing and visual acceptance have not been established by the Python checks.
