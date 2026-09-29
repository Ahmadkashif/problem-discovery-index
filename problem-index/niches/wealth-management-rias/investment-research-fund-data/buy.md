# Classifying Strategies From Holdings That Arrive Quarterly and Late

**Niche:** [[niches/wealth-management-rias/investment-research-fund-data/profile|Investment Research & Fund Data Providers]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every peer group, percentile and rating rests on a category assignment inferred from stale holdings and marketing documents, maintained by analysts.
**Tags:** #transformers #graph-neural-networks #k-means-clustering #evaluation-metrics #data-integration

## The Problem
Classification is the foundation the whole product sits on. A fund's category determines its peer group, its benchmark, its percentile ranking and, downstream, its rating. Get it wrong and every comparison built on it is wrong.

Assignment is done from two poor inputs. Holdings arrive on a regulatory disclosure schedule — quarterly for most funds, with a lag — and by the time they are published the portfolio may have moved substantially, which is a well-understood limitation that the industry works around rather than solves. And stated strategy comes from prospectuses and marketing material, which are written to preserve latitude rather than to describe behaviour.

Analysts bridge the gap by reading documents, examining holdings and applying judgment, at a scale of tens of thousands of vehicles across funds, share classes, separately managed accounts, collective trusts and model portfolios — each needing to be recognised as the same underlying strategy in different wrappers.

The failure modes are quiet. Style drift goes uncaught between disclosures. Newly launched strategies are classified from documents alone. Multi-asset and alternative strategies fit categories designed decades ago for a simpler universe. And a category revision reclassifies histories, which advisers experience as their fund's percentile rank changing for no reason they can see.

## What Already Exists
Returns-based style analysis is decades old, well understood, and available in any statistical package — it infers exposures from return patterns without needing holdings, and it is the natural complement to stale disclosures. Text classification over prospectus language is straightforward with modern models. Clustering methods for grouping similar return series are standard.

None of it is assembled into the thing the product needs: a maintained, versioned, defensible classification of every investable vehicle, with confidence attached, that can survive an adviser asking why their fund moved category.

## The Customization Gap
**The output must be a stable, versioned assignment, not a clustering.** Advisers benchmark year over year, so reclassification is a visible product regression. Every change needs a reason, a date, and a preserved history — which no generic clustering tool contemplates.

**Holdings and returns are complementary and must be fused.** Holdings are precise and stale; returns are current and indirect. Combining them into a single time-varying exposure estimate with uncertainty is the core technical work, and it is specific to this domain's disclosure regime.

**Wrapper resolution is a graph problem.** The same strategy appears as a mutual fund, several share classes, a collective trust, a separate account and a model. Recognising these as one thing — and knowing when a nominally identical vehicle diverges — is entity resolution over a fund graph, and only the vendor has the ownership and relationship data to do it.

**Drift should be detected, not discovered.** A fund whose returns stop behaving like its category is emitting a signal between disclosures. Change point detection on exposures is the natural formulation and nothing in the current workflow does it.

**Confidence must be published.** A fund classified with low confidence — a new launch, an unusual mandate, a strategy that fits no category — should say so rather than being placed and ranked as though it fitted.

**The taxonomy itself must be evaluable.** Whether a category groups funds that behave alike is measurable, and the answer should drive taxonomy revision rather than committee preference.

## Target Customer
Head of Methodology or Chief Research Officer at a fund data provider, owning both the classification taxonomy and the analyst team that maintains it.

## Impact If Solved
Classification is the substrate under every ranking, rating and peer comparison this industry runs on, and it is maintained by hand against inputs that are structurally stale. Fusing holdings and returns into a confidence-weighted, drift-aware assignment improves every downstream product at once — and makes the taxonomy itself testable for the first time.
