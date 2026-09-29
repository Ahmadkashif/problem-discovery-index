# Machine Learning Opportunities — LLM Application Tooling

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Derived from:** [[problems/llm-application-tooling/high-impact|High Impact]], [[problems/llm-application-tooling/low-impact-1|Low Impact 1]], [[problems/llm-application-tooling/low-impact-2|Low Impact 2]], [[problems/llm-application-tooling/worker-life-1|Worker Life 1]], [[problems/llm-application-tooling/worker-life-2|Worker Life 2]]

---

## 1. Production-Replay Regression Evaluation
#hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #transformers #descriptive-statistics #revenue-impact

**Problem statement:** A prompt edit to fix one case changes behaviour across the entire input distribution and there is no regression test. Teams maintain twenty curated cases, see three differences, and cannot distinguish a real regression from sampling noise — so quality moves in both directions invisibly and prompts accumulate instructions nobody can evaluate.

**ML task:** Pairwise comparison of outputs under old and new configurations across replayed production inputs, with power analysis determining the sample required
**Input data:** Historical production requests with full context — retrieved documents, memory state, tool availability, configuration; outputs under each configuration version; human or judge pairwise preferences on a subset; downstream user signals where available.
**Target:** The direction and magnitude of quality change between configuration versions across the real input distribution.
**Evaluation metric:** Interval coverage on the estimated effect, and the minimum detectable regression at a given sample size — which is the number teams most need and never compute. Report the null result honestly as "no evidence of change greater than X per cent" rather than as "no change," since the current practice conflates the two and is the reason regressions ship.
**Scope:** Pairwise comparison rather than absolute scoring is the design choice that makes this work, because relative judgement is far easier and more stable for both judges and humans. Replaying production inputs removes the need for a curated reference set entirely and tests the distribution that actually matters. Judge instability must be measured and subtracted, since a judge that disagrees with itself across runs sets the noise floor. 2-3 ML engineers, 5 months.
**Data availability:** Traces with full context are captured where instrumentation is complete, which is the constraint — replaying requires the retrieval results and memory state, which are exactly the fields most commonly missing.

---

## 2. Baseline Drift Detection Against Provider Model Changes
#change-point-detection #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #large-language-models #time-series-forecasting

**Problem statement:** Provider models change, sometimes without announcement, and application behaviour shifts with no change on the team's side. This is the most common invisible cause of quality regressions and there is no stable baseline anywhere to detect it against.

**ML task:** Change point detection on a fixed evaluation set run continuously against fixed configurations, with attribution separating provider changes from application changes and traffic mix shifts
**Input data:** A fixed input set executed on a schedule against pinned configurations; output characteristics including length, structure, refusal rate, formatting and judge scores; provider model version identifiers where exposed; the application's own change log; production traffic mix over time.
**Target:** A detected behavioural change in the underlying model, distinguished from application changes and mix shifts.
**Evaluation metric:** Detection lead time relative to the point where users complained or a business metric moved — the operational benchmark. False positive rate matters because model outputs vary run to run by design, so the detector must be tuned against the natural variation of a pinned configuration, which is directly measurable by simply running it repeatedly.
**Scope:** The baseline is cheap — a few hundred fixed inputs run daily — and almost nobody maintains one, which means every regression investigation starts without the one control that would resolve it. Traffic mix decomposition is a separate and equally neglected piece: a quality metric moving because questions got harder is a different finding from the system getting worse, and it is the first thing an engineer should be able to check. 2 ML engineers, 3-4 months.
**Data availability:** Entirely within the team's control, since the baseline is generated deliberately. Provider version identifiers are inconsistently exposed, which is why behavioural detection is necessary rather than optional.

---

## 3. Request Difficulty Prediction for Model Routing
#gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #optimization-fundamentals #hypothesis-testing #bert

**Problem statement:** Applications use one model for everything, chosen against the hardest case and paid for on every request, because routing requires knowing which requests are easy and no tool predicts it. Model capability and price span more than an order of magnitude and the easy majority is subsidising the hard minority.

**ML task:** Predicting whether a cheaper model would produce an equivalent answer for a given request, with the quality-cost frontier characterised
**Input data:** Historical production requests with outputs from the expensive model; offline re-execution of the same requests against cheaper models; pairwise equivalence judgements between the two outputs; request features including length, task type, context size and retrieved content; downstream user signals.
**Target:** Whether the cheaper model's output is equivalent in quality for this request.
**Evaluation metric:** The cost-quality frontier — realised spend against measured quality across routing thresholds — is the deliverable, since the team's decision is where to sit on it. Report the quality loss at each cost saving level with intervals, and evaluate the routing policy on held-out traffic rather than on the data used to build it, since difficulty prediction overfits easily.
**Scope:** The offline comparison is what makes this safe and is entirely available: historical requests can be re-run against cheaper models at leisure, with no production risk, producing a labelled dataset of where the cheap model suffices. Semantic cache safety is the adjacent question and is measured the same way — serving cached and fresh responses to comparable requests and comparing. Fallback path quality should be characterised by the same method, since teams configure fallback without ever measuring what it produces. 2 ML engineers, 4 months.
**Data availability:** Production request history is complete in the tracing layer. Offline re-execution costs money but is bounded and one-off, which makes this unusually easy to bootstrap.

---

## 4. Prompt Library Analysis and Instruction Ablation
#bert #word-embeddings #k-means-clustering #large-language-models #evaluation-metrics #hypothesis-testing #workflow-orchestration

**Problem statement:** Prompt libraries grow to hundreds of overlapping templates that nobody can safely delete, containing accumulated instructions that contradict each other and cannot be reasoned about. The maintainer becomes a bottleneck and the only documentation.

**ML task:** Usage attribution from traces, semantic duplicate detection over prompt text, and instruction-level ablation to measure what each line actually does
**Input data:** The prompt registry and prompts embedded in code and configuration; production traces showing which prompts executed and how often; prompt version history; historical inputs for replay; instruction addition history with linked issues where recorded.
**Target:** Per-prompt usage frequency and call sites; near-duplicate groupings; and per-instruction behavioural effect measured by ablation.
**Evaluation metric:** For ablation, the measured behavioural difference when an instruction is removed, replayed across production inputs — an instruction with no detectable effect is dead and can be removed, which is the actionable output. For duplicate detection, precision on proposed merges validated by behavioural equivalence testing rather than by text similarity alone, since two similar prompts can behave differently.
**Scope:** Usage tracking requires no learning and delivers most of the value, because it is what makes deletion safe and the library only grows today for lack of it. Ablation is the genuinely useful modelling contribution: it turns an unreadable forty-line prompt into a set of measured components and identifies contradictions directly. Provenance capture — recording why an instruction was added, linked to the failure that prompted it — is a small workflow change with disproportionate long-term effect. 2 ML engineers, 4 months.
**Data availability:** Traces and prompt versions are captured. The link between an instruction and the failure it was added for almost never exists and is the piece worth instrumenting going forward.
