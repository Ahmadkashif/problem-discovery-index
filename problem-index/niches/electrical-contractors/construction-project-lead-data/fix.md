# Coverage Is Sold as a Count and Never Measured as a Rate

**Niche:** [[niches/electrical-contractors/construction-project-lead-data/profile|Construction Project Lead & Plan Data]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** The product is sold on how many projects the database contains, when what a contractor needs to know is what share of the projects in their market and trade it actually caught.
**Tags:** #probability-distributions #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #descriptive-statistics #feature-engineering #data-integration #revenue-impact #compliance

## The Problem
Coverage is the product's real promise and it is expressed as a supply-side count. A contractor cares about a different quantity entirely: of the projects that went to bid in their geography and trade last year, what fraction appeared in the database, and how early. That number is not reported, is probably not known internally, and almost certainly varies enormously — strong in large metros and major project types, thin in secondary markets and in the smaller commercial work where most of the seventy thousand electrical firms actually live. Subscribers discover the gaps by losing bids on projects they never saw, and attribute it to bad luck rather than to coverage.

## Why It's Still Broken
Measuring what was missed requires knowing about projects the database does not contain, which is the same structural difficulty that appears wherever this sweep finds a coverage claim. The tractable route is triangulation — permit records, awarded contract filings, and comparison against what subscribers report bidding — and none of it is trivial. Commercially, a count is easy to win a bake-off with and a rate invites an unflattering comparison, so nobody publishes one and no competitor forces the issue.

## What a Fix Looks Like
Coverage estimated as a rate, per market and per trade, using public permit and award records as an external frame and capture-recapture logic across independent source types to estimate what all sources jointly miss. Subscriber-reported bid activity provides a second frame where available and is worth soliciting for that reason. The estimate is reported per subscriber's actual market rather than nationally, because a national coverage figure is meaningless to a contractor working three counties. Internally the same measurement redirects the research organization — the firm's dominant cost — from wherever sources are easiest toward the markets and project types where coverage is measurably weakest, which is where subscriber churn originates. And published coverage by market becomes a claim no competitor can match without doing the same work.

## Who Feels the Pain
Contractors losing bids on projects they never saw and not knowing why; sales teams selling a count against a competitor's larger count; the research organization allocating effort without knowing where the gaps are; and renewal rates, since a subscriber who repeatedly misses local work eventually concludes the product does not cover their market.

## Impact If Fixed
Replaces a supply-side vanity metric with the number subscribers actually decide on, and directs the largest cost in the business at measured gaps. In a segment where two large competitors both claim comprehensive coverage, being the one that can state a rate by market is the strongest available position.
