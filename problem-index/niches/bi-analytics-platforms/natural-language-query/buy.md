# Text-to-SQL Against a Real Organisation's Model

**Niche:** [[niches/bi-analytics-platforms/natural-language-query/profile|Natural Language Query]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Text-to-SQL has strong models and public benchmarks, and the benchmarks use clean schemas with obvious column names, which is the opposite of every real warehouse.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #cross-validation #transfer-learning
**Contested on:** Every serious competitor in conversational analytics is fighting to return an answer that is correct against a governed model and to refuse when the model cannot support the question — and whoever refuses well takes the account, because one confidently wrong answer ends the deployment.

## The Problem
Models achieve strong accuracy on text-to-SQL benchmarks. Real warehouses have tables named after the system that produced them, columns called flag_3, seven date fields of which two are populated, a fiscal calendar that does not start in January, and a set of conventions held entirely in the heads of three analysts. The measured accuracy and the delivered accuracy are unrelated, and every vendor quoting the former is selling into the latter.

## What Already Exists
Strong general and specialised text-to-SQL models, public benchmarks and leaderboards, retrieval over schema metadata, execution-based validation, and self-correction loops that run a query and revise on error. Semantic layers provide a cleaner target than raw schemas. Query logs supply thousands of examples of correct SQL for real questions, which is the best available adaptation data and sits unused in every platform.

## The Customization Gap
The adaptation is to an organisation's own semantic reality. It requires: (1) grounding in the semantic layer rather than the physical schema wherever one exists, which converts an open-ended generation problem into a constrained composition problem and is the single most effective change available; (2) mining the query log for question-to-SQL pairs, since the platform holds a large corpus of queries that analysts wrote to answer real questions and the dashboard titles and request tickets supply the questions — this is the in-domain training and evaluation data everyone lacks and nobody has assembled; (3) capture of tacit convention as explicit model content, because the exclusions and defaults analysts apply automatically are the difference between a plausible query and a correct one, and they are not in any schema; (4) execution-based verification with result sanity checks — row counts, null rates, magnitude against history — which catches a large share of wrong answers cheaply and is entirely mechanical; and (5) evaluation on the customer's own questions, reported honestly, since a vendor quoting benchmark accuracy is quoting a number with no bearing on the deployment.

## Target Customer
BI platform vendors, conversational analytics entrants, semantic layer vendors, and internal data platform teams building this rather than buying it.

## Impact If Solved
The models are good and the gap is entirely contextual, which means the leverage is in the grounding and the in-domain data rather than in the model. The query log is the asset every platform holds and nobody has mined, and it is simultaneously the training data and the evaluation set.
