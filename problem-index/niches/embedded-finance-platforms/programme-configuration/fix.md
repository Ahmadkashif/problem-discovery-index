# Found Out at Bank Review

**Niche:** [[niches/embedded-finance-platforms/programme-configuration/profile|Programme Configuration]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The programme is built, tested and ready, and the sponsor bank's review says the fee structure is not acceptable for this customer segment.
**Tags:** #compliance #workflow-orchestration #automation #quick-win #optimization-fundamentals #evaluation-metrics #worker-facing #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to turn the twenty programme archetypes that keep getting rebuilt by hand into configurable starting points that carry their bank-specific constraints with them — and whoever does it takes launch time from months to days.

## The Problem
Eight weeks of implementation, and the bank review comes back with three findings: the fee schedule will not pass for this segment, the onboarding flow needs an additional disclosure, and the limits proposed are above what this bank allows for a programme of this type. Every one of those was knowable on day one. The solutions engineer probably suspected two of them. None of it was checked, because there was nothing to check against — the constraints exist as accumulated experience, not as a document or a rule.

## Why It's Still Broken
Bank constraints are communicated in review rather than in advance, so the process is structured as approval rather than as validation, and nobody inverted it. The constraints live in solutions engineers' heads and in the memory of past rejections. Each bank differs and none publishes a specification. And the delay is absorbed by the customer, who has no alternative.

## What a Fix Looks Like
Write the constraints down and check early. Extract the constraints from the history of bank review findings, which is the fix and is a corpus every platform has and none has mined. Encode them as checks that run against a programme configuration, so the finding arrives on day one instead of week eight. Publish the known constraints to implementation teams, since most of the delay is knowledge asymmetry rather than genuine disagreement. Run the check before build rather than after, because the cost of a finding scales with how much was built on the assumption. Record every review finding in a structured form, so the constraint library grows from the reviews themselves rather than from a documentation effort nobody funds. Flag the constraints that are uncertain rather than pretending the model is complete, since an honest maybe still saves the eight weeks. Track findings per bank, which reveals both the strict partners and the ones whose policy is drifting. Route a genuinely novel proposal to early bank conversation instead of to build, because that is where pre-submission discussion pays. Reuse findings across programmes, since the same rejection keeps arriving. And measure review cycles per launch, which is the number that shows whether the library is working.

## Who Feels the Pain
Implementation teams rebuilding after review; customers whose launch slips two months; solutions engineers repeating constraints nobody wrote down; and bank reviewers reading proposals that never had a chance.

## Impact If Fixed
The process is structured as approval and nobody inverted it into validation. Mining past review findings into configuration-time checks moves the finding from week eight to day one using a corpus that already exists.
