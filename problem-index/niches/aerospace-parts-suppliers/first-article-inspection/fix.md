# The Delta FAI Nobody Noticed Was Due

**Niche:** [[niches/aerospace-parts-suppliers/first-article-inspection/profile|First Article Inspection & AS9102 Packages]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** A switch of heat treater, a drawing revision or a part not run for two years triggers a partial FAI, and the trigger is often noticed only when the customer's auditor asks.
**Tags:** #large-language-models #compliance #workflow-orchestration #automation #quick-win #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to get an AS9102 package accepted by the customer's quality representative the first time. Two contests sit inside it, with different inputs, vendors and winners: extracting every requirement from the drawing or model onto Form 3, and proving every material and special process on Form 2 with genuine, conforming certificates from approved sources. Decomposed into contested sub-niches below.

## The Problem
Purchasing moves a plating job to a second Nadcap processor because the first is full. Engineering loads revision D of a drawing. A part number last made in 2023 comes back on order. Each should trigger a full or partial FAI. The ERP doesn't know the rule, and the quality manager learns about the change after parts have shipped.

## Why It's Still Broken
The triggers live in different systems (purchasing, engineering, order history), and nobody owns the check.

## What a Fix Looks Like
A nightly job that compares, per part number, the last accepted FAIR against the current drawing revision, processors, material sources, manufacturing location and last production date, and opens a delta-FAI task with the reason pre-filled for Form 1.

## Who Feels the Pain
Quality managers facing audit findings; customers who receive parts without a valid FAIR; shipping, which holds orders while a late FAI is done.

## Impact If Fixed
A simple cross-check prevents the audit finding and customer escape that a missed delta FAI causes, each costing ~1–3 weeks of containment work (estimate).
