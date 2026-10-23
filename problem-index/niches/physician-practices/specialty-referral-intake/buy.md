# Document AI Tuned to Referral Packets

**Niche:** [[niches/physician-practices/specialty-referral-intake/profile|Referral Intake in Specialty Practices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General document AI can read a fax; a specialty practice needs it to know what a complete referral for its specialty looks like and to act on what is missing.
**Tags:** #transformers #large-language-models #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn each inbound faxed referral into a scheduled, insurance-cleared first visit within a day, and whoever converts the most referrals into kept first visits takes the account.

## The Problem
A referral packet is a mix of a typed cover sheet, scanned handwriting, EHR printouts from a dozen systems and pages turned sideways. Coordinators spend ~10–15 minutes per packet (estimate) finding the patient, the reason, the insurance and the attachments.

## What Already Exists
General document AI (AWS Textract, Google Document AI, Azure Document Intelligence), e-fax inbox tools, EHR document classification, and healthcare-specific intake automation such as Tennr.

## The Customization Gap
The specialty layer needs:

- a per-specialty definition of a complete referral (a colonoscopy referral needs prior scope history and anticoagulant status; a sleep referral needs a questionnaire);
- payer rules on whether a referral or authorization must be on file before the visit;
- automatic requests to the sending office for missing items, by fax or Direct message;
- writing the structured referral into the PM system and offering slots to the patient.

## Target Customer
Specialty groups of 5–100 physicians that receive hundreds of referral faxes a week.

## Impact If Solved
Intake time per packet could fall to ~3 minutes (estimate). Faster first contact could convert ~10%–15% more referrals into kept visits (estimate), each worth a new patient and downstream procedures.
