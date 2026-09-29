# Collection Coverage as a Measured Rate Per Market

**Niche:** [[niches/event-planning/meetings-intelligence-data/profile|Meetings & Events Intelligence Data]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is a record of meetings that happened, assembled by human observation of a population nobody enumerates, and it is sold on how many records it contains rather than on what share of the market it caught.
**Tags:** #bayesian-inference #probability-distributions #confidence-intervals #hypothesis-testing #monte-carlo-methods #evaluation-metrics #feature-engineering #optimization-fundamentals #data-integration #revenue-impact

## The Problem
A hotel sales team buys this data to find accounts that book group business in their market. The value depends entirely on coverage — what fraction of meetings in that market the collection actually observed — and coverage is never stated. It is certainly uneven: strong in markets with dense property coverage and cooperative sources, thin where collection is harder, and systematically biased toward properties and event types that are easier to observe. A salesperson reading an account's meeting history cannot tell whether the gaps mean the account did not meet or the collection did not see it, and those imply opposite actions. Internally, coverage is managed as researcher assignment and record volume, which are supply-side measures.

## Why Nobody Has Built This
Estimating what was missed requires knowing about meetings the collection never observed, which is the same structural difficulty that appears everywhere in this sweep where a coverage claim is made. The tractable route is triangulation — overlap between independent collection channels, comparison against venue-side occupancy and event calendars where obtainable, and capture-recapture logic across collection waves — and none of it is trivial. Commercially, record count wins a bake-off and a coverage rate invites an unflattering number, so no competitor forces the issue.

## What to Build
Coverage estimated as a rate per market and property tier, using overlap between independent collection channels to estimate what all channels jointly miss, and calibrated where external frames exist. Reported to the subscriber for their own market rather than nationally, because a national figure means nothing to a sales team working one city. Records then carry an explicit distinction between observed absence and unobserved period, which is the difference a salesperson needs and currently has to guess at. Internally the same estimate redirects the research operation — the dominant cost — from wherever collection is easiest toward the markets and segments where coverage most limits the product's usefulness, which is where subscriber churn originates. And a stated coverage rate per market becomes a claim no competitor selling record counts can match.

## Target Customer
VPs of research and chief data officers at meetings intelligence providers running 100-400 researchers, and the hotel sales leaders who prospect against these records and cannot tell a gap from a fact.

## Impact If Built
Replaces a supply-side vanity metric with the number subscribers actually decide on, and points the largest cost in the business at measured gaps rather than at collection convenience.
