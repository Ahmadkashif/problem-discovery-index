# Reaching the Page and Reading It Are Different Businesses

**Niche:** [[niches/web-data-extraction-firms/collection-infrastructure/profile|Collection Infrastructure]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Access infrastructure competes on successful requests per dollar against evolving detection, and extraction competes on fields returned correctly from unfamiliar markup, and firms sell them as one product.
**Tags:** #data-integration #evaluation-metrics #large-language-models #workflow-orchestration #automation #descriptive-statistics #revenue-impact #convex-optimization
**Contested on:** Not terminal — the contest differs by whether the problem is reaching the page or reading it, and the decomposition is recorded in the profile.

## The Problem
A firm sells a combined product and a customer's failures are attributed to it as a whole. When a collection underperforms, nobody can say whether requests are being blocked, pages are rendering incompletely, or the parser is reading the wrong element — because the pipeline reports one success rate at the end. Meanwhile a customer who has excellent access infrastructure of their own and needs only structuring, or who has a parser and needs only reach, is sold both. The bundling obscures the diagnosis and misprices both halves.

## Why Nobody Has Built This
Bundling raises revenue per customer and the stack genuinely is sequential, so building it as one product is natural. Access is the historical core of these businesses and extraction was added to move up the value chain, which makes separating them feel like a retreat. And the failure attribution problem is invisible to the seller, who sees a delivery rate rather than a customer's confusion.

## What to Build
Instrument the boundary and price the halves separately. Report the pipeline as distinct stages with their own success rates — request succeeded, page rendered completely, fields extracted, validation passed — since attributing a failure to a stage is the diagnostic customers most need and a single end-to-end number makes it impossible. Make each stage independently consumable, so a customer with their own access can buy structuring and one with their own parser can buy reach, which is how a substantial part of the market would prefer to buy and is not offered. Price each stage on its own cost driver — successful requests for access, pages parsed for extraction — because the current blended price hides that one half is a bandwidth business and the other a model inference business with entirely different marginal economics. Report per-target reachability separately from per-target parseability, since a hostile site and a complex site are different problems with different remedies. Make the page snapshot available with the extraction, so a customer can verify or re-parse without re-fetching, which also removes load from the target. Expose retry and cost behaviour per stage, so a customer can set their own trade-offs. And be explicit which half a given firm is actually good at, since bundling lets a weak half hide behind a strong one.

## Target Customer
Extraction engineers procuring access, data teams procuring structure, and the firms currently selling one blended product to both.

## Impact If Built
A single end-to-end success rate makes failure attribution impossible for the customer. Stage-separated reporting and pricing exposes that one half is a bandwidth business and the other a model inference business, which the blended price conceals from both sides.
