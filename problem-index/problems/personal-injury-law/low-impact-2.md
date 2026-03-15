# Medical Lien Management and Resolution Tracking

**Industry:** [[personal-injury-law|Personal Injury Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic accounts payable and legal billing tools track invoices but have no logic for the specific lien resolution process in PI cases — Medicare, Medicaid, ERISA, and health insurer liens each have their own statutory processes, reduction formulas, and mandatory resolution sequences before settlement proceeds can be disbursed.
**Tags:** #automation #tabular-ml #data-integration #compliance

## The Problem
When a PI case settles, the settlement proceeds cannot be disbursed to the client until all medical liens are resolved. Medical liens arise from Medicare (the Medicare Secondary Payer Act requires reimbursement of Medicare payments related to the injury), Medicaid (state-specific lien rights), ERISA health insurance plans (subrogation rights), and Letters of Protection (LOPs — medical providers who treated the client on credit in exchange for a lien on settlement proceeds). Each lien type has different legal requirements: Medicare liens must be confirmed with CMS (Centers for Medicare & Medicaid Services) and formally resolved; Medicaid liens have state-specific reduction formulas; ERISA lien reduction is governed by the common fund doctrine; LOP amounts must be negotiated with each provider. Managing this across a 200-case active docket is an administrative nightmare with both legal exposure (distributed before all liens are resolved) and financial opportunity (negotiating lien reductions that increase client net recovery).

## What Already Exists
Lien resolution services (MedFinancial, Lien Management Associates) handle Medicare lien resolution as an outsourced service. Filevine and SmartAdvocate have some lien tracking fields. General billing and accounts payable software tracks what's owed. None of these integrate the statutory lien type logic (what are the reduction rights for this specific lien type?), track lien negotiation correspondence, calculate the expected net-to-client after all liens are resolved, or flag cases where settlement disbursement is legally blocked pending outstanding lien resolution.

## The Customisation Gap
A PI lien management module needs to: automatically identify and classify all liens when a case settles (Medicare, Medicaid, ERISA, LOP) from the case file; pull current Medicare/Medicaid lien amounts from the relevant federal/state portals; calculate the reduction amount available under applicable law for each lien type; track correspondence with each lienholder; and produce a final disbursement calculation showing the client's net recovery, attorney fee, and each lien payment. The statutory lien type logic and disbursement sequencing rules are PI-specific and are not in any general-purpose legal billing tool.

## Impact If Solved
Reduces lien management time by 40-60% per settled case. More importantly, ensures all liens are properly resolved before disbursement — protecting the firm from Medicare Secondary Payer Act liability, which can result in double damages if Medicare is not reimbursed before settlement proceeds are distributed.
