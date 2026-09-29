# The Best Record of What Households Actually Install, Used to Report Against a Target

**Niche:** [[niches/energy-auditors/utility-program-implementers/profile|Utility Efficiency Programme Implementers]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The implementer sees which measures are recommended, which are actually installed, by whom, at what incentive, across many utilities and years — and uses it to forecast a savings number for a regulator.
**Tags:** #gradient-boosting #causal-inference #survival-analysis #evaluation-metrics #time-series-forecasting

## The Problem
A utility is obliged by its regulator to deliver a quantity of energy savings. It contracts an implementer to make that happen: recruit and manage the contractor network, market the programme, process rebates, verify installations, and report the savings claimed.

The implementer therefore sits at the exact point where an efficiency recommendation either becomes a retrofit or does not. Across many utility contracts and many years, that produces the most complete record in existence of what measures households and businesses actually adopt — recommended, offered, incentivised, installed or abandoned, by property type, income segment, contractor and incentive level.

What that record is used for is a participation forecast and a savings claim. The forecast answers whether the utility will hit its target; the claim is computed by applying deemed savings values to counted installations.

Two much larger questions go unasked.

The first is what actually drives adoption. Incentive levels are set by convention and negotiation, not by estimated elasticity, though the record contains years of variation in incentive level, marketing approach and contractor mix against observed uptake. Nobody can say what an extra hundred dollars on a heat pump rebate buys in participation, in which segment, which is the single most consequential question in programme design.

The second is realisation. Claimed savings use deemed values; independent evaluation contractors later estimate what was actually realised, sometimes years afterwards, and those findings adjust future deemed values. The implementer holds the installation detail that would predict realisation — measure, home characteristics, contractor, installation quality — and treats evaluation as something that happens to it rather than as an outcome to model.

## Why Nobody Has Built This
The contract defines the deliverable as savings against a target, so analysis outside that is unfunded.

There is also an uncomfortable incentive. An implementer that could predict realisation accurately would be predicting the gap between what it claims and what it delivers — and it is paid against the claim.

And programme design authority sits with the utility and the regulator, not the implementer. Elasticity findings would inform decisions the implementer does not make, which is why nobody has been motivated to produce them.

## What to Build
Adoption and realisation as modelled quantities.

**Estimate incentive elasticity by measure and segment.** Incentive levels change across programmes, utilities and years, which is quasi-experimental variation the implementer can exploit directly. This is the highest-value analysis available and it needs no new data.

**Model the recommendation-to-installation funnel.** Audit recommendation, offer, quote, installation. Where the funnel leaks, by measure and segment, is where programme money is wasted.

**Predict realisation before evaluation does.** Fit against historical evaluation findings using the installation-level detail only the implementer holds. An implementer that can forecast its own realisation rate is in a materially stronger position with both the utility and the regulator.

**Model contractor effect.** Contractors vary enormously in conversion and in installation quality, and the implementer manages the network. Which contractors produce durable savings is measurable and is currently managed by relationship.

**Forecast participation with uncertainty.** Targets are met or missed on a schedule, and a forecast with an honest interval is worth more to a utility than a point estimate delivered confidently and revised quarterly.

## Target Customer
VP of Analytics or Chief Programme Officer at an efficiency programme implementer. The commercial argument is that these contracts are competitively rebid on cost per unit of savings, and an implementer that can demonstrate why its designs convert has an argument no competitor can price against.

## Impact If Built
Billions of dollars of ratepayer money flow through efficiency programmes annually, with incentive levels set by convention and savings claimed against deemed values. The party holding the adoption record is contracted to hit a number, and could instead say what actually moves households to install.
