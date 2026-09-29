# The Same Document, The Ninth Time

**Niche:** [[niches/identity-verification-vendors/reusable-verified-identity/profile|Reusable Verified Identity]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The person verified with this vendor for this customer four months ago and is being asked to do the whole thing again.
**Tags:** #quick-win #data-integration #automation #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to let a person verify once and prove it everywhere without the verifier becoming a tracker — and whoever makes that acceptable to relying parties and to the person removes the repetition the whole category is built on.

## The Problem
Cross-organisation reuse is hard. Reuse within one relationship is not, and it does not happen either. The same person opens a second product with the same institution, or returns after a lapsed application, or re-verifies for a periodic refresh, and is put through the full process again — same vendor, same document, same images, same risk of failing this time when they passed last time. The prior verification is in the vendor's own records.

## Why It's Still Broken
Verification was built as a per-transaction service, so each request is handled independently — a stateless design cannot recognise a returning person and nobody added the state. Retention policies limit how long results are kept, sometimes more tightly than necessary. Billing is per verification. And nobody measures the repeat rate, so the waste is invisible.

## What a Fix Looks Like
Recognise the person who already passed. Detect that this applicant has previously verified with this customer and surface the prior result, which is the fix and is a lookup within a single relationship. Apply a freshness policy rather than a binary reuse, since a verification from last month and one from three years ago are different and both are currently treated as nothing. Re-verify only what has changed or expired, as a document expiry or an address change needs checking and the face match from last month does not. Set retention deliberately to support reuse within what policy and law allow, rather than defaulting to the shortest interval. Report the repeat verification rate, which will be larger than expected and is the number that motivates the change. Let the customer configure the reuse policy, because their regulatory position determines what is acceptable. Tell the applicant their prior verification was used, since that is both reassuring and the honest thing to do. Handle the case where the prior result was a failure, as repeating an identical failing process helps nobody. Price reuse so the commercial incentive does not block it, which is the real obstacle. And measure applicant time saved, since that is the benefit that matters most to the person.

## Who Feels the Pain
People repeating verification with the same institution; applicants who passed once and fail the second time; customers paying twice for the same check; and support teams handling the complaints.

## Impact If Fixed
A stateless per-transaction design cannot recognise a returning person, and nobody added the state. Reuse within one relationship needs no federation, no liability framework and no new standard — only a lookup and a freshness policy.
