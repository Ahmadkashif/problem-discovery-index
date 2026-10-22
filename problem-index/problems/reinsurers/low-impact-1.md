# Cedent Exposure Submissions in Model-Ready Form

**Industry:** [[reinsurers|Reinsurers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every reinsurer re-keys the same cedent exposure spreadsheets into its catastrophe models each renewal, fixing geocodes, construction codes and insured values by hand, because generic document and data tools do not know what a model-ready exposure file must contain.
**Tags:** #large-language-models #k-nearest-neighbors #gradient-boosting #feature-engineering #data-integration #automation #quick-win

## The Problem
A property cat submission arrives from the broker four to eight weeks before 1 January (estimate). Its core is the exposure: tens of thousands to millions of locations with address, construction class, occupancy, year built, number of storeys, roof type, total insured value by coverage, deductibles and policy limits. Some cedents send model-ready files in a vendor format. Many send spreadsheets in their own layout, with construction described in free text ("joisted masonry", "JM", "brick veneer"), values in mixed currencies and units, and coordinates missing or geocoded only to postcode centroid. The reinsurer's exposure analysts map the fields, recode construction and occupancy into each model's scheme, re-geocode, flag implausible values, and only then run the models. Supercede described the submission process at its 2021 launch as typically taking several months of spreadsheets sent between cedents, brokers and reinsurer panels.

The same file is cleaned again by every reinsurer on the panel, each in its own way, and the quality of the cleaning varies with how busy the analyst is in mid-December.

## What Already Exists
Generic document extraction and ETL tools (Alteryx, intelligent document processing platforms, spreadsheet automation) and the vendors' own import utilities in Verisk Touchstone and Moody's RMS. Exposure data standards such as the Oasis Open Exposure Data format and vendor exchange formats. Submission preparation products such as Supercede's Packs, and the analytics teams of reinsurance brokers, described in [[independent-insurance-agents|Independent Insurance Agents]]' reinsurance broking analytics pocket, which clean data before it goes to market.

## The Customisation Gap
The generic tools move data; they do not know what makes exposure model-ready. The reinsurance-specific logic is: mapping free-text construction and occupancy descriptions to each model's codes, with the differences between them; geocoding resolution flags and their effect on modelled loss; insured-value plausibility checks against rebuild-cost benchmarks by region and occupancy; detection of missing secondary modifiers (roof age, opening protection) that move hurricane loss materially; policy terms (deductibles, sublimits, layers) structured for the financial module; and a data-quality score per submission the underwriter can use as a pricing input rather than a complaint. A broker's cleaned file solves the broker's problem. The reinsurer still needs its own view of what was wrong with the data, because that view is part of its price.

## Impact If Solved
A standard, reusable intake turns a two-to-three day cleaning job per large submission into hours (estimate). It also gives cat teams the capacity to model more programmes in the renewal window and puts a consistent data-quality measure under every quote. That measure feeds directly into the own-view-of-risk adjustments described in [[problems/reinsurers/high-impact|the high-impact problem]].
