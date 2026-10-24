# The Paper Requisition From a Practice With an EHR

**Niche:** [[niches/clinical-laboratories/hospital-outreach-lab-partnerships/profile|Hospital Outreach Programmes & Reference Lab Partnerships]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** A practice with a modern EHR prints a lab requisition by hand because its interface to the outreach lab broke months ago and nobody noticed.
**Tags:** #data-integration #descriptive-statistics #automation #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to be the lab community practices send their routine orders to, and whoever keeps the largest share of each practice's routine order volume year on year takes the account.

## The Problem
Outreach labs receive a steady flow of paper or faxed requisitions from practices that are supposed to be interfaced. Each needs manual accessioning, carries handwriting and missing fields, and returns results by fax or portal rather than into the EHR, which is exactly what makes the practice consider another lab.

## Why It's Still Broken
Interface failures are silent: the practice's staff fall back to paper without telling anyone, and the lab sees only a rising paper share it does not track by client. Ownership is split between interface analysts, client services and sales.

## What a Fix Looks Like
Track electronic versus paper order share per practice weekly and alert when a practice's share drops. Check the interface's message logs for that practice automatically, and route a fix ticket with the likely cause (expired credentials, a changed provider ID, an upgraded EHR) before the account manager's next visit.

## Who Feels the Pain
Accessioners keying paper, practices getting faxed results, and outreach leaders losing clients to labs whose interfaces work.

## Impact If Fixed
Moving a practice from paper back to electronic ordering removes manual accessioning and most missing-information denials for its volume. At ~$3 of handling per paper requisition (estimate), a programme receiving 500 avoidable paper requisitions a day saves ~$375,000 a year.
