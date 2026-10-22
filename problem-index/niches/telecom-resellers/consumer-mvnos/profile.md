# Consumer MVNOs

**Parent Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Category:** High Market Share
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in consumer mobile resale is fighting to sell host-network service below the host's own brands while paying the host wholesale", but that produces two contests with different winners. Cable and converged MVNOs win by moving their subscribers' traffic off the host's network onto their own Wi-Fi and small cells inside a broadband bundle. Independent digital MVNOs have no network to offload to, so they win by keeping a newly acquired subscriber past the point where acquisition cost is repaid. Decomposed into contested sub-niches below.

## Profile
**Market Size:** ~$15B a year in US consumer MVNO service revenue, cable MVNOs included (estimate)
**Share of Parent Industry:** ~25% of a ~$60B resale economy (estimate)
**Digital Adoption:** High at the front end (eSIM activation, app-only brands), Low in the back office (wholesale reconciliation, care that can't see the host network)
**Target Buyer:** VP of Mobile or Head of MVNO at the reseller
**Automation Potential:** High for activation, fraud screening and reconciliation; medium for care

## What Makes This a Distinct Niche
A consumer MVNO sells mobile service on a network it doesn't run, under a wholesale contract with one host. The largest are inside cable operators: Charter's Spectrum Mobile had 11.8M lines at end-2025. Next come prepaid and digital brands, some now owned by the hosts themselves. In November 2025 Boost Mobile moved its traffic onto AT&T's network, which turned the fourth national brand into a hybrid reseller with 7.53M subscribers in Q1 2026. Every consumer MVNO shares the same constraints: the host sets the cost floor, controls the network experience and sees subscriber problems before the MVNO does.

## Current Tools & Gaps
MVNE and BSS platforms such as Telgoo5 handle activation, charging and billing. Payment fraud tools screen card orders, and host portals provide line status. The gaps: no view of the host network from care; activation fraud screened as card fraud only; port-out and SIM-change requests authenticated with weak signals; and wholesale cost not joined to retail margin by subscriber. The FCC's November 2023 SIM-swap and port-out order (WC Docket 21-341) requires carriers to authenticate customers before a SIM change or port-out and to notify them immediately, but a July 2024 bureau order (DA 24-649) deferred compliance with all of its rules until OMB approval and a Federal Register compliance-date notice, and no such notice had appeared by October 2026.

## Problems
- [[niches/telecom-resellers/consumer-mvnos/build|🔨 Build: Port-Out Takeover Defence for MVNOs]]
- [[niches/telecom-resellers/consumer-mvnos/buy|🛒 Buy: Card Fraud Scoring Adapted to eSIM Activation]]
- [[niches/telecom-resellers/consumer-mvnos/fix|🔧 Fix: Customer Care That Can't See the Host Network]]
