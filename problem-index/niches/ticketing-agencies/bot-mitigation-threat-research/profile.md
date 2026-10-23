# Bot Mitigation & Waiting-Room Vendors' Threat Research

**Parent Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Vendors that defend onsales and reservation releases against automated buying: Queue-it's virtual waiting rooms and bot-management services from Akamai, HUMAN, Kasada, DataDome and Cloudflare. Their threat-research teams track scalper bot frameworks, residential proxy networks and account-farm tactics, and publish annual bot reports such as Imperva's, which put bad bots at 40% of web traffic in 2025. Ticketers and retailers pay for the protection.

## Insight Function
**Size:** 10-60 threat researchers and data scientists per vendor (estimate)
**Output:** Detection models and signatures, onsale threat briefings for clients, annual bot reports used as marketing
**Proprietary data:** Traffic telemetry and attack signatures aggregated across client sites
**Clock:** Clients' onsale and release dates
**Buyer:** Head of threat research or chief product officer at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 1 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **31/60** |

**Kill switches:** none live. Aggregated attack signatures are the vendor's own derived data, the standard model in security.
**Verdict:** Logged — below threshold. The research sells protection; nobody buys it for itself. The vendor-level workflow is analysed as [[niches/edge-cdn-providers/bot-and-abuse-management/profile|Bot & Abuse Management]] under Edge & CDN Providers. These vendors see traffic, not tickets, which is why the account-farm problem in [[niches/ticketing-agencies/onsale-bot-enforcement/profile|Onsale Bot & Purchase-Limit Enforcement]] remains open.
