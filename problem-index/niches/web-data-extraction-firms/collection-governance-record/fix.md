# Approved Once, Never Revisited

**Niche:** [[niches/web-data-extraction-firms/collection-governance-record/profile|Collection Governance Record]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A collection is reviewed and approved at onboarding, and then the site adds terms, the robots directives change, a law takes effect and the customer starts using the data for model training — and nothing re-examines it.
**Tags:** #compliance #change-point-detection #automation #evaluation-metrics #workflow-orchestration #data-integration #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to maintain a continuous, queryable account of what is being collected, from where, under what permission and for whose purpose — and whoever does that takes the account, because it is the evidence that makes the whole business defensible.

## The Problem
A collection approved three years ago runs unchanged today. Since approval the target added an explicit prohibition on automated collection to its terms, tightened its robots directives, and began serving personal data in a field it did not previously expose. A privacy law took effect covering residents whose data is in the collection. The customer, who described the purpose as competitive price monitoring, now uses the output as part of a model training corpus. All four changes are material, none triggered anything, and the approval that authorises the traffic describes a situation that no longer exists in any respect.

## Why It's Still Broken
Re-review is unbilled work with no trigger, and the approval reads as a permanent state rather than a point-in-time assessment. Nobody watches target terms, because watching thousands of sites' terms is work nobody has assigned even though it is mechanical. Customer purpose changes silently and is not something the firm asks about again. And raising a re-review means potentially stopping revenue, which is a conversation the commercial side does not initiate.

## What a Fix Looks Like
Make the approval a monitored state rather than an event. Watch every target's robots directives and terms of service for change and raise it against the affected collections automatically, which is mechanical, cheap and is the single change that would catch the most material events. Give every approval an expiry, so a collection is re-examined on a cadence rather than persisting indefinitely by default. Re-confirm customer purpose periodically, since purpose drift — particularly toward model training — is the change most likely to alter permissibility and the one the firm currently never learns about. Detect changes in what a target is serving, such as newly exposed personal data fields, which is visible in the firm's own extracted output and is checked by nobody. Trigger review on external events: a relevant judgment, a new law taking effect, litigation involving the target. Record each re-review with its reasoning, building a precedent library, which the compliance reviewer niche develops. Support graduated responses — narrow the fields, reduce the rate, exclude a jurisdiction — rather than only continue or stop, since the binary choice pushes toward continuing. And report the age distribution of approvals, because a firm whose median approval is three years old has a governance posture it has not examined.

## Who Feels the Pain
Firms running traffic authorised by a stale assessment; customers inheriting a risk that has grown since they were told it was managed; and target sites whose changed terms are being ignored because nobody read them.

## Impact If Fixed
The approval describes a situation that no longer exists in any respect. Watching targets' terms and directives for change is mechanical and catches the most material events, and re-confirming customer purpose catches the drift toward model training that the firm otherwise never learns about.
