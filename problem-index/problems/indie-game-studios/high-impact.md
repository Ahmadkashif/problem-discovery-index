# You Find Out Whether the Game Works After It Is Finished

**Industry:** [[indie-game-studios|Indie Game Studios]]
**Type:** High Impact
**One-liner:** A studio commits three years and learns the commercial answer in launch week, when every signal that predicted it was available eighteen months earlier and unreadable by anyone on the team.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #confidence-intervals #bayesian-inference #evaluation-metrics #hypothesis-testing #revenue-impact

## The Problem
An independent game's commercial outcome is decided in a short window. Launch week sales dominate lifetime revenue for most titles, launch visibility is driven by wishlist accumulation and early velocity, and the algorithmic surfacing that follows compounds whichever way the first days went. There is no gradual build and very little second chance.

The studio arrives at that week having spent its entire runway. By then the game is what it is: the art direction, the hook, the first fifteen minutes, the price point and the genre positioning are all fixed, and those are precisely the variables that determined the outcome.

Signals were available much earlier. Wishlist accumulation rate and its shape after each public beat, demo retention and where players stop, the ratio of wishlists to demo downloads, the response pattern to a trailer, and how playtesters describe the game in their own words — all of these are observable during development and all of them relate to the eventual commercial result. Studios collect some of them and cannot interpret any of them, because interpretation requires knowing what a healthy wishlist curve looks like for this genre at this price, which requires seeing thousands of other games' curves.

The practical consequence is that the most important decisions are made on vibes. A studio cannot tell whether its first fifteen minutes are a problem or whether its genre is simply slow to wishlist, cannot tell whether a disappointing demo response means the demo or the game, and cannot tell whether to delay, cut scope, change the trailer or change the price. So it proceeds, and finds out.

## Why It's Unsolved
The comparative data sits with the platforms and the aggregators. Steam gives a studio its own numbers and nothing about anybody else's; third-party estimators reconstruct approximate sales from review counts with substantial error. Nobody publishes the trajectory data — wishlist curves by genre, demo conversion benchmarks, the relationship between pre-launch signals and outcomes — because the parties who hold it either have no reason to share it or sell advice derived from it.

Publishers are that second group, and their value proposition is precisely this pattern recognition. A publisher who has funded forty games knows what a worrying wishlist curve looks like. That knowledge is worth a large revenue share, which is a reasonable trade and also an argument for why it has not been commoditised.

The sample problem is real for any individual studio. One game is one observation; a studio cannot learn from its own history because it has two or three data points across a career. Only a cross-studio dataset answers anything, and assembling it requires studios to contribute their own numbers to a pool — which is feasible, has been attempted informally through developer communities and spreadsheets, and has never been done systematically.

And the counterfactual is genuinely hard. Knowing that a wishlist curve is below the genre median does not tell a studio what to change, because the causal question — would a different trailer, price, or opening have helped — is not answerable from observational trajectory data alone.

## What a Solution Looks Like
Build the comparative base. Wishlist curves, demo retention, review velocity and revenue outcomes, contributed by studios into a pool and reported back as benchmarks by genre, price band, platform and launch window. That single artefact would convert a studio's own opaque numbers into a position relative to a distribution, which is the interpretive frame nobody currently has.

Forecast the outcome with honest uncertainty. Wishlist trajectory is predictive of launch sales and the relationship is estimable across many titles; the useful output is a distribution rather than a number, because a studio deciding whether to delay six months needs to know the spread, not a point. Reporting that at intervals through development turns the commercial answer from a launch-week revelation into a series of updates.

Instrument the parts a studio can still change. Demo and playtest telemetry — where players stop, what they skip, which tutorial step loses them, how long until the hook lands — is directly actionable and is the one signal that arrives while the game is still malleable. Most single-player indie projects collect none of it.

Test the malleable variables properly. Trailers, capsule art, price and store copy are cheap to vary and their effect on wishlist conversion is measurable with real experiments rather than opinion. Those are the decisions where evidence is both obtainable and currently absent.

## Impact If Solved
This industry loses most of its studios to commercial outcomes that were predictable and unpredicted, after the money was spent. A comparative benchmark base plus early forecasting with honest intervals changes the decisions that are still open — scope, delay, price, positioning, whether to seek a publisher and on what terms — and it partially commoditises the pattern recognition that publishers currently charge a large revenue share to supply.
