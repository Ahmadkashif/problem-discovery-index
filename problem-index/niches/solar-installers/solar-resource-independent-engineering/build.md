# P90 Is a Promise About Frequency and Nobody Counts

**Niche:** [[niches/solar-installers/solar-resource-independent-engineering/profile|Solar Resource Assessment & Independent Engineering]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every financed solar project is sized on an exceedance probability that says how often production should fall short, and the firms issuing those numbers have never counted how often it did.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #time-series-forecasting #causal-inference

## The Problem
An energy yield assessment does not just say how much a plant will produce. It says it with a distribution: P50 is the central estimate, P90 is the level exceeded in nine years out of ten. Lenders size debt to the P90 because they need a production level that is very likely to be met. Equity is priced off the P50. The gap between them is set by an uncertainty analysis combining resource variability, model error, equipment tolerance and degradation.

Those are falsifiable claims about frequency. A plant assessed at a given P90 should fall below it about one year in ten. Plants have been operating for a decade and more; production is metered continuously and reported to owners, lenders and registries monthly.

The comparison is not made. There is scattered published work suggesting the industry's estimates have been systematically optimistic, and there is no standing, firm-level record of how issued assessments performed. The uncertainty components are assigned from convention and expert judgment — a percentage for interannual variability, a percentage for model uncertainty, a percentage for equipment — combined in a way that assumes independence they do not have, and never checked against realised spread.

The firms are the natural place to fix this. They issued the assessments, they often remain engaged as independent engineer through operations, and the operating data flows past them.

## Why Nobody Has Built This
The incentive is negative and obvious. A firm that published its own historical bias would hand every counterparty a negotiating tool, and in a market where the independent engineer is chosen by the developer but relied on by the lender, being known as the optimistic one and being known as the pessimistic one are both commercially bad.

Attribution is also genuinely hard. A plant that underperformed may have had a bad resource year, a curtailment event, an availability problem, soiling, or a design flaw. Separating resource error from operational loss requires work nobody is paid for.

And the data is fragmented by ownership. Production belongs to the asset owner, assessments belong to whoever commissioned them, and the two rarely sit in the same system even inside the same firm.

## What to Build
A standing validation record, treated as a scientific asset.

**Archive every assessment as structured data.** The full distribution, the loss assumptions, the uncertainty components, the resource dataset version, and the design as assessed. Retrospective reconstruction from PDFs is possible but painful; the value starts when this is a database.

**Score the distribution, not the point.** Compute where each operating year fell in the predicted distribution. Across many plant-years, those quantiles should be uniform if the uncertainty was right. That single test — the standard way to grade a probabilistic forecast — has apparently never been run at firm scale in this industry.

**Decompose the miss.** Separate resource deviation, availability, curtailment, soiling and degradation, using satellite irradiance for the actual year against the long-term expectation. Only the resource and model components belong to the assessment; the rest belong to operations, and conflating them is why nobody has drawn conclusions.

**Estimate uncertainty components empirically.** Interannual variability is measurable from the reprocessed satellite record. Model uncertainty is measurable from validation against operating plants. Both are currently conventions.

**Recalibrate degradation.** Assessments assume a degradation rate that runs for twenty-five years of financial modelling and is taken from literature. Fleets now have a decade of measured degradation by technology and climate, and it is knowable.

**Use it internally first, then commercially.** An independent engineer with a demonstrated calibration record is worth more to a lender than one without, and the first firm to have one changes what lenders ask for.

## Target Customer
Chief Scientist or Head of Technical Advisory at a solar resource data provider or an independent engineering practice. The strongest version of this sits with a firm that both supplies the resource dataset and stays on as operating-phase engineer, because it holds both halves.

## Impact If Built
Tens of billions of dollars of solar project debt and equity are sized annually against exceedance probabilities that have never been validated. Getting the distribution right — and being able to prove it — improves capital allocation across the entire asset class, and it is buildable from data that already exists in these firms and the fleets they monitor.
