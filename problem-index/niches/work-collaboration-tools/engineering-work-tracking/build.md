# The Ticket That Follows the Code Automatically

**Niche:** [[niches/work-collaboration-tools/engineering-work-tracking/profile|Engineering Work Tracking]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Engineering work leaves a complete trail of branches, reviews, builds and deployments, and engineers still move a card across a board by hand to describe work the system watched them do.
**Tags:** #graph-theory #bert #gradient-boosting #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor in engineering work tracking is fighting to make the tracker reflect what the code actually shows — and whoever connects the ticket to the commit, the review and the deployment most completely takes the engineering organisation.

## The Problem
A ticket sits in Code Review. In fact the pull request was approved and merged four days ago, the change was deployed to production on Tuesday, and the engineer moved on to something else without updating the board. The standup discusses it. A dashboard reports work in progress that includes it. Every one of those facts — merged, deployed, no subsequent activity — is in a system the tracker integrates with. The connection exists and is used to display a link rather than to determine the state.

## Why Nobody Has Built This
The ticket-to-code connection depends on a convention — putting an identifier in a branch name or commit message — which is fragile, forgotten and silently absent for a substantial share of work. Inferring the connection without the convention requires matching a change to a ticket by content, timing and author, which is achievable and has not been attempted. And moving status automatically requires the vendor to take a position on when a ticket is done, which differs between teams and is politically easier to leave configurable and therefore unset.

## What to Build
The connection inferred rather than conventional, and the state derived from it. A change is linked to a ticket by explicit reference where present and by content, author, timing and file-scope similarity where not, with a confidence and a review path for the ambiguous — which recovers the substantial share of work that currently has no link at all. State follows the pipeline: branch created, review requested, review approved, merged, deployed to each environment, each of which is an observable event and each of which maps to a state the team can define once. Stalled work is detected by its signature — a review requested and not completed, a branch with no activity, a change merged but not deployed — rather than by a person noticing. And the honest output is the divergence: tickets whose recorded state disagrees with the pipeline, which is the list an engineering manager should look at and which currently requires someone to check by hand.

## Target Customer
Engineering work tracking vendors, the repository and pipeline platforms extending into planning, and engineering organisations whose boards are maintained in parallel with the work.

## Impact If Built
Manual ticket maintenance is the most consistently resented overhead in engineering process and is entirely redundant given what the pipeline records. Inferring the link without the convention is the piece that makes it work in practice rather than in demonstration, and the divergence list gives engineering managers a better instrument than the standup it would partly replace.
