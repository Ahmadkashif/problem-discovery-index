# A Patch on Each Case Forever

**Niche:** [[niches/ai-agent-platforms/failure-clustering-and-repair/profile|Failure Clustering & Repair]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agent failures cluster in ways that only emerge in production, and each one is fixed as a specific case rather than as a systematic improvement, so the fix rate never catches the discovery rate.
**Tags:** #k-means-clustering #dbscan #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #automation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a stream of individual agent failures into a small number of named, systematically fixable causes — and whoever does that takes the account, because the alternative is patching one case at a time forever.

## The Problem
A reliability engineer receives eleven failure reports in a week. They read eleven trajectories, write eleven prompt amendments, and ship. Seven of the eleven were the same underlying cause — the agent mishandles any request where the customer mentions two order numbers — and the seven amendments each address a surface variation of it while an eighth phrasing will fail next week. The engineer has no view showing that seven of eleven share a cause, because failures arrive as tickets and nothing groups them. The prompt grows, the deployment does not get more reliable, and the pattern repeats.

## Why Nobody Has Built This
Failures arrive through support channels as individual customer complaints, which is the wrong unit for the analysis and the only unit anybody receives. Clustering trajectories requires representing them in a comparable form, which nobody has defined. Fixing a cause rather than a case takes longer and is harder to report as progress. And the reliability engineer is under pressure to close the eleven tickets.

## What to Build
Cluster the failures and fix the causes. Embed and cluster failed trajectories by their shape — task type, step sequence, tool calls, error points, input characteristics — so eleven tickets present as three causes with counts and examples, which is the build and it immediately changes what a week of work achieves. Name each cluster in domain terms, so a cause is something the team and the customer can discuss rather than a cluster identifier. Estimate each cluster's prevalence in production, including the failures nobody reported, since reported failures are a biased sample and the silent ones are frequently larger. Rank by impact, combining prevalence with the severity of the failure. Grow a regression suite from every cluster, using real trajectories as test cases, which is how a fix stays fixed and is the artefact the category most conspicuously lacks. Measure whether a fix generalised, by re-running the whole cluster rather than the single reported case — this distinction between covering a case and fixing a cause is the point of the whole build. Track failure rate by cause over time, so progress is visible as causes eliminated rather than tickets closed. And feed clusters into the deployment templates, since a cause seen at several customers is a product issue.

## Target Customer
Agent reliability and evaluation teams, the vendors whose deployments oscillate rather than improve, and the customers experiencing the failures.

## Impact If Built
Eleven tickets are three causes and nothing shows that. Clustering by trajectory shape changes what a week of reliability work achieves, and re-running the whole cluster after a fix is what distinguishes covering a case from fixing a cause.
