# The Only Long-Run Coating Performance Record in Existence, Stored as PDFs

**Niche:** [[niches/painting-contractors/protective-coatings-consulting/profile|Protective Coatings Consulting & Failure Analysis]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Coating service life is quoted as a convention — twenty to twenty-five years for a three-coat system — and the only organisations holding decades of field evidence about what actually happens publish none of it.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals

## The Problem
Every recoating decision on a bridge, water tank, ship or process vessel is a timing decision. Recoat too early and the owner spends millions of dollars of remaining life; recoat too late and corrosion has moved into the steel, turning a paint job into a structural repair at ten times the cost.

The timing is decided against service life expectations that are conventions. A given coating system in a given environment is said to last a certain number of years, a figure that originated in manufacturer literature and accelerated laboratory testing and has propagated through specifications for decades. Accelerated weathering — salt fog chambers, cyclic exposure cabinets — correlates poorly with field performance and everyone in the industry knows it.

Meanwhile the consultancies have been surveying real structures for forty years. Each survey records what system was applied, when, over what surface preparation, in what exposure, and what condition it is in now. Repeat surveys on the same asset produce a time series. Failure investigations record what went wrong and why. Across a large consultancy this is thousands of asset-years of observed coating performance under known conditions — the only body of field evidence about coating durability that exists anywhere, including inside the manufacturers.

It sits in report files, one asset at a time, and has never been assembled.

## Why Nobody Has Built This
The reports were written to answer a client's question about one structure, and once answered the file closed. Nobody was paid to make the observations comparable across assets, and consulting economics do not fund work no client asked for.

The condition data is also recorded in a form that resists aggregation. Surveys report rust grade, blistering, adhesion pull-off values and per cent breakdown against standard scales, embedded in narrative, with the exposure and preparation history described in prose. Turning forty years of that into a comparable dataset is a large, unglamorous extraction job.

There is also a genuine commercial hesitation. A consultancy that published measured service lives would be contradicting manufacturer literature its clients specify from, and would be doing so about products made by companies it also works for.

## What to Build
A survival model of coating systems, fitted on the consultancy's own survey archive.

**Extract the surveys into structure.** System, surface preparation standard, application date and conditions, substrate, exposure environment, and every recorded condition observation with its date. Decades of reports are the training corpus, and the extraction is the moat — a competitor would need forty years to reproduce it.

**Model time to defined failure, not average life.** Coating end-of-life is a threshold crossing on a condition scale, observed at irregular inspection intervals, with most assets not yet failed. That is interval-censored survival data, and it is the right frame for a question the industry currently answers with a single number.

**Report the curve, not the number.** An owner planning a capital programme needs the probability the coating survives to each of the next ten budget years. That is what turns an assessment into a capital planning input, and it is exactly what the current deliverable cannot say.

**Separate preparation from product.** Surface preparation is widely believed to matter more than the coating itself, and the archive contains the variation — specified preparation standard, achieved profile, ambient conditions at application — that would let that belief be measured instead of asserted.

**Publish the backtest.** Predicted versus observed condition on assets resurveyed after the model was fitted. No party in the coatings industry has ever published a validated service life prediction.

## Target Customer
President or Director of Consulting Services at a protective coatings consultancy. The commercial argument is that condition surveys are increasingly commoditised by inspection firms competing on day rate, and a defensible remaining-life prediction is a service no inspection firm can offer.

## Impact If Built
US owners of steel infrastructure spend billions annually on recoating scheduled against conventional service life figures with no field validation. A validated survival model would shift a substantial fraction of that spending to better timing — and would give the consultancy the one thing its competitors structurally cannot copy.
