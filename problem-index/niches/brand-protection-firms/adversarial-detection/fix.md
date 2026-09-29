# Fix: Nobody Knows What Is Being Missed

**Niche:** Adversarial Detection
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Detection reports what it found, no firm estimates what it did not, and an adversarial system with no recall measurement optimises toward whatever is easiest to find.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #automation #revenue-impact
**Contested on:** Whether detection finds the listings of operators who have learned exactly what it matches on.

## The Problem

A monthly report says forty thousand infringing listings were detected. The number that would make it meaningful — how many existed — appears nowhere.

Without a denominator, the count is uninterpretable. Forty thousand out of fifty thousand is excellent. Forty thousand out of four hundred thousand is not, and both produce the same report.

The consequence is not merely reporting. In an adversarial system, an objective with no recall term drives detection toward whatever is cheapest to find. Listings that copy brand photography and put the name in the title are cheap to find and plentiful, so they dominate the count. Operations that have adapted are expensive to find and produce few detections per unit of effort, so they are systematically deprioritised by an optimisation nobody chose.

So a firm can report growing detection volume year after year while the sophisticated operators — who account for most of the actual loss — become progressively better represented among the undetected.

Recall is measurable. Not perfectly, and well enough to change behaviour: test purchases, brand-supplied seizure and market data, and periodic deep manual sweeps of a sample category all produce estimates. None of these is exotic and none is done routinely.

## Why It's Still Broken

**The denominator is unknown and assumed unknowable.** The true population of infringing listings is not directly countable, which is treated as meaning it cannot be estimated — though sampling handles exactly this.

**The count is what the contract rewards.** A firm measured on detections has no reason to produce a figure that contextualises its own headline downward.

**Recall estimation costs money and produces a worse number.** Test purchases and manual sweeps are real expenditure whose output makes the reported performance look smaller.

**The brand cannot check.** A client has no independent view of the infringing population, so they cannot ask the question from a position of knowledge.

**Nobody in the chain is measured on loss.** The brand's manager reports takedowns upward, the firm reports takedowns to the manager, and actual counterfeit sales are measured by nobody.

**It has always been this way.** The metric is industry convention, which makes its absence invisible rather than contested.

## What a Fix Looks Like

**Estimate recall by sampling a category deeply.** Take one product category and one marketplace, search it exhaustively by hand, and compare against what detection found. This is a week of work, produces a real recall estimate for that slice, and nobody does it.

**Use test purchases as ground truth.** Buying suspected counterfeits establishes what exists and whether detection found those listings. Brands do this for evidence and the results are rarely joined back to the detection system.

**Join to the brand's own market data.** Sales shortfalls, grey-market observations, customer complaints about fakes and seizure data all bound the true problem and sit with the client.

**Report a recall estimate alongside the count, with its uncertainty.** A wide, honestly-stated estimate is enormously more useful than no denominator, and the firm that publishes first sets the expectation.

**Measure recall separately for sophisticated operations.** Overall recall may be adequate while recall against the operators that matter is poor. Breaking it out is where the finding is.

**Change the objective to estimated infringing volume removed.** Weighting by scale rather than counting listings redirects detection effort toward operations and away from the plentiful easy listings.

**Brands should ask.** A client requiring a recall estimate at renewal changes what the firm optimises, and it is a question any brand can ask at the next contract discussion.

## Who Feels the Pain

The brand, paying for detection whose coverage is unknown and receiving a number it cannot interpret.

The brand's manager, reporting a takedown count upward with no way to answer whether it represents most of the problem or a fraction.

The detection team, working toward an objective that quietly rewards the easy population, with no metric that would tell them the hard one is escaping.

And consumers buying counterfeits from the operations that adapted, which are the ones least represented in any takedown count.

## Impact If Fixed

A single deep manual sweep of one category produces a real recall estimate for a week of effort, and no firm has one.

Reporting recall alongside the count makes the headline interpretable for the first time, and the firm that does it first defines what a credible report looks like.

And changing the objective from listings removed to estimated infringing volume removed redirects an entire industry's detection effort from the population that is cheapest to find toward the population that causes the loss.
