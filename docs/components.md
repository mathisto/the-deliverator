# Deliverator components — reference slice

Status: accepted identity for first-party web UI; experimental component API and unpublished package. This is a growing working library, not a complete component catalogue.

## Use established foundations

Lit 3 implements the Web Components. Native HTML implements button activation, range keyboard behavior and focus. Storybook 10 with Vite hosts the catalogue. No Bootstrap styles, copied component framework, custom slider mechanics or homegrown focus manager.

The custom part is the visual grammar: semantic roles, spacing, state treatment and the way controls compose with a live artifact. React Aria is a candidate for complex React interactions when an actual React consumer needs them. Rails ViewComponent can render server-side compositions later. Neither adapter is needed to validate these native web controls.

Do not build dialogs, focus traps, autocomplete, drag-and-drop or accessible menus from scratch. Choose a maintained behavior library for that consumer when the requirement exists. Do not introduce a second headless library for the same interaction.

## Run

```sh
npm ci
npm run check
npm run build
npm run storybook
```

Catalogue: `http://127.0.0.1:6010`. `npm run build-storybook` produces a static catalogue. Only the small `dist/deliverator.js` bundle goes to consumers; Storybook is development tooling. The package is deliberately private/unpublished while its API is experimental.

Load generated `palette/signal.css`, `ui/tokens.css`, `ui/controls.css`, optional `ui/fonts.css`, then the built module. Production consumers should pin an explicit library revision and use build-generated assets, not fetch mutable source from GitHub.

## Components

| Component | Contract | Application responsibility |
| --- | --- | --- |
| `dv-button` | `label`, `variant="quiet\|primary"`, `disabled`, `control-id`, optional `icon` | Handle the native button click; supply a truthful state label. |
| `dv-icon-button` | Required `label` and `icon`; native button with name, title and 44px target | Supply action-specific labels, including changes such as Pause → Resume. |
| `dv-choice-group` | `label`, `value`, `options: {value,label,icon?}[]`, `disabled`, optional `icon-only`; emits bubbling `dv-change` with `detail.value` | Apply the selection to application state; set `value` for external state changes. |
| `dv-range` | `label`, `value`, `min`, `max`, `step`, `format="percent\|number"`, `disabled`, `control-id` | Handle native `input`; choose the domain and units. Percent displays value × 100. |
| `dv-toolbar` | Required `label`; wrapping native control group | Group related controls. This is not an ARIA toolbar and does not add arrow navigation. |
| `dv-exhibit` | Required `heading`; `stage`, `context` and optional `heading` slots. `source-url` and optional `source-label` create the shared top-right GitHub action. Omit source properties when no public source is available, including closed-source products | Supply the actual project, explanation and destination. Do not duplicate the same preview on both sides. |

Iconography follows the [Phosphor contract](icons.md). Add new glyphs through the shared subset manifest; do not author another SVG path or mix icon families. The catalogue includes an Icons story.

```js
import './deliverator.js';
const views = document.querySelector('dv-choice-group');
views.options = [
  { value: 'sheet', label: 'Sheet' },
  { value: 'both', label: 'Both' },
  { value: 'falling', label: 'Notes' }
];
views.value = 'both';
views.addEventListener('dv-change', event => app.setView(event.detail.value));
```

## Ownership and accessibility

Component implementations own markup, styles and UI state. Consumers own engine state. The controls render in light DOM so native labels, ordinary event listeners and existing engine integrations work without a framework adapter. `nativeControl` exposes the actual button/input after `updateComplete`; do not depend on incidental descendants. The first portfolio bridge uses this escape hatch while the old engines still own their control state. New integrations should update component properties.

The accepted [motion grammar](motion.md) is on by default through `ui/controls.css`. Consumers copying the CSS directly must keep `ui/motion.css` beside it; bundled consumers resolve the import at build time. Use its shared timing and travel tokens for new components.

These are not form-associated custom elements yet: use the internal native control deliberately if needed; do not assume setting a custom-element `name` creates a submitted value. Action buttons always use `type="button"`. Choice groups use independently focusable native toggle buttons, not custom radios or a roving Tab model. `aria-pressed` carries selection; a rounded border, surface and color reinforce it. A visible label is mandatory. Icon-only actions are not the default for unfamiliar choices.

`--dv-control-edge` is stronger than the decorative `--dv-rule`. Signal denotes focus, selection and primary action; it is not success/warning. CSS is scoped to library elements/classes and never resets consumer piano keys, canvases or game UI. Components inherit semantic tokens. Future palette adapters map those aliases once rather than adding per-component theme branches.

The accepted [typography recipe](typography.md) has independent heading, reading, breadcrumb, code and control roles. Use their semantic tokens and load `ui/fonts.css`; do not hard-code font families in individual components. The workbench can still exercise alternatives without changing the accepted defaults.

## Additions and review

1. Identify a repeated intent in real consumers. Keep project-specific simulation out of the library.
2. Reuse a native primitive or maintained behavior library. Write down any additional keyboard contract.
3. Add component states and a real composition to the catalogue.
4. Exercise keyboard, touch sizing, disabled states, long content and narrow layouts.
5. Validate in the portfolio test bench before migrating production.

Next candidates: project-header actions, source links, code viewport/syntax roles, gallery controls, status/fallback region and the palette menu. These are an inventory, not implemented components. Preserve themed artifacts such as the Fallout terminal and Stone Rose study within the shared exhibit boundary.

## Test bench boundary

MattKelly.io builds an ignored local page with `scripts/build_deliverator_testbench.py --library ../the-deliverator`. It copies the exact built library and records its hashes. Tallboy and PixelSim run their existing engines behind replacement host controls; Page to Hand uses an isolated copy of its already-built browser preview. Its proprietary source and analysis engine do not belong in this repository. The test bench is excluded from the portfolio release packager.

Sources: [Lit](https://lit.dev/docs/), [Storybook Web Components + Vite](https://storybook.js.org/docs/get-started/frameworks/web-components-vite), [React Aria](https://react-aria.adobe.com/), [ViewComponent](https://viewcomponent.org/).

## Existing applications

[Consumer integration](adoption.md) describes the revision-pinned web export and the native-markup adapter. Use the adapter to preserve existing behavior during migration, then replace repeated UI with first-class components as each real interaction is validated. The adapter is a bridge, not evidence that an application is fully migrated.

Exhibit headings do not need a separator rule. Project-title links use the shared app-window icon and no persistent underline. Source actions are owned by `dv-exhibit`, not manually repeated inside the heading slot. Do not link a private repository as though it were publicly available.
