# The Fraud Pattern That Arrives Three Times

**Niche:** [[niches/embedded-finance-platforms/cross-programme-intelligence/profile|Cross-Programme Intelligence]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same attack hits programme after programme on the same rails and each one discovers it independently.
**Tags:** #graph-theory #change-point-detection #gradient-boosting #quick-win #automation #evaluation-metrics #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn the simultaneous view of hundreds of financial products built on identical infrastructure into predictions a single programme could never make — and whoever does it first defines what the position is worth beyond billing.

## The Problem
An attacker finds that a particular onboarding flow can be passed with a specific document pattern, or that a particular payout timing allows a balance to be drained before a reversal lands. It works on one programme. Two weeks later it works on another, because they share the infrastructure and the pattern generalises. By the time it is recognised as one attack rather than three incidents, it has run across a dozen programmes. The platform saw all of them and connected none of them.

## Why It's Still Broken
Incidents are handled per programme because the customer relationship is per programme, so the response is scoped to the affected account and nobody looks across. There is no mechanism to warn the other programmes, and no agreement covering what may be shared. Fraud teams sit inside the programmes rather than at the platform. And each incident feels like bad luck rather than the third instance of a pattern.

## What a Fix Looks Like
Connect the incidents. Match incident signatures across programmes so that the second occurrence is recognised as the second, which is the fix and is straightforward pattern matching over data the platform already holds. Watch for the same identifiers, devices and behavioural signatures moving between programmes, since attackers reuse infrastructure and that reuse is visible only from here. Alert the unaffected programmes when a pattern is detected, because the warning is worth far more than the postmortem and the mechanism to send it does not exist. Abstract the alert so it names the technique rather than the victim, which is what makes it shareable at all. Maintain a shared signature library, so a pattern seen once protects everyone after. Prioritise by which programmes share the exposed characteristic, since not every programme is vulnerable to every technique. Feed the signatures into onboarding and transaction rules automatically, rather than relying on each programme to act. Track how long a pattern takes to spread, because that number sets how fast the warning must move. Establish the sharing terms in the operating agreement, since the legal question is the real blocker and it is answerable. And measure losses avoided on programmes warned before they were hit, which is the number that funds it.

## Who Feels the Pain
Programmes attacked by techniques the platform had already seen; end customers losing money to a known pattern; fraud teams reinventing a response; and sponsor banks absorbing losses that were preventable.

## Impact If Fixed
Incident response is scoped to the affected programme because the relationship is, so nobody looks across. Signature matching over data already held turns the third occurrence into the second one's warning.
