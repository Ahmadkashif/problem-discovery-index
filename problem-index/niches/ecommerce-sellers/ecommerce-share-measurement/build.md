# Estimation Error Measured Against Contributed Truth

**Niche:** [[niches/ecommerce-sellers/ecommerce-share-measurement/profile|E-Commerce Share Measurement Providers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Some brands contribute their actual sales and the rest are estimated, which means the firm holds a standing ground truth set for its own estimation models and does not use it as one.
**Tags:** #gradient-boosting #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #feature-engineering #hypothesis-testing #time-series-forecasting #data-integration #revenue-impact

## The Problem
Category share rests on estimating sales for every product from observable signals — rank, review velocity, pricing, assortment presence — because marketplaces publish nothing. For contributing brands the firm knows the answer exactly. That contributed data is used to build models and then treated as delivered product, rather than maintained as a continuous validation set. So error is unmeasured in the places it matters most: categories with few contributors, price tiers where the observable signals behave differently, and periods of unusual promotional activity when clients most need the number. A brand comparing the firm's estimate of a competitor against its own knowledge of its own sales is performing the validation the vendor should be doing.

## Why Nobody Has Built This
Contributed data is governed by agreements written for aggregate reporting, and using it as a model evaluation set is a use nobody has explicitly mapped — so the safe default is to use it for fitting and not for standing measurement. There is also a selection problem that makes naive validation misleading: brands that contribute are systematically larger and better organized than those that do not, so measured accuracy on contributors overstates accuracy overall. Correcting for that requires modelling the contribution decision, which is real work nobody has been assigned.

## What to Build
A standing validation function on the contributed subset, with the selection bias modelled rather than ignored. Estimates are versioned and scored against contributed actuals continuously, with error decomposed by category, price tier, marketplace, seasonality, and — critically — by how much observable signal the product generates, since a low-review-velocity item is intrinsically harder. Selection is corrected by modelling contribution propensity from observable characteristics and reweighting, so reported accuracy reflects the whole population rather than the well-behaved part of it. The outputs are three: calibrated confidence published with every estimate, which is what a brand making a range decision actually needs; identification of the category and tier combinations where the model is weak, which directs both modelling effort and contributor recruitment; and a demonstrable accuracy claim, which in a market where several vendors publish similar-looking share numbers is the only durable differentiator.

## Target Customer
Chief analytics officers and heads of research at share measurement providers running 100-500 analysts, and the brand insights leaders who set assortment and pricing strategy against these estimates with no error bars.

## Impact If Built
Converts an unmeasured claim into a measured one using data already in hand, and directs contributor recruitment — the firm's main data acquisition cost — at the categories where it most improves the estimate rather than at whoever is willing.
