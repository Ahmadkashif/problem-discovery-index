# A Time-Bar and Liability Map for Every Open Claim

**Niche:** [[niches/ocean-shipping-carriers/cargo-claims-pi-handling/profile|Cargo Claims & P&I Handling]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each cargo claim needs the carrier's own evidence assembled against a one-year clock, and the evidence sits in systems the claims handler cannot search.
**Tags:** #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to resolve each cargo claim inside the one-year Hague-Visby time bar for the least money, and whoever settles claims at the lowest paid-to-claimed ratio takes the account.

## The Problem
A reefer container of grapes arrives soft. The receiver's insurer sends a claim with a survey report. To respond, the handler needs the booking's temperature setting, the reefer's logged temperatures and power-off periods, the stowage position, the voyage's weather and delays, the B/L clauses and the shipper's pre-trip records. These sit in separate systems and some must be requested from terminals. Meanwhile the one-year time bar runs, and extensions must be agreed in writing.

## Why Nobody Has Built This
Claims volumes per carrier are modest compared with billing or booking, so in-house IT ranks them low, and the evidence crosses operations, equipment and commercial systems. P&I clubs see many carriers' claims but under club rules, not as a product.

## What to Build
A claims workbench that reads each incoming claim, opens a case with the time-bar date and every extension, and pulls the carrier's evidence automatically: reefer logs, stowage, weather, delays, B/L terms and inspection photos. It drafts a liability analysis with the likely defences and the limitation amount. A model trained on the carrier's closed claims estimates the settlement range by claim type, so handlers know which to fight and which to settle early.

## Target Customer
Claims managers at container lines and tramp operators handling claims below their P&I deductible.

## Impact If Built
Cutting the paid-to-claimed ratio by 5 points on ~$20M a year of claims kept below the club deductible (estimate) saves ~$1M a year (estimate), with no claims lost to missed time bars.
