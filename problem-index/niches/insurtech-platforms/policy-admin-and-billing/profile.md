# Policy Administration & Billing

**Parent Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in policy administration is fighting to get a product, rate or form change into production across every state it is filed in without breaking billing, reporting or reinsurance — and whoever shortens that cycle most takes the account.

## Profile
**Market Size:** ~$3.6B US policy administration and billing systems
**Share of Parent Industry:** ~23% of insurtech revenue
**Digital Adoption:** High — every carrier runs one and most are mid-programme on replacing it
**Target Buyer:** Product, underwriting operations and technology leaders at carriers
**Automation Potential:** High — the change cycle is dominated by validation work that is automatable

## What Makes This a Distinct Niche
Policy administration is the system of record for what the carrier sold and what it is owed. Everything about its competitive position reduces to change velocity: how quickly a carrier can launch a product, adjust a rate, revise a form, enter a state, or respond to a competitor. Carriers buy these systems explicitly for that reason and the programmes reliably disappoint, not because the configuration is inadequate but because a change to a rating structure propagates into billing, into statutory and management reporting, into reinsurance cessions and into the data that feeds every downstream analysis — and establishing that it has not broken any of them is a manual exercise. Billing in particular is where changes break quietly: an instalment structure that does not handle a mid-term endorsement correctly produces incorrect invoices for months before anyone notices, and the notice usually comes from a policyholder.

## Current Tools & Gaps
Guidewire PolicyCenter and BillingCenter, Duck Creek's equivalents, Socotra, EIS and the MGA-focused platforms compete here with extensive configuration tooling. The gaps: configuration is not managed as versioned engineering artefacts, so changes are reviewed in a user interface rather than diffed; rating regression is manual; billing correctness under the awkward cases — mid-term endorsements, cancellations and reinstatements, instalment plans, agency bill versus direct bill — is established by testing scenarios someone thought of; and the relationship between a filed rate and the configuration that implements it is maintained by documentation and diligence rather than by a check. Multi-state variation multiplies all of it, since the same product exists in fifty slightly different forms.

## Problems
- [[niches/insurtech-platforms/policy-admin-and-billing/build|🔨 Build: Configuration as Versioned, Testable Artefacts]]
- [[niches/insurtech-platforms/policy-admin-and-billing/buy|🛒 Buy: Property-Based Testing Applied to Rating and Billing]]
- [[niches/insurtech-platforms/policy-admin-and-billing/fix|🔧 Fix: The Billing Error Found by the Policyholder]]
