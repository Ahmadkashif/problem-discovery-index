# Visit-or-Phone Decisions Learned from What the Nurse Found

**Niche:** [[niches/answering-services/hospice-after-hours/profile|Hospice & Home Health After-Hours Lines]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experienced hospice on-call nurses can tell from a family's description whether death is close or the pain is out of control; nothing records which night calls truly needed a visit, so newer nurses and the answering service cannot learn it.
**Tags:** #tacit-knowledge-ml #gradient-boosting #logistic-regression #evaluation-metrics #large-language-models #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to tell, at 2 a.m., which family calls need a hospice nurse in the home and which a nurse can settle by phone, inside the agency's response standard, and whoever sends a nurse to every visit that needs one and to none that don't takes the account.

## The Problem
A hospice on-call nurse may cover a large territory overnight. Each visit can mean an hour or more of driving, so the decision to go versus coach the family by phone shapes the whole night. Experienced nurses read the family's words ("breathing has changed", "he's restless", "she hasn't woken") against what they know of the patient. That judgement is held in heads, not records.

## Why Nobody Has Built This
The night call, the visit note and the patient's trajectory sit in different systems: the answering service's log, the hospice EHR and the death record. Agencies are small, and outcome joins require their data under a business associate agreement.

## What to Build
Under the agency's agreement, the night call is joined to whether a visit was made, what was found (death, uncontrolled symptoms, family reassured) and whether the patient was transferred. A model of visit need is learned from the call transcript and patient context, and shown to the on-call nurse as a second opinion with similar past calls. Agencies get a monthly view of phone-managed calls that led to next-day crises.

## Target Customer
Clinical directors at hospices with 100+ census; answering services and triage providers with hospice accounts.

## Impact If Built
Visits go where they are needed, nurses' nights are less wasted, and fewer families end up calling 911 because the right visit was not made.
