# The Increase Letter With No Reason Recorded

**Niche:** [[niches/self-storage-operators/existing-customer-rate-increases/profile|Existing-Customer Rate Increases (ECRI)]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Fix (Pain Point)
**One-liner:** An increase goes out, the tenant complains to the city, and nobody can say why that tenant got that size or when the notice was delivered.
**Tags:** #large-language-models #compliance #workflow-orchestration #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to size each existing tenant's increase so the added rent outweighs the move-outs it causes, and whoever earns the most net rent per increase notice after twelve months of induced move-outs takes the account.

## The Problem
Batches are approved in a spreadsheet or a vendor screen. Overrides happen ("skip unit 214, she's moving", "give the business tenants 15%") and leave no trace. When a tenant disputes an increase, the operator has the letter and the new rate but not the reason, the delivery proof or the comparison to street rate. New York City's 2026 settlement with Extra Space followed more than 100 complaints and turned on exactly this: increases after move-in without adequate notice.

## Why It's Still Broken
Facility software stores the rate change, not the decision. Revenue managers approve hundreds of increases at a sitting and have no reason to type explanations. Until 2026 few regulators asked for one.

## What a Fix Looks Like
Make the batch screen record the decision. Each increase is stored with its inputs (tenure, in-place rent, street rate for the unit type, the recommendation), the approved size, and a one-click reason for any override. The notice date and delivery evidence are attached, along with the rule check that passed. A language model drafts a plain-English reason from the inputs for the file. The same record becomes the training data for the move-out model.

## Who Feels the Pain
Revenue managers answering complaints; district managers handling angry tenants; compliance and legal teams facing city and state consumer agencies; owners of managed stores asking why move-outs rose.

## Impact If Fixed
Answering a dispute drops from an hour of reconstruction to a minute (estimate). Each recorded override adds to a labelled dataset that would otherwise never exist. At ~5,000 increases a month for a 100-store operator (estimate), that is ~60,000 labelled decisions a year.
