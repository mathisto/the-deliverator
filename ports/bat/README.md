# bat

bat reads tmTheme files. Its theme name comes from the filename, so select **Deliverator-Signal**.

From the repository root on a POSIX shell:

```sh
mkdir -p "$(bat --config-dir)/themes"
cp ports/bat/Deliverator-Signal.tmTheme "$(bat --config-dir)/themes/"
bat cache --build
bat --theme=Deliverator-Signal path/to/a/file
```

PowerShell:

```powershell
$themeDirectory = Join-Path (bat --config-dir) 'themes'
New-Item -ItemType Directory -Force -Path $themeDirectory | Out-Null
Copy-Item -LiteralPath 'ports/bat/Deliverator-Signal.tmTheme' -Destination $themeDirectory
bat cache --build
bat --theme=Deliverator-Signal path/to/a/file
```

Some Linux packages call the binary `batcat`. The per-command `--theme` option is a reversible preview. To remove the imported theme, remove only this tmTheme file and rebuild bat’s cache. Do not delete an existing configuration directory.

The plist is format-checked. CI also imports and renders it with bat; consult the current run for runtime evidence.
