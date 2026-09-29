# Win Probability From Outcomes the Platform Can Observe

**Niche:** [[niches/grant-writers/grant-opportunity-prospect-platforms/profile|Grant Opportunity & Funder Research Platforms]]
**Industry:** [[industries/grant-writers|Grant Writers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform matches nonprofits to opportunities but never learns which matches were won, so it recommends without ever being scored.
**Tags:** #logistic-regression #gradient-boosting #ml-recommendation #survival-analysis #evaluation-metrics #revenue-impact

## The Problem
A federal proposal takes 40-80 hours to write and wins 10-25% of the time. The platform's entire value proposition is telling a nonprofit which of the thousands of open opportunities are worth that investment — and it makes that call on stated eligibility and keyword overlap. It does not know, for any recommendation it has ever made, whether the organization applied and whether it won.

The research team maintains rich funder profiles and a matching engine, and the match score is the product. But nothing closes the loop. A funder that has quietly stopped making new grants in a programme area, a programme whose awards all go to organizations above a size the platform does not check, an agency that has funded the same twelve institutions for a decade — these are visible in outcomes and invisible in eligibility criteria. Every user learns them the expensive way, one 60-hour proposal at a time.

## Why Nobody Has Built This
The platform's revenue does not depend on being right. Subscriptions renew on coverage and convenience — how many opportunities, how current, how easy to search — and a customer who loses a competitive grant blames the competition, not the recommendation. There has never been commercial pressure to measure match quality, so no mechanism to measure it was ever built.

The outcome data is also assumed unavailable. It is not. Federal awards are published; foundation grants appear in annual filings; and the platform can ask users directly, because the user has an immediate reason to tell it — an applicant who reports an outcome wants better recommendations next time. What is missing is the deliberate decision to collect it.

## What to Build
A win-probability layer that sits under the existing matching engine and is trained on realized outcomes.

Three components. First, **outcome capture**: resolve published award records back to the opportunities in the platform's own catalogue, and prompt users on the applications they told the platform they were pursuing. Second, **a calibrated model** predicting probability of award given applicant characteristics, opportunity characteristics, and the funder's award history — calibrated, because a nonprofit deciding whether to spend 60 hours needs a probability it can trust, not a rank. Third, **expected-value ranking**: probability times award size against the effort the opportunity demands, so a 40% chance at $50,000 sorts correctly against a 6% chance at $2M.

The funder-level signal is the interesting part. Award histories show concentration patterns no eligibility statement admits to — a de facto minimum organizational size, a geographic preference, a strong prior toward previous grantees. Surfacing those explicitly turns the researcher-maintained funder profile from a description into a prediction.

## Target Customer
VP of Research or Chief Product Officer at a funder research platform. The commercial argument is straightforward: a competitor that can say what proportion of its recommended opportunities were won has a claim no incumbent in this market can currently make.

## Impact If Built
The nonprofit sector spends an enormous quantity of professional labour writing proposals that had no realistic chance. Redirecting even a fraction of it toward opportunities with genuine fit is a direct increase in funded programme work at zero additional cost. For the platform, it converts a searchable database — a category under permanent pricing pressure — into a service whose accuracy compounds with every cycle it runs.
