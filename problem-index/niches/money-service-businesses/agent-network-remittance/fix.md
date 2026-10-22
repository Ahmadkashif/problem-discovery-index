# Field Visit Notes Nobody Reads Twice

**Niche:** [[niches/money-service-businesses/agent-network-remittance/profile|Agent-Network Retail Remittance]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** Contracted auditors visit thousands of agent stores a year and write what they saw in free text that never reaches the risk rating.
**Tags:** #large-language-models #bert #feature-engineering #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to tell a complicit or careless agent from a merely busy one before a regulator, prosecutor or sponsor bank does, and whoever tells them apart earliest takes the account.

## The Problem
A field auditor checks the clerk's ID handling, the posted disclosures and the transfer logs, and notes what felt wrong: the owner was absent again, a clerk could not explain the threshold, customers waited outside for someone. The structured part of the form is pass/fail; the useful part is the note, and it is filed and forgotten.

## Why It's Still Broken
Notes are written by contractors in varied styles and languages, and nobody has the time to read thousands of them. Risk ratings are built from fields that are easy to count, so the observations that experienced auditors care about most never enter them.

## What a Fix Looks Like
Language-model extraction of a fixed set of observations from each note — owner absence, clerk knowledge gaps, cash-handling irregularities, signs of third-party direction — with the passage quoted, fed into the agent file and the risk rating, and a weekly digest of agents whose notes changed tone.

## Who Feels the Pain
Agent oversight investigators who learn about a store's history only after it is in trouble, field auditors whose work goes unread, and compliance officers explaining to an examiner why a warning sign was recorded and ignored.

## Impact If Fixed
Observations already being paid for start shaping risk ratings within weeks, at almost no cost beyond processing the notes.
