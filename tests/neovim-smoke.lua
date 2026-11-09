local ok, err = pcall(function()
  vim.opt.rtp:append('ports/neovim')
  vim.cmd('colorscheme deliverator-signal')
  local palette = vim.fn.json_decode(table.concat(vim.fn.readfile('palette/signal.json'), '\n')).tokens
  assert(vim.g.colors_name == 'deliverator-signal')
  local normal = vim.api.nvim_get_hl(0, { name = 'Normal' })
  assert(normal.bg == tonumber(palette.bg:sub(2), 16))
  local keyword = vim.api.nvim_get_hl(0, { name = 'Keyword' })
  assert(keyword.fg == tonumber(palette.accent:sub(2), 16))
  assert(vim.g.terminal_color_0 and vim.g.terminal_color_15)
end)
if not ok then
  vim.api.nvim_err_writeln(tostring(err))
  vim.cmd('cquit 1')
else
  print('Deliverator Neovim smoke test passed')
  vim.cmd('qa!')
end
