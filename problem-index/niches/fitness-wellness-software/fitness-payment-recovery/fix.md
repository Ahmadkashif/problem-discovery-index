# Involuntary Churn Counted as Churn

**Niche:** [[niches/fitness-wellness-software/fitness-payment-recovery/profile|Fitness Payment Recovery]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Fix (Pain Point)
**One-liner:** A member who left because a card failed and a member who decided to leave appear identically in every fitness platform's churn report, so the half of the problem that is mechanical is invisible and nobody works on it.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #survival-analysis #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in fitness billing is fighting to recover a failed membership payment before the member treats the failure as a decision — and whoever recovers most involuntary churn takes the account.

## The Problem
A studio's monthly churn is 6%. The owner works on the service, the schedule and the community, because churn is understood as a satisfaction problem. A portion of that 6% — frequently a substantial portion — is members whose payments failed and who were suspended, some of whom were actively attending in the week they were removed. Nobody has separated the two, so the owner's entire retention effort is directed at the half they can influence slowly while the half they could fix in a fortnight is invisible. The distinction is trivially available in the billing data.

## Why It's Still Broken
Churn reporting was built as a single number because that is how subscription businesses have traditionally reported it, and the involuntary component is buried in the same cancellation events as voluntary ones. Separating them requires attributing each cancellation to its cause, which the system knows — a payment-failure suspension is a distinct event from a member-initiated cancellation — and does not surface. And nobody has asked, because a studio owner does not know the distinction exists as a thing to ask about.

## What a Fix Looks Like
Split the number and report both. Voluntary cancellations, with their stated reasons, and involuntary terminations following payment failure, with their failure reasons, are separate lines with separate trends. Within involuntary, report the recovery rate and the attendance status of the members lost — because a member who was attending three times a week and was removed for a card failure is a plainly recoverable loss and a specific person the studio can call today. Report the composition to the studio rather than only to the platform, since it is the studio's business and the studio's relationship that can fix it. And measure the reactivation rate of involuntarily churned members, which is the number that reveals how much of this was genuinely lost and how much was a temporary problem badly handled.

## Who Feels the Pain
Studio owners working on the wrong half of their churn; members removed from a service they were actively using; and front desk staff dealing with the resulting conversation with no context.

## Impact If Fixed
Splitting churn takes a query and reframes a studio's entire retention effort by revealing a mechanical component that can be reduced immediately. The list of actively-attending members lost to payment failure is the single most actionable artefact in this industry and is available to every platform today at the cost of a report.
