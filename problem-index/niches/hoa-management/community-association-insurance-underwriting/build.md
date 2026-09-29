# The Only Empirical Failure Record for Multifamily Buildings, Used to Set a Rate

**Niche:** [[niches/hoa-management/community-association-insurance-underwriting/profile|Community Association Insurance Underwriting]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These underwriters hold decades of losses joined to building age, construction, roof and maintenance posture across thousands of associations — the closest thing to a component failure database for American multifamily housing.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals

## The Problem
A community association must carry a master property and liability policy, and a small number of specialty insurers write most of them. Underwriting means pricing the building: age, construction type, roof age and material, plumbing and water loss history, life safety systems, and — since the Surfside collapse — the association's structural maintenance posture and reserve position.

That work accumulates something no one else has. Across large books of associations, over decades, the insurer holds building characteristics joined to what actually failed and what it cost. Not a survey, not a sample — the loss record for a large slice of American multifamily housing, at building level.

There is no public equivalent. Building codes specify how things must be built; nothing records how they then behave. Reserve studies estimate component life from published tables. Engineers assess individual buildings. The only party observing thousands of buildings and their failures over time is the one pricing the insurance.

What it produces is a rating model and a renewal quote.

The unbuilt work is substantial and the market conditions have made it urgent. Association insurance has hardened severely, in coastal states it is now a primary driver of assessment increases, and capacity has withdrawn from exactly the buildings hardest to assess. In that environment the ability to distinguish a well-maintained older building from a poorly maintained one is the whole underwriting problem, and it is currently done by inspection and judgment.

Water loss is the sharpest case. It is the dominant frequency driver in these books, it is strongly related to plumbing material and age, and the insurer holds the joint distribution.

## Why Nobody Has Built This
The invoice is a policy. Analysis is an underwriting input, so it is funded to the point where it prices adequately and no further.

Books are also fragmented across carriers and programme managers, and each holds too few of the rare structural events to model them alone. That is a genuine statistical problem and it is exactly the argument for a pooled loss study that nobody has convened.

And the finding is commercially double-edged. An insurer that could price maintenance posture precisely would be revealing that much of the current book is mispriced.

## What to Build
The loss record as a building performance dataset.

**Model component failure as survival.** Roof, plumbing, envelope and mechanical systems fail as a function of age, material, climate and maintenance. That is time-to-event data with censoring, and the book is full of it.

**Estimate the maintenance effect.** Reserve funding level, deferred maintenance findings and completed capital projects are recorded at underwriting and are the variables the market currently prices by intuition.

**Predict water loss frequency.** The dominant driver, with the strongest observable relationship to building attributes, and the one most amenable to prevention incentives.

**Turn the model into loss control that pays.** An insurer able to say which specific intervention reduces expected loss by how much can price a credit for it — which aligns the association, the manager and the carrier, and is a product rather than a rating table.

**Feed the reserve study layer.** Reserve studies estimate component life from published averages. Empirical service lives from a real loss book would improve the reserve studies that the same insurer underwrites against — a genuinely unusual loop where the insurer improves its own input.

## Target Customer
Chief Underwriting Officer at a community association specialty insurer or programme manager. The argument is that this is a hardened market where capacity is scarce and the winner is whoever can price the buildings others cannot assess.

## Impact If Built
Association insurance is now a leading cause of assessment increases for millions of American households, priced on judgment about maintenance posture, in a market that withdrew capacity after a structural failure nobody predicted. The only empirical record of how multifamily buildings actually fail sits in these books and produces a quote.
