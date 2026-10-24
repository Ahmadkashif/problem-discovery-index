# Claim Scrubbers Adapted to Vision-Plan Routing Rules

**Niche:** [[niches/optometry-practices/routine-vs-medical-visit-billing/profile|Routine-vs-Medical Visit Billing]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic claim scrubbers already catch bad codes; adding each vision plan's routing, split-billing and coordination rules would let them catch the wrong payer.
**Tags:** #decision-trees #large-language-models #automation #compliance #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bill each eye exam to the payer its findings support, vision plan or medical, and whoever collects the most revenue per exam that survives payer audit takes the account.

## The Problem
Practices already pay for scrubbing, through their EHR or clearinghouse. It checks whether a claim is well formed, not whether it went to the right plan. A routine exam sent to medical without a qualifying complaint, or a medical visit sent to the vision plan, passes the scrubber.

## What Already Exists
Scrubbers in the optometry EHRs, Availity and Waystar edits, and Eyefinity's VSP claim checks validate codes, modifiers, NPIs and formats. Medical-necessity edits exist for some diagnostic tests against Medicare coverage policies.

## The Customization Gap
The scrubber needs a rule pack per vision plan covering when medical services may be billed, whether same-day vision and medical claims are allowed, refraction handling, and coordination-of-benefits order. It also needs a check that the chief complaint supports a medical claim. Most of this can be encoded as rules once someone reads the manuals, and updated each plan year.

## Target Customer
EHR vendors and optometry billing services, which would resell it to their practices.

## Impact If Solved
Catching the wrong-payer claim before submission on even 2% of a practice's ~4,000 yearly exams would avoid ~80 denials or recoupments a year (estimate), each costing ~20–30 minutes of rework.
