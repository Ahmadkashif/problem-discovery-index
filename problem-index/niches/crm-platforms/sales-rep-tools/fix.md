# Hours a Week of Entry Nobody Has Measured

**Niche:** [[niches/crm-platforms/sales-rep-tools/profile|Sales Representative Tools]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Sales organisations assert that representatives spend too much time on administration and none of them measures it, so the field count of required fields grows every quarter and nobody can say what it costs.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor building for representatives is fighting to make the CRM something a seller opens because it helps them rather than because they are required to — and whoever the representatives use unprompted takes the seat.

## The Problem
Someone in marketing needs a field to segment on. Someone in finance needs another for revenue recognition. A product team wants a competitive-loss reason. Each is individually reasonable and each becomes a required field on the opportunity. Three years later there are forty required fields, representatives fill them with whatever passes validation, and the data is worse than it was with twelve. Nobody ever computed what a field costs — a minute per deal per representative per update, across the organisation, forever — because the cost falls on people who are not in the meeting where the field is added.

## Why It's Still Broken
Field additions are governed by whoever administers the CRM and are approved on the merit of the request rather than against a budget, because there is no budget — the cost is diffuse, unmeasured and borne by someone else. The usage telemetry that would price it exists in every platform and is used for licence management rather than for this. And representatives' complaints about administrative burden are perennial and unquantified, which makes them easy to acknowledge and ignore.

## What a Fix Looks Like
Measure the burden and put a price on a field. Time in the CRM, by screen and by activity, is derivable from the platform's own telemetry without any additional tracking, and separating data entry from useful work — reading an account, preparing for a call — is a classification over that telemetry. Report administrative minutes per representative per week as a standing metric, in aggregate to leadership and individually to the representative as their own information. Then govern field additions against it: a proposed required field carries an estimated cost in representative hours per year, and the requester has to justify it against that. Audit the existing fields the same way — fill rate, distinct values, and whether anything actually consumes them downstream, which reliably shows that a substantial number of required fields feed no report at all and can be removed immediately. That audit is a query and is the fastest available improvement to both the burden and the data quality.

## Who Feels the Pain
Representatives filling fields to satisfy validation rather than to record anything; analysts building on data entered under duress; and administrators adding fields with no mechanism to refuse.

## Impact If Fixed
The unused-field audit typically removes a meaningful share of required fields immediately, which improves data quality and reduces burden at the same time. Pricing a field in representative hours changes the governance conversation permanently, because it introduces the only constraint that has ever been missing from it.
