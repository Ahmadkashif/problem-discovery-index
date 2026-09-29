# Defect Clustering and Root Cause Practice

**Niche:** [[niches/ai-agent-platforms/failure-clustering-and-repair/profile|Failure Clustering & Repair]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software quality engineering established that defects cluster and that fixing causes beats fixing symptoms, with the practice to support it, and agent reliability works ticket by ticket.
**Tags:** #k-means-clustering #evaluation-metrics #hypothesis-testing #descriptive-statistics #confidence-intervals #automation #dbscan #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a stream of individual agent failures into a small number of named, systematically fixable causes — and whoever does that takes the account, because the alternative is patching one case at a time forever.

## The Problem
That defects cluster, that a small number of causes produce most failures, and that a regression suite grown from real defects is the highest-value test asset are among software quality engineering's oldest and best-supported findings. The practice built around them — defect taxonomy, root cause analysis, regression suites seeded by field defects, and escape analysis asking why testing missed it — is standard in any mature engineering organisation. Agent reliability teams work through a ticket queue.

## What Already Exists
Defect clustering and taxonomy practice; root cause analysis methods with structured techniques; regression suites grown from field defects; defect escape analysis; crash and error grouping in production monitoring; and orthogonal defect classification for categorising failures by cause type.

## The Customization Gap
The adaptation is to a defect that is a probabilistic behaviour rather than a deterministic bug. It requires: (1) grouping by trajectory similarity rather than by stack trace, since there is no exception to group on and the signature is the shape of the interaction — defining that signature is the enabling piece; (2) a fix that shifts a rate rather than eliminating a behaviour, which means the regression test must be statistical, running a cluster of cases and checking a rate rather than asserting a single pass; (3) a defect taxonomy specific to agents — misread intent, wrong tool, wrong argument, lost context, hallucinated fact, wrong stopping point — which does not exist and would be immediately useful across the whole industry; (4) escape analysis asking why the evaluation set did not contain this shape, which is how the evaluation set improves and is the discipline that most reliably converts production failures into prevention; and (5) accounting for the silent failures, since only some agent errors are reported and the defect practice assumes reported defects are the population.

## Target Customer
Agent reliability teams, platform vendors, and the software quality engineering profession for whom this is a new and unusually noisy defect domain.

## Impact If Solved
Defect clustering and cause-over-symptom are among quality engineering's best-supported findings and this category ignores them. A published agent defect taxonomy would be immediately useful industry-wide, and statistical regression tests are what a probabilistic fix actually requires.
