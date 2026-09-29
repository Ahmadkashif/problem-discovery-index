# Machine Learning Opportunities — QA & Test Automation Vendors

**Industry:** [[qa-test-automation-vendors|QA & Test Automation Vendors]]
**Derived from:** [[problems/qa-test-automation-vendors/high-impact|High Impact]], [[problems/qa-test-automation-vendors/low-impact-1|Low Impact 1]], [[problems/qa-test-automation-vendors/low-impact-2|Low Impact 2]], [[problems/qa-test-automation-vendors/worker-life-1|Worker Life 1]], [[problems/qa-test-automation-vendors/worker-life-2|Worker Life 2]]

---

## 1. Cosmetic Versus Behavioural Change Classification
#bert #gradient-boosting #graph-theory #large-language-models #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics

**Problem statement:** Tests break because structure changed while behaviour did not, and self-healing repairs the binding without asking whether behaviour changed — which means a test can heal its way past a genuine regression and report success it has not verified. Nobody measures how often that happens.

**ML task:** Binary classification of an application change as cosmetic or behavioural, conditioned on the failing test's intent, gating any automatic repair
**Input data:** The application diff; before-and-after rendered output including DOM structure and visual representation; the failing test's assertions and interaction sequence; semantic roles and accessibility attributes of affected elements; historical repairs with whether the repaired test subsequently caught a real defect; production incidents linked to changes.
**Target:** Whether the change altered user-observable behaviour, established from developer intent, subsequent incidents and manual adjudication on a sample.
**Evaluation metric:** The critical number is the rate at which the classifier labels a behavioural change as cosmetic, because that is the case where healing masks a regression — it should be reported as its own class and be very close to zero, with the system failing loudly whenever confidence is short. Overall accuracy is a distraction; the asymmetric error is the entire product.
**Scope:** Semantic roles and accessibility attributes are far more stable than class names or DOM position and are the natural anchor for a behaviour-oriented binding. Visual comparison contributes strongly and is noisy for legitimate redesigns. The honest framing is that healing should be rare and audited rather than routine and invisible, which is the opposite of how the feature is currently marketed. 3 ML engineers, 6 months.
**Data availability:** Vendors observe changes, failures and repairs across many applications. The label — did behaviour actually change — requires adjudication and does not exist as a corpus, which is the main obstacle.

---

## 2. Failure Triage Classification
#gradient-boosting #bert #logistic-regression #k-nearest-neighbors #confidence-intervals #cross-validation #evaluation-metrics #worker-facing

**Problem statement:** A developer or test engineer facing forty overnight failures must determine, for each, whether it is a real defect, a flaky test, a break from their own change, or a break from someone else's. The triage is the slow part and the failure output supplies neither test intent nor change context.

**ML task:** Multiclass classification of test failure cause from failure output, the change under test, and the test's own history
**Input data:** Failure messages, stack traces and screenshots; the diff under test and its file paths; the test's historical pass and fail pattern; concurrent changes from other authors; flakiness statistics; environment and runner conditions; subsequent resolution — a fix, a re-run, a test repair.
**Target:** The cause as ultimately established by whoever resolved the failure.
**Evaluation metric:** Accuracy per class, with real-defect recall weighted most heavily, since misclassifying a genuine regression as flaky is exactly the failure that lets defects ship. Report the reduction in triage time against the manual baseline, which is the metric the engineer experiences.
**Scope:** Flakiness history is the strongest single feature and is available from execution records. Attribution between the current change and a concurrent one requires reasoning about which files the test exercises, which connects to test relevance modelling. This is one of the most immediately deliverable items in the category because the labels — what someone did next — are recorded automatically. 2 ML engineers, 4 months.
**Data availability:** Excellent. Execution history, diffs and resolutions are all captured by CI and test platforms and are rarely joined.

---

## 3. Risk-Weighted Coverage and Selective Mutation
#graph-theory #gradient-boosting #hypothesis-testing #confidence-intervals #k-means-clustering #evaluation-metrics #feature-engineering

**Problem statement:** Coverage measures lines executed, not behaviours verified, and is uniform where risk is not. Mutation testing measures the right thing and is too slow to run exhaustively, so the industry reports a number everyone knows is close to meaningless.

**ML task:** Risk scoring per code region from incident history, change frequency and business path value; and selection of mutation targets to make mutation testing affordable
**Input data:** Coverage data at line and branch level; production incident history linked to code regions; change frequency and churn; user path analytics indicating business value; code complexity metrics; test assertions and their targets; historical mutation results where available.
**Target:** Code regions that subsequently produced production defects, as the risk label; and for mutation, whether a mutant survives.
**Evaluation metric:** For risk weighting, whether the prioritised gap list actually precedes the defects that occur — evaluated forward in time rather than fitted retrospectively. For selective mutation, defect-detection equivalence against exhaustive mutation at a fraction of the compute, which is the number that makes the technique adoptable.
**Scope:** Incident-to-code linkage is the essential join and is inconsistently maintained in most organisations, which is the practical blocker. Assertion quality analysis — detecting tests that execute a path and verify nothing meaningful — is a separable, cheap and revealing analysis nobody offers. Selective mutation targeting only the highest-risk regions is what converts a good technique from impractical to routine. 2 ML engineers, 5 months.
**Data availability:** Coverage is universal. Incident linkage is weak. Business path analytics live in product analytics tools and are never joined to code.

---

## 4. Minimum Covering Matrix from Failure Correlation
#k-means-clustering #dimensionality-reduction #hypothesis-testing #optimization-fundamentals #gradient-boosting #confidence-intervals #evaluation-metrics

**Problem statement:** The browser and device matrix multiplies every test run in time and cost and is chosen by convention. Nobody knows which combinations have ever produced a distinct failure, though the vendor observes exactly that across thousands of customers.

**ML task:** Estimation of failure correlation structure across environment combinations, followed by a set-cover optimisation for the minimum matrix preserving historical detection
**Input data:** Test execution results across browser, version, operating system and device combinations at fleet scale; failure co-occurrence patterns; application characteristics and rendering technology; customer real user analytics on actual environment distribution; the diff under test.
**Target:** Distinct failures — defects caught by one combination and not by others.
**Evaluation metric:** Historical detection preservation: of the distinct failures observed across the full matrix, what proportion would the reduced matrix have caught, at what proportion of the cost. Report it as a curve so a customer chooses their own point rather than accepting a recommendation.
**Scope:** Fleet-scale correlation is the vendor's unique asset — a single customer rarely has enough distinct failures to estimate it. Weighting by the customer's own real user distribution rather than by global browser statistics is the second half and matters because the populations differ. Risk-based matrix selection per change, broad for rendering changes and narrow for logic that cannot differ, is a straightforward extension. 2 ML engineers, 4 months.
**Data availability:** Grid vendors hold enormous execution histories across combinations. Whether a failure was genuinely environment-specific rather than flaky requires the triage classifier as a prerequisite.
