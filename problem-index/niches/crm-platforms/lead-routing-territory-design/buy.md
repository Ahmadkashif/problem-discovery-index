# Territory Design as the Optimisation Problem It Is

**Niche:** [[niches/crm-platforms/lead-routing-territory-design/profile|Lead Routing & Territory Design]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Territory alignment is a districting problem with a substantial operations research literature and commercial tooling in field service and logistics, and enterprise sales organisations solve it every year in a spreadsheet with fairness as the objective.
**Tags:** #optimization-fundamentals #combinatorics-and-counting #dynamic-programming #convex-optimization #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in routing and territory software is fighting to assign a lead or an account to the representative who will actually convert it — and whoever can evidence that a design outperforms the incumbent one takes the account.

## The Problem
Annual planning. The territory map is redrawn to balance quota, which means equalising the sum of account potential across representatives. The balance is the objective, because it is the thing that can be defended in a room full of sales leaders. Whether the design maximises revenue — which would mean accounting for travel where it matters, relationship continuity, representative fit and the disruption cost of moving an account between people — is a different question that the spreadsheet cannot represent and that nobody asks.

## What Already Exists
Territory design is the political districting problem with a different name, and it has a large operations research literature covering balance, contiguity, compactness and multi-objective formulations. Commercial territory optimisation tooling exists in field sales and service. Constraint solvers handle problems of this size easily. Sales territory alignment products exist and are largely balance calculators. The methodology is mature and under-applied.

## The Customization Gap
The adaptation is to an objective that is revenue rather than balance, with the real constraints included. It requires: (1) account potential estimated rather than assumed, since balance computed on a potential estimate that is really last year's revenue simply preserves the existing distribution; (2) disruption cost modelled explicitly, because moving an account mid-relationship destroys value and every annual realignment does it wholesale without counting the cost — this is the single largest omission in current practice; (3) representative fit and continuity as objectives alongside balance, so the design uses information the organisation has and currently discards; (4) fairness as a constraint with a stated tolerance rather than as the objective, which is the substantive change and is defensible precisely because it is explicit; and (5) scenario comparison as the output, since the deliverable is a conversation among sales leaders and a single optimal answer will be rejected while three annotated options will be discussed.

## Target Customer
Revenue operations and sales planning functions, territory and quota planning vendors, and the consultancies who run annual alignment engagements.

## Impact If Solved
Annual realignment destroys relationship value at a scale nobody counts, and including disruption cost in the objective typically produces a design that moves far fewer accounts for the same balance. Bringing districting methodology to a problem currently solved in a spreadsheet is an import rather than an invention, and the scenario framing is what makes the output usable in the room where the decision is actually made.
