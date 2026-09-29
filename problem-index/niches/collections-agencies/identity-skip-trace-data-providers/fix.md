# Confidence Is a Sorted List, Not a Stated Probability

**Niche:** [[niches/collections-agencies/identity-skip-trace-data-providers/profile|Identity Resolution & Skip Trace Data Providers]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A search returns candidate addresses and numbers in order of an internal score nobody outside can interpret, so the customer's dialler treats the first three as equivalent and the consequences of being wrong land on whoever answers.
**Tags:** #probability-distributions #confidence-intervals #evaluation-metrics #logistic-regression #bayesian-inference #hypothesis-testing #cross-validation #compliance #worker-facing #data-integration

## The Problem
Results come back ranked, with a score that reflects internal linkage strength and has no external meaning. The customer needs a different quantity: the probability that this number reaches this specific person right now. Those diverge in ways that matter — a link can be strong on historical evidence and stale in fact, which is exactly the case that produces a call to a reassigned number and a statutory damages claim. Because the score cannot be interpreted as a probability, agencies build their own thresholds from experience, apply them inconsistently, and dial down the list until something works. The provider's most consequential output is a ranking whose meaning every customer has to reconstruct for themselves.

## Why It's Still Broken
Calibration requires outcome data the provider has not systematically collected, which is the same root cause behind the other gaps here. Ranking is also sufficient for the search interface's core job and was never challenged: sorting is what a search product does. And there is an unspoken commercial logic in ambiguity — a stated probability of sixty percent invites the customer to ask why they are paying for it, whereas a top-ranked result implies confidence without asserting it. That logic no longer holds now that a wrong dial carries statutory liability, but the product has not caught up.

## What a Fix Looks Like
Calibrated probability as the returned quantity, with the components separated. A result should express both the strength of the identity link and the currency of the contact point, because those fail differently and the customer acts on them differently — a strong link to a stale number is a mail candidate, not a dial candidate. Calibration is estimated against field outcomes and validated continuously, with the model reporting when it is operating outside the population it was calibrated on rather than extrapolating silently. Presentation matters as much as the statistics: a dialler integration should receive a number it can threshold against its own risk tolerance, and a compliance team should be able to document why a contact attempt was reasonable, which is a defence they cannot currently mount. Where the provider genuinely does not know, saying so is more valuable than a rank, because the customer can route that account to a different treatment rather than dialling into liability.

## Who Feels the Pain
Agencies dialling down a list without knowing what the ranking means; compliance officers who cannot evidence the basis for a contact attempt; consumers who are called about someone else's debt because a reassigned number ranked first; and the provider, whose product is judged on wrong-party contacts it gave the customer no way to avoid.

## Impact If Fixed
Directly addresses the industry's largest liability exposure, which makes it a compliance purchase rather than a data purchase and changes both the buyer and the price. Separating link strength from contact currency is also a straightforward product improvement that competitors would have to rebuild their outcome loop to match.
