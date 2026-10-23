# Onsale Bot & Purchase-Limit Enforcement

**Parent Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to stop one buyer from holding many accounts at an onsale without blocking real fans, and whoever catches the most limit-breaking account clusters at a false-block rate the artist will tolerate takes the account.

## Profile
**Market Size:** ~$300M a year spent by ticketing platforms, marketplaces and reservation systems on bot management, queueing, identity checks and trust-and-safety review (estimate)
**Share of Parent Industry:** ~1.2% of industry receipts (estimate)
**Digital Adoption:** High. The defences are software; linking accounts to the person behind them is the gap
**Target Buyer:** Head of trust and safety or fan protection at a primary ticketer; CISO at a marketplace or reservation contractor
**Automation Potential:** Very high for detection and limit enforcement; appeals stay human

## What Makes This a Distinct Niche
The BOTS Act of 2016 bans circumventing a ticket seller's security measures and purchase limits. Executive Order 14254 (March 2025) told the FTC to enforce it with the states. The FTC sued broker Key Investment Group in August 2025 and Live Nation and Ticketmaster in September 2025, citing five brokers who controlled more than 246,000 tickets through thousands of accounts. Imperva's 2026 report put bad bots at 40% of all web traffic. Simple bots are now the easy part. The contest is the account farm: real browsers, real cards and real-looking people, coordinated by one broker. Enforcement has moved from blocking traffic to proving that many accounts are one buyer, and the regulator now reads the results.

## Current Tools & Gaps
Ticketmaster Verified Fan and SafeTix, AXS mobile ID, Queue-it waiting rooms, bot management from Akamai, HUMAN, Kasada, DataDome and Cloudflare, analysed at the vendor level under [[niches/edge-cdn-providers/bot-and-abuse-management/profile|Bot & Abuse Management]]. Gaps: limits enforced per account rather than per person, no link between onsale purchases and later resale listings, and enforcement evidence not kept in a form a regulator can audit.

## Problems
- [[niches/ticketing-agencies/onsale-bot-enforcement/build|🔨 Build: An Account-Cluster Graph From Purchase to Resale]]
- [[niches/ticketing-agencies/onsale-bot-enforcement/buy|🛒 Buy: Bank Entity Resolution Adapted to Buyer Accounts]]
- [[niches/ticketing-agencies/onsale-bot-enforcement/fix|🔧 Fix: Purchase Limits Counted per Account]]
