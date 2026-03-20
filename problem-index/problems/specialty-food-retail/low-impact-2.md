# Allergen and Dietary Label Compliance for Prepared Foods

**Industry:** [[specialty-food-retail|Specialty Food Retail]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Stores selling prepared foods generate compliant allergen and nutritional labels from their recipes instead of guessing with handwritten signs.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance

## The Problem
Specialty food stores that make prepared items — deli salads, bakery goods, sandwiches, soups, grab-and-go meals — are subject to FDA allergen labeling requirements (FSMA, FALCPA) and increasingly to state-level calorie disclosure laws. Most small stores handle this with handwritten "contains: nuts, dairy" signs or generic printed cards that are not updated when recipes change. When a bakery swaps one flour brand for another (with different trace allergen warnings), the label often does not follow. A single mislabeled item can cause an allergic reaction, a lawsuit, or an FDA warning letter.

## What Already Exists
Nutritional analysis software (Nutritionix, MenuCalc, ReciPal) can calculate nutritional panels and allergen flags from ingredient lists. These tools work well for packaged food manufacturers with stable recipes and formal ingredient specs. They assume the user can provide precise weights, brand-specific ingredient lists, and consistent batch sizes — inputs that a bakery counter employee rotating through 30 daily recipes with substitutions does not reliably have.

## The Customisation Gap
A specialty food retail solution needs to handle recipe variability: the same soup may use different cheese brands week to week depending on what the buyer sourced, and each brand carries different allergen cross-contamination warnings. The system must parse natural-language recipes ("a handful of the good parmesan" needs to resolve to a specific SKU in inventory with known allergen data), pull allergen and nutritional data from linked ingredient records, and regenerate labels when any ingredient substitution occurs. NER on ingredient lists plus a mapping layer to the store's actual purchased inventory would bridge the gap between recipe as written and label as required.

## Impact If Solved
Stores avoid the $10K–$50K cost of an allergen-related incident (recall, legal fees, reputational damage). Staff spend zero time manually researching allergen data for recipe changes. Compliance becomes automatic rather than aspirational, which is particularly valuable as FDA enforcement of small retail prepared food labeling increases.
