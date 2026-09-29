# Cross-Tool Dependency Visibility

**Industry:** [[work-collaboration-tools|Work Collaboration Tools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Integration marketplaces are enormous and every connector syncs fields between two tools, which means a company with nine tools has thirty-six brittle pairwise links and still cannot see what is blocking what.
**Tags:** #graph-neural-networks #bert #word-embeddings #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration

## The Problem
Real work spans tools. A feature exists as a task in a work management platform, a design in a design tool, tickets in an issue tracker, code in a repository, a document in a wiki, a conversation in a messaging app and a launch date in a spreadsheet. The dependency between them is real and lives nowhere.

Integrations exist in abundance and operate pairwise: when this changes there, update that here. They sync status fields and create linked records. What they do not do is establish that these seven artefacts across five tools are the same piece of work, which is the thing that would make dependency visible.

So blocking relationships are tracked by humans, in the task's description, in a comment, or not at all. A team discovers that its work was blocked by another team's unfinished dependency when the deadline arrives.

The pairwise architecture also degrades badly. Nine tools is thirty-six possible connections, each configured separately, each breaking independently when an API changes, each maintained by whoever set it up and has since changed roles.

## What Already Exists
Integration marketplaces at every platform contain hundreds of connectors. iPaaS products (Zapier, Workato, Tray) handle general orchestration. Atlassian, Microsoft and Google each offer deep integration within their own estates. Some platforms support cross-tool linked issues. Enterprise service management tools model dependencies within their own scope.

## The Customisation Gap
There is no work-item resolution layer. Recognising that a Jira ticket, a Figma frame, a pull request, a document and a Slack thread all concern the same piece of work is entity resolution across systems, using titles, participants, timing, references and content overlap. It is entirely tractable and nobody has built it, because each vendor's incentive is to be the centre rather than to make a heterogeneous estate coherent.

Dependency inference is the second half. Blocking relationships are visible in behaviour — this work consistently waits on that team, this review step always precedes that deployment — and can be learned from history rather than declared. Declared dependencies are always incomplete because declaring them is work nobody is paid for.

Cascade impact is what makes it actionable: when something slips, which downstream work is affected and by how much. That requires the graph, which requires the resolution layer, which is why nobody has it.

## Impact If Solved
Cross-team dependencies are where organisational work actually fails, and they are invisible because the tooling is pairwise and field-level. A resolution and dependency layer would show, for the first time, what a company's work actually depends on — and it can be inferred rather than declared.
