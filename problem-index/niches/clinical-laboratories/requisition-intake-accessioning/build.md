# Requisition Reading That Knows What the Claim Will Need

**Niche:** [[niches/clinical-laboratories/requisition-intake-accessioning/profile|Requisition Intake & Accessioning]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Accessioners key what the requisition says; nobody checks, while the specimen is still on the bench, whether what it says is enough to run the test and get it paid.
**Tags:** #large-language-models #transformers #gradient-boosting #feature-engineering #automation #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to register each specimen and its requisition completely on first touch, and whoever accessions the highest share without a callback to the ordering office takes the account.

## The Problem
A paper or faxed requisition arrives with handwritten tests, a diagnosis written in words, an insurance card photocopy and a patient name that differs from the tube label by a middle initial. The accessioner keys it, the specimen moves on, and missing or mismatched information surfaces later as a rejected specimen, a duplicate patient record or a denied claim.

## Why Nobody Has Built This
Document capture tools read forms; they don't know the lab's test catalogue, its specimen requirements or the payer rules that decide whether the diagnosis supports the test. LIS vendors treat order entry as data entry.

## What to Build
A vision-language reader for requisitions and labels that extracts patient, tests, diagnoses and insurance, maps free-text tests to the catalogue and diagnoses to ICD-10 codes, and matches tube labels to the requisition. It checks completeness for both the bench (specimen type, volume, timing) and the claim (covered diagnoses, Z-codes, ABN). Clean requisitions flow straight into the LIS; the rest reach the accessioner with the exact problem flagged, and a request goes to the ordering office automatically.

## Target Customer
Specimen processing directors at regional, outreach and reference labs receiving thousands of paper or faxed requisitions a day.

## Impact If Built
Cutting accessioning time on paper requisitions from ~3 minutes to ~1 (estimate) frees about a third of the keying staff. Catching billing gaps at the door lowers denials for missing information on the same volume.
