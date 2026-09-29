# Making a Programme Portable

**Niche:** [[niches/embedded-finance-platforms/bank-partnership-and-charter/profile|Bank Partnership & Charter Access]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every programme is built against one bank's specific requirements, so losing that bank means rebuilding rather than moving.
**Tags:** #sets-and-logic #workflow-orchestration #compliance #automation #data-integration #evaluation-metrics #optimization-fundamentals #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make the sponsor bank relationship a managed, diversified, transferable asset rather than a single dependency negotiated once — and whoever can move a programme between banks without rebuilding it removes the category's largest existential risk.

## The Problem
A sponsor bank exits the business — because its regulator pressed it, because the economics changed, because the risk appetite shifted. The platform has ninety days and dozens of programmes whose account structures, compliance configurations, fee handling, dispute processes, settlement patterns and reporting were all built against that bank's requirements. Nobody knows which parts are bank-specific and which are general, because the distinction was never drawn. The migration is discovered rather than executed.

## Why Nobody Has Built This
Bank relationships were assumed durable, so portability looked like engineering for an unlikely event — and the effort was never spent because the event had not happened. Bank-specific requirements were absorbed into implementations rather than isolated. Each bank's constraints differ enough that abstraction is genuinely hard. And a platform that builds for portability is implicitly telling its bank partner it might leave.

## What to Build
Make the coupling visible, then reduce it. Identify which parts of each programme's configuration are bank-specific and which are general, which is the core and is an analysis nobody has done — the answer is itself immediately useful. Isolate bank-specific configuration behind a boundary so that a migration becomes a substitution rather than a rebuild, which is the engineering that follows the analysis. Model the migration explicitly — what would have to change, how long it would take, what would break — since an unmodelled dependency is an unmanaged one. Maintain a second bank relationship for the programmes that warrant it, because diversification is the actual mitigation and portability is what makes it affordable. Measure the coupling per programme so the accumulation is visible as it happens rather than at the ninety-day mark. Map each bank's requirements to the general capability they constrain, which is what lets a new bank's constraints be evaluated quickly. Rehearse a migration on a small programme, since a capability never exercised is a plan rather than a capability. Score sponsor concentration as a board-level exposure, because that is the framing that funds the work. Preserve the customer experience through a migration, since end customers did not choose the bank and must not notice. And measure estimated migration time as the portfolio's key number.

## Target Customer
Platform executives and partnership leadership, sponsor banks assessing their own concentration, and the programmes whose continuity depends on a relationship they cannot see.

## Impact If Built
Portability was never built because the event had not happened and the effort looked speculative. Separating bank-specific from general configuration is the analysis that makes both diversification and migration possible, and the answer is useful the day it exists.
