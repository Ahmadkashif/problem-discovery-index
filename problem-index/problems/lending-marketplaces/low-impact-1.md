# Lender Integration and Rate Table Freshness

**Industry:** [[lending-marketplaces|Lending Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hundreds of lender products with their own eligibility rules, rate structures and state restrictions are maintained by hand, and a stale entry is a borrower shown an offer that does not exist.
**Tags:** #bert #large-language-models #k-nearest-neighbors #change-point-detection #evaluation-metrics #data-integration #workflow-orchestration #compliance

## The Problem
A marketplace carries hundreds of products across dozens of lenders. Each has eligibility criteria — minimum score, income, employment type, debt-to-income, state licensing, loan purpose restrictions, amount and term bands — and a rate structure that may be a single APR range, a grid by score band and term, or a genuine risk-based price only revealed at application.

These change constantly. Lenders adjust pricing weekly, tighten criteria without notice, pause originations in states, run promotions, and withdraw products. Communication about it ranges from an API to an email to a discovery made when borrowers start getting declined.

Maintaining the catalogue is manual. Someone reads the lender's update, works out which fields it touches, and edits the entries. Mistakes are found by borrowers.

State-level variation multiplies everything. A product available in forty-three states with different maximum rates and licensing constraints is effectively forty-three products, and the compliance consequence of showing an unavailable offer is not merely a bad experience.

Advertised rates compound it further. The headline "rates from" figure is achieved by a small minority of borrowers, and the distance between advertised and received is the number borrowers actually care about and nobody publishes.

## What Already Exists
The larger partnerships run pre-qualification APIs returning real indicative offers. Rate table management systems exist internally. Some lenders publish rate sheets in structured form. Compliance review covers advertised rate disclosures. Content teams maintain product pages.

## The Customisation Gap
Nothing extracts criteria from the lender's own published material. Product pages, rate sheets and terms documents state eligibility and pricing in prose and tables, and turning those into structured catalogue entries is a well-shaped extraction task on documents that are already public.

Nothing detects staleness. A product whose approval rate for a given profile suddenly collapses has almost certainly changed its criteria, and that is visible in the marketplace's own outcome data days before the lender's email arrives. Silent criteria changes are detectable as distribution shifts.

Advertised-versus-received is unmeasured. The marketplace sees what it displayed and, where decisions return, what was actually offered. That distribution is the most useful thing it could publish about a lender and it is neither published nor used in ranking.

And state eligibility is maintained as a matrix nobody validates against licensing registries, which are public and machine-readable.

## Impact If Solved
Catalogue accuracy determines whether the core product tells borrowers the truth, and it is maintained by hand against lenders who change things without notice. Extracting criteria from published material, detecting silent changes from outcome shifts and measuring the advertised-to-received gap turns a maintenance burden into a data asset and removes the most common way the marketplace misleads someone unintentionally.
