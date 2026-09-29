# Hybrid Monetisation Configuration

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Games now earn from both advertising and purchases, the two compete for the same player attention, and the balance is tuned by A/B tests that measure one of them at a time.
**Tags:** #causal-inference #markov-decision-processes #gradient-boosting #bayesian-optimization #confidence-intervals #survival-analysis #evaluation-metrics #revenue-impact

## The Problem
Hybrid monetisation — rewarded video, interstitials, in-app purchases and battle passes in the same game — became standard when pure advertising models stopped covering acquisition costs. It introduced a design tension that the tooling does not represent: advertising revenue and purchase revenue draw on the same player, and an ad break that earns a few cents can displace a purchase worth considerably more, or degrade the session that would have led to one.

Configuration is tuned by experiment, one variable at a time: interstitial frequency, rewarded placement, offer pricing, bundle composition. Each test reports its own metric, and a test that raises ad revenue is usually read as a win without measuring what happened to purchase revenue or to retention over the following weeks.

Retention is the delayed cost nobody prices. Aggressive ad frequency and purchase pressure both raise short-run revenue and both accelerate churn, and the churn shows up after the test has concluded and been declared successful. The result is a configuration that is locally optimal on every individual test and collectively worse than a balanced one.

## What Already Exists
Mediation platforms — AppLovin MAX, LevelPlay, AdMob — handle ad serving, waterfalls and bidding competently. Remote configuration and experimentation platforms let publishers vary almost anything live. Predictive lifetime value models exist at most serious publishers. Segmented offer systems target purchase prompts by predicted spending propensity. Ad frequency capping and placement rules are standard features.

## The Customisation Gap
The missing object is a joint objective. Total revenue per player over a long horizon, net of the retention effect, is what a publisher wants to maximise, and the experimentation practice optimises components of it separately on short windows. Measuring the cross-effect — how ad load changes purchase behaviour and vice versa — requires designs that vary both together and measure over weeks, which is more expensive and is what would actually answer the question.

The per-player dimension is the second gap. The correct ad load for a player who will never purchase is very different from the correct load for one who might, and predicted propensity is already computed at most publishers for offer targeting. Using it to set ad exposure rather than only purchase prompts is a straightforward extension that is rarely made.

The genre and game structure customisation matters more than usual here. An ad break placed at a natural pause in a puzzle game and one placed mid-session in a strategy game are different interventions, and the transferability of any finding between them is low — which means each publisher needs this fitted to their own portfolio rather than adopting an industry rule.

And the horizon needs to be long enough to include the cost. A test window of days measures the revenue and misses the churn, systematically, in the direction that favours shipping the more aggressive configuration.

## Impact If Solved
Hybrid monetisation is now the default structure and its configuration is set by tests that measure one side of a two-sided trade on a window too short to include the cost. A joint long-horizon objective with per-player ad exposure would raise total revenue and slow churn simultaneously, which is unusual — most monetisation decisions trade one against the other, and this one is currently losing both to a measurement artefact.
