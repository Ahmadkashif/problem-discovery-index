# Overnight Multi-Plan Benefits Card

**Niche:** [[niches/optometry-practices/benefits-verification-estimates/profile|Vision & Medical Benefits Verification and Patient Estimates]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An agent that checks every scheduled patient's vision and medical coverage overnight and turns each plan's wording into one standard benefits card the front desk and optician can price from.
**Tags:** #ai-agent #large-language-models #transformers #gradient-boosting #automation #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell each patient before the visit what their plans will pay for the exam, glasses and contacts, and whoever leaves the smallest gap between the pre-visit estimate and the adjudicated claim takes the account.

## The Problem
Front-desk staff check each patient on each plan's portal, copy allowances into the EHR by hand, and still misquote at checkout because the wording differs by plan and the frame chosen changes the answer.

## Why Nobody Has Built This
Vision plans control their portals, and the largest also owns the largest EHR and claims channel (VSP and Eyefinity). Multi-plan tools have had to rely on portal access and screen reading. LLM agents that can work a portal and read benefit text reliably are recent.

## What to Build
An overnight agent that uses electronic eligibility where available and works portals where not. An LLM normaliser turns every plan's benefit text into one schema: exam, lenses by type, frame allowance, contacts, copays and last-used dates. A pricing step at the optical counter combines the card with the frames and lenses chosen. A model learns from adjudicated claims where its estimates were wrong.

## Target Customer
Multi-OD groups and rollups first, then independent practices through their EHR or communication vendor.

## Impact If Built
Automating ~40 checks a day at ~5 minutes each returns ~3 staff hours daily per office (estimate), and cutting estimate-to-claim gaps reduces checkout disputes.
