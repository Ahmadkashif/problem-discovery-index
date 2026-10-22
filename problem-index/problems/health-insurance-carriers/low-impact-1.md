# Provider Directories That Answer the Phone Wrong

**Industry:** [[health-insurance-carriers|Health Insurance Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Master data management and provider attestation tools already exist, but none reconciles the plan's own contract, credentialing, claims and outreach signals into a directory entry that is still right when a member calls the office.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #large-language-models #data-integration #compliance #automation

## The Problem
A health plan's provider directory lists, for every contracted clinician, each practice location, phone number, specialty, network and product participation, and whether the clinician is accepting new patients. Under the No Surprises Act, plans must verify this information at least every 90 days and update it within two business days of a change. Medicare Advantage directories are reviewed by CMS, Medicaid MCOs answer to state secret-shopper surveys, and several states now penalise "ghost networks" of listed clinicians who do not see plan members. The same data feeds network adequacy filings, which prove the plan has enough providers of each type within the required time and distance of its members.

The data arrives badly. Large groups send rosters as spreadsheets in their own layouts, monthly or when they remember. Individual clinicians attest through CAQH ProView, or do not. Credentialing files, contract records and claims each hold a different version of where the clinician works. Outreach callers phone offices to confirm and often reach a front desk that does not know which plans the practice takes.

## What Already Exists
Plan master data management systems and provider data management modules in core administration platforms; CAQH ProView for attestation; Quest Analytics for network adequacy analysis; and outsourced directory validation services, logged in the vault as [[directory-and-list-publishers|Directory & List Publishers]]' validation vendors. Generic MDM platforms match and merge records competently.

## The Customisation Gap
The generic tools merge records; they do not judge which source is right for this field, today. A plan-specific layer needs several things. Field-level trust rules: claims billed from an address in the last 60 days outrank a two-year-old attestation, and a roster outranks a call to a front desk on network participation but not on phone number. Roster ingestion that maps each group's spreadsheet layout without a person rebuilding the mapping each month. Product-level participation logic (the clinician is in the commercial PPO but not the Medicaid HMO). A prediction of which listings are most likely wrong, so outreach goes there first rather than cycling through every record every 90 days. And an audit trail that shows a regulator when each field was last verified and how.

## Impact If Solved
Targeting verification at the listings most likely to be wrong, rather than calling every office every quarter, would cut outreach calls by ~30%–50% (estimate) and lower the error rates regulators find in secret-shopper samples. Members would stop being sent to clinicians who left the practice or the network, and network adequacy filings would rest on providers who actually see plan members.
