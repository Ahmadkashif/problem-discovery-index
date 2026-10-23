# SI Email to Draft B/L in One Pass

**Niche:** [[niches/ocean-shipping-carriers/booking-bl-documentation/profile|Booking, Shipping Instruction & B/L Documentation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An agent that turns a shipper's email or PDF into a validated draft bill of lading in the carrier's system is the most buildable automation in the industry.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn shipping instructions into a correct bill of lading before the SI cut-off, and whoever issues the highest share of bills of lading with no post-issue amendment takes the account.

## The Problem
Documentation agents open each SI, copy parties, cargo descriptions, container and seal numbers, weights and HS codes into the system, check them against the booking, and send a draft B/L for the shipper's approval. Errors become amendments after issue, which cost fees, goodwill and sometimes customs holds.

## Why Nobody Has Built This
Generic extraction stops at fields; the value is in reconciling with the booking and checking cargo and destination rules, which needs the carrier's own data. Carriers have built portals to push shippers to structured input, but many shippers and small forwarders still email.

## What to Build
An agent that reads the SI in any format, matches it to the booking, drafts the B/L in DCSA schema, validates it against cargo rules (dangerous goods, reefer, out-of-gauge), sanctions screening and destination manifest requirements, and compares it with the shipper's last bills on the same lane. Clean drafts go straight to the shipper; doubtful fields are highlighted with the reason. Agent-delivery engineers are being hired for exactly this kind of deployment: Pallet (San Francisco) lists ocean carriers among its segments, Reform (San Francisco, two FDE roles) extracts bills of lading for forwarders, and Sedna has Senior Delivery Engineers in London and Athens (checked 2026-10-24).

## Target Customer
Documentation heads at mid-sized carriers and NVOCCs issuing house bills, and shared-service directors at the large lines.

## Impact If Built
Take a carrier with ~5% of the market, issuing ~2M bills a year (derived from ~45M a year industry-wide, search summary). Halving a ~10% amendment rate (estimate) there removes ~100,000 amendments a year. Agents work exceptions rather than keying, and a two-week demo on synthetic SIs is enough to show it.
