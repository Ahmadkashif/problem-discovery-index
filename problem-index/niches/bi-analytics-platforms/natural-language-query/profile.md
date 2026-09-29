# Natural Language Query

**Parent Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in conversational analytics is fighting to return an answer that is correct against a governed model and to refuse when the model cannot support the question — and whoever refuses well takes the account, because one confidently wrong answer ends the deployment.

## Profile
**Market Size:** ~$1.9B US natural language and conversational analytics
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Medium and rising fast — promised for a decade, genuinely arriving now
**Target Buyer:** Data leadership, with departmental sponsors
**Automation Potential:** Very High for generation, and the contest is not generation

## What Makes This a Distinct Niche
Asking a question in English and receiving a number has been the category's promise since long before it was achievable, and it is now achievable enough to be sold. The contest, however, is not what everybody assumed. Generating plausible SQL from a question is close to solved. Generating the right SQL against a specific organisation's model, where revenue has four definitions and the fiscal year starts in February and the orders table contains cancelled orders that everyone knows to exclude, is not — and the failure mode is the worst available, because the system returns a confident, well-formatted, wrong number that nobody can distinguish from a right one. A wrong chart is worse than no chart, and a single incident of a leadership decision made on a hallucinated number ends the deployment permanently. Whoever wins this wins on calibration and refusal rather than on fluency.

## Current Tools & Gaps
Natural language features in every major platform, a wave of conversational analytics entrants, text-to-SQL benchmarks and research, and semantic layers being repositioned as the grounding mechanism. The gaps: refusal is not a first-class behaviour, so systems answer questions they should decline; the semantic model is treated as schema rather than as business meaning, so the tacit exclusions and conventions every analyst knows are absent; there is no verification path, so the user cannot check the answer without being able to read SQL, which defeats the purpose; and evaluation is done against public benchmarks rather than against the customer's own questions, which is where the difficulty actually is.

## Problems
- [[niches/bi-analytics-platforms/natural-language-query/build|🔨 Build: Knowing When Not to Answer]]
- [[niches/bi-analytics-platforms/natural-language-query/buy|🛒 Buy: Text-to-SQL Against a Real Organisation's Model]]
- [[niches/bi-analytics-platforms/natural-language-query/fix|🔧 Fix: The Tacit Exclusions Every Analyst Knows]]
