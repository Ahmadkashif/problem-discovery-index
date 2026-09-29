# Buy: Lead Scoring Adapted to a Market Where the Lead Pays

**Niche:** [[niches/freelance-marketplaces/proposal-and-bidding/profile|Proposal & Bidding]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sales lead scoring solves this exact prediction problem for a company's own pipeline; here the scored opportunity is someone else's job post and the person who needs the score is the one being charged to pursue it.
**Tags:** #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #feature-engineering #survival-analysis #automation #revenue-impact
**Contested on:** Whether lead-scoring machinery built for a sales team's own funnel can serve a scored population the platform is monetising.

## The Problem

Predicting whether an opportunity will close is the most commercially developed prediction problem in software. Every CRM has lead and opportunity scoring, propensity models, forecast categories and win-probability displays, built on exactly the structure this problem has: an opportunity with attributes, a pursuit cost, and a binary outcome observed later.

A marketplace could point that machinery at its job feed in a quarter. What does not transfer is everything about who the score is for. In a sales organisation the scorer, the pursuer and the beneficiary are the same company. Here the platform scores, the freelancer pursues, and the platform earns from the pursuit — which changes the product requirements far more than the modelling.

## What Already Exists

Salesforce Einstein, HubSpot predictive scoring, Clari, People.ai and the revenue-intelligence category. Underneath them, gradient-boosted classifiers over opportunity features with calibration layers and explanation surfaces, all mature. The modelling is genuinely commodity; a competent team gets a working award-probability model from the platform's own history in weeks.

## The Customization Gap

**The scored party and the paying party are different, and the platform profits from the pursuit.** No CRM has a concept for this. The product decisions it forces — whether to show the score at all, whether to show it before or after the credit is spent, whether to let freelancers filter on it — are governance decisions, not modelling ones, and they need a stated policy the vendor cannot supply.

**Two models multiply, and CRMs only build one.** Win probability in a CRM assumes the deal happens and asks who wins. Here the dominant uncertainty is whether the job is awarded to anybody, and that is the number with the most value to the freelancer. Separating post-level award probability from conditional per-freelancer win probability, and surfacing their product, is a structural change to how the score is defined.

**Calibration standards are far higher.** A sales team tolerates a lead score that ranks correctly but is numerically off, because it is used to prioritise a list. A freelancer uses the number to decide whether to spend an evening and a credit, and treats a miscalibrated 30% as a lie. The pipeline needs reliability measurement as a first-class, continuously reported output, which CRM scoring products conspicuously do not provide.

**Feedback is censored and self-fulfilling in a way CRMs do not model.** A post shown as low-probability receives fewer proposals and is therefore less likely to be awarded, and the model trains on its own effect. Standard scoring stacks have no exploration mechanism and no propensity logging, and without both the model degrades into a prophecy.

**The features are text and behaviour, not firmographics.** Enrichment vendors that power CRM scoring — company size, industry, funding — have nothing to say about an individual client posting a logo job. The predictive signal is in the brief's specificity, the budget's realism relative to the scope, and the client's own posting history, which means the feature engineering is bespoke even though the model is not.

## Target Customer

Marketplace data teams that have been asked for bid guidance and are evaluating whether to adapt the revenue-intelligence stack their go-to-market team already licenses. Also the third-party tooling vendors building freelancer-side assistants, who have the harder version of the problem because they lack the outcome labels and must infer awards from public signals.

## Impact If Solved

The commodity modelling gets reused and the five adaptations make it honest. The concrete result is a number a freelancer can budget an evening against, and a platform that has decided, deliberately and on the record, whether it is willing to show it.
