# A Catalogue That Checks Itself

**Niche:** [[niches/lending-marketplaces/product-and-rate-catalogue/profile|Product & Rate Catalogue]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of products with their own rules are kept current by people reading emails, and nothing checks whether any of it is true.
**Tags:** #large-language-models #change-point-detection #data-integration #evaluation-metrics #automation #compliance #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to keep hundreds of lender products, eligibility rules, rate structures and state restrictions accurate without maintaining them by hand — and whoever does it stops showing borrowers offers that do not exist.

## The Problem
A lender changes its minimum credit score, withdraws from a state, adjusts a rate tier, or discontinues a product. The notification arrives as an email to a partner manager, or it does not arrive at all. Someone updates a row when they get to it. In the meantime the marketplace advertises terms that no longer exist, routes borrowers to a lender that left their state, and filters out borrowers who would now qualify. Nobody knows the error rate, because nothing has ever measured it.

## Why Nobody Has Built This
The catalogue began as a small table maintained by one person, and it scaled by adding people rather than by being rebuilt — a manual process that works at fifty products is simply strained at five hundred, not obviously broken. Lender information arrives unstructured and inconsistently. Errors are discovered through complaints rather than through checks. And no one owns catalogue accuracy as a metric.

## What to Build
Extract, validate and watch for drift. Extract product terms automatically from lender rate sheets, partner emails and public pages, which is the core and turns a typing job into a review job. Validate every entry against observed behaviour, since applications, declines and funded loans reveal the real rules and a published minimum score contradicted by outcomes is a detectable error. Detect change rather than waiting for notification, because the lender's own public materials usually move before the email arrives. Flag entries by staleness, as an unverified rate from four months ago should not be presented identically to one confirmed yesterday. Let lenders confirm their own entries through a self-service view, which is the cheapest accuracy mechanism available and nobody offers it. Diff a proposed change against the current entry so review is focused on what moved. Measure catalogue error rate by sampling, since an unmeasured process cannot be improved and this one has never been measured at all. Version the catalogue so a borrower's displayed offer can be reconstructed later, which matters for both disputes and compliance. Prioritise accuracy by traffic volume, because errors on high-volume products cost far more. And alert on a state restriction change immediately, as that is the error with regulatory consequences.

## Target Customer
Partner operations leadership, compliance functions responsible for advertised terms, lenders receiving misrouted applicants, and product information vendors with no lending presence.

## Impact If Built
The catalogue scaled by adding people rather than by being rebuilt, so a process that worked at fifty products is merely strained at five hundred. Extraction plus validation against observed outcomes makes accuracy measurable for the first time.
