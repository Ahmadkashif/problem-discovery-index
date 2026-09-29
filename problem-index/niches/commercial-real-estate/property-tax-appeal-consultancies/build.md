# Appeal Outcome History as a Jurisdiction-Level Argument Model

**Niche:** [[niches/commercial-real-estate/property-tax-appeal-consultancies/profile|Property Tax Appeal Consultancies]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has argued thousands of appeals in front of the same assessors and boards and knows what works with each of them only through the individual consultants who have stood there.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #cross-validation #causal-inference #survival-analysis #tacit-knowledge-ml #data-integration #revenue-impact

## The Problem
Every appeal is a choice of argument: challenge the income approach assumptions, attack the comparable sales, argue functional obsolescence, dispute the equalization ratio. Which argument works depends heavily on the jurisdiction, the individual assessor, the board's composition, and the property type — and the firm has run that experiment thousands of times. The results live in case files and in the heads of the consultants who handled them. A consultant assigned to an unfamiliar county has no way to learn from the two hundred appeals the firm has already filed there. Portfolio-level decisions are equally blind: which parcels to appeal at all, how hard to push, when to settle, and what a realistic reduction looks like are all judgment calls made without reference to the firm's own record.

## Why Nobody Has Built This
Appeals are managed as individual matters in case management systems where the outcome is a settlement figure and a closure date, not a structured record of what was argued and how the other side responded. Jurisdictions number in the thousands with wildly different procedures, so normalizing outcomes into a comparable structure is real work. And the firm's economics are contingent — paid on savings achieved — which focuses everything on closing the current year's cases and leaves no natural owner for building the institutional record.

## What to Build
An outcome model over structured appeal history. Each appeal records the property characteristics, the assessment challenged, the arguments advanced and the evidence supporting each, the procedural path, and the outcome at every stage — informal, board, litigation — normalized across jurisdictions. That supports three things the firm cannot do today. Argument selection: which lines of attack succeed with this assessor on this property type, with the effect sizes attached. Portfolio triage: which parcels are worth appealing given expected reduction, probability of success, and cost to prosecute, which is currently decided on assessment-to-value ratios and instinct. And settlement guidance: what a case like this has historically settled for, so a consultant deciding whether to accept an offer is comparing it to the firm's actual distribution rather than to their own recollection. Jurisdiction-level profiles emerge as a by-product and are the most transferable asset — a new consultant inherits two hundred appeals' worth of knowledge about a county on their first day.

## Target Customer
National directors of property tax and practice leaders at firms running 100-1,000 consultants, and the regional managers who currently allocate appeal effort across portfolios by rule of thumb.

## Impact If Built
Raises the yield on a contingent-fee business directly — better argument selection and better triage both convert straight into recovered dollars. It also breaks the dependence on individual consultants' jurisdictional relationships, which is the practice's biggest continuity risk and the main constraint on entering new markets.
