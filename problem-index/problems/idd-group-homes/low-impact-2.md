# A Medication Record Built for Med-Certified DSPs, Not Nurses

**Industry:** [[idd-group-homes|IDD Group Homes]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Electronic medication records were designed for nurses in [[skilled-nursing-facilities|nursing homes]], while group homes pass medications through unlicensed DSPs under state certification and nurse delegation, with residents moving between home, day programme and family visits.
**Tags:** #large-language-models #gradient-boosting #logistic-regression #evaluation-metrics #compliance #worker-facing #quick-win

## The Problem
In most group homes there is no nurse on site. Medications are passed by DSPs who have completed a state medication administration course and are certified or delegated to give them under a nurse's oversight (state rules vary, estimate). A typical resident takes several scheduled medications and has PRN orders, including PRN psychotropics that may be given only as the behaviour support plan specifies. Many residents spend weekends with family or weekdays at a day programme, so medications leave the house in labelled leave-of-absence packets and must come back reconciled.

Errors are routine and now carry a federal consequence. Under the 2024 Access Rule, a medication error that leads to a call to a poison control centre, an emergency department or urgent care visit, a hospitalisation or a death is a critical incident that every state must define, track and investigate from 9 July 2027 (89 FR 40542). Lesser errors (late doses, missed signatures, wrong counts) still trigger internal reports, retraining and licensing citations.

## What Already Exists
Electronic MAR modules in IDD record systems (Therap, MediSked, iCareManager) and in [[skilled-nursing-facilities|skilled nursing]] and [[assisted-living-communities|assisted living]] EHRs; pharmacy-integrated eMARs from long-term care pharmacies, which also publish DSP guides on the Fatal Five; barcode scanning; and paper MARs printed by the pharmacy each month.

## The Customisation Gap
Nursing-home eMARs assume a licensed nurse with clinical judgement at the cart and a facility census that rarely leaves the building. A group home needs four things they do not have. First, prompts written for a DSP: plain-language purpose and side effects, the specific swallowing precautions from the person's dining plan, and when to call the delegating nurse. Second, PRN psychotropic administration tied to the behaviour support plan, requiring the de-escalation steps to be documented first and flagging patterns of PRN use for the clinician and the human rights committee. Third, leave-of-absence and day-programme transfers that count tablets out and back. Fourth, error reporting that classifies each event against the state's critical incident definition automatically, so the house knows within the hour whether this one goes to the state. The rules for who may give what (certification level, delegation scope, which routes are allowed) differ by state and must be encoded per state.

## Impact If Solved
Fewer medication errors reaching the critical-incident threshold, less night-time calling of the on-call nurse for questions a good prompt answers, and PRN psychotropic use that clinicians can actually review. A 40-home agency might cut its reportable medication incidents by ~33% and its monthly MAR reconciliation time by ~3–5 hours per house (both estimates).
