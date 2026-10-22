# Coding Every Business to the Compiler's Own Headings

**Industry:** [[directory-and-list-publishers|Directory & List Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic classifiers can guess a business's industry; a compiler needs every one of tens of millions of records coded to its own proprietary SIC extensions and directory headings, with a stable primary code, so that the counts it sells do not jump when a model is retrained.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #feature-engineering #automation #quick-win

## The Problem
The industry code is the most-used select in list buying. A buyer asks for dentists, HVAC contractors or commercial printers in a territory, and the compiler counts records coded to the matching headings. Compilers maintain their own taxonomies — extended eight-digit SIC codes and thousands of yellow-pages-style headings — mapped to NAICS for buyers who ask in that language. Each record carries a primary code and several secondary ones, assigned from the business name, carrier advertising classification, filings, the website's description and past codes.

The errors are specific and expensive. A list of dentists includes dental laboratories and dental supply distributors. A business that does plumbing, heating and electrical is primary-coded to whichever word appeared first. A retrained classifier moves tens of thousands of records from one heading to another, a repeat buyer's count shifts by double digits (illustrative) without any change in the world, and the account manager spends a week explaining it. Customers file credit claims for off-target records, and the analysts who maintain the taxonomy correct codes by hand.

## What Already Exists
Large language model APIs and fine-tunable text classifiers can assign an industry from a description with good accuracy. Map platforms publish their own place categories. NAICS autocoders exist, including the Census Bureau's own for survey responses, and commercial lookup services map businesses to SIC and NAICS.

## The Customisation Gap
The generic tools classify into public or platform taxonomies, once, without memory. The compiler's logic is: its proprietary code set and its mapping tables to SIC, NAICS and heading lists; primary-versus-secondary rules (what the business mostly does, not everything it mentions); exclusion rules buyers depend on (laboratories are not practices, distributors are not manufacturers); evidence attached to each code so an analyst can see why; and stability, meaning a code changes only when the evidence changes, with every reclassification batch previewed against the counts of the compiler's top repeat orders before release. The model has to be judged on churn as well as accuracy.

## Impact If Solved
Cleaner primary codes cut off-target credits and the hand-correction queue, and stable codes stop repeat buyers' counts from moving for no reason — the kind of surprise that costs renewals.
