# Save Offers Priced by Measured Uplift

**Niche:** [[niches/wireless-carriers/postpaid-retention-lifecycle/profile|Postpaid Phone Retention & Upgrade Lifecycle]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers spend billions on retention offers chosen by churn score, and almost none of it is tested against customers who would have stayed anyway.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #hypothesis-testing #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche (decisioning platforms, retention analytics vendors and the carriers' own lifecycle teams) is fighting to pick, line by line, the cheapest save offer that actually changes a postpaid customer's decision to port out, and whoever measures save-offer uplift most accurately takes the account.

## The Problem
A carrier's retention programme ranks lines by predicted churn and sends the riskiest ones an upgrade offer, a loyalty credit or a save-desk call. High churn risk is not the same as persuadability. Some high-risk customers leave whatever the offer, and many offers go to customers who would have stayed for free. Without holdouts the programme can't tell the difference, so its reported saves are mostly customers who were never leaving.

## Why Nobody Has Built This
Holdouts feel like deliberately losing customers, so marketing teams resist them. Retention budgets are set by campaign and channel, not by incremental line, and the data needed (offers, responses, port-outs, device and promotion states) spans systems owned by different departments.

## What to Build
An uplift engine that keeps a small randomised holdout in every retention action and estimates, per line, the incremental reduction in 90-day port-out probability from each available offer. It conditions on promo-credit end dates, device payoff, network experience on the customer's usual sectors, household line count and recent competitor offers. It then allocates the budget where uplift per dollar is highest, refreshing as outcomes arrive.

## Target Customer
Heads of retention and customer lifecycle analytics at national and regional carriers, and at large cable operators' mobile brands.

## Impact If Built
Moving even a tenth of retention spend from customers who would have stayed to customers an offer actually keeps is worth hundreds of millions a year to a national carrier (estimate), and gives finance a retention number it can audit.
