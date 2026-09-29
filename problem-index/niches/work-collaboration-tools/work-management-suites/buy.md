# Federated Query Rather Than Pairwise Sync

**Niche:** [[niches/work-collaboration-tools/work-management-suites/profile|Work Management Suites]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data federation and virtual query across heterogeneous sources is a solved discipline, and collaboration tools connect to each other with pairwise field-copying connectors that multiply quadratically and drift immediately.
**Tags:** #data-integration #graph-theory #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #descriptive-statistics #compliance
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A company runs nine tools that hold parts of its work. The integration marketplace offers connectors between each pair, so the company builds thirty-six brittle links that copy fields in both directions, conflict, drift and break silently whenever either side changes. Every one of them requires maintenance and none of them produces the thing the company wants, which is a single answer to what is blocking what. The data integration discipline solved this pattern decades ago by replacing point-to-point copying with a common model and federated query.

## What Already Exists
Data virtualisation and federated query engines are mature commercial and open products. Canonical data modelling and hub-and-spoke integration architecture are established patterns with a long literature. GraphQL federation, API gateways and event-driven integration are commodity. Identity and entity resolution across systems is mature, as several niches in this vault describe. Every component required to replace pairwise syncing is available and is standard practice one discipline over.

## The Customization Gap
The adaptation is to work objects whose semantics differ per tool. It requires: (1) a canonical work model rich enough to represent a task, a document, a review, a request and a decision without flattening them — which is the intellectual work and is where a naive common model loses exactly the information that mattered; (2) read-federation as the default rather than copying, so each tool remains authoritative for its own objects and the composed view is assembled on demand, which removes the drift problem entirely; (3) identity resolution across tools, since the same piece of work appears as a ticket, a document, a thread and a design file and relating them is the prerequisite for any dependency analysis; (4) write paths kept narrow and explicit, since bidirectional sync is the source of most conflicts and most work genuinely belongs in one system; and (5) permission propagation handled correctly, because a federated view that shows someone work they are not entitled to see in the source system is a serious failure and is the most common reason these projects are stopped.

## Target Customer
Platform and integration owners in large organisations, work management vendors, and the integration platform vendors whose connector marketplaces currently monetise the pairwise approach.

## Impact If Solved
Replacing quadratic pairwise syncing with federated read removes both the maintenance burden and the drift, and it is the architectural precondition for a cross-tool dependency view. Permission propagation is the element that determines whether it survives a security review, and it is the part most often left until last.
