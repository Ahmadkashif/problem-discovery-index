# Ratings on Thousands of Issuers From Documents Read One at a Time

**Niche:** [[niches/municipal-services/municipal-credit-rating-analysis/profile|Municipal Credit Rating & Public Finance Analysis]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The agency holds decades of financial statements for every municipality in America and assigns each rating by having an analyst read one issuer's documents.
**Tags:** #gradient-boosting #tabular-ml #survival-analysis #evaluation-metrics #anomaly-detection

## The Problem
Municipal credit is a portfolio problem treated as a series of individual cases. An analyst covers a set of issuers, reads each one's audited statements and budget, applies the published criteria, and arrives at a rating. Surveillance repeats it annually.

That process produces ratings on tens of thousands of credits, and the agency holds the entire corpus behind them: financial statements, budgets, demographic and economic data, and — uniquely — a multi-decade record of which municipal credits actually deteriorated, defaulted, or recovered. Municipal defaults are rare, which is exactly the regime where only systematic analysis over a large population can find signal that individual experience cannot.

What the corpus is not used for is prediction. Rating changes are driven by analyst review on a surveillance calendar, so an issuer whose fundamentals have been deteriorating for three years is downgraded when their analyst next looks or when something visible happens. Nobody has built a model that says which currently-stable credits look like the ones that got into trouble.

## Why Nobody Has Built This
Ratings are opinions arrived at under published criteria, and post-crisis regulation pushed hard on methodology transparency and analyst judgment — the rating must be explicable as the application of criteria by a person. A statistical model that ranks credits sits awkwardly with that framing, and the compliance instinct is to keep it well away from the rating itself.

That instinct is over-applied. Nothing in the regime prevents using a model to prioritize surveillance — deciding which of an analyst's fifty credits to examine first is an internal resource allocation, not a rating action, and it is where the model would do most good.

The other reason is that the data was never assembled. Financials live in the documents they arrived in, extracted per engagement into rating files rather than into a comparable time series across issuers.

## What to Build
A surveillance prioritization layer over the corpus.

**Assemble the panel.** Multi-year normalized financials, demographics, and rating history for every rated issuer. This is the foundational work and it is the asset.

**Model deterioration, not rating.** Predict which currently-stable credits are heading toward a downgrade or distress event over one to three years. The outcomes are in the agency's own history and the features are in the statements. Framed as surveillance triage rather than as a rating, the compliance question dissolves.

**Detect anomalies against peers.** An issuer whose reserves, pension funding, or fixed-cost ratio moves sharply relative to comparable jurisdictions is worth an analyst's attention now rather than at the next scheduled review.

**Measure the criteria.** Which factors in the published methodology actually predict deterioration, and at what weights? Criteria are calibrated by committee and expert judgment, and nobody has checked them against outcomes.

**Report analyst-level consistency.** Comparable credits rated differently by different analysts is a real phenomenon in a business built on individual judgment, and it is measurable in the agency's own data.

## Target Customer
Chief Analytics Officer or head of public finance criteria at a rating agency. The regulatory pressure runs toward defensible, evidenced methodology, and an agency that can demonstrate its criteria predict is in a better position than one that can only describe them.

## Impact If Built
Municipal credit ratings set the borrowing cost of every city, school district, and water utility in the country — the difference between a water main replaced and deferred. Catching deterioration earlier protects investors and, more usefully, gives a municipality warning while remediation is still cheap. The data has been accumulating for a century.
