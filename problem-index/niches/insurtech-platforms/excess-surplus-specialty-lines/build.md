# Coverage Comparison Across Manuscript Wordings

**Niche:** [[niches/insurtech-platforms/excess-surplus-specialty-lines/profile|Excess, Surplus & Specialty Lines]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** E&S quotes differ in coverage in ways that matter and are buried in wording, and the comparison a client needs to make an informed choice is a spreadsheet a broker built from whichever differences they noticed.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #graph-theory #tacit-knowledge-ml
**Contested on:** Every serious competitor in E&S technology is fighting to make manuscript coverage comparable across markets so a broker can tell a client what they are actually buying — and whoever makes coverage comparison reliable takes the account.

## The Problem
A broker receives four quotes for a difficult risk. They differ in premium, which is visible, and in coverage, which is not: one carries a sublimit on a peril the client cares about, one has an exclusion the others do not, one defines the insured operations more narrowly, and one attaches a condition precedent that will matter at claim time. Comparing them properly means reading four policy forms in full, which takes hours the broker does not have on every placement, so the comparison covers the differences the broker thought to check. The client chooses on price among options that were never made equivalent, and the difference surfaces at a claim.

## Why Nobody Has Built This
The whole point of manuscript wording is that it is not standard, which defeats any approach based on form recognition. Comparing coverage means understanding what a wording does rather than matching text, and until recently that was not achievable. There is also a professional caution that is entirely reasonable: a coverage comparison is close to advice, and a broker relying on an automated comparison that missed something has an errors and omissions exposure — which means the product must be an aid to the broker's reading rather than a replacement for it, and must be designed accordingly.

## What to Build
A structured coverage representation extracted from each wording — insuring agreement scope, definitions that materially narrow or broaden it, exclusions, sublimits, conditions, retentions, territory, trigger basis — with every element cited to the clause it came from. Comparison is then structural rather than textual: the same coverage dimension across four policies, with the differences surfaced and ranked by how much they matter for this client's exposures. Ambiguity is stated rather than resolved, because wordings genuinely are ambiguous and a product that flattens that is dangerous. The broker's own annotations and prior comparisons accumulate, since the expertise in this segment is knowing which differences matter for which risks, and capturing it is worth more than any general model. The output is a comparison a broker reviews and signs rather than one that stands alone, which is both the correct professional posture and the design that makes it usable.

## Target Customer
Wholesale brokers and specialty retail brokers placing E&S business, the specialty carriers who would benefit from their broader coverage being visible, and the E&S platform vendors.

## Impact If Built
Coverage comparison is the central unmet need in a growing segment and the reason clients in E&S frequently do not know what they bought. It also changes the market's competitive dynamics: a carrier offering genuinely broader terms currently competes on price because nobody can see the difference, and making coverage visible is the condition for competing on it.
