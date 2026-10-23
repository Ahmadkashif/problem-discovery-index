# Urgency Triage From the Faxed Packet

**Niche:** [[niches/physician-practices/specialty-referral-intake/profile|Referral Intake in Specialty Practices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An experienced triage nurse can skim a referral and know which "abdominal pain, please evaluate" is a likely cancer; intake software reads the fields but not the urgency.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn each inbound faxed referral into a scheduled, insurance-cleared first visit within a day, and whoever converts the most referrals into kept first visits takes the account.

## The Problem
Specialty practices book new patients weeks out. Urgent referrals should jump the queue, but the sending office's "urgent" box is ticked on half of them and blank on some that matter. Senior triage nurses read the notes, labs and history and decide. Their judgement is good and scarce, and it is not recorded.

## Why Nobody Has Built This
Intake vendors compete on extraction accuracy and speed, not clinical urgency, which carries liability. The label, whether the patient turned out to have a serious diagnosis, sits in the practice's own records after the visit and is never linked back to the referral.

## What to Build
A model that reads the full packet (notes, labs, imaging reports, medication lists) and scores clinical urgency. It is trained on the practice's past referrals linked to the diagnoses made at the first visit, and on the triage nurse's own past decisions. High-urgency referrals go to the nurse with the reasons highlighted, and the nurse's overrides become new labels.

## Target Customer
Gastroenterology, neurology, cardiology and oncology groups with new-patient waits of more than three weeks.

## Impact If Built
Cutting time to first visit for the ~5%–10% of referrals that carry a serious diagnosis (estimate) from weeks to days. Triage nurse review time could fall by about half (estimate).
