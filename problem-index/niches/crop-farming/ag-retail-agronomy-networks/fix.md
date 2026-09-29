# The Agronomist Knows the Field and the Knowledge Leaves With Them

**Niche:** [[niches/crop-farming/ag-retail-agronomy-networks/profile|Agricultural Retail Agronomy Networks]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Fix (Pain Point)
**One-liner:** A twenty-year adviser carries the drainage, the disease history and the grower's tolerances for four hundred fields, and none of it is written down.
**Tags:** #tacit-knowledge-ml #data-integration #workflow-orchestration #worker-facing #automation

## The Problem
What makes a good agronomist good is not general agronomy. It is field-specific memory: which corner of which quarter drains badly, where the compaction is, which field had white mould two years ago, which hybrid disappointed on that soil, and which grower will not spray on a Sunday.

That memory is the retailer's relationship. A grower stays with the retailer because the adviser knows the farm. It is also entirely undocumented — the recommendation record shows what was applied, not why the adviser chose it over the alternative, and not the field history that drove the choice.

Adviser movement in agricultural retail is constant. Competitors recruit advisers precisely because the accounts follow them, and when one leaves, the retailer keeps the application records and loses the reasoning. The replacement rebuilds four hundred fields of context from scratch over two or three seasons, during which the grower is being courted by the departed adviser's new employer.

The same gap shows up in ordinary operation. When an adviser is on holiday, covering a territory means working from a system that records rates and dates but not judgment. And a new hire has no way to learn from the fifty most instructive decisions the practice made last season, because those decisions exist only as outcomes.

## Why It's Still Broken
Advisers are measured on volume and on relationships, and time spent documenting reasoning is time out of the truck during the only weeks of the year when the work can be done.

There is also a quiet incentive against it. An adviser whose field knowledge is written into the employer's system is more replaceable and has less leverage. Nobody says this aloud and everybody understands it, which is why every attempt to impose documentation from above has failed.

And the tooling assumed the wrong unit. Agronomy systems are built around the recommendation and the order — a transaction record — with the field as an attribute rather than as the object that accumulates a history.

## What a Fix Looks Like
**Make the field the record, not the order.** A field page that accumulates observations, prescriptions, outcomes, soil tests, drainage notes and the grower's preferences across seasons and advisers. Everything else follows from this one structural change.

**Capture the reason at the moment of the recommendation.** One structured line: what drove this choice, what the alternative was, and what would change it next season. Seconds, inside the workflow that already produces the prescription.

**Give it back immediately.** The adviser's own field history, searchable, on a phone, in the truck — better recall than their own memory across four hundred fields. That is what makes the habit survive, and it is the only version advisers adopt willingly.

**Capture grower constraints explicitly.** Timing preferences, equipment limits, custom applicator relationships, risk appetite. These are the things a covering adviser gets wrong and a departing adviser takes with them.

**Handle the leverage problem honestly.** The system will be read as a retention tool unless it visibly serves the adviser first. Field history retrieval, faster visit prep, less evening paperwork — those are the arguments that work, and they are true.

**Use it to onboard.** A new adviser given the previous adviser's structured field histories reaches competence in a season instead of three, which is the largest single cost of the industry's turnover.

## Who Feels the Pain
Advisers covering unfamiliar territory from records that hold rates but not reasoning; new hires rebuilding context the company already paid to acquire; growers whose farm knowledge resets when their adviser changes employers; and the retailer, whose agronomic advantage over a cheaper channel is stored entirely in people it cannot keep.

## Impact If Fixed
The retailer's differentiation is adviser knowledge, and adviser knowledge is currently a liability that walks. Making the field the unit of record turns individual memory into an institutional asset, collapses the onboarding cost of a high-turnover workforce, and produces the field-history layer that prescription-outcome measurement needs as context.
