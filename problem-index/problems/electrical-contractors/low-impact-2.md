# Labor Hour Estimation from Project Scope

**Industry:** [[electrical-contractors|Electrical Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic estimating tools handle material takeoffs but not the labor productivity rates that are specific to installation type, building construction type, access difficulty, and local crew experience — the variables an experienced electrical estimator encodes from years of project data.
**Tags:** #gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #revenue-impact

## The Problem
Electrical labor estimating requires knowing how long it takes to install a circuit breaker in an accessible panel vs. a panel in a finished basement with limited access; to pull wire through an open wood-frame wall vs. an existing finished wall vs. a conduit system in a concrete commercial building; to install a light fixture on a flat ceiling vs. a vaulted ceiling at 20 feet. These productivity rates — measured in units of work per labor hour — are what separate accurate electrical estimating from guesswork. Experienced electricians have internalized these rates from years of field work and project tracking. When they write a bid, they know that roughing-in a circuit in new wood-frame residential takes 1.2 hours per circuit under normal conditions, and they adjust for the specific job's access conditions. Junior estimators, tasked with pricing a bid without that internalized rate knowledge, use generic NECA labor unit tables that often don't account for the specific job conditions accurately.

## What Already Exists
NECA (National Electrical Contractors Association) publishes labor unit manuals that provide industry-average labor hours per unit of work. ConEst and Accubid are commercial estimating software tools used by larger electrical contractors for commercial project estimating. These tools use NECA tables as their productivity base. What they don't account for is the job-specific adjustment factors that experienced estimators apply — building type, access difficulty, crew experience level, material pre-fabrication vs. field assembly — which can move the final labor estimate by 20-40% from the NECA base.

## The Customisation Gap
A labor estimating model calibrated to the specific contractor's crew and project types is the customization. A contractor doing primarily retrofit residential work has different productivity profiles than one doing primarily new commercial work — the NECA tables apply industry averages, not firm-specific actuals. A model trained on the firm's own job cost data (estimated vs. actual labor hours per work type) produces estimates calibrated to actual crew performance. The customization is also local: labor productivity is affected by local weather, local material availability, and whether the crew is union vs. non-union (different work rules affect productivity). No generic tool captures this.

## Impact If Solved
Reduces estimating errors that cause the contractor to either under-bid (losing money) or over-bid (losing the job). For a firm doing $5M in annual revenue with a 5% typical estimating error rate, improving to 2% represents $150K in prevented margin loss annually.
