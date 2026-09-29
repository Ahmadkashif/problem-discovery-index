# Coverage Varies by Channel and the Output Never Says So

**Niche:** [[niches/pharmacy-independents/prescription-market-intelligence/profile|Prescription Market Intelligence Providers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** A number built from eighty per cent of retail and a fraction of specialty is delivered as one number.
**Tags:** #evaluation-metrics #change-point-detection #data-integration #compliance #automation

## The Problem
Coverage in this business is not a single figure. It varies by channel — retail chain, independent, mail, long-term care, specialty, 340B contract pharmacy — by geography, by payer type, and over time as supplier contracts change. Everyone inside the firm knows this. Almost none of it reaches the customer.

The customer receives a national figure for their product. If that product dispenses predominantly through specialty pharmacy, where capture is thinnest and most variable, the figure carries far more uncertainty than a retail-heavy product's — and looks identical on the page.

Internally the problem shows up as unexplained movement. A series jumps, and the analytics team spends a week establishing whether a market changed or a supplier's feed did. Contract changes, chain acquisitions, a supplier's system migration, a change in what a source transmits — each shifts the observed base without anything happening in the world. Independent pharmacies, which Pass 1 notes number over nineteen thousand and dispense a substantial share of prescription value, are one of the harder channels to capture completely and one of the more volatile in coverage.

Because coverage is a modelling input rather than a reported attribute, none of this is visible to the person making a decision.

## Why It's Still Broken
Simplicity sells. A single number is easier to contract for, easier to build a customer's internal process around, and easier to compare against a competitor's. Every commercial force pushes toward one figure per cell.

Publishing coverage detail also exposes weakness. A vendor stating specialty capture by channel is telling a prospect exactly where a competitor might be stronger. Nobody wants to move first.

And measuring coverage honestly is genuinely hard, because it needs a denominator — how many prescriptions were actually dispensed in that channel — which is the same missing census that makes projection unverifiable. It is tractable with triangulation and sampling, and it has not been treated as a priority.

## What a Fix Looks Like
**Publish coverage as a dimension of every deliverable.** Estimated capture rate for the channel, geography and period the number came from, next to the number. This is a product decision more than a technical one.

**Instrument supplier feeds for drift.** Volume, mix and completeness per supplier against their own history, with alerting on breaks. The failure mode where a source quietly changes what it transmits is detectable within a day and currently surfaces weeks later as an unexplained market movement.

**Separate coverage change from market change in the series.** When capture shifts, the reported series should decompose the movement rather than absorb it. Customers experience unexplained revisions as unreliability, and the explanation exists internally.

**Set and enforce a reporting floor.** Cells below a coverage threshold should be suppressed or explicitly flagged rather than delivered as if equivalent. A thin estimate the customer trusts is worse than no estimate.

**Give the sales and support organisation the coverage picture.** The most common escalation in this business is a customer disputing a figure against their own shipment data. The answer is usually a channel coverage fact, and the person on the call does not have it.

## Who Feels the Pain
Customers making commercial decisions on figures of unknown reliability, and setting sales compensation against them; the firm's analytics staff, who spend days reconstructing why a series moved; and the client service teams, who defend numbers whose confidence they cannot state.

## Impact If Fixed
Coverage transparency is the cheapest available trust improvement in a market where the product is inherently an estimate, and it is the precondition for everything harder — measured projection error, propagated uncertainty, and reliable real-world evidence. It also converts the most frequent customer dispute from an argument into an explanation.
