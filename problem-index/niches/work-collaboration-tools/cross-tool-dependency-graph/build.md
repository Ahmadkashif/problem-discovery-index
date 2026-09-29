# Thirty-Six Pairwise Links and No Graph

**Niche:** [[niches/work-collaboration-tools/cross-tool-dependency-graph/profile|Cross-Tool Dependency Graph]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Connectors sync fields between pairs of tools, so a nine-tool company maintains dozens of brittle bilateral links and still cannot see that a design decision is blocking a ticket that is blocking a launch.
**Tags:** #graph-theory #bert #large-language-models #graph-neural-networks #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in integration is fighting to turn pairwise field syncing into a single graph of what blocks what across the whole tool estate — and whoever holds that graph owns the question every executive asks and no integration answers.

## The Problem
A launch slips. The programme manager asks why. The programme plan shows the launch task as at risk. The engineering tracker shows three open tickets, one of which has a comment saying it is waiting on the payments integration. The payments work is in a different team's board, where it is blocked on a decision recorded in a document that has been in review for eleven days because the person who has to approve it is unaware they are the blocker. Every one of those facts is written down, in four tools, connected by integrations that faithfully copy status fields between pairs of them and transmit none of the dependency. Reconstructing the chain takes an afternoon of asking people, and it is reconstructed again next week.

## Why Nobody Has Built This
The integration market formed around connectors because connectors are sellable, countable and easy to explain, and a marketplace with six hundred of them looks like comprehensive coverage. The graph requires entity resolution across systems — deciding that this ticket, that document section and that programme line refer to the same piece of work — which is materially harder than field mapping. Most dependency is expressed in prose rather than in a dependency field, and the platforms that have dependency fields find them sparsely used, which has been read as a lack of demand rather than as friction. And no vendor owns the estate, so the graph has no natural home.

## What to Build
A dependency graph over the whole tool estate, assembled from what is already written. Entities resolved across tools by identifier where one exists, and by content, participants, timing and reference where one does not. Dependency edges extracted from three sources: explicit dependency fields, which are reliable and rare; cross-tool references, links and mentions, which are common and under-exploited; and prose in comments and updates, where most real dependency lives and which language models read well enough to propose an edge for confirmation. Edges carry provenance and confidence, and proposed edges are confirmed by a human rather than asserted, because a wrong blocking relationship sends someone to chase the wrong person. From the graph: critical path across tools, blast radius when something slips, and — the highest-value output — notifying the person at the root of a chain that four things are waiting on them, which they usually do not know. Detection of cycles and of orphaned work follows for free.

## Target Customer
Operations, programme management and IT at companies running a multi-tool estate; integration platform vendors for whom this is the layer above their connectors; and work management vendors trying to be the system of record for work that spans tools they do not own.

## Impact If Built
The pairwise architecture is a structural limit rather than a maturity gap — no number of connectors produces a graph. The chain-root notification alone changes behaviour, because the most common cause of a stalled dependency is that the person at the root does not know they are one.
