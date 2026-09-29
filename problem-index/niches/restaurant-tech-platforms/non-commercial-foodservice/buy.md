# Demand Forecasting Applied to Participation and Plate Waste

**Niche:** [[niches/restaurant-tech-platforms/non-commercial-foodservice/profile|Non-Commercial Foodservice]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Institutional foodservice knows exactly how many meals it served yesterday and produces tomorrow's quantities from a historical average, while forecasting methods that would fit this problem almost perfectly are commodity.
**Tags:** #time-series-forecasting #gradient-boosting #exponential-smoothing #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in institutional foodservice software is fighting to produce a cycle menu that satisfies the nutrition regulation, the allergen safety requirement and the per-meal budget simultaneously — and whoever generates a compliant menu people will actually eat takes the account.

## The Problem
A school kitchen produces 400 servings of the entrée because it produced 400 last time this item was on the cycle. 310 are taken. The rest is discarded, which is both a budget loss against a reimbursement rate with no slack and a violation of the programme's own purpose. Participation varies predictably with the item, the day of week, the weather, whether a competing item is offered, testing schedules, and the season, and every one of those is known in advance. The forecast is a historical average because nobody has applied anything else.

## What Already Exists
Demand forecasting methods and tooling are entirely commodity, and this problem is friendlier than most commercial forecasting: the population is known and bounded, attendance is recorded, the menu is planned weeks ahead, and the calendar is published. Point of sale systems in K-12 record every meal served by student and by item. Plate waste studies are an established methodology in the nutrition literature. Weather and calendar data are free. Nothing here requires invention.

## The Customization Gap
The adaptation is to the institutional structure, which differs from restaurant demand in useful ways. It requires: (1) forecasting participation as a rate against known attendance rather than as an absolute count, since attendance is separately known and modelling it into the same number wastes information; (2) item-level take rates conditioned on what else was offered that day, because the competing choice is the dominant driver and a per-item average ignores it; (3) grade band and site heterogeneity, since the same item performs very differently in an elementary and a high school and districts currently plan as if it did not; (4) integrating plate waste as a second signal — served is not eaten, and the programme's purpose is the second one — which requires a sampling protocol the district can sustain rather than a research-grade study; and (5) translating the forecast into production quantities per site with the shortfall risk stated, since running out is a worse failure than over-producing in a setting where a child does not get a meal.

## Target Customer
School district foodservice operations, hospital and senior living nutrition services, and the K-12 and healthcare nutrition vendors whose point of sale data already contains everything needed.

## Impact If Solved
Production forecasting against participation rather than history cuts waste directly against a budget with no slack in it, and the item-level take rate data is what makes the menu optimisation in the build note possible. The adaptation is small; the reason it has not happened is that nobody in this segment has treated participation as a forecastable quantity.
