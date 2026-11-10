# Usage semantics — working guide

This records the current component behavior and recommended grammar. New treatments remain reviewable proposals; the accepted fonts, icons and motion live in their own contracts.

## Selection is information

The Lisp rules are a single-choice selector. They are not seven project categories, seven statuses or seven different levels of importance. Keep idle choices in the same neutral treatment. Reserve the signal accent and visible rounded border for the current rule; preserve keyboard focus as a separate outline and `aria-pressed` as the accessible state.

Giving every rule a hue would add a legend to learn. Use identity color only when that relationship carries information elsewhere. Syntax colors already describe grammar: quoted values, operators and evaluator calls. Do not assign arbitrary operator colors merely to make the selector more lively.

A useful future experiment is a small active-operator marker connecting the selected control to its code excerpt, while preserving syntax colors. That is a code-study feature to compare, not an adopted seven-color selector. Do not silently change the existing pills while implementing this guide.

## Choose the right control

| Intent | Pattern |
| --- | --- |
| Run, pause, reset or change something | Native button through the shared action component |
| Open a project, source or another page | Link; give its destination a useful name |
| Choose one view, rule or tool from a short set | Choice group; selected state stays visible |
| Switch between distinct document panels | Tabs with the corresponding panel and keyboard contract; use established behavior |
| Display a category | Noninteractive tag; do not make it resemble an actionable selector |
| Include/exclude independent filters | Toggle/filter controls with an explicit multi-select contract |
| Describe live, paused, failed or unavailable state | Status text and appropriate semantics, not another selected-looking pill |

Signal means selected, focused or primary action. It does not mean every positive value, completed result or status is yellow-green. Error and success colors need genuine application state and an accompanying label; never rely on color alone.

## Composition

An exhibit header names the project before its demo. The same boundary contains the artifact, its controls and its explanation. The action takes visitors to the full experience. A second screenshot earns its place only when it shows something richer than the visible demo.

Small, repeated labels help scanning. They must identify an actual thing: a file, project, view, control, value or state. Do not add decorative eyebrow copy, counters or category labels to fill space.

Use stronger control boundaries where interaction needs them, and quieter rules for grouping. Avoid making every nested region another card. Keep selection, hover, focus and disabled states distinguishable; a control should not need a new hue for every interaction.
