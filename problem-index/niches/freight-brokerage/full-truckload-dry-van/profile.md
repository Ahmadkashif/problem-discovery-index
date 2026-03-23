# Full Truckload Dry Van Brokerages

**Parent Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Category:** High Market Share

## Profile
**Market Size:** $45-50B
**Share of Parent Industry:** ~60%
**Digital Adoption:** Medium-High — most FTL brokerages use a TMS (McLeod, Mercury Gate) and load boards (DAT, Truckstop), but pricing and carrier selection remain heavily judgment-driven
**Target Buyer:** Brokerage owner or VP of operations at mid-market brokerages ($10-100M revenue)
**Automation Potential:** High — lane pricing, carrier ranking, and load coverage workflows are data-rich and repetitive

## What Makes This a Distinct Niche
FTL dry van is the core commodity of freight brokerage — one shipper, one truck, one origin-destination lane. The economics are driven entirely by the spread between shipper rate and carrier cost on each load. Unlike LTL (which requires consolidation logic), reefer (which requires temperature compliance), or flatbed (which requires specialized equipment matching), dry van FTL is a pure pricing and capacity procurement game. The broker's competitive advantage is speed of coverage (getting a carrier booked within hours of receiving the tender) and margin optimization (pricing each load to maximize spread without losing the shipper). Mid-market brokerages ($10-100M) are large enough to have meaningful transaction data but lack the internal data science teams that C.H. Robinson or Echo have built.

## Current Tools & Gaps
McLeod Software and Mercury Gate provide TMS functionality for load management and carrier communication. DAT and Truckstop provide load posting and spot rate benchmarks. Parade provides carrier capacity procurement automation. The gap is in integrated pricing intelligence: no mid-market TMS provides a lane-by-lane pricing recommendation that factors in the broker's own transaction history, current market capacity signals, and shipper-specific rate sensitivity.

## Problems
- [[niches/freight-brokerage/full-truckload-dry-van/build|🔨 Build: Real-Time Margin Optimization Dashboard]]
- [[niches/freight-brokerage/full-truckload-dry-van/buy|🛒 Buy: TMS-Integrated Lane Pricing Intelligence]]
- [[niches/freight-brokerage/full-truckload-dry-van/fix|🔧 Fix: Carrier Coverage Speed Bottleneck]]
