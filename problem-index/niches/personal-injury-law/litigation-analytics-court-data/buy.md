# Three Thousand Counties That Never Agreed on What a Case Is Called

**Niche:** [[niches/personal-injury-law/litigation-analytics-court-data/profile|Court Data & Litigation Analytics Platforms]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The same law firm appears as forty different entities, the same case type has two hundred local names, and the fix is a team of people maintaining rules by hand.
**Tags:** #transformers #word-embeddings #graph-neural-networks #transfer-learning #data-integration

## The Problem
Federal courts publish through one system. State trial courts — where nearly all personal injury litigation lives — publish through thousands of separate county systems that share no schema, no vocabulary and no identifier space. One county calls it "Motor Vehicle Tort", the next "Personal Injury — Auto", the next files it under a generic civil code with the nature of the claim visible only in the complaint text. Some publish structured data; some publish images of paper; some publish nothing without a physical visit.

Every analytic the platform sells depends on reconciling this. A judge's motion grant rate requires knowing that fourteen name variants are one judge. A counsel history requires knowing that a firm's forty spellings, offices, and post-merger names are one firm. A case-type benchmark requires mapping two hundred local labels onto one taxonomy — including the ones that are genuinely ambiguous.

This is done by rules and by people. Normalisation teams write and maintain matching logic county by county, and the rules break whenever a court changes its case management system, which happens constantly. The cost scales with coverage, which is why coverage stalls.

## What Already Exists
Entity resolution and record linkage are mature fields with strong open tooling, and modern text embedding models handle name and string variation far better than the edit-distance and rule-based approaches most of these platforms were built on. Commercial master data management suites solve the same abstract problem for customer records.

None of it is built for this. Generic entity resolution assumes a reasonably consistent record structure and a fixed set of fields. Court records offer neither: the informative content is often free text in a docket entry written by a clerk, the available fields vary by county, and the ground truth for whether two judges are one person is not in the data at all.

## The Customization Gap
**Court structure is the disambiguating signal.** Two identically named attorneys are distinguished by which courts they appear in, alongside whom, in what case types. That is a graph — parties, counsel, judges, courts, cases — and resolution on it is far stronger than resolution on strings. Generic tools do not model the graph because their domains do not have one.

**The taxonomy is the product and it must be stable.** Customers benchmark year over year, so a reclassification is a visible product regression. Mapping local labels onto the taxonomy therefore needs confidence scoring, an explicit unmapped bucket, and versioning — not a classifier that quietly changes its mind. Generic classification tooling offers none of this.

**Docket text is a genre, not prose.** Clerk-written entries are terse, abbreviated, inconsistently capitalised, and locally idiomatic. A model has to be adapted to the genre, and the platform has hundreds of millions of entries to adapt it on.

**Some of the corpus is images.** Scanned filings and paper-only counties need extraction before any of this applies, and the layouts are county-specific and old.

**Court transitions are the failure mode to design for.** A county migrating case management systems silently changes formats, and a rule-based pipeline fails without complaint. Drift detection on ingestion — this county's records no longer look like they did last week — is the operational requirement, and it is what a generic MDM deployment will never give.

## Target Customer
VP of Data or Head of Data Operations at a litigation analytics platform, running a normalisation team whose size scales linearly with the coverage the product is trying to grow.

## Impact If Solved
Normalisation cost is the constraint on court coverage, and coverage is the moat. Breaking the linear relationship between counties covered and headcount required is what lets the platform expand into the state and county courts where the litigation the customers actually care about is filed.
