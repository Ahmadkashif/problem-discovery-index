# Heavy-Tail Estimation

**Parent Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to identify, from a few days of behaviour, the small fraction of players who will produce most of a cohort's value — and whoever does it takes the account.

## Profile
**Market Size:** ~$6B US
**Share of Parent Industry:** ~15% of category spend
**Digital Adoption:** High but mis-specified
**Target Buyer:** UA data science
**Automation Potential:** Very high — modelling over existing cohort data

## What Makes This a Distinct Niche
This half is a modelling problem over data the UA function already holds. Given a cohort's first days of behaviour, what is the distribution of value it will produce — and specifically, how many high-value players does it contain. It requires nothing from anyone outside the UA team, improves bidding directly, and can be bought and deployed without changing how the function is measured or what anyone believes lifetime value is a property of.

## Current Tools & Gaps
A gradient-boosted model on aggregate early features, trained on mean squared error. The gaps: no distributional output; no tail-specific evaluation; no separation of the become-a-spender event from the conditional value; no use of full behavioural sequences; and no per-source tail calibration.

## Problems
- [[niches/game-user-acquisition-firms/heavy-tail-estimation/build|🔨 Build: Finding the Few Who Matter]]
- [[niches/game-user-acquisition-firms/heavy-tail-estimation/buy|🛒 Buy: Rare Event Modelling From Fraud and Medicine]]
- [[niches/game-user-acquisition-firms/heavy-tail-estimation/fix|🔧 Fix: Predicting a Mean for a Distribution That Has None Worth Having]]
