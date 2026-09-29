# Vendor Master Data and Onboarding

**Industry:** [[ap-automation-vendors|AP Automation Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The vendor master is a decade of duplicated, stale and inconsistent records, and it is simultaneously the root of most exceptions and the surface that payment fraud attacks.
**Tags:** #graph-neural-networks #bert #k-nearest-neighbors #word-embeddings #gradient-boosting #evaluation-metrics #data-integration #compliance

## The Problem
The vendor master accumulates. The same supplier exists as "Acme Corp", "Acme Corporation", "ACME Corp." and "Acme Corp - NEW", created by four people over eight years. Some records carry tax identifiers and some do not. Bank details were entered from a form that arrived by email. Contacts left their companies years ago. Records for vendors that no longer trade are never closed because nobody is sure.

Duplicates cause duplicate payments, which is a direct and recurring loss that entire firms exist to recover after the fact. They also cause exceptions, because an invoice from one spelling does not match a purchase order raised against another.

Onboarding a new vendor requires collecting tax documentation, bank details, insurance certificates where relevant, sanctions screening, and diversity or ESG attributes that many buyers now track. It is a form-and-email process with a chase loop, and it is where fraudulent vendors enter.

Bank detail changes are the dangerous event. A request to update a vendor's bank account, arriving by email, is the mechanism of business email compromise. The control is a callback, and the callback frequently uses a number from the same email.

Maintenance essentially does not happen. Vendors merge, change names, change banks, go out of business, and the master file learns about it when a payment fails or an invoice does not match.

## What Already Exists
Vendor portals for self-service onboarding are standard in the larger platforms. Tax form collection and validation are automated. Sanctions screening is a mature vendor category. Bank account verification services exist (micro-deposits, Plaid, Trustpair, nsKnox). Duplicate detection tools ship with most ERPs and rely largely on exact and fuzzy name matching.

## The Customisation Gap
Entity resolution is done on names and addresses when it should be done on a graph. The same vendor across records shares tax identifiers, bank accounts, remittance addresses, contact domains, invoice templates and buyer-side transaction patterns; linking on that structure is far stronger than string similarity and is the established method in every adjacent domain.

Cross-customer verification is the platform's unique and unused asset. A vendor invoicing four hundred buyers on the same platform has an observable, corroborated identity — its bank details, its address, its invoice format, its price levels. A bank detail change that appears for one buyer and for no other buyer of the same vendor is exactly the signal that stops business email compromise, and it requires no new data.

Nothing monitors decay. Vendors that have stopped invoicing, contacts whose email domains now bounce, entities that no longer appear in registries — all detectable, none monitored.

And price benchmarking is left on the table. The platform sees what hundreds of buyers pay the same vendor for comparable goods, which makes an invoice priced well outside the distribution a flag worth raising and is currently visible to nobody.

## Impact If Solved
Vendor master quality determines duplicate payment losses, a large share of exceptions, and the entire attack surface for payment fraud. Graph-based entity resolution and cross-customer corroboration are both available to a platform today, address all three at once, and constitute the one thing a platform can do that no individual customer ever could.
