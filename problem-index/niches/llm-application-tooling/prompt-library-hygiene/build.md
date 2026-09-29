# Hundreds of Templates Nobody Can Delete

**Niche:** [[niches/llm-application-tooling/prompt-library-hygiene/profile|Prompt Library Hygiene]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Prompt libraries grow into hundreds of overlapping templates that nobody can safely delete, because no one knows which are in use, which duplicate each other, or what any of them do that matters.
**Tags:** #k-means-clustering #dbscan #word-embeddings #evaluation-metrics #descriptive-statistics #automation #data-integration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to tell a team which of their prompts are used, which duplicate each other and which can be deleted — and whoever does that takes the account, because the estate only grows and nobody can safely remove anything.

## The Problem
A team's registry holds four hundred and twenty prompts. Nobody knows how many are live. Six versions of a summarisation prompt exist with small differences, three of which were experiments that ended. A support prompt and a chat prompt are ninety percent identical and diverged eight months ago in ways nobody intended. A change to the returns policy wording needs to be made in five places and is made in two. Deleting anything is unthinkable because nobody can prove it is unused, so the estate grows every quarter and the cost of every change grows with it.

## Why Nobody Has Built This
Registries were built to store and version prompts, so usage and lifecycle were never in the design. Usage tracking requires joining the registry to production traces, which crosses a product boundary. Similarity detection on text is easy and behavioural equivalence is less so, and the cautious answer to both is to keep everything. And there is no cost line attached to a bloated registry, so it never becomes a project.

## What to Build
Make the estate measurable and prunable. Track usage from production traces per prompt and version, which is a join the tooling can make and which immediately identifies the dead half of most registries — this alone is the bulk of the value. Detect duplicates and near-duplicates by text and structure, and show the diffs, so silent divergence becomes visible rather than accumulating. Test behavioural equivalence between similar prompts on a shared input set, so a merge can be made confidently rather than avoided — this is what converts a detected duplicate into an actual deletion. Attach an owner to every prompt, treating unowned as a finding, since nothing without an owner will ever be reviewed. Give prompts a lifecycle with an expiry for experiments, so the default is removal rather than permanence and the estate stops growing by construction. Report the estate's size, growth and dead share as a standing metric, which is what makes the problem visible to whoever funds the cleanup. Surface where a policy statement appears across the estate, so a change can be made everywhere it lives. Archive rather than delete, since the fear of losing something is what prevents removal and an archive removes it. And warn at creation when a near-identical prompt already exists, which stops the growth at its source.

## Target Customer
Teams with accumulated prompt estates, the platform teams maintaining them, and the registry vendors whose products store without managing.

## Impact If Built
Joining the registry to production traces identifies the dead half of most registries immediately. Behavioural equivalence testing is what turns a detected duplicate into a confident merge, and creation-time warnings stop the growth at its source.
