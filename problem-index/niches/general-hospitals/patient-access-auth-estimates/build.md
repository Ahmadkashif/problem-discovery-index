# Authorization Requirement Prediction From the Order Itself

**Niche:** [[niches/general-hospitals/patient-access-auth-estimates/profile|Patient Access: Prior Authorization, Eligibility & Estimates]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Patient access teams look up each payer's authorisation list by hand for every scheduled service, when the hospital's own remittance history already shows which code, payer and plan combinations get denied for missing authorisation.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get every scheduled service verified, authorised and priced before the patient arrives, and whoever clears the most scheduled cases with no human touch and no downstream authorisation denial takes the account.

## The Problem
Payer authorisation requirements vary by plan, product, code, site of service and diagnosis, and change through bulletins. Staff check portals or vendor rule libraries for each order. Errors either waste time on unnecessary requests or produce "no authorisation" denials that are hard to appeal.

## Why Nobody Has Built This
Rule-library vendors maintain lists from payer publications, a reading job. The hospital's 835 history, which shows what each payer actually denies for lack of authorisation, sits in a different system and is not used to correct the lists.

## What to Build
A model that predicts, from the order (CPT/HCPCS, diagnosis, site, payer, plan, product), whether authorisation is required and likely to be approved. It is trained on the hospital's remittances and authorisation outcomes, and it reconciles disagreements with payer policy documents read by an LLM. Clear "not required" cases go straight to scheduling, and "required" cases go to automated submission with the clinical packet drafted.

## Target Customer
Patient access directors at systems with high technical-denial rates for missing authorisation.

## Impact If Built
Fewer unnecessary requests and fewer missed ones. Cutting authorisation-related technical denials by ~33% (estimate) protects revenue that is rarely recovered on appeal. It also removes ~20–30% of authorisation requests that were never needed (estimate).
