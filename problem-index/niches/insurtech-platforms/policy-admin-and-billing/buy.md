# Property-Based Testing Applied to Rating and Billing

**Niche:** [[niches/insurtech-platforms/policy-admin-and-billing/profile|Policy Administration & Billing]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Property-based and generative testing exist precisely for systems with combinatorial input spaces, insurance rating and billing are the canonical example of one, and both are tested with scenarios a person thought of.
**Tags:** #combinatorics-and-counting #hypothesis-testing #evaluation-metrics #confidence-intervals #automation #compliance #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in policy administration is fighting to get a product, rate or form change into production across every state it is filed in without breaking billing, reporting or reinsurance — and whoever shortens that cycle most takes the account.

## The Problem
Testing a rating change means constructing test policies and checking the premium. The number of combinations — coverages, limits, deductibles, endorsements, states, effective dates, classes — is vastly larger than any hand-built test suite, so the suite covers what someone thought of and the defects live in what nobody did. Billing is worse, because the interesting cases are sequences: an endorsement mid-instalment, followed by a cancellation, followed by a reinstatement, on an agency-bill account with a prior credit. Nobody writes that test until a policyholder finds it.

## What Already Exists
Property-based testing frameworks are mature and available in every major language, and the technique — specifying invariants and generating inputs to violate them — was developed for exactly this shape of problem. Model-based testing for stateful systems handles the sequence cases. Metamorphic testing addresses the case where the correct output is unknown but the relationship between outputs is knowable, which is precisely the rating situation. Snapshot and approval testing is trivial to adopt. None of this is new or expensive.

## The Customization Gap
The adaptation is to insurance's own invariants. It requires: (1) domain invariants stated explicitly — premium is monotonic in limit, adding a coverage never decreases premium, a mid-term endorsement's pro-rata plus the remaining instalments equals the endorsed annual premium — which is the intellectual work and which product analysts can supply once asked in these terms; (2) a risk generator that produces realistic rather than uniformly random policies, since uniform generation wastes effort on combinations that cannot occur and misses the density of real business; (3) stateful sequence generation for billing, modelling the policy lifecycle as a state machine and generating valid transition sequences, which is where the expensive defects are; (4) metamorphic relations across states and effective dates, comparing a change's effect in one state against another where the filing was identical, which catches configuration errors no single-output test can; and (5) failure shrinking presented in domain terms, so a found defect arrives as a minimal reproducing policy rather than as a generated blob.

## Target Customer
Core system vendors, carrier configuration and quality organisations, and the implementation partners running validation programmes.

## Impact If Solved
Property-based testing finds the combinatorial defects that manual suites structurally cannot, and the billing sequence cases in particular are where carriers currently absorb both remediation cost and policyholder trust. The technique is free and mature; the adaptation is stating the invariants, which is a fortnight of a product analyst's time and has never been asked of one.
