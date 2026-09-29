# Document Extraction Extended to the Loss Run's Meaning

**Niche:** [[niches/insurtech-platforms/commercial-submission-intake/profile|Commercial Submission Intake]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Extraction from ACORD forms and loss runs is now a competitive commodity, and every vendor extracts the numbers while the pattern in those numbers — which is what an underwriter actually reads a loss run for — is left to a person.
**Tags:** #bert #large-language-models #transformers #survival-analysis #evaluation-metrics #confidence-intervals #automation #feature-engineering
**Contested on:** Every serious competitor in submission intake is fighting to turn a broker's email attachments into a structured, triaged submission and rank it by the probability it will be quoted and bound — and whoever raises quote-to-submission ratio most takes the account.

## The Problem
A loss run lists claims: dates, descriptions, paid amounts, reserves, status. Extraction pulls them into fields. An experienced underwriter reads the same document and sees something different — whether the claims cluster in one location or one time period, whether the frequency is stable or accelerating, whether the reserves on open claims look like they will develop, whether a large loss is a one-off or the expression of a hazard that is still present, and whether the pattern is consistent with what the application says the business does. That reading is the underwriting, and the extraction stops one step before it.

## What Already Exists
Document extraction for insurance documents is a competitive category with multiple credible vendors and improving accuracy on ACORD forms, loss runs and schedules. Claims development triangles and loss development methodology are actuarial standards with published techniques. Enrichment data on properties, vehicles, businesses and hazards is purchasable. Every input is available; the synthesis is missing.

## The Customization Gap
The adaptation is to produce the underwriter's reading rather than the fields. It requires: (1) claim-level normalisation across carriers' loss run formats, which differ substantially and where the same concept is labelled differently — this is entity and schema resolution and is the unglamorous prerequisite; (2) development analysis on open claims, applying standard loss development to estimate ultimate rather than presenting incurred as though it were final, which is the most common way a naive read of a loss run misleads; (3) pattern features computed and presented — frequency trend, severity distribution, concentration by location and cause, time clustering — as the summary an underwriter would have written; (4) consistency checking between the loss run, the application and enrichment data, since the contradictions are where the underwriting risk usually is and a human finds them by noticing; and (5) confidence and provenance on every derived statement, because an underwriter will use a summary they can trace and will ignore one they cannot.

## Target Customer
Carriers, MGAs and wholesale brokers processing commercial submissions, and the extraction vendors who currently compete on field accuracy.

## Impact If Solved
Moving from fields to a reading is what converts extraction from a transcription saving into underwriting leverage, and it is the difference between the current product category and the one it is trying to become. Loss development on open claims is the single highest-value element and is a standard actuarial technique applied to a document that is currently read as if incurred were final.
