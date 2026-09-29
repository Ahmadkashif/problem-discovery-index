# Classical ML Experimentation

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to make a large population of cheap runs genuinely comparable — so that a team can say what changed, what it was worth, and where the next run should go — and whoever does that takes the account, because comparability is the only thing a tracking tool is bought for at this scale.

## Profile
**Market Size:** ~$490M US
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** High for logging, near zero for concluding
**Target Buyer:** Data science organisations and their engineering leads
**Automation Potential:** Very High — comparison and search allocation are both computable

## What Makes This a Distinct Niche
The classical workload is many cheap runs: sweeps over tabular models, feature set variations, sampling strategies, thresholds. A team produces hundreds or thousands a month across dozens of projects. The binding problem is not capturing them — that works — but that the population is not comparable. Two runs differ in a hyperparameter, a feature set, a data snapshot and a preprocessing change, and the platform reports the metric difference without being able to say which of the four caused it. Search budget is spent on regions already shown to be unpromising because nobody reads four hundred rows. The alternative these buyers compare against is a spreadsheet and a naming convention, which is a low bar the products clear and then stop at.

## Current Tools & Gaps
Run tables, parallel coordinate plots, sweep orchestration with random and Bayesian search, and report sharing. The gaps: no attribution of a metric difference to the specific change that caused it; no significance treatment, so runs differing within seed noise are ranked confidently; no reuse of prior sweeps to warm-start the next one; and no way to ask what the team has already learned about a question somebody is about to re-investigate.

## Problems
- [[niches/mlops-platforms/classical-ml-experimentation/build|🔨 Build: Four Hundred Runs and No Conclusion]]
- [[niches/mlops-platforms/classical-ml-experimentation/buy|🛒 Buy: Experimental Design and Sequential Testing]]
- [[niches/mlops-platforms/classical-ml-experimentation/fix|🔧 Fix: Ranked Confidently Within Seed Noise]]
