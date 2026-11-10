# Deliverator agent entry

Use Deliverator for Matt Kelly's first-party interfaces when the task or project instructions call for his shared design language. This is UI guidance, not a blanket instruction to redesign every repository, upstream project, game or document.

1. Read this checkout's `AGENTS.md` and [design-system.md](design-system.md), then the consumer's `PRODUCT.md`, `DESIGN.md` or equivalent. Explicit user direction governs conflicts.
2. Read the relevant component contract and compose existing components. The library owns presentation/interaction contracts; the application owns its data and engine state.
3. Inherit the accepted typography, Phosphor vocabulary and restrained motion. Use semantic tokens, bundled assets and licenses. Keep project artwork and original engines intact.
4. For a missing repeated UI intent, build and document a library component with real consumer evidence. Use native or established behavior for complex interactions; do not create another parallel kit or framework adapter speculatively.
5. Use [semantics](semantics.md) for control choice and [voice](voice.md) for copy. Distinguish settled choices from working proposals. Preserve accessibility, visible focus, touch targets and reduced motion.
6. Validate the actual changed behavior and responsive composition. Report what was exercised and which consumers have migrated. New library acceptance does not mean every app has already adopted it.

Do not treat this entry point as authority to install global configuration, publish source, change repository visibility, push, deploy, or replace product-specific identities. Those actions follow the user's scope and each repository's instructions.
