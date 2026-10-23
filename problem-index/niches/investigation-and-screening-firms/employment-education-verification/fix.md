# Pass-Through Fees Decided Order by Order

**Niche:** [[niches/investigation-and-screening-firms/employment-education-verification/profile|Employment, Education & Licence Verification]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Whether a verification goes to a fee-charging database or a free phone call is decided by each specialist on each order, and employers dispute the fees on their invoices months later.
**Tags:** #logistic-regression #decision-trees #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to close an employment, education or licence verification without a human phone call, and whoever answers the most verifications from direct, instant sources takes the account.

## The Problem
Instant verification databases and third-party verifiers charge per request, and screeners usually pass the fee to the employer. Some employers cap pass-through fees or require approval above a threshold; others want speed whatever it costs. Specialists choose route by habit, and the employer sees the result only on the invoice, where disputed fees become credits and account friction.

## Why It's Still Broken
Client fee preferences are written in contracts and onboarding notes, not in the routing logic, and nobody has data on when the paid route actually saves time over a call.

## What a Fix Looks Like
Encode each client's fee policy (cap, approval threshold, speed priority) as a routing rule, and attach to each order the expected time saved by the paid route from the firm's history. Route automatically within policy, request approval when outside it, and show the fee decision and reason on the report.

## Who Feels the Pain
Account managers handling invoice disputes; specialists second-guessed on routes; employers surprised by fees.

## Impact If Fixed
Fee disputes fall, verification spend matches what each employer actually values, and specialists stop making a commercial decision on every order.
