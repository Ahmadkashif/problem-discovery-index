# Account Hierarchy and Data Hygiene

**Industry:** [[crm-platforms|CRM Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Enrichment vendors will fill in firmographics for any account, and nothing keeps the relationships between accounts correct — so the same customer exists four times and nobody can say what a global account is worth.
**Tags:** #bert #word-embeddings #graph-neural-networks #dbscan #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration

## The Problem
A CRM's account object drifts immediately. The same company is created as "Acme Corp", "Acme Corporation", "ACME" and "Acme Corp - EMEA" by four representatives over three years. Subsidiaries are entered as independent accounts. An acquisition happens and nothing in the CRM reflects it. Contacts leave and their records stay, with an email address that bounces and a title from two roles ago.

The consequences are constant. Duplicate accounts split the relationship history, so a representative calls into an account another team is already working. Territory assignment breaks because the parent is in one territory and the subsidiary in another. Nobody can answer what total revenue from a global customer actually is, which is the question the chief revenue officer asks most often.

Contact decay is the quieter cost: business email addresses turn over at roughly a quarter to a third annually, so a database left alone becomes substantially undeliverable within two years.

## What Already Exists
Enrichment providers (ZoomInfo, Clearbit, Dun & Bradstreet, Apollo) supply firmographics, hierarchy data and contact records with reasonable coverage of larger companies. Deduplication tools are standard in the platforms and available from specialists. Master data management platforms handle this at enterprise scale. Email validation services detect bounces.

## The Customisation Gap
Enrichment appends attributes to records; it does not fix the relationships between them. Corporate hierarchy from a data provider reflects legal structure, and the structure that matters commercially is how the customer actually buys — which division holds the budget, which entity signs, which subsidiary was acquired and now buys through the parent. That is knowable from the company's own transaction and engagement history and is not in any external dataset.

Deduplication is treated as a periodic clean-up rather than as continuous entity resolution, and the two errors are asymmetric in a way the tools ignore: merging two genuinely different accounts destroys history and is very hard to undo, while leaving a duplicate is merely untidy. Matching thresholds are set without that asymmetry in view.

Contact decay is predictable rather than merely detectable. Tenure, role, engagement trend and the account's own hiring activity all bear on whether a contact is still there, and the platform could flag likely departures before the email bounces — which is when a representative discovers it, usually mid-campaign.

## Impact If Solved
The account graph is what every territory, forecast and customer analysis rests on, and it is maintained by whoever last cared enough. Continuous resolution with the merge asymmetry respected fixes the foundation, and it uses the platform's own engagement history rather than a purchased hierarchy that describes a different question.
