# The Tracker That Knows What It Cannot See

**Niche:** [[niches/work-collaboration-tools/work-management-suites/profile|Work Management Suites]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A work tracker represents only the work that happens inside it, which is a fraction of the work, and it renders the rest as a task somebody remembered to create.
**Tags:** #graph-theory #data-integration #bert #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #descriptive-statistics
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A programme spans engineering, design, legal review, a vendor contract, a marketing launch and a finance approval. The tracker holds tasks for the engineering work in detail, one task called "Legal review" with no visibility of what legal is actually doing, one for the vendor contract sitting in a procurement system, and a marketing plan that lives in a different product entirely. The programme view is therefore precise about a third of the work and fictional about the rest, and the parts it cannot see are usually where the delays come from — because the work it does see is done by people who use the tracker.

## Why Nobody Has Built This
Each product's business model is to be the place work happens, so representing work that happens elsewhere is a concession to a competitor, and the integration strategies reflect it: connectors sync fields into the tracker to make it more complete-looking rather than to make the other tool a first-class participant. The deeper reason is that representing external work well requires understanding its state, which requires more than a field sync — and that is the same inference problem as this industry's first niche, applied across a boundary.

## What to Build
A representation of external work as a first-class object with an inferred state. Work that lives elsewhere — a legal review in a contract system, a purchase in a procurement system, a design in a design tool, a campaign in a marketing platform — is represented by a proxy that carries what can be observed about it: its identity in the source system, its state as reported there, its last activity, and the dependency relationship to the work in the tracker. Where the source system exposes state, it is read rather than synced, so the proxy is a live view rather than a copy that drifts. Where it exposes only activity, the state is inferred as this industry's first niche describes. Dependency is the point: the tracker's value is in knowing what is blocking what, and a proxy that carries an accurate blocked-since date for an external item is worth more than a full field sync of a system nobody looks at. And the honest part of the design is representing what is not known — an external item whose state cannot be observed is shown as unobserved rather than as a green task.

## Target Customer
Work management platform vendors, programme functions in organisations running several tools, and the integration platform vendors whose connectors currently sync fields.

## Impact If Built
Cross-boundary work is where programmes actually slip and is where every tracker is weakest, because each product's incentive is to pull work inward rather than to represent it where it lives. A proxy with an inferred state and an honest unknown is a better programme view than a complete-looking board built on invented tasks.
