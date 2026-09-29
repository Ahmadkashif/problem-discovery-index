# Player Valuation From Sports Analytics

**Niche:** [[niches/esports-organizations/roster-valuation/profile|Roster Valuation]]
**Industry:** [[industries/esports-organizations|Esports Organizations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sports analytics built contribution metrics that separate the player from the team, and esports signs contracts on raw statistics.
**Tags:** #causal-inference #bayesian-linear-regression #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish what a player will contribute to a different team, when every statistic available depends on the patch, the meta, the role and the teammates they had — and whoever solves the transfer takes the account.

## The Problem
Professional sport spent two decades solving exactly this. The central insight — that raw counting statistics reflect opportunity and context rather than ability — produced adjusted plus-minus, wins above replacement, possession-adjusted metrics, park and league adjustments, ageing curves and projection systems. These methods are public, well understood, and used to justify enormous contracts. Esports has the same problem in a more extreme form and has borrowed almost none of it.

## What Already Exists
Contribution metrics adjusted for teammates and context; replacement-level baselines; league and environment adjustment factors; ageing curves; and projection systems with uncertainty.

## The Customization Gap
The adaptation is to a sport whose rules change every few weeks. It requires: (1) the game itself changing with each patch, so a season is not a homogeneous environment and historical data decays in relevance far faster than in any physical sport — this is the substantive difference and it breaks the standard longitudinal methods; (2) roles that are chosen per match rather than fixed, making role adjustment a within-season problem; (3) careers of five to eight years with ageing curves nobody has established; (4) far smaller sample sizes, since a season is dozens of matches rather than hundreds; and (5) no shared statistical infrastructure across leagues, so the data assembly is itself a project.

## Target Customer
Esports organisations, general managers and coaching staff, player agencies, and sports analytics vendors.

## Impact If Solved
Sport solved context adjustment because contracts depended on it, and the methods are public. A game whose rules change every few weeks breaks the standard longitudinal approach, and that is what has to be rebuilt.
