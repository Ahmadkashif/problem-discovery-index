# Remaining Useful Life From Observations Instead of a Table

**Niche:** [[niches/home-inspection/commercial-property-condition-assessment/profile|Commercial Property Condition Assessment Firms]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has assessed the same buildings across successive sales for twenty years and still assigns remaining life from a published expected-useful-life table.
**Tags:** #survival-analysis #gradient-boosting #ml-time-series #evaluation-metrics #tabular-ml

## The Problem
A property condition assessment produces two things a lender acts on: the immediate repairs a borrower must fund at closing, and the replacement reserve table that sets the monthly escrow for the life of the loan. Both rest on remaining useful life estimates for every major system — roof, HVAC, elevators, parking, envelope.

Those estimates come from an expected useful life table adjusted by the assessor's site observation. The table is a national average by component category, and it is largely the same table the industry has used for decades.

The firm, meanwhile, holds something far better and does not know it. A national assessment practice has walked tens of thousands of buildings, many of them more than once as properties traded, refinanced, or entered a lender's portfolio review. It has recorded a roof's condition in 2014 and again in 2021. It has scoped immediate repairs and, often, later assessed the same building after the work was done or not done. That is a longitudinal record of building components ageing under observation, with the assessor's notes attached — and every new report reaches past it for the table.

## Why Nobody Has Built This
Reports are the unit of everything: the engagement, the fee, the file, the archive. Component observations live inside report documents keyed to a project number, so there is no component table spanning projects, and without one there is nothing to fit a model to. Building that table means mining twenty years of PDFs and inconsistent report templates, which is a real project with no obvious owner.

The professional posture matters too. The assessment is signed by an engineer against an ASTM standard, and the standard's reference to published useful life tables makes using them safe. A firm-specific model is initially the harder thing to defend, even where it is the better estimate — a reflex that mistakes convention for rigour.

And nobody is graded. The reserve table projects a decade or more forward; by the time reality diverges the loan has been sold and the report is nobody's concern.

## What to Build
A component-level survival model on the firm's own longitudinal assessment record.

**Mine the archive into a component table.** Every assessment is a set of observations: component, type, installed or estimated age, observed condition, location, date. Extracting them from historical reports is unglamorous and is where the entire asset is.

**Fit time-to-replacement with proper censoring.** Most components observed have not been replaced, which is exactly what survival methods handle. The covariates the firm already records are the ones that matter: climate, building age and class, ownership type, prior deferred maintenance, and the assessor's condition rating.

**Learn what the ratings are worth.** A condition rating is an assessor's judgment, and its predictive value can be measured — does a "fair" HVAC system from this firm actually reach replacement sooner than a "good" one, and by how much? Nobody in this industry has ever answered that, and the answer is both a model input and a training tool.

**Output intervals, not points.** A reserve table built on medians understates the risk of early failure, which is the risk the lender is actually exposed to. A distribution turns the reserve table into a funding decision the lender can reason about.

## Target Customer
National practice leader or chief technical officer at a property condition assessment firm. The commercial pressure is real: this work is bid competitively on price and turnaround, margins are thin, and the only thing a national firm has that a two-person shop does not is twenty years of observations it currently does not use.

## Impact If Built
Reserve tables drive real money — escrow on billions of dollars of commercial mortgages — and they are built on national averages nobody has validated. A firm estimating from its own observed record produces numbers that are closer to right and, more importantly, can say why, which is the only defensible position in a commoditizing market.
