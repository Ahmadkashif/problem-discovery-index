# Build: Results, Reasons and Reusable Assessments

**Niche:** [[niches/talent-assessment-platforms/the-candidate/profile|The Candidate]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Give the candidate their own results, a real reason for the outcome, and a way to reuse a completed assessment rather than retaking an equivalent one for every employer.
**Tags:** #confidence-intervals #descriptive-statistics #evaluation-metrics #compliance #large-language-models #workflow-orchestration #worker-facing #quick-win
**Contested on:** Whether an assessment result can be made portable between employers without compromising the instrument.

## The Problem

A candidate completes an assessment. Everything they produced is computed, scored, banded and delivered to the employer. They receive nothing.

Then they apply elsewhere and take an equivalent instrument — frequently the same underlying construct, sometimes the same publisher's test — for the same job family, a fortnight later. And again. A candidate in a serious job search may complete a dozen assessments in a quarter, generating a dozen scores of essentially the same thing, seeing none of them.

The waste is enormous and it falls entirely on the person with the least power in the transaction. The information is all computed; none of it is returned; and the repetition is structural rather than necessary.

## Why Nobody Has Built This

Returning results is seen as creating risk: a candidate who knows their score might contest it, and a candidate who knows what is measured might prepare, which the instrument treats as contamination.

Portability is harder. An assessment result reused across employers requires a shared instrument, a trusted intermediary, an expiry convention, and item security strong enough that a portable score is not simply an invitation to prepare once and coast. It also removes a revenue event for the vendor, since each administration is billed.

And the candidate is not the customer. Nobody in the transaction is paid to serve them.

## What to Build

Results, reasons and a portability mechanism.

**Return the result.** Score with its interval, what each scale measures in plain language, and where they sit relative to a reference group. This is a rendering of data already computed. The preparation objection is largely answered by item rotation — which is needed regardless — and by returning the construct rather than the items.

**Give a real reason for the outcome.** Not "we have decided to proceed with other candidates" but which stage they did not pass and on what basis. Where the rejection was on an assessment score, say so and say the band. This is what a growing set of regulatory directions is moving toward and it is a template change.

**Provide a correction route.** Technical failures, accessibility problems, a disrupted administration and data errors all occur, and there is frequently no way to raise any of them. A defined route with a human and a timeline is the minimum, and the volume is far lower than it appears because almost nobody currently has a way to try.

**Build portability where the instrument allows.** A candidate who completed a cognitive assessment six weeks ago should be able to present that result to the next employer rather than retaking it. This needs a neutral custodian, an expiry convention reflecting the construct's stability, a verification mechanism, and the candidate's consent for each release. The established publishers are the natural custodians of their own instruments and this would be a significant service to the market.

**Make the time estimate honest.** Published estimates are routinely optimistic, and a candidate who budgeted thirty minutes for a fifty-minute assessment abandons or rushes. The vendor has the completion time distribution; publishing the median and the upper quartile costs nothing.

**Measure abandonment as a selection effect.** Who abandons, at what point, and how that population differs. This matters to the employer — their applicant pool is shaped by it — and nobody reports it.

## Target Customer

Employers competing for candidates in tight markets, where assessment experience measurably affects completion and reputation. Regulators, whose direction is toward disclosure and contestability. And the established publishers, for whom a portable, verified result is a service only they can offer for their own instruments.

## Impact If Built

The candidate gets back something for their hour — their own result, a real reason, and a route to raise an error. Repeated administration of the same construct to the same person across employers becomes avoidable. And the abandonment that silently shapes every applicant pool becomes visible.
