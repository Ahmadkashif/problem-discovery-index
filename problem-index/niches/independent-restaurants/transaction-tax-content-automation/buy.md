# Monitoring Thirteen Thousand Jurisdictions That Announce Nothing

**Niche:** [[niches/independent-restaurants/transaction-tax-content-automation/profile|Transaction Tax Content & Determination]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A district changes its rate by council resolution posted as a PDF, and the effective date is in six weeks.
**Tags:** #ocr #anomaly-detection #named-entity-recognition #data-integration #automation

## The Problem
The corpus covers state, county, city, and special district taxes — transit districts, stadium districts, tourism improvement districts — well past thirteen thousand jurisdictions, plus the boundaries that determine which ones apply to an address. Rates change constantly, and the local layer changes most.

There is no feed. A special district is created by a ballot measure. A city adjusts its rate by ordinance posted in council minutes. A state changes the taxability of a food category in a budget bill and clarifies it later in a department bulletin. Boundaries change by annexation, recorded in a county GIS file updated on nobody's schedule.

Research staff monitor what they can and rely on state notification lists, subscriptions, and customer reports for the rest. A missed change means wrong tax on every affected transaction from the effective date until someone catches it.

## What Already Exists
Web change monitoring, document extraction, and legislative tracking are all mature commodity categories, and the state-level layer is well served by existing regulatory tracking services.

## The Customization Gap
Everything hard here is below the state line.

**Jurisdictions with no publication convention.** Thousands of local bodies, each posting to its own site in its own format, most with no notification mechanism at all. Acquisition is per-source and the sources change without warning — closer to the court-record problem than to regulatory tracking.

**Effective dates are the payload.** A rate change is only useful with its precise effective date, and rate changes are almost always announced ahead of the date they apply. The system exists to have the right number loaded before the first transaction, which means extraction has to get the date as reliably as the rate.

**Boundaries are geospatial and drift.** Which jurisdictions apply to an address is a spatial question over district boundaries that change by annexation and by new district formation. Monitoring boundary files is a different discipline from monitoring text, and both feed the same determination.

**Taxability changes hide in prose.** A rate change is a number. A change to whether prepared food sold with utensils is taxable arrives in a budget bill or a department bulletin as sentences, and it matters more. Detecting a substantive taxability change requires reading, not diffing.

**Coverage must be provable.** The product's claim is completeness across every US jurisdiction, so the system must report which jurisdictions are genuinely monitored, when each was last verified, and where a source has gone quiet. An unmonitored jurisdiction currently looks exactly like a quiet one.

## Target Customer
VP of Tax Research or Head of Content Operations, where a fixed research team covers a jurisdiction count that only grows and a customer base that assumes total coverage.

## Impact If Solved
Every missed change is wrong tax on real transactions with a liability that accrues silently. Systematic local-layer monitoring converts the company's central claim from a staffing effort into an auditable process, and frees researchers from watching sources to analysing the changes that matter.
