# Hearing-Record Model of Approval Odds and Timing

**Niche:** [[niches/land-developers/discretionary-rezoning-public-hearings/profile|Discretionary Rezoning & Public Hearings]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every rezoning vote, continuance and condition is published, and nobody has turned the record into a forecast of how long the next case will take and whether it will pass.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #bert #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to carry rezoning and planned-development cases from filing to a council approval at the density the deal needs, and whoever gets the highest share of filed cases approved at the requested lot count takes the account.

## The Problem
Land managers price entitlement risk from memory of how a council behaves. The evidence (years of staff reports, votes, continuances and conditions) sits in public systems, case by case, in PDFs and agenda items nobody has joined.

## Why Nobody Has Built This
Agenda systems are built for clerks, not analysts. Each city structures items differently, staff reports are long PDFs, and the outcome of a case can span several agenda items over months. Until language models, reading them at scale was a manual research project.

## What to Build
Ingest a metro's agenda systems (starting with open APIs such as Legistar's), link items into cases by case number and parcel, and extract staff recommendation, requested and approved density, conditions, speakers and votes. Fit time-to-approval and approval-probability models with comparables, calibrate them per jurisdiction, and capture the land manager's own forecast beside the model's. This is the owner's MVP and [[problems/land-developers/ml-opportunity|ML Opportunities]] entry 1.

## Target Customer
Land acquisition and entitlement teams at national and regional builders, land developers and land-banking platforms; also data-center and energy developers facing the same councils.

## Impact If Built
An approval forecast with comparables lets a developer price the land and set the feasibility period from evidence. Walking away from one tract a year that would have been denied saves ~$0.3M of studies, legal fees and extension payments (estimate). Raising the share of cases approved at the requested lot count by 5 points on 300-lot cases keeps 15 lots per case, ~$1.6M at $108,400 a lot (estimate).
