# TMS-Embedded Carrier Recommendation Module

**Niche:** [[niches/freight-brokerage/load-matching-dispatch/profile|Load Matching & Dispatch Automation]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Parade and Newtrul provide carrier matching as standalone platforms, but dispatchers won't alt-tab to a separate tool during rapid-fire load coverage — the carrier recommendation must be embedded inside the TMS dispatch screen where the dispatcher already works.
**Tags:** #gradient-boosting #automation #data-integration #quick-win

## The Problem
A dispatcher covering 30 loads per day operates in their TMS — McLeod, Mercury Gate, or a custom system. When a carrier matching tool requires switching to a separate browser tab or application, the dispatcher uses it for the first week and then reverts to their mental carrier list because the context switch takes too long during high-pressure coverage periods. Standalone carrier matching tools have low adoption rates because they interrupt rather than enhance the dispatch workflow.

## What Already Exists
Parade provides carrier capacity procurement with a standalone interface. Newtrul provides carrier matching from the carrier side. McLeod and Mercury Gate have basic carrier search functionality. No TMS provides a recommendation engine embedded in the dispatch screen that surfaces the best carriers for each load without requiring the dispatcher to leave their workflow.

## The Customization Gap
A TMS-embedded carrier recommendation needs: (1) deep integration with the specific TMS data model (McLeod's database schema differs from Mercury Gate's); (2) a recommendation panel within the dispatch screen that shows ranked carriers with acceptance probability, last rate on this lane, and days since last load; (3) one-click outreach from the recommendation panel (call, text, email) without leaving the TMS; (4) feedback loop where the dispatcher's accept/decline decisions train the model. The TMS-specific integration work is the barrier — each TMS requires a custom integration.

## Target Customer
Dispatch desk managers at brokerages using McLeod or Mercury Gate who have evaluated standalone carrier matching tools and found adoption too low to justify the cost.

## Impact If Solved
Embedded carrier recommendations used by 80%+ of dispatchers (vs. 20-30% adoption for standalone tools) deliver the full time-savings value: 15-20 minutes per load in reduced outreach time, translating to 3-4 additional loads covered per dispatcher per day.
