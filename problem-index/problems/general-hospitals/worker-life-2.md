# The Case Manager Faxing Twenty Nursing Homes

**Industry:** [[general-hospitals|General Hospitals]]
**Type:** Worker Life Changing
**One-liner:** A hospital case manager gets back the afternoons she spends sending referral packets and chasing call-backs from nursing homes and Medicare Advantage plans, and the dignity of telling a family where their mother is going by Friday.
**Tags:** #large-language-models #gradient-boosting #logistic-regression #evaluation-metrics #worker-facing #workflow-orchestration #automation

## The Problem
An RN case manager or social worker on a medical floor carries ~15–25 patients (recalled). Each morning she reviews who is medically ready, and for each patient who needs post-acute care she starts the same loop. She confirms the family's choice list, assembles a referral packet (H&P, therapy notes, medication list, wound photos, insurance), sends it to several skilled nursing facilities through CarePort, Aidin or fax, and then calls each one to find out whether they will accept the patient, when, and at what level of care. If the patient has Medicare Advantage, she also requests authorisation from the plan, which denies more than one in five SNF discharge requests at first submission (Premier survey, 2025). Then she arranges a peer-to-peer review with the plan's medical director, or appeals. Every day the patient waits is an avoidable day: the hospital is not paid for it under the DRG, and the bed is not available for the ED patient boarding downstairs.

## Why It Matters to the Worker
Case managers describe the work as being a switchboard operator with a nursing licence. Most of the day goes on calls, hold music and re-sending packets because a facility "didn't get the fax". The clinical part of the job, judging what level of care the patient needs and preparing the family, gets the least time. The worst moments are conversations with families: explaining that the facility they chose declined without saying why, that the plan denied the stay, or that the patient must go to a facility forty miles away. She is measured on avoidable days and length of stay she does not control, and burnout and turnover in case management are high (recalled).

## What a Solution Looks Like
A placement assistant that assembles the referral packet from the chart automatically, tailored to what each facility's intake team asks for. It predicts which facilities are likely to accept this patient given acuity, payer, behaviours, dialysis or wound needs, and each facility's own acceptance history. It sends referrals in priority order and reads the replies, escalating to the case manager only when a human call is needed. In parallel it drafts the MA authorisation request with the clinical evidence the plan's criteria require, and tracks the plan's decision clock. The case manager sees one board per patient: sent, viewed, accepted, declined (with reason), and authorisation status.

## Impact If Solved
Halving the time from "medically ready" to accepted placement would cut ~0.3–0.5 avoidable days per post-acute discharge (estimate), thousands of bed-days a year for a 400-bed hospital. It would also give each case manager back ~1–2 hours a day (estimate) for the clinical and family work the role exists for.
