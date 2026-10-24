# The Engineer Behind the Air Gap

**Industry:** [[defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Worker Life Changing
**One-liner:** Engineers on export-controlled and classified programmes work on segregated networks with decade-old tools, retype data across the air gap, and wait days for release reviews of every slide they want to share.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #worker-facing #workflow-orchestration

## The Problem
An engineer on a classified missile or space programme works in a closed area: no phone, no personal laptop and a workstation on a network separated from the company's business systems and from the internet. Software arrives late through an accreditation process, so the tools are whatever was approved years ago. Data needed on both sides (a schedule, a parts list, a test summary) moves by approved transfer procedures or is retyped by hand. On unclassified but ITAR-controlled work the walls are lower but similar: controlled technical data stays on US-person-only systems, and commercial cloud AI tools are usually off limits.

Every document leaving the controlled environment needs a review. A presentation for a supplier, a conference paper, a slide for a programme review on the unclassified side goes to a classification or export reviewer who reads it against the security classification guide or the export classification, marks or strips it, and sends it back, often after several days (estimate). Engineers learn to write less and share later.

## Why It Matters to the Worker
The friction is constant and lands on the most skilled people. Engineers who would use modern code and analysis tools at home spend hours on manual transfers and reformatting. They can't work remotely or take work home, so crunch periods mean longer days on site. Release delays make them look slow to suppliers and colleagues, and a marking error is a security incident with their name on it, which makes everyone conservative.

## What a Solution Looks Like
Approved, on-premises language models deployed inside the classified or export-controlled enclave, with the same help engineers get elsewhere: search across the programme's own documents, drafting, code assistance and data summarisation. For releases, a pre-review assistant that reads a draft against the programme's security classification guide or export classification, highlights the passages and figures likely to be controlled with the guide paragraph cited, and proposes a releasable version, so the human reviewer confirms instead of reading cold. Structured cross-domain transfer of routine data replaces retyping.

## Impact If Solved
Cutting release review from days to hours and removing manual re-entry could return several hours a week to each cleared engineer (estimate), and in an industry short of cleared engineers, keeping them in the job is worth more than any single efficiency.
