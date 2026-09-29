# Contest Every Claim or Predict Which Ones Are Winnable

**Niche:** [[niches/hr-consultants/unemployment-claims-management/profile|Unemployment Claims Management]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has millions of claims joined to their determinations and decides what to contest using a rule of thumb.
**Tags:** #logistic-regression #gradient-boosting #binary-classification #evaluation-metrics #revenue-impact

## The Problem
When a separated employee files for unemployment, the employer has seven to fourteen days to respond or lose the right to contest. The firm handles that for thousands of employers across all fifty state systems, at enormous volume.

The decision on each claim — respond and contest, respond and concede, or push to a hearing — determines both the employer's tax rate and the firm's own economics, since much of this work is priced on outcome. It is made in minutes by an analyst applying separation reason, documentation quality, and their sense of how that state tends to rule.

The firm holds, for every claim it has ever handled, the separation facts, the documentation available, the position taken, the state, the determination, whether it was appealed, and how the appeal went. Millions of rows, cleanly labelled by an outcome that is unambiguous and arrives within weeks. It is one of the best-shaped prediction datasets in this entire index, and it is used to bill.

Nothing predicts. There is no estimate of win probability before the position is chosen, no measurement of which documentation actually moves a determination, and no comparison between analysts making the same call differently.

## Why Nobody Has Built This
The clock dominates everything. Response deadlines are short and unforgiving, volumes are large, and the operation is built to never miss one. Every system, metric, and staffing decision serves throughput, and nothing in that structure asks whether the position taken was the right one.

Historical outcomes are also stored as case records rather than as data. Reconstructing them into a modelling set means mining a case management system built for retrieval by claim, not for analysis across claims.

And there is a defensible-looking default: contest most things. It avoids the harder judgment and it feels safe. It also spends analyst hours on claims that were never winnable, and concedes some that were, and nobody can quantify either because nobody has measured.

## What to Build
Outcome prediction at intake, on the firm's own history.

**Predict determination probability before the position is set.** Separation reason and its narrative, tenure, wage, documentation present, state, employer history, and the claimant's stated reason. Every one of these is captured at intake today, and the label is in the file within weeks.

**Model by state, because the states genuinely differ.** The same separation facts produce different determinations in different states, and hearing representatives know this qualitatively. A model per state — or a shared model with state effects — makes it explicit and transferable.

**Measure what documentation is worth.** Which evidence actually changes a determination, by separation type and state? The firm chases documentation from employers constantly, and has never established which requests are worth making. Some are decisive and some are ritual.

**Score appeal value separately.** A hearing costs real representative time. Predicting appeal success from the first determination and the record turns an intuition into an expected-value calculation.

**Surface analyst variance.** Similar claims positioned differently by different analysts, with different outcomes, is a training signal and a quality signal. It exists in the data now.

## Target Customer
SVP of Operations or general manager at a UI claims management firm. The economics are immediate: where fees are contingent on outcome, better claim selection is directly revenue, and where they are per-claim, it is capacity freed from unwinnable contests.

## Impact If Built
This is one of the cleanest prediction problems in the vault — short feedback loop, unambiguous labels, enormous volume, decision made under time pressure by a human using intuition. The firm has been generating the training data for decades as a by-product of billing. For employers, better selection means a lower tax rate; for the firm, it means analyst hours spent where they change an outcome.
