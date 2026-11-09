# Neovim

Preview colorscheme; Neovim 0.9+. Core syntax, basic Tree-sitter/LSP groups, UI, diagnostics and ANSI colors are included. This is not a claim of complete plugin coverage.

From a checkout, add `ports/neovim` to your runtime path before selecting it:

```lua
vim.opt.rtp:append('/path/to/the-deliverator/ports/neovim')
vim.cmd('colorscheme deliverator-signal')
```

With lazy.nvim:

```lua
{
  'mathisto/the-deliverator',
  lazy = false,
  priority = 1000,
  config = function(plugin)
    vim.opt.rtp:append(plugin.dir .. '/ports/neovim')
    vim.cmd('colorscheme deliverator-signal')
  end,
}
```

Remove that configuration or select another colorscheme to switch back. CI has an isolated headless load check; consult its current result. Visual acceptance and plugin-specific checks remain open.
