# Iconography

**Phosphor is Deliverator's icon family**, selected by Matt. Use SVG assets from the pinned `@phosphor-icons/core` package. No icon font download, CDN dependency, hand-drawn replacements or mixing in another UI icon family.

## Grammar

- Regular weight for general actions, materials, navigation and brands.
- Fill weight for play, pause and stop. The denser silhouette makes small transport actions readable.
- 24px general icons, 22px transport icons, within a minimum 44px target. Never shrink the hit area to the glyph.
- Inherit semantic foreground; transport and selected controls may use the action ink. Keep disabled actions visibly disabled.
- Use the app-window icon for opening a project. The adjacent link text names the destination; no diagonal launch arrows.
- Use GitHub's Phosphor logo for source links. Keep descriptive accessible names and hover titles on icon-only actions.
- Rounded choices use the same 8px control radius as buttons, inside a 12px group. Selection has a visible border as well as color. No square bottom-tab underline treatment.
- Game artwork, mathematical drawings, notation and simulations are content, not UI icons. Do not replace them with pictograms.

## Add an icon

Add its semantic name and upstream asset path to `ui/icon-map.json`, then run:

```sh
npm run check
npm run build
npm run build-storybook
```

`tools/build-icons.mjs` creates `ui/icons.generated.ts` and `dist/icons.svg`, plus the MIT license. Do not edit generated glyphs. Only the named subset goes into the consumer bundle. `iconMarkup(name)` returns trusted, bundled SVG; never pass arbitrary user SVG to the renderer. Unknown names fail instead of silently drawing the wrong action.

The sprite includes compatibility aliases for the old portfolio. For example `arrow-up-right` now resolves to the app-window glyph; new markup uses `open-project`. Aliases can be removed once all consumers migrate. The existing engine adapter uses `setAction` to change play/pause/stop without replacing the focused button.

## Selection

We considered [Lucide](https://lucide.dev/license) (ISC) and [Tabler](https://github.com/tabler/tabler-icons) (MIT). Both are viable families. [Phosphor](https://github.com/phosphor-icons/core) was chosen for its broader expressive range, regular and filled variants within one family, and Matt's explicit preference. Its [MIT license](https://github.com/phosphor-icons/core/blob/main/LICENSE) permits personal and commercial use with the notice retained. The installed package and generated consumer sprite include that notice.
