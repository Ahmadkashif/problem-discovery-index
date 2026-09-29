# Reading the Curve

**Niche:** [[niches/indie-game-studios/signal-interpretation/profile|Signal Interpretation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The wishlist curve, the demo retention and the playtest stopping points are a forecast, and the studio sees three unrelated numbers.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #k-nearest-neighbors #cross-validation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn a studio's own wishlist shape, demo retention and playtest behaviour into a commercial forecast — and whoever reads those signals best tells a two-person team what three years of their life is worth while they can still change it.

## The Problem
Each signal is individually weak and jointly informative. A wishlist curve's slope and its response to events says something about organic demand. A demo's retention profile says something about whether the game holds people. Playtest stopping points say something about where it loses them. Together, against comparable games, they support a forecast. Separately, presented as counters in three different places, they support nothing, which is what a studio currently has.

## Why Nobody Has Built This
The signals live in different systems — the store, the engine, a playtest build — and nobody joins them, so the joint reading has never been attempted from inside a studio. Modelling requires the benchmark corpus. Studios have no analytics capacity. And the relationship between development-stage signals and outcomes has never been established publicly.

## What to Build
Model the signals jointly against outcomes. Combine wishlist trajectory, demo funnel, playtest behaviour and genre into a single forecast, which is the core and is where the joint signal beats any individual one. Model the curve's shape rather than its level, since the slope and its response to events carry most of the information. Use demo retention as the strongest single predictor available, because a demo is the closest thing to the product and its funnel is measurable. Read playtest stopping points as a design signal and a commercial one, as they indicate both what to fix and how the game will be received. Produce a range and a confidence, since precision on a three-year decision would be dishonest. Recommend an action — change the positioning, cut the scope, delay, go wider on demos — as a forecast without an option is only bad news. Update as the project progresses, so the studio sees whether their changes moved anything. Handle the studio with almost no data, since that is most of them and a sparse forecast is still better than folklore. Validate prospectively and report accuracy, which is what distinguishes this from the advice already circulating. And present it in the language of a developer rather than of an analyst.

## Target Customer
Studio leadership, publishers evaluating projects, funders, and game analytics vendors.

## Impact If Built
The signals live in different systems and nobody joins them, so the joint reading has never been attempted. Combining wishlist shape, demo funnel and playtest behaviour is where a forecast becomes possible from data the studio already has.
