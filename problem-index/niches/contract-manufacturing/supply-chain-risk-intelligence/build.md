# Map Coverage as a Measured Property, Not a Node Count

**Niche:** [[niches/contract-manufacturing/supply-chain-risk-intelligence/profile|Multi-Tier Supply Chain Risk Intelligence]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is a map of a supply chain nobody can see the whole of, and it is sold on how many nodes it contains rather than on what fraction of the client's actual exposure it covers.
**Tags:** #graph-theory #graph-neural-networks #bayesian-inference #probability-distributions #confidence-intervals #evaluation-metrics #feature-engineering #monte-carlo-methods #data-integration #compliance

## The Problem
Multi-tier maps are assembled from voluntary supplier disclosure, trade records, and analyst research, and they are necessarily incomplete. Suppliers decline to name their own suppliers; trade records miss domestic movements and services; research reaches what it reaches. The client sees a map with a certain number of nodes and treats the absence of a risk as evidence of no risk, which is exactly wrong — the unmapped portion is where the unmanaged exposure sits, and it is systematically not random, because the suppliers least willing to disclose are frequently the ones with something to disclose. Coverage is reported as node counts and tier depth, which are supply-side metrics, and never as a fraction of the client's spend or product exposure actually mapped.

## Why Nobody Has Built This
Estimating what is missing from a map requires reasoning about what you cannot see, which is genuinely hard and has no obvious method until you look for one. The commercial instinct also runs against it: a vendor that quantifies its own blind spots is arming a client to discount the product, and no competitor is doing it. And the sales metric — nodes mapped, tiers deep — is easy to compare in a bake-off, so it has become the industry's language even though it answers none of the questions a risk executive actually has.

## What to Build
Coverage as a modelled, client-specific quantity. For a given client, the measurement is the fraction of spend, of bill of materials, and of revenue-at-risk for which the chain is mapped to a defined depth — not a node count. What is missing is estimated by triangulation: comparing what different clients' disclosures reveal about shared sub-tiers, using trade record structure to infer relationships that no supplier disclosed, and treating newly discovered nodes across successive research rounds as an indicator of how much remains. Where coverage is thin, the system says so and says where, which converts an invisible gap into a research priority. That in turn directs the mapping effort — the vendor's largest cost — at the parts of a client's chain that most reduce unmeasured exposure rather than at whichever suppliers respond fastest. And the same estimate makes the risk output honest: an alert-free component with poorly mapped sub-tiers is a different statement from an alert-free component whose chain is fully known.

## Target Customer
Chief research officers and heads of supply chain intelligence at risk vendors running 100-600 analysts, and the supply chain risk executives who currently cannot tell an absence of alerts from an absence of visibility.

## Impact If Built
Replaces a sales metric with a decision-relevant one, which is a stronger position in a category where clients are increasingly sophisticated about what these maps do and do not contain. It also redirects the vendor's largest cost from opportunistic mapping to targeted mapping, and gives regulatory-driven buyers — who must demonstrate due diligence rather than merely perform it — the coverage statement their obligation actually requires.
