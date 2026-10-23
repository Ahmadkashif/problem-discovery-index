# Booking, Shipping Instruction & B/L Documentation

**Parent Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn shipping instructions into a correct bill of lading before the SI cut-off, and whoever issues the highest share of bills of lading with no post-issue amendment takes the account.

## Profile
**Market Size:** ~$1.2B global spend on booking and documentation staff, portals and document tooling at carriers (estimate)
**Share of Parent Industry:** ~6% of carrier shore-side spend (estimate)
**Digital Adoption:** Medium — portals, INTTRA and DCSA APIs carry a growing share; email and PDF shipping instructions remain common
**Target Buyer:** Head of Documentation / Global Shared Services Director
**Automation Potential:** Very high — extraction, reconciliation and drafting are rule-bound and labelled by the issued B/L itself

## What Makes This a Distinct Niche
The bill of lading is a receipt, a contract of carriage and, when negotiable, a document of title (recalled), so its contents carry legal and customs weight. Carriers issue roughly 45 million a year, only about 1.2% electronically in 2021 (search summary). DCSA's member carriers have pledged 50% electronic within five years and 100% by 2030 (DCSA). Each B/L starts from a booking and a set of shipping instructions keyed by documentation agents, mostly in offshore shared-service centres (estimate), against SI and VGM cut-offs. Manifest rules such as US advance filing and EU ICS2 add data checks (recalled). The work is repetitive, high volume and judged on one measurable outcome: was the bill right first time.

## Current Tools & Gaps
Carrier booking and documentation systems, INTTRA (E2open) and CargoSmart portals, DCSA booking and eBL standards, eBL platforms (essDOCS, Bolero, WAVE BL, CargoX), generic document extraction. Gaps: email and PDF SIs keyed by hand, validation against cargo and destination rules done by agents' memory, and the shipper's past corrections unused. See [[problems/ocean-shipping-carriers/low-impact-1|Shipping Instructions to a Draft Bill of Lading]]. Data ownership decides how this is trained. Booking requests and shipping instructions are the shipper's or forwarder's submissions; the US import manifest copy becomes public through CBP's AMS release (recalled), which is what [[niches/customs-brokers/import-export-transaction-data/profile|Import & Export Transaction Data Providers]] resell. Booking confirmations, draft and master bills and amendment history are the carrier's records, and house bills belong to the NVOCC that issues them. A vendor therefore trains per carrier under that carrier's service agreement, a model pooled across carriers needs each carrier's consent, and the demo runs on synthetic SIs and the public DCSA schemas.

## Problems
- [[niches/ocean-shipping-carriers/booking-bl-documentation/build|🔨 Build: SI Email to Draft B/L in One Pass]]
- [[niches/ocean-shipping-carriers/booking-bl-documentation/buy|🛒 Buy: Document Extraction Adapted to the DCSA eBL Schema]]
- [[niches/ocean-shipping-carriers/booking-bl-documentation/fix|🔧 Fix: The Amendment Fee Nobody Wanted to Charge]]
