# Buy: Cost-Sensitive Learning and Model Monitoring

**Niche:** Threshold Optimisation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning operations solved distribution drift monitoring and threshold recalibration as standard practice, and moderation thresholds are set once and left.
**Tags:** #change-point-detection #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #convex-optimization #automation #data-integration
**Contested on:** Whether the operating point is computed from the score distribution and the stated costs, and maintained as both drift.

## The Problem

Detecting that a model's input or output distribution has shifted, and that its calibration or operating point needs revisiting, is standard machine learning operations practice.

Drift detection compares the current distribution against a reference and alerts when it moves. Calibration monitoring checks whether predicted probabilities still correspond to observed frequencies. Threshold recalibration on model update is a documented step in deployment practice. Shadow deployment runs a new model alongside the old to compare before switching. And cost-sensitive learning handles the optimisation of a decision threshold given asymmetric error costs, with an established literature.

Trust and safety classification is a production machine learning system with unusually high consequences, deployed by vendors who are machine learning organisations, and the operating point is treated as a customer configuration value that nobody monitors.

The tooling is standard, the practice is documented, and the gap is that the threshold was framed as configuration rather than as part of the model's deployment.

## What Already Exists

Model monitoring: Evidently, Arize, Fiddler, WhyLabs and the monitoring features in the ML platforms, with drift detection, calibration monitoring and performance tracking.

MLOps deployment practice: shadow deployment, canary releases, threshold recalibration as a release step, and rollback on degradation.

Cost-sensitive learning: the literature and implementations for optimising a decision threshold under asymmetric costs, entirely standard.

Calibration methods: Platt scaling, isotonic regression and the apparatus for making scores correspond to probabilities, which is what makes a threshold interpretable.

Trust and safety products: scores, configurable thresholds, and periodic model updates.

## The Customization Gap

**The threshold sits on the wrong side of the product boundary.** MLOps treats the decision threshold as part of the deployed system. These products treat it as customer configuration, which is why it is outside the monitoring.

**Model updates do not recalibrate.** Standard practice recalibrates on release. Here a model is updated and the customer's threshold is carried over, which can move the operating point substantially and is not flagged.

**Calibration is rarely established.** A score that is not calibrated is not a probability, which makes cost-based threshold optimisation impossible and makes the score's meaning unclear to the customer setting a threshold on it.

**Outcome labels are scarce.** Monitoring performance needs labels, which in moderation means reviewed outcomes — available in small volumes from the review queue and rarely fed back as monitoring data.

**Drift is per-customer.** The vendor monitors their own test set; the drift that matters is in each customer's content distribution, which requires per-customer monitoring the vendor may not have visibility into.

**Automatic adjustment is riskier here.** Moving a moderation threshold automatically has consequences that moving a recommendation threshold does not, which argues for recommend-and-approve rather than for automation.

## Target Customer

The vendors themselves, who are machine learning organisations applying MLOps practice to their models and not to the decision threshold their customers operate.

Model monitoring vendors, for whom per-customer operating point monitoring in a high-consequence deployment is an adjacent application.

Platform machine learning teams, who frequently run monitoring for their own models and have not extended it to the vendor-supplied classifiers they depend on.

## Impact If Solved

Standard MLOps practice applies directly and has not been applied because the threshold was framed as configuration rather than as part of the deployed system.

Recalibrating on model update is a documented release step whose absence here is the largest silent failure in the category.

And establishing score calibration properly would make the threshold interpretable to the customer setting it — currently they are choosing a number on a scale whose meaning nobody has established.
