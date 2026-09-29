# Confirmation Strength Is Not Surfaced to the Party Acting On It

**Niche:** [[niches/funeral-homes/death-verification-data-providers/profile|Death Verification Data Providers]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Fix (Pain Point)
**One-liner:** A death confirmed by a state vital record and one inferred from a single obituary match are returned in the same format, and the customer terminates a benefit on either.
**Tags:** #confidence-intervals #probability-distributions #evaluation-metrics #descriptive-statistics #bayesian-inference #feature-engineering #compliance #worker-facing #data-integration #hypothesis-testing

## The Problem
Records enter the file from very different sources with very different authority — a state registration, a funeral home submission, an obituary, a credit or utility signal, a third-party compilation. Some are near-certain; some are inferences that could be a name collision. The returned result does not distinguish them. Customers then take irreversible action on both: a benefit is stopped, an account is frozen, a policy is paid out. When a confirmation turns out to be wrong, the harm falls on a living person who must prove they are alive, which is a well-documented and reputationally severe failure mode in this industry, and it originates in a distinction the provider holds internally and does not pass on.

## Why It's Still Broken
The product has been sold as a lookup — the question is binary, so the answer is presented as binary — and provenance is captured for internal quality management in codes that mean nothing to a customer. There is also a commercial reflex against qualifying an answer: a competitor returning a confident yes looks stronger in a bake-off than one returning a qualified yes. And customers have not demanded it, because they have not seen a product that offered it and do not know how much the underlying evidence varies.

## What a Fix Looks Like
Confirmation strength as a returned, first-class property: the source class, the number of independent corroborating sources, the match confidence, and the resulting probability that this specific individual is deceased — with a simple, consistent tier a customer's system can act on programmatically. Downstream that lets a customer route by strength rather than treating all confirmations alike: act immediately on state-registered confirmations, hold and verify on single-source inferences, which is what a careful administrator would do if they could see the difference. Internally the same surfacing turns source quality into a measurable property that acquisition and matching investment can be managed against. And it gives the provider the strongest available answer to the failure that most damages this industry — the living person declared dead — which is that the confirmation was flagged as weak and the customer's own policy determined what happened next.

## Who Feels the Pain
Living people whose benefits stop and who must prove they exist; benefit administrators making irreversible decisions on evidence of unknown strength; compliance teams unable to document why a termination was reasonable; and the provider, whose reputation is set by its worst confirmations rather than its average.

## Impact If Fixed
Addresses the industry's most serious harm using information already held internally, and converts a binary lookup into a decision-support product that different customers can use according to their own risk posture. In a market where competitors return confident answers from the same kinds of sources, showing the basis is the stronger position rather than the weaker one.
