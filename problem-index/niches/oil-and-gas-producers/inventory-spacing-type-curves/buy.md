# Experiment Tracking Pointed at Type Curves

**Niche:** [[niches/oil-and-gas-producers/inventory-spacing-type-curves/profile|Inventory, Spacing & Type-Curve Planning]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine-learning teams already version every model with its inputs and grade it against outcomes; type curves are models too, and nobody versions them.
**Tags:** #evaluation-metrics #feature-engineering #bayesian-inference #data-integration #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to rank an operator's undrilled locations and set their spacing so the wells drilled land on the forecasts that funded them, and whoever's location forecasts come closest to realised 24-month production takes the account.

## The Problem
A type curve is a forecast built from chosen inputs, revised several times, and used to justify spending. When the well underperforms, nobody can say which version funded it or which analogs went into it.

## What Already Exists
Experiment-tracking and model-registry tools (MLflow, Weights & Biases, Neptune) record every model version with its data, parameters and evaluation, and compare them against held-out results. Planning tools such as ComboCurve and Enverus save curves and projects.

## The Customization Gap
The oil and gas layer: a type curve record that holds its analog well list, normalisation choices (lateral length, proppant), decline parameters and haircut; links from each curve to the locations it funded and the date it was approved; alignment of actual production to the curve by months on production, with downtime and choke changes removed; and a grading report by bench, spacing band and engineer. Connectors to ARIES, PHDwin, ComboCurve and state production data replace the Python integrations an ML team would write.

## Target Customer
Reservoir engineering managers who want accountability for type curves without replacing their planning software.

## Impact If Solved
Versioning and grading every curve costs little, and within two years of production it gives an operator drilling ~150 wells a year a graded record of ~300 locations (estimate). That is enough to see which benches and spacing bands its curves systematically miss.
