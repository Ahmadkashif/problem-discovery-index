# Coverage Is Sold as a Number and Nobody Knows What Is Missing

**Niche:** [[niches/personal-injury-law/litigation-analytics-court-data/profile|Court Data & Litigation Analytics Platforms]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** An analytic computed over a venue with silently incomplete data looks exactly like one computed over a complete venue.
**Tags:** #evaluation-metrics #change-point-detection #causal-inference #compliance #automation

## The Problem
The platform sells statistics: this judge grants this motion at this rate, cases of this type in this venue take this long. The statistic is computed over whatever the platform has managed to collect from that court.

What it has collected is never everything, and how far from everything varies enormously — by county, by case type, by year, and by document type. Some courts do not publish orders, only that an order was entered. Some publish filings but not dispositions. Some backfill history for a few years and no further. Some went dark for six months during a system migration and nobody noticed until a customer asked.

None of this reaches the customer. A rate computed over sixty per cent of a venue's cases renders identically to one computed over ninety-eight per cent. An attorney valuing a case against a venue benchmark cannot tell whether the benchmark is solid or thin, and a firm-wide practice built on those benchmarks inherits the gaps without knowing they exist.

Internally the situation is not much better. Coverage is tracked as counts of courts and documents ingested, which is a measure of effort rather than completeness. There is usually no answer to the direct question — what fraction of the cases actually filed in this county last quarter do we have — because the denominator is not available from the same source that supplies the numerator.

## Why It's Still Broken
Completeness has no ground truth. The only authority on how many cases a court has is the court, and courts publish caseload statistics late, aggregated differently, and sometimes not at all. Measuring what you are missing requires a second, independent source, and building one is unglamorous work that no customer asked for.

The commercial pressure runs the other way. Coverage is the competitive claim in this market, so a vendor has a strong incentive to state courts covered and a weak incentive to state how completely. Publishing per-venue completeness would mean publishing where you are weak, in a market where procurement compares coverage tables.

And the analytics were built before anyone anticipated the question. Rates are computed straight from the corpus; there is no field for the size of the population they should have been computed over.

## What a Fix Looks Like
**Estimate completeness, per court, per period, per document type.** Compare against court-published caseload statistics where they exist, against sequential case numbering where courts assign it, and against independent sampling — pull a small random sample of case numbers directly and check whether the platform has them. That last method is cheap, works everywhere, and gives an honest confidence interval on coverage.

**Attach coverage to every analytic.** A grant rate carries the number of cases it was computed over and the estimated share of the population that represents. This costs a design decision, not a research programme.

**Suppress or flag below a floor.** A benchmark computed over a thin slice of a venue is worse than no benchmark, because the customer will use it. Define the floor, publish it, and let sparse cells say so.

**Monitor ingestion for silent breaks.** Volume by court and document type against its own history, with alerting on drops. The migration failure mode — a county whose format changed and whose feed quietly emptied — is detectable in a day and currently surfaces in months.

**Model the missingness where it is not random.** Courts that publish dispositions late make recent periods look faster; courts that publish only contested matters make settlement rates look low. These are correctable biases once the mechanism is characterised, and invisible until then.

## Who Feels the Pain
Attorneys valuing cases against benchmarks whose reliability they cannot assess; the platform's own data team, which cannot answer a coverage question in a customer call; and the analytics team, whose careful work is undermined by a denominator nobody measured.

## Impact If Fixed
Per-venue completeness with stated uncertainty is a genuine differentiator in a market where every vendor claims coverage and none quantifies it — and it is the precondition for anything predictive, because a model trained on a corpus with unmeasured, non-random gaps inherits every one of them.
