# A Taxonomy That Survives the Game

**Niche:** [[niches/game-analytics-vendors/event-taxonomy-ownership/profile|Event Taxonomy Ownership]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every number the studio trusts rests on a schema nobody owns.
**Tags:** #data-integration #workflow-orchestration #compliance #evaluation-metrics #automation #sets-and-logic #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to keep an event schema coherent as a game changes for years, when the schema was designed early by whoever was available and nobody owns it — and whoever takes ownership takes the account.

## The Problem
The event schema is designed at the beginning of a project, usually quickly, by an engineer with other priorities. Then the game runs for years. Features are added and instrumented ad hoc, mechanics change while the events describing them do not, parameters are repurposed, and events are duplicated because nobody knew one already existed. Every analysis rests on this and nobody is responsible for it.

## Why Nobody Has Built This
The schema is a shared dependency with no owner, which is how it decays. Analytics vendors accept whatever is sent because rejecting events breaks customers. Governance sounds like process overhead to a game team. And the damage is gradual and attributed to analysis rather than to instrumentation.

## What to Build
Give the taxonomy a registry, a review and an owner. Maintain a schema registry as the authoritative definition of every event and parameter, which is the core and is the artefact whose absence causes everything else. Review new events before they ship rather than discovering them in the data, which is a lightweight gate that prevents most duplication. Enforce naming and structure conventions automatically at the instrumentation layer. Detect semantic drift — an event whose distribution or context changes without a schema change — since that is the silent failure nobody catches. Provide a deprecation process so old events can be retired rather than firing forever. Version the schema alongside the game's builds, which is what makes historical analysis honest. Document what each event means in terms a designer recognises, as the current definitions are code. Flag duplicates and near-duplicates on submission. Assign a named owner for the taxonomy, which is the organisational half and the part that actually determines success. And make the registry the thing analysts consult rather than a spreadsheet somebody maintained until they left.

## Target Customer
Studio data platform teams, game analytics vendors, publishers standardising across titles, and data governance tooling providers.

## Impact If Built
Every number the studio trusts rests on a schema nobody owns, and it decays for exactly that reason. A registry with a review gate and a named owner is the artefact whose absence causes everything else.
