# Practice Myopia Outcomes Registry

**Niche:** [[niches/optometry-practices/pediatric-myopia-management/profile|Pediatric Myopia Management Programmes]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A registry that tracks every enrolled child's axial growth against the forecast for their treatment, and shows the practice and families how well the programme works.
**Tags:** #gaussian-processes #bayesian-inference #time-series-forecasting #causal-inference #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to slow eye growth in children enrolled in myopia control, and whoever shows the lowest measured axial elongation per child per year across a practice's programme takes the account.

## The Problem
A practice may have a hundred children in myopia control across three products. It cannot say which treatment is working best for its own patients, or which children are growing faster than expected.

## Why Nobody Has Built This
Each manufacturer tracks its own product. Biometer software plots single children. Few practices measured axial length until recently, and the products have arrived only in the last few years.

## What to Build
Pull biometer and refraction data into one registry. Forecast each child's growth with a hierarchical Bayesian model using treatment as a covariate. Flag children above their expected curve. Report programme outcomes by product, age and adherence, and give families a plain-language growth chart.

## Target Customer
Practices with established myopia clinics, groups standardising a paediatric service line, and franchisors such as Treehouse Eyes.

## Impact If Built
If the registry flags ~10% of ~100 enrolled children a year for an earlier change of treatment, each gaining ~0.1 mm less growth (estimate), the practice shows measurably better outcomes and keeps more families enrolled.
