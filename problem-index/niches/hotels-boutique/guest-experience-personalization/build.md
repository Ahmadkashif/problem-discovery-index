# Automated Guest Preference Capture and Surfacing

**Niche:** [[niches/hotels-boutique/guest-experience-personalization/profile|Guest Experience Personalization]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically captures guest preferences from in-stay behavior and surfaces them to staff at the moment of service — forcing personalization to depend on staff memory, which is lost with every turnover.
**Tags:** #bert #text-classification #nlp #recommendation #tabular-ml #worker-facing

## The Problem
A returning guest's preferences are scattered across PMS notes ("prefers high floor"), past housekeeping requests ("extra pillows, hypoallergenic"), restaurant POS data (orders Sauvignon Blanc, never dessert), and front desk interaction logs ("asked about yoga classes"). No system aggregates these signals into a structured guest profile. The front desk agent greeting a returning guest sees "RETURNING GUEST — 3 PRIOR STAYS" in the PMS but has no idea what the guest likes, what went wrong last time, or what room they preferred.

## Why Nobody Has Built This
Guest preference data is distributed across 4-5 systems (PMS, housekeeping logs, F&B POS, messaging platforms, review text) with no shared guest identifier. Aggregating this data requires cross-system integration and NLP extraction from unstructured notes. Building the preference profile is 50% of the problem — the other 50% is surfacing it at the right moment: showing the front desk agent the guest's preferences before check-in, showing housekeeping the room setup preferences before the clean, showing the restaurant the dining preferences before seating.

## What to Build
A guest intelligence layer that integrates with PMS, F&B POS, and messaging systems to automatically build structured guest profiles: room preferences (floor, view, bed type), service preferences (pillow type, minibar stocking, turndown timing), dining preferences (wine, dietary restrictions, favorite dishes), and satisfaction history (past complaints, resolutions). The profile surfaces to staff via a mobile app at the moment of service — the front desk sees it at check-in, housekeeping sees it during room assignment, the restaurant sees it at seating.

## Target Customer
Boutique hotel GMs who want to deliver chain-level personalization without chain-level CRM investment — properties with 20-35% repeat guest rates and 30%+ annual staff turnover.

## Impact If Built
Systematic personalization increases guest satisfaction scores by 10-15% and repeat booking rates by 8-12% — worth $50K-$150K in annual revenue from reduced acquisition costs and increased guest lifetime value.
