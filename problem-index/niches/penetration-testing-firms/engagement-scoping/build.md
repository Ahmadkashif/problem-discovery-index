# Build: Scope From Discovery, Not From a Questionnaire

**Niche:** Engagement Scoping & Estimation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A scoping engine that discovers the actual attack surface before quoting and estimates effort from the firm's own history of what similar estates took.
**Tags:** #gradient-boosting #confidence-intervals #evaluation-metrics #graph-theory #bayesian-inference #linear-regression #automation #revenue-impact
**Contested on:** Whether an engagement's size is set by what the attack surface actually contains, or by an asset list the client compiled by asking around.

## The Problem

Scoping is the highest-leverage decision in the entire engagement and is made with the worst information anyone will have.

The client answers a questionnaire from memory and internal enquiry. Asset inventories in most organisations are incomplete — this is not a criticism of any particular client, it is the well-documented normal state, and it is precisely why external testing is valuable. So the count that determines the engagement's size is produced by the same process whose unreliability the engagement exists to check.

The firm then converts that count into days with a rule of thumb held in a scoper's head. Every firm has hundreds of completed engagements with quoted days, actual effort and — if anyone computed it — the coverage achieved. None of them has turned that into an estimate. The scoper's intuition is real expertise and it is uncalibrated, unexamined and unshared, and it produces the same systematic bias for years because nothing ever measures it.

The result is engagements sized wrong in both directions. Undersized ones produce thin coverage reported as an assessment. Oversized ones lose bids to competitors guessing lower. Neither error is visible after the fact.

## Why Nobody Has Built This

**Pre-sales discovery is unbilled work on an opportunity that may not close.** Running real discovery before quoting costs time on every prospect, most of whom go elsewhere, and no firm wants to fund it.

**Accurate scoping raises prices and loses bids.** A firm that correctly determines the estate is twice the stated size quotes twice the days and loses to a competitor who accepted the questionnaire. The market currently rewards under-scoping, which is the central obstacle and the reason this needs coverage reporting alongside it to work.

**Unsolicited discovery is delicate.** Enumerating a prospect's external surface before a contract exists is legally and reputationally sensitive, even using entirely passive public sources. The framing and consent model matter enormously and are easy to get wrong.

**Effort data is not recorded in a usable form.** Firms track billed days. Almost none record what coverage those days achieved, which is the dependent variable any estimate needs — which is why this depends on [[niches/penetration-testing-firms/coverage-measurement/profile|🎯 Coverage Measurement]] existing first.

**Scopers own the judgement.** Estimation expertise is a senior person's professional standing, and a model that does it explicitly is not obviously welcome to the people whose approval it needs.

**Internal surface is invisible from outside.** External discovery is tractable; internal networks, authenticated application surface and cloud configuration are not, and they are often the larger part.

## What to Build

**Passive discovery before the quote, with consent.** Certificate transparency, public DNS, passive reconnaissance sources, cloud provider ranges, code and package registries, and public API documentation — all passive, all from public sources, framed explicitly as a scoping service the prospect agrees to. Delivered as a free pre-engagement asset map, which is genuinely useful to the prospect and is a strong commercial opening in its own right.

**Reconcile discovered against declared.** The output that matters: assets the client did not list, applications not mentioned, subdomains nobody owns, third-party services in scope by implication. This conversation, held before the contract, is worth more to the client than most of the engagement and reframes scoping from a haggle into a finding.

**Estimate from the firm's own history.** A model over completed engagements — asset counts and types, technology stack, application complexity, role counts, authentication surface — predicting the days required to reach a target coverage depth, with an interval. Trained on the firm's own data, so it learns that firm's testers and standards rather than an industry average.

**Quote against a coverage target, not a day count.** The commercial shift this makes possible: instead of selling ten days, sell a stated depth across a stated surface, with the days derived. This aligns what the client buys with what they think they are buying, and it is how the assurance-level vocabulary in [[niches/penetration-testing-firms/assessment-assurance/profile|🔵 Assessment Assurance]] becomes sellable.

**Flag inadequate scopes before signing.** When the requested budget cannot reach meaningful coverage of the discovered surface, say so in the proposal, with the coverage the budget will actually buy and what full coverage would cost. Some clients will take the smaller engagement knowingly, which is a legitimate choice and a far better one than an uninformed one.

**Recheck at kickoff.** Enterprise procurement takes months. A discovery re-run on the first morning catches what changed, and takes an hour.

**Calibrate continuously.** Predicted versus actual on every engagement, per scoper and per asset class, so the systematic biases become visible and correctable. No firm has ever looked at this and every firm could.

## Target Customer

Testing firm commercial leadership, where the pre-sales asset map is immediately useful as a sales instrument regardless of the estimation model — which is the wedge that gets it adopted.

Firms with a quality position to defend benefit most, because accurate scoping only stops being a competitive handicap once coverage is visible, and they are the ones who want coverage visible.

## Impact If Built

The engagement gets sized against reality. Every downstream problem in this industry — thin coverage, unstated gaps, reports that overpromise — begins with a number set by a questionnaire.

The reconciliation conversation is a better product than the questionnaire it replaces. Telling a prospect about assets they did not know they had, before any contract, is the most persuasive possible demonstration of why they need testing.

And calibrated estimation turns a decade of one scoper's uncorrected intuition into a measured capability, which is the difference between expertise and habit.
