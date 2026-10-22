# Retransmission Subscriber Reports Nobody Audits

**Industry:** [[broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Royalty-management software already reconciles licensing income for music and brand owners, but retrans fees are paid per subscriber per month on counts the distributors report themselves, and most stations check them only by trend.
**Tags:** #bayesian-inference #exponential-smoothing #change-point-detection #hypothesis-testing #feature-engineering #data-integration #revenue-impact

## The Problem
BIA put local TV retransmission fees at ~$14.3B in 2024. That money arrives as monthly or quarterly payments from cable operators, satellite providers, telco video services and virtual distributors such as YouTube TV and Hulu + Live TV. Each payment is computed as a contracted per-subscriber rate, often escalating yearly and varying by tier, times a subscriber count that the distributor reports. A mid-size group's distribution team receives reports from dozens of distributors covering hundreds of headends and zip-code footprints across its markets (estimate). The counts move with cord-cutting, system sales, tier repackaging, out-of-market carriage and vMVPD territorial rules.

The station side usually checks the totals against last month and the contract rate, and books the revenue. Under-reporting is rarely fraud. It is a headend left off after a system migration, subscribers moved to a tier the distributor treats as exempt, or a vMVPD counting by billing address while the agreement counts by DMA. It surfaces, if at all, in a contractual audit that the station can invoke only once per period and that costs outside fees. The retrans agreement is also where reverse compensation to the network is calculated, often on the same subscriber counts, so an error in one flows into the other.

## What Already Exists
Royalty and rights-management software (Rightsline, Flowhaven and similar) tracks licensing contracts, rate schedules and incoming royalty statements for content and brand owners. ERP and revenue-recognition tools book the receivable. Specialist audit firms run contractual audits of distributor reports on commission or fee. Nielsen and the distributors' own disclosures give market-level subscriber trends, and S&P Global and BIA publish industry estimates of retrans per subscriber.

## The Customisation Gap
Retrans needs domain logic the royalty tools do not carry. They need to map distributor systems and zip footprints to DMAs and to the station's licensed carriage area, including significantly viewed and out-of-market exceptions. They need tier definitions that decide which subscribers are billable, and contract-specific escalators, minimum guarantees and most-favoured-nation terms. Every count also needs an expected value it can be tested against: a model of each system's subscriber trajectory, built from its own history, peer systems in the market, broadband-only household trends and the distributor's public results. Finally the audit trail must hold up under the agreement's audit clause and the confidentiality that surrounds retrans terms.

## Impact If Solved
Recovering even ~0.5–1% of retrans revenue through earlier detection of under-reported systems (estimate) would be worth tens of millions of dollars a year across the industry. A large group's distribution team could check every system monthly instead of auditing one distributor every few years, and would go into the next negotiation knowing its real subscriber base.
