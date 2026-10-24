# Lab Claims Built From a Requisition, Not a Visit

**Industry:** [[clinical-laboratories|Clinical Laboratories]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Claim scrubbers were built for practices that saw the patient; a lab bills from a requisition someone else filled in, so the generic edits miss the failures that actually deny lab claims.
**Tags:** #large-language-models #gradient-boosting #logistic-regression #feature-engineering #compliance #automation #revenue-impact #data-integration

## The Problem
A lab never meets most of its patients. The specimen arrives with a requisition, paper or electronic, completed by a medical assistant in the ordering office, and everything the claim needs comes from it: the diagnosis codes that establish medical necessity, the patient's insurance, the ordering provider's NPI, sometimes a signed Advance Beneficiary Notice. When the requisition is incomplete, the lab finds out weeks later when the claim denies, long after the patient and the ordering office have moved on.

The failures follow lab-specific rules. Medicare national coverage determinations cap how often some tests are paid and list the diagnoses that justify them. Molecular tests in MolDX states need a DEX Z-code on the claim. Payers bundle individual results into panels or "ceiling" codes; in XiFin's data, "procedure not paid separately" made up 59.4% of routine lab denials in 2025, up from 33.0% in 2018. Tests on specimens collected during a hospital stay follow Medicare's date-of-service rule: a test on a stored specimen takes the test date rather than the collection date only if, among other conditions, it was ordered at least 14 days after discharge (42 CFR 414.510), which decides whether the hospital or the lab bills it. A lab running 20,000 requisitions a day cannot work denials one by one at $20–40 a line.

## What Already Exists
Hospital and physician revenue cycle suites (Waystar, Experian Health, Availity and clearinghouse scrubbers) run payer edit libraries, eligibility checks and NCCI edits. Lab-specific RCM systems (XiFin, Telcor, Quadax) add medical-necessity and frequency checks and work queues. Large labs build their own rules engines; Quest is rebuilding order-to-cash with Epic.

## The Customisation Gap
The generic scrubber checks the claim it is given. A lab needs checks at accessioning, while the specimen is still in the building and the ordering office can still be called. Diagnosis codes have to be validated against NCD and LCD covered-code lists per test and per MAC. Each payer's bundling and panel rules have to be predicted before billing, not learned from the denial. Z-codes must be matched to the exact test version, and ABN requirements flagged before the test is run. It also needs an estimate of each requisition's collectable value, so staff chase the $400 genetic panel with a missing diagnosis first and let the $9 CBC go. Underneath sit two modelling tasks: extracting fields from scanned requisitions, and predicting denial probability from payer, test, diagnosis and ordering office history.

## Impact If Solved
Catching missing and mismatched information at accessioning rather than at denial lifts first-pass payment on the lines that matter. For a regional lab billing ~$150M a year, recovering even 1% of avoidable denials returns ~$1.5M (estimate). It also takes most of the follow-up calls off client services, because the ordering office is asked once, the same day.
