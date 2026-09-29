# Resolving Who the Supplier Is

**Niche:** [[niches/ap-automation-vendors/vendor-identity-resolution/profile|Vendor Identity Resolution]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same supplier appears under a dozen spellings across the customer base, and the platform has already seen all of them resolved somewhere.
**Tags:** #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #transfer-learning #data-integration #automation #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to determine which records refer to the same supplier across a decade of duplicates, abbreviations, mergers and typos — and whoever resolves most accurately using what every other buyer knows owns the record everything else depends on.

## The Problem
A supplier's name appears as the legal entity, the trading name, an abbreviation, a misspelling, a former name after an acquisition, and a division name. Tax identifiers are recorded inconsistently or not at all. Addresses change. Within one customer this is a hard matching problem with thin evidence. Across a customer base where the same supplier invoices hundreds of buyers, the evidence is abundant — and no platform has pooled it.

## Why Nobody Has Built This
Matching was implemented as an exact-string duplicate check at record creation, so the problem was scoped as accident prevention rather than as identity resolution — and that scope has never been revisited. Resolution across customers requires a shared reference nobody built. Registry data is fragmented and costs money. And nobody measured the duplicate rate, so the problem's size is unknown even to the customers living with it.

## What to Build
Resolve against a shared reference built from the network. Construct a cross-customer supplier reference from the platform's own invoice and payment data, which is the core and is the asset no single customer could assemble. Match on the strong identifiers first — tax identifier, bank account, registered address — since names are the weakest evidence and are what current checks rely on. Use invoice content as matching evidence, because the same supplier's invoice layout, line item language and terms recur and are highly distinctive. Model corporate structure so parents, subsidiaries and divisions are related rather than merged, as collapsing them is as wrong as splitting them. Express match confidence rather than a binary, since a wrong merge is expensive and the uncertain cases must reach a human. Enrich from business registries where available, which anchors the network resolution in external truth. Handle mergers and rebrands as events rather than as contradictions, because they are the main source of legitimate change. Resolve at the moment of record creation and at invoice arrival, so the resolution is preventive rather than a cleanup. Maintain a persistent entity identifier across customers, which is what makes cross-buyer intelligence and payment verification possible. And measure resolution accuracy against reviewed samples, since an unmeasured matcher drifts.

## Target Customer
Data and operations leadership, AP and procurement teams, and entity resolution and business data vendors with no invoice-level evidence.

## Impact If Built
Matching was scoped as accident prevention at record creation and never revisited as identity resolution. The same supplier invoicing hundreds of buyers is evidence no single customer has, and it makes the hard cases tractable.
