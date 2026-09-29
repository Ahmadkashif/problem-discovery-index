# Machine Learning Opportunities — AI Agent Platforms

**Industry:** [[ai-agent-platforms|AI Agent Platforms]]
**Derived from:** [[problems/ai-agent-platforms/high-impact|High Impact]], [[problems/ai-agent-platforms/low-impact-1|Low Impact 1]], [[problems/ai-agent-platforms/low-impact-2|Low Impact 2]], [[problems/ai-agent-platforms/worker-life-1|Worker Life 1]], [[problems/ai-agent-platforms/worker-life-2|Worker Life 2]]

---

## 1. Per-Task Success Prediction and Trajectory Anomaly Detection
#gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #large-language-models #change-point-detection #revenue-impact

**Problem statement:** Customers cannot be told in advance what fraction of tasks an agent will complete correctly or which ones it will fail. Deployments proceed as pilots with review policies relaxed by accumulated comfort rather than by measurement, and failures cluster on input characteristics discoverable only in production.

**ML task:** Binary success prediction per task from request features and agent history, plus in-flight anomaly detection over the executing trajectory
**Input data:** Request text and structured attributes; the agent's historical outcomes on similar requests; trajectory features as execution proceeds — tool sequence, retry counts, state transitions, latency, model confidence where exposed; downstream signals including human correction, customer return contact and contradicting subsequent requests; explicit outcome labels where human review occurred.
**Target:** Task success as determined by human review where available, and inferred from downstream signals otherwise.
**Evaluation metric:** Precision at the review threshold is the operative number, since the deployment use is routing a fixed human review budget to the most likely failures — report failures caught per hundred tasks reviewed against random sampling, which is the honest baseline. Calibration matters because the same score drives authorisation decisions.
**Scope:** Downstream signals are the unlock, because they are free and arrive continuously while human review labels are expensive and sparse — validating that these weak labels correlate with true outcomes on a small human-reviewed anchor is the first task. In-flight anomaly detection is where intervention is still cheap and is a different model from pre-execution prediction. Non-determinism means the same input can succeed and fail, so the target is a probability rather than a property of the request. 3 ML engineers, 6 months.
**Data availability:** Trajectories are captured completely by every platform. Outcome labels are the scarce resource — human review covers a small fraction, and downstream signals require joining to the customer's own systems, which is the integration most deployments skip.

---

## 2. Production Failure Clustering and Cross-Customer Pattern Transfer
#k-means-clustering #dbscan #bert #word-embeddings #large-language-models #evaluation-metrics #hypothesis-testing #transfer-learning

**Problem statement:** Forward-deployed engineers triage failures individually and patch each with a specific instruction, producing prompt sets that grow for a year into something nobody can reason about. The same edge cases recur across customers in a vertical and nothing accumulates.

**ML task:** Semantic clustering of failed trajectories by root cause, with matching against a library of known failure patterns and their remediations
**Input data:** Failed trajectories with request, tool calls, state and outcome; engineer diagnoses and applied fixes; instruction set versions over time; customer vertical and configuration; failure patterns and remediations across the vendor's whole customer base.
**Target:** Root cause cluster per failure, and a matched known pattern with its remediation where one exists.
**Evaluation metric:** Cluster purity judged by forward-deployed engineers on a sample, and the proportion of new failures matched to an existing known pattern — which is the number that measures whether the library is accumulating value. Time from failure to diagnosis against the current manual baseline.
**Scope:** Instruction set ablation is a separate and immediately useful analysis: replaying historical tasks with individual instructions removed identifies which are load-bearing, which are dead and which conflict, and it is the only way to prune a prompt that has grown for a year. Cross-customer transfer requires contractual permission and is the vendor's clearest path from services margins to software margins. 2 ML engineers plus a forward-deployed engineer, 5 months.
**Data availability:** Trajectories and instruction versions are captured. Engineer diagnoses are recorded in tickets and commit messages inconsistently and are the labels this needs, so structuring diagnosis capture is the prerequisite.

---

## 3. Risk-Based Action Authorisation
#gradient-boosting #logistic-regression #confidence-intervals #markov-decision-processes #evaluation-metrics #hypothesis-testing #compliance

**Problem statement:** Approval gates are placed by intuition at the level of an action type with a threshold someone guessed, and never revisited against measured reliability. Too tight reproduces the cost the agent was meant to remove and produces rubber-stamping; too loose produces the incident that suspends the deployment.

**ML task:** Expected-cost routing — combining predicted failure probability with action cost and reversibility to decide per task whether human approval is required
**Input data:** Predicted task failure probability; action type, magnitude and reversibility classification; historical approval decisions with reviewer, latency and outcome; realised cost of past failures; reviewer rejection rates and whether rejections correlated with genuinely bad actions.
**Target:** The routing decision that minimises expected cost, and separately, whether a given human approval was meaningful.
**Evaluation metric:** Failures prevented per approval requested — the efficiency of the human attention being spent — against the current static threshold policy. Report reviewer behaviour separately: approval latency distributions and rejection rates, since a reviewer approving everything in two seconds provides the appearance of safety without the substance, and measuring that is uncomfortable and necessary.
**Scope:** Reversibility classification is the input the category has barely represented and is the variable that should dominate the decision — an irreversible cheap action deserves more scrutiny than a reversible expensive one. This is a policy-sensitive system and the routing rule should be inspectable and adjustable by the customer rather than learned end to end, since the trade-off between automation and risk is theirs to set. 2 ML engineers plus a risk specialist, 4-5 months.
**Data availability:** Approval decisions and outcomes are logged. Realised failure costs are rarely recorded and are needed to make the expected-cost calculation real rather than notional.

---

## 4. Connector Generation and Tool Description Optimisation
#large-language-models #transformers #evaluation-metrics #transfer-learning #hypothesis-testing #confidence-intervals #data-integration #automation

**Problem statement:** Every deployment stalls on integrations to the customer's own systems, built by forward-deployed engineers repeatedly with per-customer variations. Separately, an agent's ability to use a tool correctly depends heavily on how the tool is described, and descriptions are written as an afterthought by engineers with no measurement of which ones work.

**ML task:** Generating connector implementations and tool descriptions from API specifications and instance schemas, plus measuring tool selection accuracy attributable to description quality
**Input data:** OpenAPI specifications and API documentation; customer instance schemas including custom fields and objects; the vendor's corpus of prior connectors across customers; trajectory data showing tool selection decisions and their correctness; historical tool descriptions with their measured selection accuracy.
**Target:** A working connector with tool descriptions, and the selection accuracy achieved by a given description.
**Evaluation metric:** For connectors, the proportion accepted without engineer modification and the reduction in integration days per deployment. For descriptions, tool selection accuracy measured on held-out trajectories — a direct A/B comparison between description variants, which is easy to run and which nobody runs, meaning a systematic source of agent failure is currently attributed to model limitations.
**Scope:** Tool description quality is the underappreciated half and the cheaper one: it requires no code generation, just systematic measurement of which descriptions produce correct selection, and the trajectory data to measure it already exists. Connector breakage detection is a third piece — integration failures surface as agent failures and are debugged in the wrong place entirely. 2 ML engineers, 4 months.
**Data availability:** Prior connectors sit in the vendor's codebase and are a strong corpus. Trajectory data linking tool descriptions to selection outcomes is complete and unanalysed.
