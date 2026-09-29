# Human Preference Operations

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to collect preference ratings that measure the model rather than the presentation — and whoever does that takes the account, because the current ratings are substantially a measurement of length and formatting.

## Profile
**Market Size:** ~$190M US
**Share of Parent Industry:** ~24% of category revenue
**Digital Adoption:** Low — infrastructure solved, quality unmeasured
**Target Buyer:** Labs and evaluation firms running preference collection at scale
**Automation Potential:** High — the corrections are all statistical

## What Makes This a Distinct Niche
Pairwise human preference has become the field's headline measure, and the infrastructure for collecting it is solved and widely available. What is not solved is that the ratings it collects are shaped by presentation order, response length, formatting and confident tone far more than the people reporting the results acknowledge. These are well-documented effects with a literature behind them, and the standard reporting pipeline corrects for almost none of them. A leaderboard built on uncorrected preference is partly a leaderboard of verbosity, which is known inside the field and does not appear next to the numbers.

## Current Tools & Gaps
Pairwise comparison interfaces, rating platforms, rater pools, and rating aggregation into ratings systems. The gaps: order and position effects are not designed out or corrected; length and formatting confounds are not adjusted for; rater quality is estimated with methods that assume a knowable correct answer, which preference does not have; rater populations are not characterised, so the preference being measured belongs to an unspecified group; and disagreement between raters is treated as noise when it is frequently a real difference in legitimate taste.

## Problems
- [[niches/ai-model-evaluation-firms/human-preference-operations/build|🔨 Build: Rating the Formatting]]
- [[niches/ai-model-evaluation-firms/human-preference-operations/buy|🛒 Buy: Survey Methodology and Psychometrics]]
- [[niches/ai-model-evaluation-firms/human-preference-operations/fix|🔧 Fix: Rater Quality Measured Against an Answer That Does Not Exist]]
