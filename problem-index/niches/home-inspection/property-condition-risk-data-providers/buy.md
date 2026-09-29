# Model Monitoring Adapted to a Ground Truth That Arrives Years Late

**Niche:** [[niches/home-inspection/property-condition-risk-data-providers/profile|Property Condition & Risk Data Providers]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every model monitoring platform assumes labels come back in days, and here the label is a claim that may arrive in five years or never.
**Tags:** #anomaly-detection #evaluation-metrics #computer-vision #data-integration #automation

## The Problem
A property data firm runs dozens of models in production — roof condition from imagery, structure detection, attribute inference, replacement cost. They are retrained periodically and scored against held-out labelled data, and between retrains nobody really knows whether they are still working.

The ways they silently stop working are specific. An imagery provider changes capture cadence or resolution and a condition model's inputs shift underneath it. A region gets reflown after a hailstorm and every roof in it suddenly grades worse for a reason that is real but not what the score is being used for. A permit data source changes its schema and a feature quietly becomes null for one state. None of these produce an error. They produce scores that are wrong in a direction nobody notices until a client asks.

## What Already Exists
Production ML monitoring is a well-served category — Arize, WhyLabs, Evidently, Fiddler, and the cloud providers' own offerings all do drift detection, performance tracking, and alerting competently, and they are widely deployed.

## The Customization Gap
Every one of them is built around a feedback loop measured in days, and this one is measured in years.

**Performance monitoring without labels.** Standard tooling tracks accuracy as labels arrive. Here they do not arrive, so monitoring must run on proxies: score distribution stability within a geography, agreement between models that should agree, consistency of the same property scored across successive imagery captures. That last one is the strongest available signal and no generic platform has any notion of it, because generic platforms have no notion of a persistent entity scored repeatedly over time.

**Drift that is geographic and seasonal by nature.** A national score distribution shift is meaningless; a shift confined to one metro after a reflight is the alert. Monitoring has to be spatially partitioned by default, and standard tooling partitions by feature value, not by place.

**Upstream imagery as a monitored input.** The model's real dependency is a vendor's capture programme — resolution, angle, season, time since last flight. Those are the variables that move, and they are not features in the model, so nothing watches them.

**Property-level consistency as the primary check.** The same house scored twice a year apart should move slowly and in one direction. A property whose condition improves without a permit is an error signal, and aggregating those across the portfolio is a better health metric than any distributional statistic.

**Vintage-aware evaluation.** When outcomes do eventually arrive, they attach to scores produced by a model version that may be three generations old. Evaluation has to track which version produced which score, which almost no monitoring deployment does because it never has to.

## Target Customer
VP of Machine Learning or Head of Data Platform at a property data provider running a large model portfolio on continuously refreshed imagery.

## Impact If Solved
Silent degradation in a model that underwrites property risk is expensive in a way that is discovered late — through a client escalation or a book that performed worse than priced. Monitoring built for a slow-feedback regime catches it in weeks rather than at the next retrain, and it makes the case for a retrain evidential rather than calendrical.
