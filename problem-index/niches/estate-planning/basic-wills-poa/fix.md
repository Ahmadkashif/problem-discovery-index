# Plan Staleness & Client Re-Engagement

**Niche:** [[niches/estate-planning/basic-wills-poa/profile|Basic Wills & POA]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Fix (Pain Point)
**One-liner:** Estate plans are drafted once and forgotten — attorneys stop losing the re-engagement revenue from clients whose plans are stale due to life changes, law changes, or simple time passage.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact

## The Problem
An estate plan is a living document that should be reviewed every 3-5 years or after any major life event (birth, death, divorce, move to a new state, significant asset change). In practice, 60-70% of estate plans are never updated after initial signing. Clients forget. Attorneys have no systematic way to track which clients are due for review or which life events should trigger outreach. The result: plans that name a deceased executor, leave assets to an ex-spouse, or fail to account for new children or grandchildren. For the attorney, this is also a massive revenue leak — plan updates are a $500-$1,500 engagement that requires minimal new work but generates meaningful recurring revenue from an existing client relationship.

## Why It's Still Broken
Estate planning attorneys store client files in filing cabinets or basic document management systems (NetDocuments, iManage). These systems store documents but don't extract or track the key parameters that determine when a review is needed: date of last update, named fiduciaries (and whether they're still alive and competent), beneficiary designations, asset values at time of planning, and state of residence. Without structured data on each client's plan parameters, attorneys can't build automated review triggers. They rely on memory, manual file reviews, or generic "it's been 3 years" reminders that don't account for the specific reasons a particular client's plan may need updating.

## What a Fix Looks Like
A client lifecycle management layer that extracts key parameters from existing plan documents (fiduciary names, beneficiary designations, asset references, state of domicile, date of execution) and monitors for trigger events: publicly available life events (property purchases, marriage/divorce filings in some jurisdictions), law changes affecting the client's plan structure, and time-based review intervals. The system generates personalized outreach: "Your will names John Smith as executor — is he still the right choice?" or "You moved from California to Texas in 2024 — your community property provisions may need updating." Attorneys see a dashboard of clients due for review, prioritized by urgency and revenue potential.

## Who Feels the Pain
Estate planning attorneys who have built a client base of 200-500+ plans over a career but have no systematic way to stay in touch with past clients or identify which plans need updating. The clients themselves, who may be unaware their plans are dangerously outdated.

## Impact If Fixed
Recovers $50K-$150K per year in update revenue for a solo attorney with 300+ past clients. Reduces malpractice exposure from outdated plans that fail to reflect the client's current wishes. Transforms estate planning from a one-time transaction into a recurring client relationship.
