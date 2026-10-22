# A Fac Desk That Has Read Every Survey Before

**Niche:** [[niches/reinsurers/facultative-underwriting/profile|Facultative Reinsurance Underwriting]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A fac underwriter reads a ~60-page engineering survey for each risk while the reinsurer's archive of thousands of past surveys, quotes and losses sits unsearched.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #gradient-boosting #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to read an individual-risk submission (engineering survey, statement of values, loss runs) and return a priced line inside the broker's turnaround, and whoever answers fastest without missing the risk's worst feature takes the account.

## The Problem
Each submission contains a risk engineering report, a statement of values and loss runs. The decisive facts — sprinkler impairments, hot-work controls, a recommendation outstanding from the last survey, a loss trend in the runs — are scattered across pages. The underwriter's judgement is good but bounded by what they have personally seen.

## Why Nobody Has Built This
Fac volumes are small next to primary commercial lines, the documents vary widely, and past files were never structured, so no vendor has built for the fac desk specifically.

## What to Build
Extraction of survey findings, protections, hazards and open recommendations into a structured record; retrieval of the most similar past risks the reinsurer quoted, wrote or declined, with their terms and loss outcomes; and a short brief that leads with the risk's worst features, so the underwriter starts from the decision rather than the reading.

## Target Customer
Heads of property and casualty facultative at reinsurers and at the fac units of large carriers.

## Impact If Built
Faster, better-informed quotes on mid-sized risks, where speed wins the line, and fewer missed hazards on the large ones.
