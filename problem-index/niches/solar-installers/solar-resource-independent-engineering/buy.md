# Satellite Irradiance Corrected Against Ground Stations That Are Mostly Dirty

**Niche:** [[niches/solar-installers/solar-resource-independent-engineering/profile|Solar Resource Assessment & Independent Engineering]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The bankable resource dataset is a satellite model bias-corrected against ground measurements, and the ground measurements are the least reliable part of the chain.
**Tags:** #gaussian-processes #bayesian-inference #change-point-detection #evaluation-metrics #data-integration

## The Problem
Solar resource datasets are built by modelling irradiance from satellite imagery, then correcting the model against ground stations. The satellite model is systematic and reproducible; the correction is where the accuracy claim comes from, and it rests on the ground data.

Ground data is difficult. Pyranometers drift, and require cleaning and recalibration on a schedule that project sites rarely keep. Soiling depresses readings gradually and looks exactly like a real resource decline. Shading from equipment installed after commissioning appears as a step change. Data loggers gap. A station may be excellent for a year and quietly wrong for the next two.

Assessing which measurements to trust — and how far — is expert work done by analysts inspecting time series, applying quality control procedures, and making judgment calls about whether an apparent bias is real or instrumental. On a project with a year of on-site measurement, that judgment materially moves the P50 and therefore the financing.

The same judgment is embedded in the vendor's own bias-correction network, where station quality determines how much correction propagates into a whole region's dataset.

## What Already Exists
Standard quality control procedures for irradiance data are published and widely implemented. Open tooling exists for basic screening — physical limits, consistency between components, tracking against clear-sky models. Anomaly detection in time series is mature. Gaussian process regression is standard machinery for spatial interpolation with uncertainty.

What is missing is the integration. Published quality control flags physically impossible values; it does not distinguish soiling from a real cloudiness trend, or say how much weight a partially compromised station should carry in a bias correction. Generic anomaly detection has no concept of a pyranometer's failure modes. And nothing off the shelf produces the output that matters: a correction with an uncertainty that honestly reflects how good the reference data was.

## The Customization Gap
**Instrument failure modes are the ontology.** Soiling, drift, shading, levelling error, moisture ingress, cable faults — each has a signature in the time series, and each implies a different correction. A model must classify the failure, not just flag the anomaly, because the response differs.

**Soiling is the hard case and the important one.** It is gradual, recovers abruptly after cleaning or rain, and is confounded with real atmospheric variation. Separating it requires joint reasoning across nearby stations, satellite estimates and precipitation — a domain-specific inference no generic tool performs.

**Station quality must be a weight, not a gate.** The current practice is largely to include or exclude. A weighted correction where each station contributes according to an estimated reliability is both more accurate and more honest, and it changes the uncertainty that reaches the assessment.

**Uncertainty must propagate to the deliverable.** The output that matters is a corrected time series with a defensible uncertainty, because that uncertainty is a component of the P90 a lender relies on. Any tool that returns a corrected series without one is producing a number the workflow cannot use responsibly.

**The training data is the vendor's own network.** Years of station records with maintenance logs, calibration certificates and analyst quality assessments is the supervision this needs, and only a resource data vendor has it.

## Target Customer
Head of Solar Resource or Chief Scientist at a resource data provider, or the technical lead of an independent engineering practice running on-site measurement campaigns.

## Impact If Solved
The accuracy claim of a bankable dataset rests entirely on the quality of the ground reference, and that quality is currently assessed by analysts one station at a time. Automating the classification of instrument failure — with weights and honest uncertainty flowing through to the corrected series — improves the datasets every solar financing in the country depends on, and it is the precondition for the empirical uncertainty estimates the validation work above requires.
