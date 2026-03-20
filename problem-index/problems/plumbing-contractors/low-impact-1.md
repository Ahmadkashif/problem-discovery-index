# Job Scope and Quoting from Voice or Photo Intake

**Industry:** [[plumbing-contractors|Plumbing Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic voice-to-text and photo tools exist but don't understand plumbing-specific scope language or translate a technician's field assessment into a structured quote with labor hours, materials list, and tiered pricing options that the dispatcher can present to the customer over the phone.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #loss-functions #evaluation-metrics #automation

## The Problem
Residential plumbing service calls follow a consistent structure: technician assesses the problem, estimates the scope and labor, quotes the customer, and gets approval before starting work. The quoting step is where revenue is made or lost — a vague quote leads to disputes; a slow quote loses the job to a competitor who quotes faster. Currently, the technician calls or texts the dispatcher with a verbal scope description ("this is a water heater replacement, 40 gallon gas, need to run new gas line because the existing flex is corroded"), and the dispatcher manually builds the quote in ServiceTitan, pulling material costs from memory or a price book and calculating labor. This takes 10-15 minutes per quote, during which the customer waits and the technician stands idle.

## What Already Exists
ServiceTitan has a price book and quoting workflow. Generic voice-to-text apps transcribe field descriptions. GPT-4 can generate service descriptions from freeform text. None of these know what a "40-gallon gas water heater installation including gas line, T&P valve, expansion tank, and permit" should cost in labor and materials for a specific contractor in a specific market — they don't know the local labor rates, the contractor's markup structure, the current wholesale price of a 40-gallon Rheem unit, or the flat-rate pricing tiers the contractor uses.

## The Customisation Gap
A plumbing-specific quoting tool needs: (1) a structured plumbing scope language that maps verbal descriptions to specific task codes (water heater replacement 40G gas = specific labor unit + specific material list); (2) integration with the contractor's price book and current material costs; (3) tiered option generation (good/better/best — basic replacement vs. replacement with expansion tank vs. tankless upgrade); (4) jurisdiction-specific permit cost inclusion. The plumbing scope taxonomy and the three-tier option structure are specific to residential plumbing service contracting and are not in any general-purpose quoting tool.

## Impact If Solved
Reduces quote generation time from 10-15 minutes to under 2 minutes. Enables technicians to quote on-site without dispatcher involvement, improving close rates by eliminating the delay between assessment and customer decision.
