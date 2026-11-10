# Motion grammar

Matt accepted the restrained type-study motion as Deliverator's default. This applies to shared components and future consumers; it is not a claim that every existing project has been migrated.

## Feedback, continuity, restraint

| Interaction | Default |
| --- | --- |
| Fine-pointer hover | 1px lift, slight offset shadow, existing hover ink/surface |
| Press, including keyboard | 1px depression and .985 compression; 100ms response |
| Surface / selection change | 150ms color and border continuity; state updates immediately |
| Ink / range feedback | 120ms color response |
| Exhibit focus boundary | 180ms border transition; the card itself stays stationary |

Use the tokens in `ui/tokens.css` and rules in `ui/motion.css`, imported by shared controls. Do not duplicate timing values in individual components. New UI should use the same feedback vocabulary before inventing a new effect. Motion must not delay activation, shift page layout, move labels around, or compete with the real project demonstration.

No default bounce, elastic settling, cursor attraction, perspective tilt, scroll reveals, page-load choreography or perpetual UI loops. A new expressive moment needs a specific purpose and review; adding one to every component defeats the grammar.

Coarse-pointer devices receive press feedback without synthetic hover. `prefers-reduced-motion: reduce` removes spatial movement and shadows, retains brief color feedback, and stops exhibit transitions. An explicit `data-motion="off"` on the document removes the shared feedback motion entirely. The portfolio workbench exposes that switch for comparison. Neither mechanism changes an application's renderer, game or practice-engine state; those keep their own lifecycle and pause controls.

The accepted reference is the local type study's restrained response. [Carbon](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview) provides the productive-motion model, and [WCAG](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) explains motion preferences. The implementation uses native state selectors and CSS, without another animation dependency.
