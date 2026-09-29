# Matching Optimised on the Click

**Industry:** [[lending-marketplaces|Lending Marketplaces]]
**Type:** High Impact
**One-liner:** The marketplace decides which lender a borrower sees using the only signal lenders return to it, which is whether the borrower clicked — not whether they were approved, at what rate, or whether the loan ever performed.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance #revenue-impact

## The Problem
A borrower arrives with a need and a profile: credit band, income, purpose, amount, state, sometimes a soft-pull bureau file. The marketplace ranks lenders and presents offers or routes the lead.

Ranking is a function of lender bid, predicted click probability, and whatever partner agreements specify. In some cases a pre-qualification API returns a genuine indicative offer; in many it does not, and the "offer" displayed is a rate table entry the borrower may not qualify for.

The borrower clicks. From that point the marketplace's visibility usually ends. Whether the lender approved, what rate was actually offered, whether the borrower accepted, whether the loan funded, and whether it performed — each of these is known to the lender and contracted back to the marketplace inconsistently, incompletely, or not at all. Funding notification exists in the better partnerships because the fee depends on it. Terms and performance almost never come back.

So the ranking model optimises the click. This is a rational response to the available signal and it produces a specific, compounding set of harms.

Borrowers are routed to lenders who will decline them. Each attempt may cost a hard inquiry, which lowers the score marginally and looks like shopping distress in aggregate. The borrower's experience is a sequence of declines from a site that presented itself as matching them.

Lenders receive leads they cannot convert and conclude the marketplace's quality is poor. Their remedy is to bid less or to leave, which the marketplace experiences as a revenue problem and addresses with volume.

And the marketplace cannot distinguish its good matches from its bad ones. A lender with a high bid and a low approval rate for a given profile outranks one with a modest bid and a high approval rate, because only the bid is measurable.

The ranking is also a regulated statement. Presenting paid placement as a personalised match is a disclosure question, and it is much harder to defend when the ranking has no relationship to whether the borrower will actually be served.

## Why It's Unsolved
Lenders have no reason to return decision data and several reasons not to. Their underwriting is proprietary, approval rates by profile are competitively sensitive, and a marketplace that could predict a lender's decisions could arbitrage them. The contracts reflect this, and they were written when the marketplaces had less leverage than they now have.

Attribution is genuinely hard even with cooperation. A borrower who visits three sites and applies to five lenders produces overlapping records, and identity resolution across that is imperfect. Loan performance data is sensitive under credit reporting rules, and returning it at the individual level raises permissible-purpose questions that are not trivial.

The business model rewards volume. Revenue per lead is the metric, more leads is the reliable way to increase it, and improving match quality reduces routing volume in the short term while improving it only later and only if lenders reward it. The incentive gradient runs against the fix.

And the missing data is invisible on every internal dashboard. Click-through, conversion to click, and revenue per session all look healthy in a system that is systematically misrouting borrowers, because nothing in the reporting represents the borrower's outcome.

## What a Solution Looks Like
Make decision return a condition of participation. This is the whole problem and it is commercial. A lender that returns approve or decline with a reason band, and the terms actually offered, receives better-matched traffic; one that does not receives the traffic the model cannot place confidently. That is a legitimate and enforceable structure, and it is how the marketplace converts its position into data.

Approval probability modelled per lender per profile, from returned decisions where available and inferred from funding patterns where not. Even sparse decision data across a large volume produces a usable approval surface, and it immediately changes the ranking.

Rank on expected borrower outcome, with the commercial component explicit and separable. Expected value to the borrower — probability of approval times quality of terms — is computable, and a ranking that blends it with bid transparently is both better and far easier to defend than one where the two are entangled.

Inquiry cost treated as a real cost. Every routing decision spends a fraction of the borrower's credit profile. A marketplace that models this stops sending borrowers to five lenders in the hope that one approves.

Honest pre-qualification. Where a lender provides a genuine soft-pull indicative offer, show it; where the displayed number is a rate table entry the borrower may not receive, say so. The gap between advertised and actual received rates is measurable by the marketplace and is currently measured by nobody.

## Impact If Solved
The marketplace occupies the only position from which the borrower's full shopping journey is visible, and it optimises against a signal that is three steps away from whether the borrower was helped. Obtaining decision data changes the ranking, the lender relationship and the regulatory posture simultaneously, and it is available to any marketplace with enough volume to make participation worth a lender's while.
