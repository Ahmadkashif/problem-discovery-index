# Marketing Attribution Vendors

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$3B US for measurement and attribution software and services, spanning multi-touch attribution, marketing mix modelling, incrementality testing and the mobile measurement partners
**Tech Maturity:** Statistically serious, epistemically unresolved. Rockerbox, Measured, Northbeam, Haus, INCRMNTAL, Recast and Prescient AI sit alongside the older mix-modelling houses and the open-source implementations from Meta and Google. The modelling is often genuinely good; the category's problem is that it sells answers to a causal question from observational data and has no accepted way to check whether any given answer is right.
**Workforce:** Marketing scientists and econometricians, measurement consultants and customer success scientists, data engineers on identity and ingestion, experiment designers, client-side analytics teams

## Key Pain Themes
Three methods compete and none is sufficient alone. Multi-touch attribution assigns fractional credit along observed paths and was undermined first by its own correlational logic and then by the collapse of cross-site identity; it survives mostly because clients are used to it. Marketing mix modelling has returned as the serious answer and is underdetermined in ways practitioners understate — channel spends move together, adstock and saturation curves are specification choices, and priors frequently do more work than the data. Incrementality experiments answer the question correctly and cost money, take weeks, and at most advertisers' scale detect only large effects.

The consequence is that two vendors modelling the same business return materially different channel contributions, and the client is advised to triangulate. Triangulation between three methods with unknown biases is not a methodology, and everybody involved knows it.

The deeper issue is validation. These vendors sell a number that reallocates budget, and almost none of them systematically backtest their own output against experimental ground truth — not because it is impossible, but because the client would then see how often it is wrong. A category whose entire product is measurement has no accepted measurement of itself.

## Current Tech Landscape
Open-source mix modelling — Meta's Robyn, Google's Meridian, PyMC-Marketing — has commoditised the core technique and shifted the value to specification, priors and validation. Geo-experiment tooling from Haus, Measured and Google's own libraries makes randomised testing practical and remains underused. Server-side tagging, conversion APIs and consent-mode modelled conversions have partly replaced the identity layer that MTA depended on, with each platform modelling its own gaps. The mobile side runs on AppsFlyer, Adjust, Branch and Singular under SKAdNetwork and its successors, where aggregation and delay are imposed by the operating system rather than chosen.

## Problems
- [[problems/marketing-attribution-vendors/high-impact|🔴 High Impact: Selling a Causal Answer With No Way to Check It]]
- [[problems/marketing-attribution-vendors/low-impact-1|🟡 Low Impact: Mix Model Specification and Identifiability]]
- [[problems/marketing-attribution-vendors/low-impact-2|🟡 Low Impact: Conversion Collection and Consent Gaps]]
- [[problems/marketing-attribution-vendors/worker-life-1|🟢 Worker Life: The Marketing Scientist Defending the Number]]
- [[problems/marketing-attribution-vendors/worker-life-2|🟢 Worker Life: The Analyst With Five Sources of Truth]]
- [[problems/marketing-attribution-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/marketing-attribution-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This category exists because advertisers need a causal answer and the data available is observational. Every technique it sells is a different way of guessing at a counterfactual, and the one method that does not guess — randomised experiment — is the one the category treats as an occasional supplement rather than as the foundation. The opportunity is inversion: make experiments the ground truth and treat every model as an interpolator between them, continuously validated against the next experiment it failed to predict. That is a product nobody sells, it is buildable from tools that already exist, and it is resisted because it would make each vendor's error rate visible — which is also precisely why the first vendor to do it credibly would reset the category's terms.
