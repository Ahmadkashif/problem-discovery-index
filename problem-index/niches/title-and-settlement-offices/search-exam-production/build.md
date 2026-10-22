# Clean-File Triage Calibrated by County

**Niche:** [[niches/title-and-settlement-offices/search-exam-production/profile|Title Search & Examination Production]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Two-thirds of files need almost no examiner judgement, but every file waits in the same queue for the same examiner.
**Tags:** #tacit-knowledge-ml #gradient-boosting #transformers #large-language-models #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a clean chain into an underwriter-acceptable commitment in minutes and send only the genuinely defective chains to an examiner, and whoever draws that line most accurately takes the lender channel's refinance and purchase volume.

## The Problem
An agency's examiners work orders first in, first out. A refinance with a five-year-old prior policy and one mortgage gets the same queue position as a purchase with an estate in the chain. Lenders measure the agent on commitment turn time, and the clean files wait behind the hard ones.

## Why Nobody Has Built This
Underwriter AI tools review a search package for defects; none estimates, for this agency and county, the probability that its own senior examiners would pass the file with a standard commitment. That needs the agency's history of dispositions, which nobody has captured.

## What to Build
A triage model that scores each incoming search package for the probability that the commitment will be standard, trained on the agency's past commitments and examiner edits, calibrated by county and transaction type. Files above a threshold the agency sets get an auto-drafted standard commitment for a quick examiner sign-off; files below go to a senior examiner with the instruments driving the score highlighted. Track post-closing defects on auto-drafted files as the control.

## Target Customer
Multi-county agencies with lender-channel volume and turn-time commitments.

## Impact If Built
Clean files turn in minutes, examiners spend their day on the files that need them, and the agency can show lenders a measured turn time.
