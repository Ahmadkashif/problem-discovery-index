# Estimation From Evidence

**Niche:** [[niches/game-porting-studios/port-estimation/profile|Port Estimation]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The commercial risk of the whole business is priced by intuition and nobody has checked the intuition.
**Tags:** #gradient-boosting #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact #hypothesis-testing #descriptive-statistics #bayesian-linear-regression
**Contested on:** Every serious competitor in this niche is fighting to quote a fixed price and a fixed date for work whose difficulty depends entirely on properties of a codebase they cannot see until after the contract is signed — and whoever estimates it accurately takes the account.

## The Problem
A porting studio bids fixed price against a fixed date on a codebase it has barely seen. Effort depends on renderer structure, platform-specific code in gameplay systems, memory budget usage, engine version support and undocumented custom work — none of which is visible in a scoping call. The studio that has done dozens of projects holds the only dataset that exists about what makes a port expensive, and treats each new project as a bespoke engagement rather than as another observation.

## Why Nobody Has Built This
Each project is run as a one-off, so the data is never assembled. The expert's judgement works well enough that nobody questions it. Recording estimates against actuals invites uncomfortable conversations. And the studios are service businesses with no analytics function.

## What to Build
Turn the studio's own project history into an estimator. Build a structured record of every past project — measured codebase characteristics, the estimate, the actual hours, and what specifically went wrong — which is the core and is worthless for a year and decisive thereafter. Model realised effort against measurable codebase properties rather than against subjective complexity, since the whole value is in replacing judgement with something checkable. Produce a range with a stated confidence rather than a point, because a point estimate on this is a fiction everyone then plans against. Price risk explicitly, as the current practice buries contingency in a margin that then absorbs the error invisibly. Identify the specific factors that have historically caused overruns and check for them at bid time, which is the fastest available improvement. Support staged bidding — a paid assessment before a fixed quote — which changes the commercial structure and is the honest answer to the information problem. Calibrate the expert's judgement against outcomes, which is valuable and sensitive and is the thing nobody does. Handle the moving-target risk as a separate priced item rather than absorbing it. Report estimate accuracy as a business metric, which is what drives the whole practice. And make the model's reasoning visible so experienced staff can argue with it rather than being replaced by it.

## Target Customer
Porting and co-development studios, publishers commissioning ports, engine and platform partners, and services estimation vendors.

## Impact If Built
The only dataset about what makes a port expensive sits in the studio's own history and is never assembled. Modelling realised effort against measured codebase properties replaces an uncheckable judgement with a range and a risk price.
