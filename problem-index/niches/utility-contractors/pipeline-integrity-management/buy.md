# Millions of Sensor Traces Read by People Who Are Retiring

**Niche:** [[niches/utility-contractors/pipeline-integrity-management/profile|Pipeline Integrity Management & In-Line Inspection]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every inspection run produces sensor data that a trained analyst interprets signal by signal, and the analysts take years to train in a workforce that is thinning.
**Tags:** #cnns #transformers #semantic-segmentation #transfer-learning #evaluation-metrics

## The Problem
An inspection tool traverses hundreds of miles of pipe recording magnetic flux leakage, ultrasonic thickness or geometry data from dozens of sensors at high sampling rates. The result is an enormous volume of signal in which a small number of features matter.

Interpretation is the product. An analyst reads the traces, distinguishes metal loss from a weld, a fitting, a repair sleeve, a dent, an appurtenance or a sensor artefact, classifies what remains, and sizes it. Automated first-pass detection exists and is standard; the classification and sizing that determine whether a crew is dispatched still rest heavily on human interpretation of the signal shape.

That skill takes years to build. It is domain knowledge about how a specific tool responds to a specific geometry in a specific pipe, learned by seeing thousands of examples with feedback from digs. The analysts who hold the most of it are senior, and the pipeline of replacements is thin — the same demographic problem this index has recorded in reserve engineering, coatings consulting and regulatory science.

Throughput is the visible symptom. Analysis time gates how quickly results reach an operator, and operators are working against regulator-set deadlines.

## What Already Exists
Deep learning on one-dimensional sensor signals and on two-dimensional sensor-by-distance images is mature, and the pipeline inspection literature contains substantial published work on automated defect classification and sizing. Vendors already deploy automated detection and some assisted classification. Industrial NDE more broadly has adopted learned models for weld and casting inspection.

The gap is that published work is trained on small curated datasets, evaluated against analyst labels rather than against dig measurements, and does not reflect the operational conditions that make real runs hard: speed variation, sensor lift-off, magnetisation shortfall in heavy wall, and the enormous diversity of legacy pipe features. A generic anomaly detector does not produce a sized, classified, regulator-defensible call.

## The Customization Gap
**The label should be the dig, not the analyst.** Training on analyst calls reproduces analyst bias. Training and evaluating against verification measurements is what makes the model better than the person, and only a vendor with a verification archive can do it.

**Feature classification is the hard half.** Most signals are not defects. Distinguishing a genuine anomaly from a sleeve, a tap, a support or a magnetisation artefact is where analyst expertise concentrates, and it is a classification problem over signal morphology with a long tail of rare legacy features.

**Tool physics is a prior, not a nuisance.** How a given sensor configuration responds to a given geometry is known from first principles and calibration testing. A model that ignores it wastes the strongest structural information available.

**Every call must be defensible.** Results are submitted to regulators and defended in enforcement. A call needs an inspectable basis — the signal region and the reasoning — which rules out an opaque classifier.

**Uncertainty must reach the deliverable.** A sized anomaly with a confidence is usable in the dig decision above; a bare number is not.

**Human review is the design target.** Routing confident calls automatically and directing analysts to genuinely ambiguous signals is the achievable and correct goal, and it is where the throughput gain is.

## Target Customer
VP of Data Analysis or Chief Technology Officer at an in-line inspection vendor, running an analysis organisation whose size and seniority set both turnaround and quality.

## Impact If Solved
Analysis capacity constrains how fast operators get results against statutory deadlines, and analyst expertise is concentrated in people approaching retirement in a specialty that takes years to train into. Learning the classification and sizing from dig-verified labels both preserves that expertise institutionally and improves on it, because the model is trained against the ground truth rather than against the last analyst's opinion.
