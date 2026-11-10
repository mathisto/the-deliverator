# Consumer integration

Build once, export a self-contained runtime, then integrate it in the consumer's source build. Do not load mutable library source from GitHub at runtime.

```sh
npm ci
npm run check
npm run build
python tools/export_web.py --output /path/to/app/public/deliverator
```

The export includes the palette, role tokens, licensed fonts, controls, module, icon sprite and a manifest of file hashes and the source Git revision. Commit the library before exporting a release so the revision identifies the actual input.

```html
<link rel="stylesheet" href="/deliverator/deliverator.css">
<script type="module" src="/deliverator/dist/deliverator.js"></script>
```

Compose `dv-exhibit`, `dv-toolbar` and the documented controls in new UI. Keep engine state in the application. A projected `heading` slot supports a real project-title link and source action; the `heading` property remains its accessible name and fallback.

## Preserve existing behavior

For an existing React, Svelte or native HTML application, opt in with `data-deliverator` on the document root and additionally load `ui/application.css` and `ui/application.js`. The adapter adds the shared button class without replacing controls, changing handlers or dispatching actions. It observes newly inserted buttons as well.

Mark an original notation, keyboard or artwork region `data-dv-preserve` before applying the adapter. Palette aliases belong in a small consumer stylesheet; map them to existing semantic roles without circular variables. Retain functional theme choices and original project artifacts.

The native adapter does not convert application icons, complex interactions or all layouts into components. Inventory these separately. Use only the pinned Phosphor sprite for owned interface icons; never replace scientific diagrams or game art with UI icons.

## Verify the consumer

- Build from its source and run the checks relevant to the changed UI.
- Exercise the actual controls and engine, including dynamic labels and selection.
- Inspect desktop and narrow layouts, visible focus and reduced motion.
- Record source integration, build, browser review and deployment as separate states.

Avoid publishing private application source, deployment details or proprietary engines as part of a shared runtime export.
