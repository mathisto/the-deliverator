# Deliverator design system

Build Matt Kelly's first-party interfaces from a shared vocabulary, with the real work providing the character. The system should make projects recognizably related without making a piano, a game reconstruction and a language experiment look interchangeable.

## What is settled

- [Typography](typography.md): Etoile headings; Aile reading and controls; Iosevka Mono breadcrumbs and code.
- [Icons](icons.md): Phosphor, regular for general UI and filled media transport. App-window symbols replace diagonal launch arrows.
- [Motion](motion.md): restrained feedback on by default, with reduced-motion support.
- [Component contracts](components.md): existing controls and exhibit composition, native semantics, 44px minimum targets, shared rounded control geometry.

Matt has accepted the current Signal appearance for first-party web UI and requested rollout. Editor and terminal port loading remains independently verified. Generated colors remain owned by the palette recipe. The package is still an unpublished reference implementation, not a finished UI framework.

## How to use it

1. Read the product's own brief and distinguish its UI from its artifacts. Preserve original game art, notation, mathematical drawings and real application engines.
2. Compose existing components. Use semantic roles for color, type, motion and geometry rather than independently recreating the look.
3. When a needed component is missing, develop it here with its behavior, states and catalogue example, then consume it. Use native behavior or an established behavior library for complex interactions.
4. Build the consumer from a pinned library revision. Preserve asset paths and licenses; avoid independently maintained CSS copies. The local portfolio bridge records copied-asset hashes as an intermediate integration.
5. Check the actual interaction, keyboard path, narrow layout and motion preferences. A screenshot of an idle control is not enough evidence for a working component.

[Usage semantics](semantics.md) and [voice](voice.md) are working guidance for review. They consolidate the current direction; they do not authorize rewriting every project or replacing an explicit product brief.

## Next components, in order

| Component / pattern | Problem it solves | First consumer |
| --- | --- | --- |
| Project-header actions and action links | One clear route to the full project and source, consistently named and placed | Workshop exhibits |
| Code study | Shared syntax roles, source captions, active-code treatment, bounded scrolling and readable results | Lisp and Stone Rose |
| Field and native select | Consistent label, help/error, disabled and invalid states; no custom dropdown mechanics by default | Typography workbench |
| Status and fallback region | Real loading, unavailable, empty, error and retry behavior without dead controls or invented activity | WASM previews |
| Gallery / project peek | Consistent selection, captions and destination, while preserving each project's artwork | SCRAPLIGHT and Carmen |

Also establish spacing/density and responsive composition tokens from these actual consumers. Do not create a hundred speculative primitives or a React/Rails adapter before a real consumer needs it.

## Agent entry and enforcement

Use [agent-entry.md](agent-entry.md) as the small entry point and the repo-owned [Deliverator skill](../skills/deliverator-ui/SKILL.md) for the workflow. Keep the detailed decisions here. An agent's global instructions should point here rather than repeat the design system.

Instructions express intent; implementation provides stronger consistency. The next enforcement step is a pinned package/asset dependency, catalogue cases for component states, and consumer checks for missing or stale assets. Do not claim automatic brand compliance from an installed skill alone. CI should target owned UI, with explicit boundaries for game rendering, syntax illustrations and other project artifacts.

The portfolio is the first test bench. Keep adoption incremental and record which consumers have migrated; publishing the library, changing repository visibility, deploying the site and applying desktop themes remain separate actions.
