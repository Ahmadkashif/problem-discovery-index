# The Certificate That Expired in March

**Niche:** [[niches/ap-automation-vendors/vendor-onboarding-and-compliance/profile|Vendor Onboarding & Compliance]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The supplier's insurance certificate lapsed eight months ago and the file still shows it as on record.
**Tags:** #compliance #quick-win #automation #evaluation-metrics #workflow-orchestration #data-integration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to onboard a supplier once, verify them properly, and never ask them for the same document again — and whoever does it across a network collects the evidence every buyer currently gathers separately.

## The Problem
Onboarding collected the documents and stored them. The tax form is from four years ago and the supplier has since restructured. The insurance certificate expired in March. The screening was run once, at onboarding, before the supplier's owner appeared on a watchlist. Every one of these has an expiry or a staleness that is knowable, and the file records that a document exists rather than whether it is currently valid. Nobody looks until an auditor asks.

## Why It's Still Broken
Onboarding was designed as a gate, so the process ends when the document is received — a workflow with a completion state does not naturally acquire a maintenance state. Expiry dates are inside PDFs nobody extracted. Chasing renewals is nobody's job. And no report shows the file's current validity.

## What a Fix Looks Like
Extract the dates and watch them. Extract expiry dates from documents at upload rather than storing an image, which is the fix and makes every subsequent check automatic. Report the proportion of the vendor file with expired or stale documentation, since it is one view and the number will be startling. Chase renewals before expiry rather than after, because a supplier renews readily when asked at the right time. Re-screen continuously rather than at onboarding, as screening is cheap, automated and currently a one-time event. Flag suppliers with expired documentation before a payment, which is where the consequence actually lands. Prioritise by spend and by risk, since a large supplier with lapsed insurance matters and a dormant one does not. Track which requirements each buyer actually enforces, as many are collected and never checked. Show the supplier what is expiring, because they can act and are not told. Record validation outcomes rather than receipt, which is the difference between having a document and having evidence. And review the requirement list itself, since some documents are collected out of habit and checked by no one.

## Who Feels the Pain
Compliance teams discovering gaps at audit; buyers exposed to uninsured suppliers; suppliers chased in a panic; and AP staff maintaining an expiry spreadsheet by hand.

## Impact If Fixed
A workflow with a completion state does not naturally acquire a maintenance state, so onboarding ends when the document arrives. Extracting expiry dates at upload turns a static file into a monitored one.
