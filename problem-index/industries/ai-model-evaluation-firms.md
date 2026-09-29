# AI Model Evaluation Firms

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$800M US model evaluation, benchmarking and assurance, growing quickly from a small base
**Tech Maturity:** Rapidly maturing tooling on a foundation that is quietly broken — LMSYS Chatbot Arena, Stanford's HELM, Scale's evaluation arm, Patronus, Braintrust, Galileo and Vals AI have built real infrastructure. The measurements they produce are increasingly untrustworthy for a reason nobody has solved: the models being evaluated may have seen the benchmarks.
**Workforce:** Evaluation engineers, benchmark designers, domain expert raters, human preference operations staff, research scientists, report writers

## Key Pain Themes
Benchmark contamination is the field's structural crisis. Public benchmarks are in the training corpora of the models they measure, and the extent is unknowable because training data is undisclosed. Every published score is therefore an upper bound of unknown looseness, and the field's response — private held-out sets, dynamic generation, adversarial variants — buys time rather than solving the problem. Underneath sit two operational burdens: constructing domain-specific evaluation harnesses, where generic frameworks handle the mechanics and the actual grading criteria for a specialised task must be authored from scratch; and human preference collection, where the infrastructure exists and rater quality determines the result and is measured badly. Evaluation engineers spend their time chasing flaky automated graders, and the domain experts doing the rating are exposed to a job that is more cognitively demanding and worse paid than the industry admits.

## Current Tech Landscape
LMSYS Chatbot Arena has become the de facto public leaderboard through pairwise human preference at scale, with its own well-documented biases toward style and length. HELM and the academic benchmark ecosystem provide breadth and are heavily contaminated. LLM-as-judge has become the dominant automated grading method and inherits the judge model's own biases, including a measurable preference for outputs resembling its own. Evaluation platforms (Braintrust, Langfuse, Patronus, Galileo) provide harnesses, tracing and regression testing for application teams. Private evaluation contracts with frontier labs are the largest revenue pool and the least visible part of the market.

## Problems
- [[problems/ai-model-evaluation-firms/high-impact|🔴 High Impact: Benchmark Contamination and Measurement Validity]]
- [[problems/ai-model-evaluation-firms/low-impact-1|🟡 Low Impact: Domain-Specific Grading Criteria]]
- [[problems/ai-model-evaluation-firms/low-impact-2|🟡 Low Impact: Human Preference Collection Quality]]
- [[problems/ai-model-evaluation-firms/worker-life-1|🟢 Worker Life: Evaluation Engineer Chasing Flaky Graders]]
- [[problems/ai-model-evaluation-firms/worker-life-2|🟢 Worker Life: Domain Expert Rater]]
- [[problems/ai-model-evaluation-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ai-model-evaluation-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry exists to produce trustworthy numbers about systems whose training data is undisclosed, using benchmarks that may be inside it, graded by models with their own biases, or by humans whose reliability is estimated with methods that assume a knowable answer. Every layer of the measurement stack has a validity problem, and the field's own literature documents them clearly while the commercial practice largely proceeds as though they were solved. The firms hold the raw material to do better — millions of graded items with judge, rater, model and prompt attached — and the incentive to publish uncomfortable findings about measurement is weak in a market where customers are buying reassurance.
