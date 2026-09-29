# Niche Analysis — AI Model Evaluation Firms

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Benchmark Integrity | 🔵 High Market Share | $290M | None — contamination is unmeasured and reported around | Anyone relying on a published score |
| 2 | Evaluation Platforms | 🔵 High Market Share | $310M | High | Frontier labs; separately, application teams |
| 3 | Domain Grading Criteria | 🟠 Low Digitized | $220M | Very Low — authored by an expert every time | Regulated and specialist industry buyers |
| 4 | Human Preference Operations | 🟠 Low Digitized | $190M | Low — infrastructure solved, quality unmeasured | Labs and evaluation firms running preference collection |
| 5 | The Expert Rater | 🟣 Underserved Audience | $150M | None — piece rates against rubrics that do not fit | The physicians and attorneys doing the rating |
| 6 | The Evaluation Engineer | 🟣 Underserved Audience | $130M | None — debugging graders by hand | Evaluation engineering teams |
| 7 | Judge Model Validity | ⚡ Highly Automatable | $170M | Low — the dominant method, least validated | Every firm using a model as a grader |
| 8 | Graded Item Corpus | ⚡ Highly Automatable | $140M | None — the material to fix measurement, unused | The firms themselves |

## Why These Niches

This is an industry that sells trustworthy numbers and has a validity problem at every layer of its own measurement stack. Contamination is the structural one: public benchmarks are plausibly inside the training corpora of the models they measure, the extent is unknowable because the corpora are undisclosed, and the field reports scores as though the question were settled. That makes integrity the largest contested surface and the one a buyer would pay a premium for.

Evaluation platforms **failed the filter as one niche**. A firm contracted privately by a frontier lab is fighting to surface capability and risk the lab's own team missed, on models nobody outside has seen, under conditions where the finding is the product. A platform sold to an application team is fighting to tell them whether last Tuesday's prompt change made their product better on their own task, in continuous integration, at a cost that fits a product budget. The buyers, the cadence, the alternatives and the definition of a good result share nothing. Decomposed below.

The two underdigitised areas are where expert judgement enters. Harnesses are mature and free, and the criteria deciding whether an answer is actually correct in radiology or tax must be written by a specialist each time. Preference collection infrastructure is solved and available, and the ratings it produces are shaped by presentation order, length and formatting more than the people reporting them acknowledge.

The two underserved constituencies are the practising physician or attorney rating outputs at piece rates against rubrics that do not cover their real cases, and the evaluation engineer whose days go to establishing whether a score moved because the model changed or because the grader did.

The automation niches are judge validity — the dominant grading method and the least validated — and the corpus of graded items with judge, rater, model and prompt attached, which is the raw material for fixing measurement and which the commercial incentive discourages examining.

## Niches
- [[niches/ai-model-evaluation-firms/benchmark-integrity/profile|🔵 Benchmark Integrity]]
- [[niches/ai-model-evaluation-firms/evaluation-platforms/profile|🔵 Evaluation Platforms]]
  - [[niches/ai-model-evaluation-firms/frontier-lab-assurance/profile|🎯 Frontier Lab Assurance]]
  - [[niches/ai-model-evaluation-firms/application-regression-harnesses/profile|🎯 Application Regression Harnesses]]
- [[niches/ai-model-evaluation-firms/domain-grading-criteria/profile|🟠 Domain Grading Criteria]]
- [[niches/ai-model-evaluation-firms/human-preference-operations/profile|🟠 Human Preference Operations]]
- [[niches/ai-model-evaluation-firms/the-expert-rater/profile|🟣 The Expert Rater]]
- [[niches/ai-model-evaluation-firms/the-evaluation-engineer/profile|🟣 The Evaluation Engineer]]
- [[niches/ai-model-evaluation-firms/judge-model-validity/profile|⚡ Judge Model Validity]]
- [[niches/ai-model-evaluation-firms/graded-item-corpus/profile|⚡ Graded Item Corpus]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Evaluation Platforms** is not: it names the shape of the product rather than the contest, and the two businesses inside it are barely related. Frontier lab assurance is won on finding what the lab's own evaluation team did not, is bought by a handful of organisations under strict confidentiality, and competes against the lab's internal capability. Application regression harnesses are won on catching a regression in a product team's own task inside a build pipeline, are bought by thousands of engineering teams, and compete against a spreadsheet of test prompts and a person's judgement. Different buyers, different cadence, different alternatives, different definition of success. Decomposed into two contested sub-niches.

Two candidates were rejected. *Red teaming and adversarial safety evaluation* was rejected because its contest — finding harmful capability under adversarial pressure — belongs to the AI red teaming industry covered separately in this vault. *Production tracing and observability for model applications* was rejected because it belongs to LLM application tooling, also covered separately, and restating it here would duplicate it.
