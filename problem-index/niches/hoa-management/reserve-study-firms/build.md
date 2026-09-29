# Component Life Estimated From Tables Instead of From Thirty Years of Observations

**Niche:** [[niches/hoa-management/reserve-study-firms/profile|Reserve Study Firms]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has watched thousands of roofs actually fail and still estimates roof life from a published table.
**Tags:** #survival-analysis #gradient-boosting #ml-time-series #evaluation-metrics #revenue-impact

## The Problem
A reserve study is a life prediction repeated a hundred times. For each component the analyst assigns a remaining useful life and a replacement cost, and those two numbers, compounded across a thirty-year horizon, determine what every homeowner in the community pays every month.

The remaining life comes from a published table adjusted by the analyst's site observation. Asphalt shingle: 20-25 years. Elevator modernization: 25-30. Pool plaster: 10-15. The table is a national average of a component category, and it is the same table the firm used in 1998.

Meanwhile the firm has inspected thousands of communities, many of them repeatedly across decades. It has recorded the condition of a roof, then come back in five years, then in ten, and often recorded the year it was actually replaced and what it actually cost. That is a survival dataset on real building components with real covariates — climate, exposure, original installation quality, maintenance history — and it is used for nothing. Each new study reaches for the table.

## Why Nobody Has Built This
The output is a report, and reports were stored as reports. Component inventories live inside individual study documents, in the firm's report software, keyed to the study rather than to the component. There is no component table across studies, so there is no dataset to fit anything to, and building one means restructuring how the firm has stored its work since it started.

There is also a professional-standards reflex. Reserve study standards reference expected useful life tables, and using them is defensible in a way that a firm-specific model initially is not. That reflex is misread: the standards do not forbid better estimation, and a model fitted on observed replacements in comparable climates is more defensible than a national average, not less — provided it can be explained.

The last reason is that nobody is scored. A study projects thirty years forward, and by the time reality diverges the report is long past anyone's attention.

## What to Build
A component survival model on the firm's own inspection and replacement history.

**Restructure the archive around components.** Every study is a set of component observations with a date, a condition, and a location. Extracting them from historical reports is the unglamorous foundation and it is where the asset actually is.

**Fit time-to-replacement as survival, with censoring handled properly.** Most observed components have not been replaced yet, which is exactly what survival analysis is for. Covariates that matter: climate zone, exposure, building age, original construction era, observed condition at each inspection, and the association's maintenance posture — all of which the firm records already.

**Produce a distribution, not a point.** A roof with a 21-year median life and a wide interval demands a different funding strategy from one with a tight interval, and current practice collapses both to a single number. The funding plan is where that uncertainty belongs, and it is thrown away before it gets there.

**Recalibrate cost the same way.** Replacement cost estimates come from cost manuals; the firm has seen actual invoices for the same work in the same markets. Regional cost multipliers fitted to observed replacements beat a national manual with a location factor.

## Target Customer
Principal or president of a reserve study firm, particularly one operating across several states with a long archive. The competitive context makes this urgent: statutory mandates in Florida and elsewhere have pulled new entrants into the market who compete on price, and an established firm's only durable advantage is that it has been watching these buildings for thirty years.

## Impact If Built
Community associations are chronically underfunded, and the reason is compounding estimation error, not board negligence — a component that fails five years before the plan assumed produces the special assessment that appears in every account of why associations end up in crisis. A firm estimating from observations rather than a national average produces a funding plan that is closer to right, and can say why.

It also converts a report business into something that compounds. The archive is the asset; today it is a shelf of PDFs.
