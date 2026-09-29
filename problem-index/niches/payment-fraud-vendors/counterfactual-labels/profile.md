# Counterfactual Label Acquisition

**Parent Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to obtain honest outcomes for the transactions the model declines — and whoever pays the visible short-term cost of that experiment first can say something about its own accuracy that no competitor can contradict or match.

## Profile
**Market Size:** ~$1.3B US
**Share of Parent Industry:** ~19% of category revenue
**Digital Adoption:** Very Low — almost nobody runs it
**Target Buyer:** Risk executive leadership
**Automation Potential:** Moderate — the mechanism is simple, the decision is commercial

## What Makes This a Distinct Niche
This contest is evidence acquisition. A small randomised approval allowance on transactions the model would decline produces unbiased labels in the region where the model is weakest, and a large network running it continuously would obtain the only honest estimate of false decline rates anywhere. The mechanism is trivial to build. The obstacle is that the cost is visible and immediate while the benefit is invisible and permanent, which makes this an executive decision rather than a technical one.

## Current Tools & Gaps
Occasional threshold experiments, merchant-requested policy tests and anecdotal decline analysis. The gaps: no continuous randomised allowance; no unbiased false decline estimate; experiments run ad hoc and not preserved; no methodology published; and no product built around the resulting evidence.

## Problems
- [[niches/payment-fraud-vendors/counterfactual-labels/build|🔨 Build: Buying the Missing Half]]
- [[niches/payment-fraud-vendors/counterfactual-labels/buy|🛒 Buy: Experimentation and Bandit Practice]]
- [[niches/payment-fraud-vendors/counterfactual-labels/fix|🔧 Fix: The Experiment Nobody Will Fund]]
