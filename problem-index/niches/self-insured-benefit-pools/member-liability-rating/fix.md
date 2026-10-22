# The Experience Modifier Swung by One Claim

**Niche:** [[niches/self-insured-benefit-pools/member-liability-rating/profile|Member Liability Rating & Contribution Allocation]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Fix (Pain Point)
**One-liner:** A small town's liability contribution doubles because of one large claim, then falls back three years later, with no signal about its actual risk in between.
**Tags:** #bayesian-inference #regularization #monte-carlo-methods #evaluation-metrics #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to price each member's liability coverage close to its own risk (sworn officers, jail beds, payroll, road miles, past losses), and whoever keeps its low-loss members from leaving for commercial quotes at renewal takes the account.

## The Problem
Experience modifiers in pool formulas use a few years of a member's losses against expected losses. For a small member, one claim dominates. Pools cap losses or modifiers by hand, case by case, and members experience the swings as arbitrary.

## Why It's Still Broken
Formulas were set years ago by an actuary and are revisited rarely. Credibility tables are borrowed from commercial lines and are not recalibrated on the pool's own data. Board members resist changes that move any one member's number.

## What a Fix Looks Like
Recalibrate credibility on the pool's own member-level history, cap single losses at a level chosen by simulation, and show the board how volatility and fairness trade off under candidate formulas before adoption.

## Who Feels the Pain
Finance officers of small members whose budgets cannot absorb a doubling; underwriters fielding appeals; boards defending the formula.

## Impact If Fixed
Contributions that members can budget, with modifiers that reflect risk rather than luck.
