# Payer FHIR Prior-Auth APIs Wrapped for Hospital Schedulers

**Niche:** [[niches/general-hospitals/patient-access-auth-estimates/profile|Patient Access: Prior Authorization, Eligibility & Estimates]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payers must expose FHIR prior-authorisation APIs from 2027; hospitals need those APIs wrapped into scheduling and patient-access workflows, with fallbacks for every payer that is late.
**Tags:** #large-language-models #data-integration #workflow-orchestration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to get every scheduled service verified, authorised and priced before the patient arrives, and whoever clears the most scheduled cases with no human touch and no downstream authorisation denial takes the account.

## The Problem
Even with APIs, the hospital still deals with hundreds of payers, plans and delegated benefit managers, each at a different stage of implementation, alongside portals and fax for the rest.

## What Already Exists
HL7 Da Vinci implementation guides (Coverage Requirements Discovery, Documentation Templates and Rules, Prior Authorization Support) and payer APIs mandated by CMS-0057-F (recalled). Clearinghouse authorisation products and EHR payer platforms connect to some payers.

## The Customization Gap
Hospital adaptation needs:

- triggering from scheduling and order entry, not from a separate worklist;
- assembling the clinical documentation the payer's template asks for from the chart;
- routing by payer between API, portal bot, voice agent and fax;
- tracking decision clocks;
- linking approved units and dates to scheduling so a rescheduled case does not fall outside its authorisation.

## Target Customer
Patient access and revenue-cycle IT leaders preparing for the 2027 payer API deadline.

## Impact If Solved
The hospital gets the benefit of the payer mandate from its 1 January 2027 start, not after each payer's slow rollout. Staff time moves to the ~20–30% of requests that need a human (estimate).
