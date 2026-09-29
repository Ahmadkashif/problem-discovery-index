# Rate Engines Extended to Client-Specific Taxability Determination
**Niche:** [[niches/accounting-firms-smb/salt-research-units/profile|State & Local Tax Research Units]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Avalara and Vertex answer "what is the rate here" with total reliability and stop precisely at the question that requires professional judgment — "is this thing taxable here at all."
**Tags:** #bert #transformers #large-language-models #transfer-learning #evaluation-metrics #data-integration #compliance #automation

## The Problem
Indirect tax compliance splits into two questions. Is this transaction taxable in this jurisdiction, and if so at what rate? The second question is fully automated and has been for years. The first is answered by a researcher reading state authority and applying it to the client's specific products, services, and delivery methods. That determination then gets configured into the rate engine as a product tax code, and from that point the engine executes it faithfully — including faithfully executing it after it has become wrong. The determination layer is where the professional work is, where the liability sits, and where no tooling exists.

## What Already Exists
Avalara, Vertex, and Sovos provide accurate rates, jurisdiction boundaries by address, filing calendars, and return preparation. Their product tax code taxonomies encode common determinations for standard goods. Research platforms publish state-by-state analysis that a researcher reads. Each of these is mature and does its job well.

## The Customization Gap
Rate engines accept a determination as configuration and never revisit it. They cannot tell a firm that a product tax code assigned two years ago rests on guidance a state has since amended, because they hold no link between the configuration and the authority behind it. What needs building alongside them is a determination layer that sits upstream: it records why each product tax code was assigned, ties that to specific authority, monitors for changes to that authority, and pushes corrections back into the engine's configuration when the basis moves. The rate engine stays exactly as it is — the adaptation is a system of record for the judgment that configures it, which is the part the vendor deliberately does not own.

## Target Customer
SALT researchers who make determinations and the compliance staff who configure and operate the rate engines downstream of them.

## Impact If Solved
Closes the gap between a determination becoming stale and the compliance system continuing to apply it — the most common cause of accumulated indirect tax exposure. Makes engine configuration auditable, with each product tax code traceable to the authority and researcher behind it.
