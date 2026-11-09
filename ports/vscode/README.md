# VS Code

This folder is a preview theme extension, not a Marketplace listing. The `publisher` string is a local extension namespace, not a claim of registered Marketplace publication.

From the repository root, open an isolated development host:

```sh
code --extensionDevelopmentPath="$(pwd)/ports/vscode"
```

On PowerShell:

```powershell
code --extensionDevelopmentPath="$PWD/ports/vscode"
```

In that window, run **Preferences: Color Theme** and select **The Deliverator — Signal study**. UI, TextMate syntax and semantic-token mappings are supplied. Close the development host to leave the preview; no extension needs to be installed in your normal profile.

The manifest, theme contribution path and data formats are checked. Full VS Code visual acceptance, VSIX packaging and Marketplace publication remain open.
