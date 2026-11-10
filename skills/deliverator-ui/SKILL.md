---
name: deliverator-ui
description: Build, refine or review Matt Kelly's first-party product UI using the Deliverator component library, typography, iconography and motion grammar. Use when the task or project instructions call for Deliverator; preserve distinct project artifacts and explicit product direction.
---

# Deliverator UI

Resolve the canonical Deliverator checkout from the project's instructions, the configured `DELIVERATOR_ROOT`, or the path supplied by the user. When running from this repository-owned skill, the checkout is two directories above this folder. A copied skill still needs a resolvable canonical checkout; do not substitute remembered rules or an unrelated UI kit if it is missing.

Read `<checkout>/docs/agent-entry.md`, which links the maintained design-system guide and component contracts. Read only the relevant deeper references. Keep detailed decisions in the library rather than duplicating them in this skill or the agent's global instructions.

Inspect the consumer's existing integration and compose the supported components. If a genuine component is missing, develop it in the library with a real consumer and catalogue case, then integrate it. Keep application state and project engines outside the library.

Preserve the user's scope: this workflow does not itself authorize a broad migration, global installation, source publication, deployment or upstream visual redesign. Validate the changed interface in its real context and distinguish an available library component from a successfully migrated consumer.
