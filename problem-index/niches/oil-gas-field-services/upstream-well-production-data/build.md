# Type Curves Published as Averages Over the Best Forecasting Dataset in Energy

**Niche:** [[niches/oil-gas-field-services/upstream-well-production-data/profile|Upstream Well & Production Data Providers]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm holds every well ever drilled with its completion design and its full production history, and publishes an average decline curve.
**Tags:** #ml-time-series #gradient-boosting #survival-analysis #evaluation-metrics #causal-inference

## The Problem
Every drilling and acquisition decision in shale runs on a type curve: an expected production profile for a well in a given area with a given completion. Operators build capital budgets on them, banks size credit facilities against them, and buyers price acquisitions with them.

Type curves are constructed as averages. Group wells by area and vintage, normalize, fit a decline, publish. The method is transparent, conventional, and discards most of what the data contains.

The corpus supports far more. Every well's location, depth, lateral length, proppant and fluid volumes, stage count, spacing to offsets, completion date, and full monthly production history — across hundreds of thousands of wells and fifteen years of a technology that changed continuously. That is a very large, well-labelled panel for predicting production from design and geology, and it is used to compute group means.

The consequences are concrete. Type curves systematically mislead where the underlying population is heterogeneous, which is most places. Parent-child well interference — where a new well degrades an existing one — is visible in the data and absent from the curves. And the uncertainty around a forecast, which is what a lender or an acquirer most needs, is not reported at all.

## Why Nobody Has Built This
The type curve is an industry convention with regulatory weight behind it. Reserve reporting and bank borrowing bases are built on decline analysis methods that are decades old and well understood, and a vendor publishing something different is asking customers to defend an unfamiliar method to their auditors and lenders.

The data business also grew as a data business. Coverage, normalization, and timeliness are the competitive axes, and the analytics layer has historically been a workspace for customers to run their own analysis rather than a set of models with opinions.

And nobody scores forecasts. Type curves are published for areas, wells are drilled against them, and outcomes are observable within a year — and no one systematically reports how the published curves performed.

## What to Build
Well-level production prediction with honest uncertainty.

**Model production from design and geology directly.** Lateral length, proppant intensity, fluid loading, stage spacing, landing zone, and offset spacing against realized production. Every variable is in the database and the outcome arrives monthly.

**Report distributions, not curves.** A forecast with a prediction interval is what an acquirer or a lender is actually making a decision against, and it is what the method currently cannot produce.

**Model interference explicitly.** Parent-child degradation and offset frac hits are among the largest economic effects in modern shale, they are estimable from spacing and timing in the corpus, and they do not appear in a type curve at all.

**Separate design effects from geology.** Operators change completion designs over time and across acreage, which confounds naive comparison. Handling that properly is what would let the product say what a design change is worth rather than what a vintage produced.

**Publish backtests.** How published forecasts performed against realized production, by area and vintage. No competitor does it, and in a market where the customer's auditor asks where the number came from, being the vendor with a measured track record is a strong position.

## Target Customer
Chief Data Officer or SVP of Product at an upstream data provider. The commercial context is that coverage and normalization are increasingly matched across vendors, and the analytics layer is where differentiation now has to come from.

## Impact If Built
Capital allocation across US shale runs on type curves computed as averages over heterogeneous populations, with no stated uncertainty and no accounting for well interference. Better forecasts with honest intervals would improve billions of dollars of drilling and acquisition decisions annually — and the dataset that supports it is the firm's existing product.
