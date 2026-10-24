# Authorization Matched to the Exam Actually Performed

**Industry:** [[diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Eligibility and authorization tools confirm that an approval exists; an imaging centre gets paid only if the approval matches the CPT code, contrast, body part, date window and site actually scanned, and nothing checks that match again when the protocol changes.
**Tags:** #large-language-models #bert #gradient-boosting #feature-engineering #evaluation-metrics #automation #data-integration #revenue-impact

## The Problem
The ordering practice obtains the authorization; that work and its tooling belong to [[physician-practices|Physician Practices]]. The centre then has to verify, at intake, that what was approved is what it is about to do. An intake coordinator reads the faxed order, looks up the patient's plan, finds the authorization number on the order or calls the practice for it, and checks it in the radiology benefit manager's portal (EviCore, Carelon, Evolent) or the plan's own. The approval covers one CPT code, often one site of service, a unit count and a 30–90 day window (recalled ranges). The centre then changes things for good reasons. The radiologist protocols the lumbar MRI with and without contrast (72158 rather than 72148). The patient reschedules past day 60. The order said left knee and the history says right. The scan moves to the sister site across town, which has a different tax ID on the approval.

Each mismatch becomes a "no authorization" or "service does not match authorization" denial weeks later. Most are not overturnable, because the plan approved something else, and the technical fee of an MRI is written off or billed to a patient who was told it was covered.

## What Already Exists
Eligibility and benefits checks (270/271) through clearinghouses and Availity; authorization status lookups and portal automation from Experian Health, Waystar, Infinx and other revenue-cycle vendors; RIS intake screens with an authorization-number field; voice agents and outsourced teams that phone payers for status. Hospitals' scheduling-side version of this check, built into Epic and run by patient access teams, is analysed under [[general-hospitals|General Hospitals]]. The payer's side of the same decision is analysed under [[health-insurance-carriers|Health Insurance Carriers]].

## The Customisation Gap
The generic tools answer "is there an approval for this patient?" An imaging centre needs "does this approval cover the exam we will perform, at this site, on this date?", re-asked every time something moves. That needs imaging-specific logic. It must map with-contrast, without-contrast and with-and-without variants, and laterality and body-part families, to the CPT codes each benefit manager treats as interchangeable or not. It must hold per-payer rules on whether a protocol upgrade can be amended after the scan, and in what window. It must tie site of service and rendering tax ID to the approval. It must re-run the check when a radiologist changes the protocol, a scheduler moves the date or site, or a technologist adds a sequence. And it must read faxed orders and practice-attached approval letters, which is where many of the authorization facts actually arrive.

## Impact If Solved
A centre doing ~150 advanced exams a day that loses even 2% of them to authorization mismatches writes off three MRI or CT technical fees a day, worth ~$300,000–$500,000 a year at typical commercial rates (estimate). A check that re-runs on every protocol, date and site change, and prompts the amendment before the scan, turns most of those denials into a phone call made the day before.
