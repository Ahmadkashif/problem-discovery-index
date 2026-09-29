# The Complaint Nobody Classified

**Niche:** [[niches/print-on-demand-platforms/artwork-outcome-corpus/profile|Artwork-Outcome Corpus]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Customers describe exactly what was wrong with their print in their own words, the message is resolved with a refund, and the description — the only direct evidence of the failure mode — is never classified or counted.
**Tags:** #large-language-models #evaluation-metrics #k-means-clustering #descriptive-statistics #confidence-intervals #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn millions of artwork-to-physical-outcome pairs into a model of what will print well — and whoever does that owns a capability commercial printing never had the data to build.

## The Problem
A customer writes that the colours are much duller than the picture and the edges of the text look fuzzy. That is a precise diagnosis of a gamut problem and a resolution or stroke-width problem, delivered free by the person best placed to observe the result. The agent refunds and closes the ticket with a reason code of quality issue. Tens of thousands of such messages a year contain the failure mode, the product, the artwork and the facility, and the only thing extracted is a code with five options that describes none of them.

## Why It's Still Broken
Support reason codes are chosen for operational routing rather than for diagnosis, and the code set was written when the system was built. Classifying free text was laborious before it became trivial and nobody revisited the practice. The support system and the production data live apart, so even a well-classified complaint would not connect to the order that caused it. And the complaint is treated as a cost to resolve rather than as a measurement.

## What a Fix Looks Like
Classify the text and join it to the order. Classify every complaint into specific failure modes automatically — colour shift, dullness, banding, fill-in, drop-out, cracking, placement, sizing, durability — which is now trivial and immediately converts the largest free diagnostic stream in the business into data, and is the fix. Join the classification to the artwork, product, facility, machine and parameters, which turns individual complaints into a defect Pareto by cause. Report failure modes by facility and by artwork characteristic, which is where the actionable findings are. Feed the classified complaints into the outcome prediction as labels, since they are more specific than a binary reprint flag. Detect emerging failure modes from the text rather than waiting for a category to be added, since a new problem appears in customers' words before it appears in anybody's taxonomy. Replace the operational reason codes with the diagnostic ones where the two conflict, or keep both. Sample and read, since a reviewer reading fifty complaints a week finds things no classifier will. And close the loop to merchants and facilities, because the customer's description is the most persuasive evidence either of them will ever receive.

## Who Feels the Pain
Merchants never told why their design disappoints; facilities never told which failure mode they produce; and platforms discarding the most specific failure data they receive.

## Impact If Fixed
Customers deliver a precise diagnosis in their own words and it is reduced to a five-option code. Automatic classification joined to the production record turns the largest free diagnostic stream in the business into a defect Pareto by cause.
