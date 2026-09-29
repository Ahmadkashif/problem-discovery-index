# Root Cause Analysis From Manufacturing Quality

**Niche:** [[niches/data-labeling-services/delivery-manager-diagnosis/profile|The Delivery Manager]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturing quality has a century of practice in tracing a defect back to a shift, a machine, a batch or a procedure change, and annotation delivery traces it by hand.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #k-means-clustering #automation #compliance
**Contested on:** Every serious competitor that takes this seriously is fighting to turn a customer complaint that the data is bad into a diagnosis with a cause — and whoever does that takes delivery, because the escalation is currently a week of working backwards through a pipeline that records everything except why.

## The Problem
Manufacturing quality management solved this shape of problem long ago: when a defect appears, trace it to the shift, the operator, the machine, the material batch or the process change, using recorded production data and a structured set of comparisons. The discipline has control charts, traceability requirements and root cause methodology. Annotation delivery is a production process with operators, shifts, batches and procedure changes, and its defects are traced by reading examples.

## What Already Exists
Statistical process control with control charts and out-of-control rules; traceability practice requiring every unit to carry its production context; structured root cause methodology; change-point detection for identifying when a process shifted; and stratified comparison, which is the core analytical move.

## The Customization Gap
The adaptation is to a process whose output quality is a judgement rather than a measurement. It requires: (1) a quality signal that exists before the customer complains, since statistical process control assumes a measurable output property and annotation quality is assessed downstream — which means using the available proxies, agreement and review outcomes, with their known limitations stated; (2) the guideline as a process parameter, since a guideline change is the equivalent of a procedure change and is the commonest cause, and it must be versioned against output exactly as manufacturing versions a work instruction; (3) the annotator cohort as a stratification dimension, because training cohorts behave like production batches and a cohort trained on a superseded guideline is the classic traceable defect; (4) tolerance for a moving target, since the customer's own criteria frequently evolve during a project, which has no manufacturing analogue and must be treated as a specification change with a date; and (5) honest handling of the cases where the process was fine and the specification was wrong, which is a meaningful share and which the manufacturing framing handles well.

## Target Customer
Delivery organisations, annotation platform vendors, and the quality management vendors for whom this is an adjacent process.

## Impact If Solved
A century of production quality practice addresses exactly this traceability problem and the category reads examples. Versioning the guideline against output is the traceability requirement that makes the commonest cause provable, and cohort stratification finds the classic batch defect.
