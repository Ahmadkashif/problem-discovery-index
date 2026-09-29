# Receipt Capture and Documentation Chase

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The documentation requirement is an audit artefact, the collection of it is a nagging loop between software and employees, and nobody has asked which receipts are actually needed.
**Tags:** #object-detection #cnns #bert #large-language-models #gradient-boosting #evaluation-metrics #automation #worker-facing

## The Problem
Substantiation requires a receipt above a threshold. The employee is meant to photograph it, forward the email, or let the platform find it. The platform reminds them, then reminds them again, then escalates to their manager, then blocks the card.

Employees lose receipts, forget, or never had one. The reminder loop runs for weeks. The controller chases what remains at month end. The employee is annoyed, the manager is annoyed at being copied, and the controller is annoyed at chasing.

Extraction from the receipts that do arrive is imperfect. Photographs are creased, folded, thermal-faded, taken at angles in bad light. Itemised detail — which matters for policy, tax and coding — is harder to extract reliably than the total. Foreign currency and tax lines add failure modes.

Automatic capture works where it works. Email parsing catches digital receipts; some merchants push detail through the network; corporate travel bookings arrive structured. Everything else is a photograph.

The requirement itself is rarely examined. Many companies require receipts at thresholds well below anything an auditor cares about, out of caution, which generates a large volume of chase for documentation nobody will ever look at.

## What Already Exists
Document extraction is built into every platform. Email forwarding and inbox integrations are standard. Some merchants and networks provide level-three data with line-item detail. Travel integrations capture itineraries. Reminder and escalation workflows are universal. IRS substantiation rules set an actual floor that is higher than most corporate policies.

## The Customisation Gap
Extraction quality on poor photographs is the persistent weak point, and the line items — not the total — are where the remaining value is, since they determine policy compliance, tax treatment and coding.

Reconstruction from context is unexploited. When a receipt is missing, the platform knows the merchant, amount, time, location and often the itinerary or calendar context. For a large share of missing receipts it could reconstruct a defensible record, or state precisely what is missing, rather than simply chasing.

Nobody optimises the requirement. Which receipts an auditor will actually sample is predictable, and the threshold at which documentation genuinely matters is knowable. A platform could tell a customer that its twenty-five dollar threshold generates several thousand chases a year for documents that carry no audit or tax consequence — which is a recommendation nobody currently makes because nobody has measured it.

And chase is uniform. Some employees always submit, some never do, and the reminder cadence is identical for both. Timing and channel could be targeted from behaviour, and the employees who never respond need a different intervention rather than more reminders.

## Impact If Solved
Receipt chase is the most visible irritation the product creates for the people who use it most, and much of it is spent collecting documentation that will never be examined. Better extraction, reconstruction from context, targeted chase and an evidence-based threshold recommendation remove most of the annoyance without weakening anything an auditor cares about.
