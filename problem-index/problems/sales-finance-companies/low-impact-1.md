# Contract-in-Transit Review

**Industry:** [[sales-finance-companies|Sales Finance Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every finance company pays funders to read each contract package against the same rules — truth-in-lending math, state fee caps, signatures, stipulations, title — and generic document AI reads the pages without knowing any of the rules.
**Tags:** #large-language-models #transformers #cnns #evaluation-metrics #automation #workflow-orchestration #compliance #quick-win

## The Problem
Between the dealer signing the customer and the lender paying the dealer sits the contract in transit. The funder receives a package — the retail installment contract, the credit application, the buyer's order, odometer statement, title application or existing title, proof of insurance, add-on product contracts and whatever stipulations the buyer required, typically pay stubs and a utility bill — either as an eContract through RouteOne or Dealertrack or as a scanned or couriered paper deal. The funder checks that the contract matches the approval (amount financed, term, rate, advance), that the Truth in Lending disclosures compute, that fees and add-on prices are within the state's caps, that every signature and initial is present, that the stipulations prove what they claim, and that the lien will be recorded. Defects go back to the dealer as a "kickback"; the dealer resubmits; the money waits.

Each day a contract sits unfunded costs the dealer, who calls, and the lender, whose share of that dealer's applications falls. Errors that slip through become the lender's: an unsigned contract, a disallowed fee or an add-on sold above the cap is a compliance finding, and under the FTC Holder Rule the dealer's misconduct can be asserted against the holder.

## What Already Exists
Intelligent document processing platforms (ABBYY, Hyperscience, Amazon Textract and similar) classify and extract fields from documents; income-verification and bank-statement tools such as Ocrolus read financial documents; the dealer networks' eContracting validates some fields at signing. Auto-specific vendors (Informed.IQ among them) verify stipulations for lenders that buy them, and servicing and origination systems hold the approval terms.

## The Customisation Gap
Generic extraction stops at fields. Funding needs the rules: state-by-state RISC form versions and their disclosure boxes; truth-in-lending recomputation of APR and finance charge; per-state caps on documentation fees, add-on prices and maximum rates; the lender's own dealer agreement terms (maximum dealer reserve, approved add-on list, advance limits); stipulation logic (a pay stub's year-to-date figure must support the stated monthly income; the utility bill's name and address must match); and title rules by state for perfecting the lien. California's CARS Act, operative October 1, 2026, adds new dealer disclosure, add-on and cancellation obligations that a funder in California must now check. The gap is a rules layer, maintained per state and per dealer agreement, sitting on top of extraction the lender can already buy.

## Impact If Solved
A rules-aware review that clears clean packages automatically and returns every defect at once, with the rule cited, would cut days-to-fund for good dealers and kickback cycles for bad ones, and turn funder time from reading pages into resolving the few genuine exceptions.
