# Virtual-Address & Mail-Drop Risk Signal Vendors

**Parent Industry:** [[industries/private-mail-centers|Private Mail Centers]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Identity-verification and know-your-business vendors (Persona, Middesk, Baselayer, LexisNexis Risk Solutions and others) tell banks, payment companies and marketplaces whether an applicant's address is a home, an office, or a mail drop. They combine the USPS DPV commercial mail receiving agency flag, which marks every CMRA address, with their own lists of virtual-office and virtual-mailbox providers and business-registry matches. Persona's address report, for example, exposes a DPV CMRA field beside a separate virtual-address detection check. Clients pay per lookup or as part of a verification bundle. The wider identity market is analysed under [[industries/identity-verification-vendors|Identity Verification Vendors]], where address checks sit inside [[niches/identity-verification-vendors/database-identity-resolution/profile|Database Identity Resolution]]; this pocket is the business-address slice that judges mailbox addresses.

## Insight Function
**Size:** No firm found with a team of 10+ dedicated to address-risk signals; the work is a feature maintained by a few people inside larger identity and KYB products (estimate)
**Output:** Address-type classifications and risk flags returned in onboarding decisions
**Proprietary data:** Compiled lists of virtual-office and virtual-mailbox provider addresses and observed business-registration patterns; the CMRA flag itself is USPS data any CASS-certified vendor can license
**Clock:** Real-time onboarding decisions; no third-party deadline governs the research itself
**Buyer:** Head of data or risk product at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | — |
| Q2 Labor mass + repeatable | ×2 | — |
| Q3 Proprietary data moat | ×3 | — |
| Q4 External clock | ×2 | — |
| Q5 Buyer + market | ×2 | — |
| **Weighted total** | | **—/60** |

**Kill switches:** none — the address lists are compiled from licensed postal data and public sources.
**Verdict:** Logged — fails gate (no dedicated address-risk team of 10+ could be named; the signal is a product feature licensed from postal data rather than an analysis function). The flag treats every one of the 1.6 million registered mailbox holders alike, and the one record that could separate a verified holder from a mail drop, the holder's Form 1583 status in USPS's CMRA database, has no outbound channel. The vendors whose whole product is pooled identity-fraud scoring clear the gate and are logged under Credit Card Issuers as [[niches/credit-card-issuers/synthetic-identity-fraud-consortia/profile|🔍 Synthetic Identity & First-Party Fraud Consortia]] (36). The CASS address-validation vendors that supply the underlying flag are logged under Last-Mile Delivery as [[niches/last-mile-delivery/address-verification-geocoding/profile|🔍 Address Verification & Geocoding]] (47, scored before the batch-review rules on Q2 and Q4).
