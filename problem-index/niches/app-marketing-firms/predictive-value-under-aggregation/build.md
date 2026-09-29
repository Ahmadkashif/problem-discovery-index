# Six Months of Value From a Few Bits

**Niche:** [[niches/app-marketing-firms/predictive-value-under-aggregation/profile|Predictive Value Under Aggregation]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Acquisition economics require predicting six-month user value from the first few days, and those days arrive as a few bits, with a random delay, nulled out entirely when the campaign is small.
**Tags:** #survival-analysis #bayesian-inference #confidence-intervals #entropy-cross-entropy-kl-divergence #evaluation-metrics #gradient-boosting #monte-carlo-methods #revenue-impact
**Contested on:** This niche is not terminal — designing what the bits encode and predicting value from them are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A team pays to acquire a user today and recovers the cost over months. To bid correctly they must estimate that user's eventual value from what is observable early. On one major platform what is observable is a single coarse value encoded in a handful of bits, arriving after a randomised delay, and suppressed entirely when a campaign's volume is below a threshold. Every acquisition decision the team makes rests on a prediction built from that, and almost nobody has measured how much error the arrangement imposes — the discipline optimises hard, with real rigour, against a quantity whose accuracy it has never established.

## Why Nobody Has Built This
The constraint arrived suddenly and the response was necessarily improvised, and improvisations that keep a business running are rarely revisited — the invention was impressive and the validation never followed. Measuring the error requires comparing predictions against realised long-run value, which takes months and a deliberate record. The schema choice is made once by whoever is available. And network-side optimisation absorbs some of the problem, which makes the remaining error easy to ignore.

## What to Build
Treat the whole pipeline as one estimation problem and measure it. Measure the prediction error end to end against realised value, which is the foundation and is what nobody does — the record required is simply the predictions made and the outcomes that followed, and without it every improvement is unverifiable. Decompose the error into its sources: schema coarseness, delay, suppression, model. This is the diagnostic that says whether to redesign the schema or improve the model, and it is the reason this niche has two sub-niches rather than one. Design the schema against measured information content, which is the first sub-niche's contest. Model delay and censoring explicitly rather than treating late data as missing, which is the second sub-niche's. Handle suppression as a structured missingness rather than as absence, since it is concentrated where new campaigns operate and biases exactly the decisions that matter most. Carry uncertainty into the bid, so a prediction with wide error informs a more cautious bid rather than the same bid. Pool across campaigns and apps to estimate what individual volumes cannot, which is where an agency or a platform has an advantage over a single advertiser. Validate against incrementality, connecting to that niche, since an accurate prediction of attributed value is still not a measure of what the spend caused. Rebuild as platform rules change, because the constraint moves and a pipeline tuned to last year's rules decays. And report prediction accuracy as a standing metric, since a discipline this numerate should not be operating without one.

## Target Customer
User acquisition teams and agencies, mobile measurement vendors, and the studios whose payback decisions rest on unvalidated predictions.

## Impact If Built
An improvisation that kept the business running was never revisited, and the discipline optimises rigorously against a quantity whose accuracy it has never measured. Decomposing prediction error into schema, delay, suppression and model is the diagnostic that says which half of the problem to fix.
