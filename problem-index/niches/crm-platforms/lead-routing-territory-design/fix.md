# The Rules Tree Nobody Dares Modify

**Niche:** [[niches/crm-platforms/lead-routing-territory-design/profile|Lead Routing & Territory Design]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Routing logic accumulates as exceptions granted to individuals over years, nobody can state what the rules currently do, and revenue operations maintains a decision tree they are afraid to change because it encodes a truce.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in routing and territory software is fighting to assign a lead or an account to the representative who will actually convert it — and whoever can evidence that a design outperforms the incumbent one takes the account.

## The Problem
The routing configuration has four hundred rules. Some implement the territory model. Some are named account assignments. Many are exceptions granted years ago to a representative or a manager who asked, whose original rationale is lost and whose beneficiary may have left. Nobody can say which rules currently fire, which are dead, which contradict each other, or what proportion of leads reach their destination through the intended path rather than through a fallback. A revenue operations analyst asked to make a change proceeds carefully and adds a rule, because removing one might break something nobody understands.

## Why It's Still Broken
The rules were added incrementally by different people over years, each addition individually justified and none documented against the whole. The configuration interface shows a list rather than a structure, so the interactions are invisible. And the political weight is real: a rule that appears dead may be someone's negotiated arrangement, and removing it without knowing is a conversation nobody wants. So the tree only grows, which is the same monotonic accumulation that afflicts claim edit libraries and CRM required fields.

## What a Fix Looks Like
Instrument the rules and make the structure visible. Every routing decision logs which rules were evaluated and which fired, which after a quarter gives a complete picture: rules that never fire, rules that fire constantly, rules shadowed by earlier ones and therefore unreachable, and the proportion of leads reaching a fallback rather than an intended rule. Present the tree as a structure with the traffic through each branch rather than as a list. Attach provenance where it exists — who added a rule, when, and why — and require it going forward, which is a one-line change with a long payoff. Retire the dead rules with the evidence attached, which makes the conversation about a specific rule that has not fired in two years rather than about the territory model. And report assignment outcomes by path, since the fallback route is frequently where conversion is worst and nobody has noticed because nobody segments outcomes by how the lead was assigned.

## Who Feels the Pain
Revenue operations analysts maintaining a system they cannot reason about; representatives receiving leads through paths nobody intended; and the organisation, whose most consequential allocation mechanism is an accumulation nobody can describe.

## Impact If Fixed
Rule firing telemetry is a logging change and reliably shows that a large proportion of the tree is dead or unreachable, which makes pruning a matter of evidence rather than courage. Outcome-by-path reporting is the finding most likely to prompt real change, because the leads falling through to a fallback are usually converting worst and nobody currently knows they exist as a category.
