# Sampling Frames That Know What They Cannot See

**Niche:** [[niches/coffee-shops-independent/coffee-sustainability-verification/profile|Coffee Origin Verification & Traceability Services]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The whole product is a statistical claim about an origin, and the sampling frame it rests on is built from incomplete farm registries — so the population being generalized to is itself an estimate nobody characterizes.
**Tags:** #bayesian-inference #probability-distributions #confidence-intervals #hypothesis-testing #monte-carlo-methods #evaluation-metrics #feature-engineering #causal-inference #data-integration #compliance

## The Problem
Verification sells a claim of the form: across this origin, this share of production meets this condition, with this confidence. The claim's validity depends entirely on the sampling frame — the enumeration of farms from which the sample was drawn. Those frames are assembled from cooperative membership lists, government registries, exporter records, and previous survey rounds, all of which are incomplete in ways that are not random. Smallholders outside cooperatives, informal producers, and farms in insecure or remote areas are systematically under-represented, and those are frequently the farms where the practices in question differ most. Frame coverage is managed operationally — get the best list available — rather than characterized statistically, so the confidence intervals published alongside the estimates account for sampling error and not for frame error, which is likely the larger of the two.

## Why Nobody Has Built This
Quantifying frame coverage requires knowing about farms that are, by definition, absent from the frame. The tractable approach is triangulation — comparing independent partial frames, using capture-recapture logic across survey rounds, and calibrating against satellite-derived production area — and each of those is real methodological work with no obvious owner in an organization structured around field operations. There is also a commercial reluctance that mirrors what this sweep has found everywhere: a verification service that publishes its own coverage uncertainty is arming a buyer to question the estimate, and no competitor is doing it, so nobody has had to.

## What to Build
Frame coverage as a modelled, published quantity. Independent partial enumerations are reconciled against each other to estimate the size and character of the uncovered population, using overlap between sources the way capture-recapture estimation does; satellite-derived production area provides an external check on total production the frame should account for; and previous rounds' newly discovered farms indicate the rate at which the frame is incomplete. The output is an explicit statement of what fraction of origin production the frame covers, how the uncovered portion likely differs, and how much that widens the interval on every published estimate. That in turn drives sampling design — effort allocated toward under-covered strata rather than toward where fieldwork is easiest, which is the current implicit optimization. And it makes the estimate defensible in exactly the setting that is about to matter most: a regulator or a buyer's auditor asking, under deforestation compliance rules, what the verification actually covers.

## Target Customer
Chief research officers and heads of methodology at verification services, and the sustainability and compliance leaders at roasters who must defend sourcing claims under regulatory scrutiny and currently receive an estimate with an interval that understates its uncertainty.

## Impact If Built
Makes the central claim honest, which in a compliance-driven market is a commercial advantage rather than a concession — a roaster facing regulatory audit needs a verification it can defend, not one that sounds confident. It also redirects fieldwork, the organization's largest cost, toward the strata that most improve the estimate rather than toward the farms that are easiest to reach.
