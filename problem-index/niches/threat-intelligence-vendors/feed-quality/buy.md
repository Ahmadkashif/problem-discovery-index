# Buy: Diagnostic Test Evaluation, Applied to Feeds

**Niche:** Feed Quality Measurement
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medicine evaluates diagnostic tests with sensitivity, specificity and predictive value against a defined prevalence, and threat intelligence reports how many indicators it ships.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #probability-distributions #logistic-regression #descriptive-statistics
**Contested on:** Whether a feed's value can be stated as a number, or remains a matter of collection breadth and analyst reputation.

## The Problem

Evaluating a test that flags a condition is a solved discipline. Medicine developed it because tests that flag too readily and tests that miss cause different harms, and both needed quantifying.

The apparatus is precise. Sensitivity is the proportion of true cases the test catches. Specificity is the proportion of non-cases it correctly passes. Positive predictive value — the probability that a positive result is real — depends on both and on prevalence, which is why a highly specific test still produces mostly false positives when the condition is rare. Test evaluation studies are designed against a reference standard and reported to established standards.

A threat intelligence feed is a diagnostic test. It flags traffic as associated with malicious activity. The base rate of genuinely malicious traffic in an enterprise network is very low, which is exactly the regime where predictive value collapses even for a specific test — and it is precisely the phenomenon the SOC analyst experiences as a queue of false positives.

The category reports indicator counts.

## What Already Exists

Diagnostic evaluation: sensitivity, specificity, predictive values, likelihood ratios, ROC analysis, and reporting standards for diagnostic accuracy studies. The literature on how prevalence drives predictive value is extensive and directly applicable.

Machine learning evaluation: precision, recall, precision-recall curves for imbalanced problems, calibration assessment — the same mathematics in a different vocabulary, and one security engineers already speak.

Screening programme evaluation: the framework for assessing whether a detection programme does more good than harm at population scale, including the costs of false positives, which maps closely onto alert fatigue.

Security-adjacent: detection engineering practice, which has begun using precision and recall for detection rules; and the academic threat intelligence evaluation literature, which has measured feed overlap and disagreement and is largely unread commercially.

## The Customization Gap

**The reference standard is the missing piece.** Diagnostic studies have a gold standard. Threat intelligence has adjudicated incidents, which are scarce, inconsistent and contested — which is why precision is the hard half and match rate is the tractable one.

**Prevalence is the insight nobody has applied.** The base rate of malicious traffic is extremely low, so even a specific indicator produces mostly false positives. Stating this explicitly, with the arithmetic, would reframe the alert fatigue conversation entirely and is a standard result in screening evaluation.

**Sensitivity is unmeasurable directly.** Nobody knows the denominator of attacks that occurred, so recall cannot be computed. Proxies exist — coverage of known campaigns, comparison against other feeds — and need to be stated as proxies.

**Evaluation must be per-context, not global.** A diagnostic test's predictive value varies by population. A feed's varies by sector, stack and geography, and reporting a single figure would repeat the mistake medicine corrected decades ago.

**Reporting standards do not exist here.** Medicine has structured reporting requirements for diagnostic accuracy studies. A comparable standard for feed evaluation would make vendor claims comparable and is the kind of artefact an independent body could produce.

**Harm from false positives is real and uncounted.** Screening evaluation counts the cost of false positives explicitly. In security that cost is analyst time and occasionally a blocked legitimate connection, and it appears in no vendor's reporting.

## Target Customer

Independent evaluators and research bodies, who could publish a feed evaluation standard and comparative studies — the role that diagnostic accuracy reporting standards play in medicine.

Vendors with telemetry, for whom applying the framework to their own feed and publishing first establishes the metric.

Security operations leadership, who could apply the prevalence arithmetic to their own alert volumes today and would find it explains their analysts' experience precisely.

## Impact If Solved

A mature evaluation discipline reaches a field that has been selling a diagnostic test without reporting its accuracy.

The prevalence argument alone would change how alert volumes are understood: analysts drowning in false positives are experiencing a predictable consequence of low base rates, not a vendor failure, and the remedy follows from the arithmetic.

And a reporting standard for feed evaluation would make vendor claims comparable, which is the mechanism by which diagnostic test claims became comparable and the market began rewarding accuracy.
