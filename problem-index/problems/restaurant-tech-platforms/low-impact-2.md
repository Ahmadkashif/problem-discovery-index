# Invoice Line to Recipe Ingredient Matching

**Industry:** [[restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Invoice capture works well, recipe costing works well, and the join between them — this distributor line item is that recipe ingredient, at this cost per usable ounce — is done by hand at every restaurant, forever.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #dbscan #feature-engineering #evaluation-metrics #data-integration

## The Problem
Food cost is the number restaurant operators watch most closely and understand least precisely. Computing it properly requires knowing what each recipe costs, which requires knowing what each ingredient costs, which requires matching every line on every distributor invoice to the ingredient it represents.

That matching is the wall. A single restaurant buys from three or four distributors, each with its own item codes and descriptions. The same chicken thigh arrives as `CHIX THIGH B/S 40# CS`, as a branded equivalent from a second distributor, and as a substitution the driver made on Tuesday. Pack sizes differ. Some items are priced by case, some by weight, some by count. Yields differ — a case of whole birds and a case of portioned thighs cost differently per usable ounce and the recipe needs usable ounces.

Back-office platforms capture invoices accurately. Somebody then sits and maps each line to an ingredient, and re-maps it whenever a distributor changes a code, which they do routinely.

## What Already Exists
Invoice capture and OCR from MarginEdge, Restaurant365, Craftable and others is genuinely good — the extraction problem is solved. Distributor EDI feeds exist for the larger operators. Recipe costing modules are standard. GS1 and GTIN standards exist for identification and are inconsistently applied in foodservice. Inventory counting apps are widespread.

## The Customisation Gap
The gap is entity resolution over a messy, drifting catalogue, and it is not a feature — it is the layer everything else depends on.

Nothing available maps a distributor line to a canonical ingredient with any reliability, because doing it requires a canonical ingredient catalogue that does not exist, plus a matcher that handles abbreviation, brand substitution, pack variation and yield. The vendor can build both, because it observes millions of invoice lines across thousands of restaurants and the same items recur constantly. A line description seen ten thousand times across a customer base does not need to be mapped by hand at the ten-thousand-and-first restaurant.

Yield normalisation is the second half and the part that changes the answer. Cost per case is not cost per usable ounce, and every meaningful comparison — between distributors, between substitutions, between recipe versions — requires the second number.

The prize is bigger than costing. Once lines resolve to canonical ingredients, the vendor can tell a restaurant that it is paying above the market for an item its neighbours buy cheaper, which is the single most valuable thing a back-office system could say and none of them can say it.

## Impact If Solved
Food cost is a third of revenue and is managed against numbers most operators know are approximate. Removing the manual mapping makes accurate costing routine rather than aspirational, and unlocks cross-restaurant price benchmarking that no single operator could ever assemble.
