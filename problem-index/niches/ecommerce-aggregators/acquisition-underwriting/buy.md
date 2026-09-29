# Credit Underwriting and Actuarial Practice

**Niche:** [[niches/ecommerce-aggregators/acquisition-underwriting/profile|Acquisition Underwriting]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lending and insurance built the discipline of pricing an uncertain future cash flow from observable characteristics, with feedback from realised outcomes, and this sector used a multiple.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #confidence-intervals #probability-distributions #revenue-impact #hypothesis-testing #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to predict whether an acquired brand's revenue survives the change of ownership — and whoever does that takes the market, because the sector's contraction was the consequence of that prediction being made badly at scale.

## The Problem
Pricing an uncertain future cash flow from what you can observe today, learning from what actually happened, and declining business that prices below your model is what credit underwriting and actuarial practice do. They have scorecards, reject inference, portfolio monitoring, loss given default modelling and a professional discipline around model governance. Aggregator underwriting used a multiple of trailing earnings adjusted by negotiation, which is a pricing convention rather than a model.

## What Already Exists
Credit scorecard development with validated feature selection; survival modelling of default and attrition; portfolio-level loss forecasting; reject inference for learning from deals not done; model governance and back-testing requirements; and pricing for risk with explicit expected loss.

## The Customization Gap
The adaptation is to a small number of large, heterogeneous acquisitions. It requires: (1) modelling with dozens rather than millions of observations, which rules out the standard scorecard approach and argues for structured priors, hierarchical pooling across acquirers and heavy emphasis on a small number of well-chosen features — this data scarcity is the real constraint and is why the sector concluded modelling was impossible; (2) features from marketplace behaviour rather than from financial history, which is where the predictive signal is and where no diligence process looked; (3) reject inference on auctions lost, since a firm learns about its pricing from the deals it did not win and nobody tracks them; (4) outcome measurement over a long horizon with censoring, which survival methods handle and which a simple realised-return figure does not; and (5) governance that survives a competitive auction, since the pressure to override the model is at its highest exactly when the model is most valuable.

## Target Customer
Acquirers and their investment committees, the lenders financing them, and the credit risk profession whose discipline transfers with a data-scarcity adaptation.

## Impact If Solved
Pricing uncertain cash flows from observables with feedback from outcomes is a mature discipline and this sector used a convention. Data scarcity is the genuine constraint, which argues for structured priors and pooling rather than for the conclusion that modelling is impossible.
