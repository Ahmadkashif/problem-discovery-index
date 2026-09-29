# Retrieval Evaluation Frameworks Already Published

**Niche:** [[niches/customer-support-platforms/knowledge-generative-deflection/profile|Knowledge & Generative Deflection]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Evaluating a retrieval-augmented answering system — faithfulness to source, answer correctness, retrieval relevance — is a developed discipline with open frameworks, and support deflection is evaluated by whether the customer clicked a thumb.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #cross-validation #automation #descriptive-statistics
**Contested on:** Every serious competitor in support deflection is fighting to detect which knowledge has quietly become wrong before it is used to answer a thousand customers — and whoever keeps the corpus true takes the account.

## The Problem
A deflection product reports that 62% of conversations were resolved without an agent, based on the customer not escalating. Some of those customers received a correct answer. Some received a wrong answer and acted on it. Some gave up. All three count as deflection. The customer satisfaction thumb is answered by a small and unrepresentative fraction. The measurement that matters — was the answer correct, and was it faithful to the source it cited — is standard practice in the evaluation discipline that grew up around these systems and is not performed in production here.

## What Already Exists
Retrieval-augmented generation evaluation is a developed area with open frameworks and published metrics: retrieval relevance and recall, answer faithfulness to retrieved context, answer correctness against a reference, and hallucination detection. Annotation tooling is commodity. Golden question sets with reference answers are a standard construct. Continuous evaluation pipelines are ordinary engineering. Every component is available and most of it is newer than the deflection products it would measure.

## The Customization Gap
The adaptation is to a production support context rather than a benchmark. It requires: (1) a golden set built from the organisation's own real questions with expert-verified answers, maintained as the product changes — which is the investment, and it is modest compared to the risk it addresses; (2) faithfulness measured separately from correctness, because an answer faithful to a stale article is exactly the failure mode this niche is about and the two metrics diverge precisely where it matters; (3) continuous production sampling rather than pre-release evaluation only, since the corpus changes underneath a system that was evaluated once; (4) severity weighting, because a wrong answer about a billing charge, a security setting or a medical device instruction is not equivalent to a wrong answer about a colour option, and an aggregate accuracy figure treats them identically; and (5) the results published to the customer of an outcome-priced contract, since a resolution that was wrong should not be billable and currently is.

## Target Customer
Support platform and deflection vendors, the support organisations buying outcome-priced resolution, and the quality assurance functions who currently sample human conversations and not automated ones.

## Impact If Solved
The evaluation discipline is mature and free and the category has deployed generatively answering systems into production without it. Severity-weighted accuracy is the specific adaptation that matters, and publishing production accuracy is what would make outcome-based pricing an honest arrangement rather than a count of conversations that did not escalate.
