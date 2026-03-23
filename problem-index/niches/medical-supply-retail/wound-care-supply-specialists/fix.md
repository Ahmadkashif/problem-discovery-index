# Dynamic Supply Schedule Updates Based on Wound Status Changes

**Niche:** [[niches/medical-supply-retail/wound-care-supply-specialists/profile|Wound Care Supply Specialists]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Fix (Pain Point)
**One-liner:** Wound care supply schedules are set at initial assessment and rarely updated as wounds heal or worsen — so patients receive too much product when healing well and too little when deteriorating, wasting inventory and delaying care.
**Tags:** #automation #workflow-orchestration #data-integration #revenue-impact #worker-facing

## The Problem
When a wound care patient is set up, the nurse establishes a supply schedule: "Ship 30 foam dressings and 1 tube of barrier cream every 30 days." This schedule is entered into Brightree and runs on autopilot. But wounds change: a wound that was draining heavily at setup may dry out as it heals (needing thinner dressings, not foam), while a wound that was stable may become infected (needing antimicrobial dressings not in the original supply kit). The supply schedule almost never gets updated to reflect wound status changes because the DME supplier doesn't receive wound assessment updates from the home health agency, and the patient doesn't know to request different supplies. Result: patients accumulate unused supplies (waste and potential audit liability) or run out of needed supplies between shipments (delayed healing).

## Why It's Still Broken
Wound assessment data lives in the home health agency's EHR, but the supply schedule lives in the DME supplier's billing system. There is no data bridge between them: the home health nurse documents wound improvement in WellSky, but the DME supplier's Brightree system has no visibility into that documentation. Communication happens when the patient calls to report a problem or when the supplier does a manual follow-up call — both reactive approaches that miss the window for proactive supply adjustment.

## What a Fix Looks Like
A wound status integration layer that receives periodic wound assessment summaries from home health agencies (via API, fax-to-digital conversion, or structured assessment forms sent to the supplier) and triggers supply schedule reviews: "Patient Smith's wound has decreased from 4.5 cm to 2.1 cm — current supply volume may exceed need, schedule review recommended." Or: "Patient Jones's wound shows increased drainage and new tunneling — current supply kit may be insufficient, clinical review recommended." The system alerts the wound care coordinator to adjust the supply schedule, generates updated insurance documentation, and modifies the next shipment.

## Who Feels the Pain
Wound care coordinators who discover supply mismatches only when patients call to complain (either accumulating unused supplies or running out), and patients who experience delayed healing because their supply kit no longer matches their wound's needs.

## Impact If Fixed
Reduces supply waste by 15-25% by right-sizing shipments as wounds heal (worth $3K-8K/year in inventory cost per mid-size wound care supplier). Improves clinical outcomes by ensuring supply changes keep pace with wound changes — particularly critical for deteriorating wounds where delayed product adjustment can lead to hospital readmission. Reduces audit risk from excess supply shipments that trigger Medicare scrutiny.
