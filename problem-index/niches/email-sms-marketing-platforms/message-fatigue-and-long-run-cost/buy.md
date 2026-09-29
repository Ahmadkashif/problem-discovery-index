# Customer Lifetime Value Practice

**Niche:** [[niches/email-sms-marketing-platforms/message-fatigue-and-long-run-cost/profile|Message Fatigue & Long-Run Cost]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lifetime value modelling is standard practice for acquisition decisions, and nobody applies it to the decision to send another message.
**Tags:** #survival-analysis #bayesian-inference #time-series-forecasting #confidence-intervals #evaluation-metrics #causal-inference #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to price what an extra message costs in the recipient's future willingness to hear from a brand — and whoever measures that changes how much the whole channel sends.

## The Problem
Customer lifetime value modelling is routine. Businesses estimate how much a customer will be worth, discount future value, and use it to decide acquisition spend, retention investment and segmentation. The methods — survival models, buy-till-you-die formulations, cohort analysis — are well established and widely implemented. The same businesses then decide messaging frequency by convention, despite messaging being one of the few marketing actions that directly and measurably damages the lifetime value they are otherwise careful to model.

## What Already Exists
Lifetime value and survival modelling; buy-till-you-die and probabilistic customer models; cohort retention analysis; discounting of future cash flows; and customer equity frameworks.

## The Customization Gap
The adaptation is from valuing a customer to pricing an action that depletes them. It requires: (1) lifetime value as a state that a controllable action degrades, rather than as a quantity to predict — this makes it a decision variable rather than a forecast and is the conceptual change; (2) a depletion-and-recovery dynamic, since responsiveness falls with sending and returns with rest, which standard models do not represent; (3) causal estimation rather than prediction, because the question is what sending did rather than what a customer is worth, and observational lifetime value models cannot answer it; (4) per-message decisions at enormous volume, so the model must be cheap to evaluate at send time; and (5) a platform-level measurement across many brands, since the depletion parameters generalise and no single brand can estimate them well.

## Target Customer
Messaging platform data teams, brand analytics functions, and lifetime value vendors for whom message fatigue is an unmodelled cost.

## Impact If Solved
Businesses model lifetime value carefully and then choose send frequency by convention, despite messaging being the action that most directly depletes it. Treating lifetime value as a state a controllable action degrades turns a forecast into a decision variable.
