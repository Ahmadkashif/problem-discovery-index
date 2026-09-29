# The Renewal Increase Set by a Rule

**Niche:** [[niches/proptech-platforms/institutional-multifamily-platforms/profile|Institutional Multifamily Platforms]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Most of a multifamily portfolio's revenue comes from renewals, renewal offers are set by a percentage rule applied by tier, and the operator holds complete first-party evidence on what every resident has accepted before and what a turn actually costs.
**Tags:** #logistic-regression #survival-analysis #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #causal-inference
**Contested on:** Every serious competitor in multifamily revenue management is now fighting to price a unit well using only what one operator legitimately knows about its own demand — and whoever prices accurately without pooled competitor data takes the market.

## The Problem
A resident's lease expires in ninety days. The renewal offer is last year's rent plus a percentage set by a policy, possibly adjusted by a tier. Whether this particular resident accepts at that increase, and what it costs if they do not — the turn, the vacancy, the leasing effort, the concession the new resident will require — is not computed. Some residents would have renewed at a considerably higher increase and were offered less. Others were pushed out by an increase that cost more in turn and vacancy than the increase would ever have earned. Both errors happen constantly and neither is measured.

## Why It's Still Broken
Renewal has been treated as an administrative process rather than as a pricing decision, partly because the revenue management products were built around new-lease pricing where the competitor data was relevant. The turn-and-vacancy cost that sits on the other side of the decision is real, unit-specific and knowable — the platform holds the turn history — and is instead represented by a portfolio average or by nothing. And there is an institutional preference for a uniform rule, because a rule is explainable to residents and to an owner in a way a per-resident number is not.

## What a Fix Looks Like
Compute both sides of the trade per resident and per unit. Acceptance probability at a given increase is estimable from the operator's own renewal history with resident tenure, prior acceptances, payment history, unit type and season as covariates — first-party data throughout. Turn cost is estimable from the unit's own condition and the operator's realised turn costs for comparable units, not from an average. Expected vacancy duration follows from the unit type and season. The offer that maximises expected revenue then falls out, with the range shown. Keep a uniform policy where the operator wants one, but let them see what it costs — the report showing which renewal decisions the rule got wrong in both directions is the artefact that changes practice. And measure concession effectiveness at renewal, which is currently pure assertion.

## Who Feels the Pain
Asset managers whose largest revenue lever is governed by a policy nobody has tested; site teams turning units that did not need to turn; and residents pushed out by an increase that made nobody better off.

## Impact If Fixed
Renewal is the majority of the revenue decision in a stabilised portfolio and is the least optimised part of it. Both sides of the calculation come from first-party data, which makes this the safest capability in the niche to build under the current legal constraint and the one with the fastest payoff.
