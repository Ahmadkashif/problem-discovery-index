# The Approval With No Record

**Niche:** [[niches/synthetic-data-providers/the-privacy-officer/profile|The Privacy Officer]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A synthetic release is approved in a meeting on a vendor PDF, and two years later nobody can reconstruct what was approved, from what source, under what configuration, or on what evidence.
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to give the person who signs the release something they can defend afterwards — and whoever does that takes the account, because that signature is the last gate every deal passes through.

## The Problem
A regulator asks about a dataset shared with a research partner in a previous year. The privacy officer who approved it has moved on. The vendor has retrained the generator twice since. The report they relied on is a PDF in an email thread. Nobody can say which source snapshot the data derived from, what configuration produced it, which version of the model was used, what attack results were current at the time, or what the officer was told. The approval happened and the basis for it has evaporated, which converts a reasonable decision into an indefensible one.

## Why It's Still Broken
The approval is a human process attached to a technical artefact and nothing joins the two. Vendors deliver reports rather than records, because a report is a sales document and a record is a liability. Generation platforms do not retain the lineage that would make reconstruction possible, which the platform niche covers. And the gap only becomes visible years later, at which point the people who could have fixed it are gone.

## What a Fix Looks Like
Make the approval a record rather than a meeting. Bind the decision to the artefact: dataset identifier, source snapshot, generator version, full configuration, privacy setting, evaluation and attack results as of that date, and the identity of the approver with their stated basis — all captured at approval time, which is the only time it is cheap. Retain it independently of the vendor, since the vendor's model will have changed and the customer's obligation has not. Version the approval, so that a regenerated dataset triggers a re-decision rather than inheriting the old one silently, which is the most common way a stale approval covers data it never assessed. Record the conditions attached to the approval — permitted recipients, retention period, permitted uses — because these are always stated verbally and never enforced. Record what was rejected and why, since the reasoning on a refused release is as defensible an asset as the reasoning on an approved one. Make it queryable, so the officer can answer what has been released, to whom, and on what basis without an email search. And produce a standing register, which is the artefact a regulator will ask for first and which almost no organisation has for synthetic releases.

## Who Feels the Pain
Privacy officers defending decisions they did not make on evidence that no longer exists; the organisations carrying the liability; and the vendors whose customers stall because approving something unrecordable feels reckless, correctly.

## Impact If Fixed
Capturing the basis at approval time is cheap and reconstructing it later is impossible. Versioning the approval so a regenerated dataset forces a re-decision closes the most common route by which a stale approval silently covers data it never assessed.
