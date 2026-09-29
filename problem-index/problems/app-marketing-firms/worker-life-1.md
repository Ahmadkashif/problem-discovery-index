# The UA Manager With Four Sets of Numbers

**Industry:** [[app-marketing-firms|App Marketing Firms]]
**Type:** Worker Life Changing
**One-liner:** Every network reports its own installs, the MMP reports different ones, SKAN reports something aggregated and late, finance reports the revenue, and the UA manager allocates a seven-figure budget across the disagreement every Monday.
**Tags:** #gradient-boosting #time-series-forecasting #change-point-detection #confidence-intervals #large-language-models #evaluation-metrics #worker-facing #data-integration

## The Problem
A user acquisition manager runs spend across eight to fifteen networks. Each has its own dashboard, its own attribution logic and its own claim on every install. The mobile measurement partner deduplicates according to its rules and reports a different total. SKAN postbacks arrive aggregated and delayed with a share of campaign identifiers suppressed. Finance reports actual revenue, on a different calendar, net of store fees and refunds.

Monday is reconciliation. Pull each network, pull the MMP, pull SKAN, pull revenue, normalise campaign taxonomies that drifted the moment two people started naming campaigns, and build the view that the allocation decision will be made from. Then adjust bids and budgets across every network, in every geography, by hand, in interfaces that mostly do not support bulk changes.

The cohort maturation problem runs underneath everything. A cohort acquired today will not reveal its value for months, so every decision is made on a prediction, and predictions from three days of data are revised substantially at day fourteen and again at day thirty. A manager who scaled a campaign on a strong day-three signal and watched it decay by day thirty carries that, and the loop is slow enough that the lesson arrives long after the spend.

## Why It Matters to the Worker
The role is quantitative and the person is usually good at it, and the majority of their week goes to assembling numbers rather than reasoning about them. That is a poor use of a scarce skill set and it is the thing UA managers consistently name when they leave.

The accountability is sharp and the control is partial. UA is measured on payback and return, and those outcomes depend on network algorithms the manager does not control, product retention they do not own, and an attribution system imposed by a platform owner. When payback slips, the UA manager explains it. When it improves, the product team's retention work usually deserves a share of the credit and rarely receives it.

The suppression problem adds a particular frustration: new campaigns, small geographies and tests are exactly where the data is nulled out, so the parts of the job that involve learning something new are the parts with the worst information. Exploration is therefore systematically discouraged by the measurement system, and the manager feels it as a series of decisions taken half-blind.

## What a Solution Looks Like
Reconcile once, automatically, and keep the disagreements visible. A standing view that shows each source, its definition and exactly why it differs from the others — attribution window, self-attribution rules, SKAN delay and threshold, revenue recognition — removes the weekly assembly and the recurring explanation, and anchoring the whole thing to finance is what makes it credible.

Report predictions as distributions with maturation. A day-three cohort estimate should arrive with the interval it deserves and with the historical revision pattern attached — cohorts like this one moved this much between day three and day thirty — so scaling decisions are made with the uncertainty visible rather than discovered later.

Automate the mechanical optimisation. Bid and budget changes within a manager's stated rules, applied across networks and geographies, with exceptions surfaced for judgement, is most of the manual work and none of the expertise.

Treat suppression as a measurement problem, not an absence. Modelling what can be inferred about nulled campaigns from the aggregate, and reporting it with honest uncertainty, gives back some of the exploration capacity the privacy threshold removed.

## Impact If Solved
Reconciliation and manual bid work consume most of a UA manager's week and produce no decisions. Returning that time to cohort analysis, creative strategy and incrementality testing is what separates a UA function that compounds from one that maintains — and honest uncertainty on immature cohorts directly reduces the most expensive recurring error in the discipline, which is scaling on a signal that had not settled.
