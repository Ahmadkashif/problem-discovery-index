# Build: The Benchmark Nobody Owns

**Niche:** Performance Evaluation & Benchmarking
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A held-out, governed, disaggregated benchmark across categories and languages, run by an institution with no commercial stake, so products become comparable and regulators have something to verify against.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bert #compliance #descriptive-statistics #data-integration
**Contested on:** Whether two products can be compared at all.

## The Problem

There is no shared benchmark for trust and safety classification. Every performance claim in the category is a vendor's statement about its own exam.

The consequences run in every direction. Buyers cannot choose on quality, so they choose on price, integration effort and language coverage claims — which means the market does not reward accuracy. Regulators requiring platforms to report moderation accuracy receive figures derived from vendor claims that nobody can verify. Researchers studying moderation outcomes have no ground truth to work from. And the per-language and per-community failures that cause most documented harm stay invisible, because no aggregate figure reveals them and no independent measurement exists.

The technical requirements are ordinary. A held-out test set with known labels, a submission protocol, disaggregated reporting, and governance preventing training on the test data. This is how machine learning benchmarks work and the pattern is well established.

The obstacles are institutional. Labelled data in these categories is expensive and legally sensitive to hold — some of it cannot be held by a general institution at all. Vendors leading on unverifiable claims have no reason to participate. And no organisation currently owns the problem.

## Why Nobody Has Built This

**Nobody owns it.** Vendors will not build a benchmark that measures them. Platforms could and have not. Researchers lack the resources and the legal position. Regulators have the mandate and not the capability. The gap is institutional and it is the whole problem.

**The data is legally and ethically hard to hold.** Some categories — child safety material in particular — cannot be held by a general benchmark organisation, which requires either specialised custodianship or evaluation conducted inside an existing lawful holder.

**Vendors would not participate voluntarily.** A leading vendor has everything to lose from measurement and nothing to gain, which means participation must be required by buyers or regulators rather than volunteered.

**Categories are policy-dependent.** What counts as harassment differs by platform policy, so a benchmark must either fix a policy definition or evaluate against several, which is a design problem rather than an obstacle.

**Test set contamination is a real risk.** A public benchmark gets trained on. Held-out governance with controlled submission is the standard answer and requires an institution to run it.

**Funding has no obvious source.** The benefit is diffuse across platforms, users and regulators, which is the classic public goods problem.

## What to Build

**Start with one category where the data is holdable.** Harassment or spam rather than the categories with severe legal constraints. A working benchmark in one category demonstrates the model and builds the institution.

**Govern the held-out set properly.** Submission-based evaluation where vendors send a model or an API endpoint and never see the test data, which is the established pattern for preventing contamination.

**Disaggregate by language and content type from the start.** The whole value is in revealing the distribution, so an aggregate leaderboard would reproduce the problem it exists to solve.

**Evaluate against several policy definitions.** Rather than fixing one definition of harassment, evaluate against a small number of stated policies so buyers can see performance against something close to their own.

**Handle the restricted categories differently.** For material that cannot be held, evaluation conducted inside an existing lawful custodian, with results published and the data never moving. This is the only workable route and it requires that institution's participation.

**Make participation a buyer requirement.** A group of large platforms requiring benchmark participation of their vendors is the mechanism that would produce participation, and it is faster than any regulatory route.

**Publish everything, including the test set composition.** The benchmark's credibility depends on its methodology being inspectable, even where the items themselves are held out.

## Target Customer

Large platforms, collectively, who are the buyers, bear the consequences of bad classification, and have the leverage to require participation of their vendors.

Regulators implementing moderation accuracy reporting requirements, who need something to verify against and currently have vendor claims.

Research institutions and standards bodies, as the natural custodians — the benchmark's value depends entirely on the holder having no commercial stake.

## Impact If Built

The category's defining gap closes, and with it buyers can choose on quality, regulators can verify platform claims, and the failures that cause most documented harm become visible.

Starting with one holdable category is the realistic route, because it produces a working institution and a demonstrated model before attempting the legally constrained ones.

And a coalition of large platforms requiring participation is the mechanism most likely to work, because it is faster than regulation and the buyers are the party with both the leverage and the interest.
