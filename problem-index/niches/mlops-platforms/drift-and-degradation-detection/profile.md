# Drift & Degradation Detection

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to tell a model owner that their model has stopped working before a business metric does — and whoever does that takes the account, because that is the question the whole category was bought to answer.

## Profile
**Market Size:** ~$310M US, existing as a separate industry
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Low — drift is detected, degradation is not
**Target Buyer:** Model owners and the business functions their models serve
**Automation Potential:** Very High — every computation is mechanical and continuous

## What Makes This a Distinct Niche
A model is deployed, performs as evaluated for a while, and then stops — because the input distribution moved, because the relationship between inputs and outcome changed, or because something upstream broke. The first signal is usually a business metric weeks later. This became a separate industry precisely because the training platforms declined to extend into it, which leaves a seam: the monitoring vendors have the production signals and not the training context, and the training vendors have the context and not the signals. The contest is degradation rather than drift. Input drift is easy to compute and frequently harmless; the thing that matters is whether the model's decisions are still good, and that requires outcomes, which arrive late, unevenly, and only for the cases the model acted on.

## Current Tools & Gaps
Model monitoring products computing input and prediction drift, data quality checks, and performance measurement where labels are available. The gaps: drift alerts that fire on harmless distribution movement and are muted within a month; no estimate of performance when labels have not arrived yet, which is the normal situation; no handling of feedback loops, where the model's own decisions determine which outcomes are ever observed; and no connection back to the training run that would say whether the current data is still inside what the model saw.

## Problems
- [[niches/mlops-platforms/drift-and-degradation-detection/build|🔨 Build: The Business Metric Moves Weeks Later]]
- [[niches/mlops-platforms/drift-and-degradation-detection/buy|🛒 Buy: Statistical Process Control and Sequential Monitoring]]
- [[niches/mlops-platforms/drift-and-degradation-detection/fix|🔧 Fix: Drift Alerts That Fire on Nothing]]
