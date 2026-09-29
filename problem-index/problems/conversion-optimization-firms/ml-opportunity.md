# Machine Learning Opportunities — Conversion Optimization Firms

**Industry:** [[conversion-optimization-firms|Conversion Optimization Firms]]
**Derived from:** [[problems/conversion-optimization-firms/high-impact|High Impact]], [[problems/conversion-optimization-firms/low-impact-1|Low Impact 1]], [[problems/conversion-optimization-firms/low-impact-2|Low Impact 2]], [[problems/conversion-optimization-firms/worker-life-1|Worker Life 1]], [[problems/conversion-optimization-firms/worker-life-2|Worker Life 2]]

---

## 1. Programme Validation Against a Permanent Holdback
#hypothesis-testing #causal-inference #confidence-intervals #bayesian-inference #monte-carlo-methods #probability-distributions #evaluation-metrics #revenue-impact

**Problem statement:** A year of reported uplifts, if real, would transform a site's conversion rate, and it does not move. The gap comes from underpowered tests, early stopping, post-hoc segmentation and the winner's curse — all standard practice — and nobody makes the comparison that would reveal it.

**ML task:** Maintain a permanent randomised holdback that never receives implemented winners, and compare the accumulated real programme effect against the sum of reported uplifts; separately, estimate the shrinkage correction for winner's curse
**Input data:** Holdback assignment and outcomes over the full period; every test's design, reported uplift, power, stopping rule and segment claims; implementation dates; baseline conversion trends and seasonality.
**Target:** The programme's actual cumulative effect on conversion, measured against the holdback.
**Evaluation metric:** The headline is the ratio of measured programme effect to reported cumulative uplift, with an interval. Expect it to be well below one and report it rather than pooling until it looks acceptable. Per-test shrinkage estimates should be validated by whether corrected predictions match the holdback-measured effect better than raw ones, which is a clean and decisive test.
**Scope:** This requires no new technique and could start tomorrow; the cost is a small amount of conversion on the holdback and the willingness to see the answer. A year of data is needed before anything can be said, which is why starting is the whole decision. 1 data scientist, 3 months to instrument, 12 months to conclude.
**Data availability:** Fully available to any firm running a programme. This is the rare case in this cluster where the evidence is not on the other side of a wall — it is simply not collected because the answer is unwelcome.

---

## 2. Power-Aware Test Planning and Sequential Analysis
#hypothesis-testing #confidence-intervals #probability-distributions #monte-carlo-methods #bayesian-inference #evaluation-metrics #time-series-forecasting #revenue-impact

**Problem statement:** Tests run on traffic that cannot detect the effects being claimed, are monitored continuously and stopped when significance appears, and are segmented after the fact until something is significant — each of which inflates false positives, and they are routinely combined.

**ML task:** Compute minimum detectable effect and required duration before launch from the page's own traffic and variance, implement valid sequential testing with pre-committed stopping rules, and enforce pre-registered segments
**Input data:** Historical traffic and conversion variance per page and segment; seasonality and weekday structure; the hypothesis and its plausible effect magnitude bounded by the prevalence of the behaviour it addresses; test configuration and declared segments.
**Target:** Whether a test as designed can detect an effect of the magnitude claimed, and a valid decision under continuous monitoring.
**Evaluation metric:** Simulation is the right instrument: generate data under a known null and under known effects, run the proposed procedure, and measure the realised false positive rate and power. That will demonstrate concretely how much the current workflow inflates error rates, which is more persuasive to a practitioner than an argument. Report the proportion of a firm's historical tests that were adequately powered — a number likely to be small and worth confronting.
**Scope:** The valuable output is refusal: declining tests whose traffic cannot support them redirects capacity to changes large enough to detect, which is a smaller and real programme. Sequential methods are available in several platforms and the practice has not followed the tooling. 1 data scientist, 3-4 months.
**Data availability:** Complete — traffic and variance history is exactly what testing platforms already hold.

---

## 3. Prevalence-Weighted Hypothesis Generation
#k-means-clustering #dbscan #gradient-boosting #graph-neural-networks #dimensionality-reduction #evaluation-metrics #feature-engineering #bert

**Problem statement:** Session recordings supply unlimited observations and no basis for judging which describe a mechanism affecting enough users to matter, so scarce test slots are allocated by how compelling a recording felt.

**ML task:** Cluster sessions by friction signature into recurring behavioural patterns, quantify each pattern's prevalence and its association with conversion, and bound the maximum achievable effect of addressing it
**Input data:** Event streams and session replays; friction signals — rage clicks, dead clicks, repeated interactions, form abandonment, error encounters; funnel position and subsequent conversion; device, browser and traffic source; historical test results linked to the patterns they addressed.
**Target:** Pattern prevalence and the conversion differential between affected and unaffected users, as an upper bound on achievable effect.
**Evaluation metric:** The operational test is whether tests prioritised by prevalence-bounded effect outperform those prioritised by subjective frameworks, measured on realised effect and on the proportion reaching adequate power. The conversion differential is correlational and must not be presented as the expected uplift — users who exhibit a friction behaviour differ from those who do not in ways beyond the friction, and stating the bound rather than the estimate is the honest framing.
**Scope:** Friction signatures must be calibrated per site against its own conversion outcomes, since a rage click on one interface is frustration and on another is a known quirk. The comparison of prevalence-bounded effect against minimum detectable effect is what eliminates most of a backlog before a slot is spent. 1-2 engineers, 4-6 months.
**Data availability:** Excellent — behavioural tooling is widely deployed and its data is used for watching sessions rather than for quantifying populations.

---

## 4. Variant Integrity Monitoring in Production
#change-point-detection #gradient-boosting #cnns #hypothesis-testing #confidence-intervals #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Client-side variants break when the underlying site changes, flicker differentially, and silently drop tracking events — producing measured differences that have nothing to do with the hypothesis and contaminating results the statistics then sit on top of.

**ML task:** Monitor running variants for rendering correctness across the site's actual device and browser mix, detect sample ratio mismatch and per-arm event rate deviations, and predict selector fragility before launch
**Input data:** Rendered captures across device and browser configurations weighted by the site's traffic mix; per-arm assignment counts, event firing rates and rendering timings; JavaScript error rates by configuration; variant code with its selector bindings; the client's deployment events where visible.
**Target:** Whether a running variant is rendering and tracking correctly, and whether a result is contaminated by implementation artefact.
**Evaluation metric:** Detection lead time on historical breakages against when they were actually noticed, which is typically days or the end of the test. Sample ratio mismatch detection is a simple, decisive check with a known distribution and should be treated as a hard gate rather than a warning — a test with a significant ratio mismatch is uninterpretable and should stop. For fragility prediction, precision on flagged selectors against subsequent breakage.
**Scope:** Automatic stopping on integrity failure is the design that matters; a warning that a variant may be broken, delivered to a busy strategist, gets deferred. Quality signals should be reported alongside every result so anyone reading it can judge whether to believe it. 2 engineers, 4-6 months.
**Data availability:** Assignment and event data are in the testing platform; cross-configuration rendering requires a capture harness, which is the main build.
