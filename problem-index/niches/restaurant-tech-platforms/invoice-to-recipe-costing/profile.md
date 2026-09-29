# Invoice-to-Recipe Costing

**Parent Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in restaurant back office is fighting to map a distributor invoice line to the recipe ingredient it actually is, at a cost per usable unit — and whoever holds the automatic match rate highest takes the account.

## Profile
**Market Size:** ~$550M US restaurant back-office and inventory software
**Share of Parent Industry:** ~5% of restaurant technology revenue
**Digital Adoption:** Medium — invoice capture is widely adopted and works; the mapping downstream of it does not
**Target Buyer:** Product leads at MarginEdge, Restaurant365, Craftable and their competitors; operators who have tried to cost a plate
**Automation Potential:** Very High — this is entity matching against a catalogue, with abundant training data at every vendor

## What Makes This a Distinct Niche
Plate costing is the arithmetic that tells an operator whether a dish makes money, and it depends on a join that nobody has automated: the line "CHKN BRST BNLS SKNLS 40# CS" on a distributor invoice is the ingredient "chicken breast" in a recipe, at some cost per usable ounce after trim and cooking loss. Every element of that sentence is a problem. Distributor item descriptions are abbreviated, inconsistent between distributors, and change without notice. Pack sizes and units vary. Yield factors — how much of a purchased unit survives to the plate — are recipe- and product-specific and are held in a chef's head. The consequence is that back-office products capture invoices beautifully, cost recipes beautifully, and require a human to sit between the two forever. Operators do the mapping during onboarding, stop maintaining it, and their plate costs quietly go stale.

## Current Tools & Gaps
MarginEdge, Restaurant365, Craftable and xtraCHEF do invoice capture well — optical extraction of distributor invoices is a solved problem in this category. Recipe costing modules are competent. Distributor catalogues are available through EDI for the large distributors and absent for the rest. The unsolved middle is the mapping, which every vendor handles by asking the customer to do it, with some assistance from previously matched items on that customer's own account. None of them pools matches across customers, despite the fact that the same distributor item appears on thousands of their customers' invoices and has already been mapped correctly hundreds of times. Yield factors are entered manually if at all, and are the largest source of error in a plate cost that appears precise.

## Problems
- [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/build|🔨 Build: A Pooled Mapping of Distributor Items to Ingredients]]
- [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/buy|🛒 Buy: Product Matching Methods From E-Commerce]]
- [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/fix|🔧 Fix: The Plate Cost That Went Stale in March]]
