# Forty Products, No Introduction

**Niche:** [[niches/embedded-finance-platforms/the-compliance-analyst/profile|The Compliance Analyst]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A new analyst is given a queue covering forty programmes and no document describing any of them.
**Tags:** #worker-facing #compliance #quick-win #automation #descriptive-statistics #evaluation-metrics #workflow-orchestration #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to give one analyst responsible for dozens of independently run products enough context to judge an alert without learning each product from scratch — and whoever supplies that context decides whether the oversight function is real or nominal.

## The Problem
Onboarding for the role is a walkthrough of the alert tool. The forty programmes are learned by encountering them — an alert arrives from a product the analyst has never heard of, they ask a colleague, the colleague says it is a payroll product and large regular transfers are normal, and that fact enters one person's memory. Six months later the analyst knows fifteen of the forty well and the rest by reputation. When they leave, the fifteen go with them.

## Why It's Still Broken
Documenting a programme is nobody's job, since the programme belongs to the customer and the analyst belongs to compliance — the fact sits between two organisations and neither owns writing it down. The information exists in scattered places: implementation notes, the configuration, the contract, the monitoring setup. Learning by exposure works well enough to keep the queue moving. And turnover cost is absorbed silently.

## What a Fix Looks Like
Write the programme down once. Generate a one-page profile per programme from the configuration, the implementation record and the observed transaction behaviour, which is the fix and requires assembly rather than authorship — everything needed already exists in the platform. Include what normal looks like numerically, since that is precisely what the analyst needs and what a written description usually omits. Link the profile from every alert, so context arrives with the work rather than requiring a search. Capture the answers colleagues give, because the informal explanations are the missing documentation and they are being spoken daily. Keep the profiles current from the data, since a programme's behaviour changes and a stale profile is worse than none. Flag the programmes an analyst has never seen an alert from, which reveals both blind spots and unmonitored products. Assign secondary familiarity deliberately, so no programme is known to only one person. Review a sample of dispositions on unfamiliar products, because that is where errors concentrate. Onboard new analysts on the profiles rather than the tool, since the tool takes an afternoon and the products take six months. And measure time-to-competence, which is the number that shows whether any of this worked.

## Who Feels the Pain
New analysts guessing for months; experienced analysts answering the same questions; programmes known to one person; and a compliance function whose capability walks out with its staff.

## Impact If Fixed
The fact sits between two organisations and neither owns writing it down. Generating programme profiles from configuration and observed behaviour replaces six months of learning by encounter with a page that already exists in pieces.
