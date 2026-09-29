# Schema Mapping Tooling Applied to Modifier Structures

**Niche:** [[niches/restaurant-tech-platforms/digital-ordering-middleware/profile|Digital Ordering & Channel Middleware]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Schema mapping and data transformation tooling is a mature commodity from the integration world, and restaurant menu onboarding is performed by people retyping modifier groups into web forms.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #large-language-models #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in ordering middleware is fighting to keep one menu correct across five channels that each model a modifier differently — and whoever requires the fewest manual rebuilds takes the account.

## The Problem
Onboarding a restaurant to a marketplace begins with a menu — sometimes a PDF, sometimes an export, sometimes a photograph of a printed menu — and ends with a person having typed several hundred items, modifier groups and prices into a web interface over several hours. Multiply by the number of channels and by the churn in restaurants, and menu data entry is one of the largest labour lines in the ordering middleware business, performed identically by every vendor in the category.

## What Already Exists
Schema matching and mapping tooling is well developed in the data integration world, including name- and value-based matching, learned correspondences and mapping repositories. Document extraction from PDFs and images is a commodity. Language models handle the semantic part — recognising that "add-ons", "extras" and "toppings" are the same concept — trivially. Product catalogue matching is a solved problem in e-commerce with a substantial literature. Everything needed is purchasable.

## The Customization Gap
The adaptation is to menus specifically, and menus have unusual properties. It requires: (1) modifier semantics as the primary matching target rather than item names, since items are easy and modifier groups are where the labour is; (2) a mapping memory across restaurants, because the same concepts recur constantly — a pizza chain's topping structure resembles every other pizza chain's — and a vendor onboarding its ten-thousandth restaurant should be solving almost nothing new; (3) confidence-gated automation with human review of the uncertain minority, presented as a diff against the source menu rather than as an empty form; (4) price and availability treated as volatile and separately synchronised, since those change daily while structure changes rarely and conflating them is why sync products are slow; and (5) validation against the channel's actual constraints before submission, so a rejected menu is caught in the tool rather than after upload.

## Target Customer
Ordering middleware vendors and marketplace onboarding teams, and the agencies that perform menu builds as a service.

## Impact If Solved
Menu onboarding labour is a direct and large cost in this niche, and mapping memory across a vendor's own customer base makes each subsequent onboarding cheaper — a compounding advantage that no competitor can copy without equivalent volume. It is also the fastest route into the niche's contested capability, because the mapping repository is exactly what the canonical model needs to be populated from.
