# Biometric Evaluation Standards

**Niche:** [[niches/identity-verification-vendors/verification-decisioning/profile|Verification Decisioning]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Public biometric evaluation programmes established how to measure matching error rates across populations, and commercial identity verification reports a pass rate.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #cnns #descriptive-statistics #compliance #cross-validation #object-detection
**Contested on:** Every serious competitor in this niche is fighting to confirm that a person is who they claim to be in seconds — and the contest splits cleanly enough that it is not terminal.

## The Problem
Public evaluation programmes for face recognition established the methodology: standard datasets, defined error metrics, false match and false non-match rates reported at operating thresholds, and disaggregation across demographic groupings. The results are published and have been for years. Commercial identity verification is a pipeline of which face matching is one component, and the pipeline as deployed — with document capture, liveness, database checks and thresholds — is evaluated by nobody.

## What Already Exists
Standard biometric evaluation protocols and metrics; demographic differential reporting; false match and non-match rate curves at operating points; test dataset construction practice; and independent evaluation infrastructure.

## The Customization Gap
The adaptation is from a matching algorithm to a deployed pipeline. It requires: (1) evaluation of the whole flow including capture, document reading and database checks, since the algorithm may be excellent and the pipeline still exclude people — this is the substantive gap and is what the standard programmes do not cover; (2) uncontrolled capture on the applicant's own device, where evaluation datasets are collected under conditions that do not represent it; (3) outcomes for rejected applicants that do not exist, unlike an evaluation set where ground truth is known by construction; (4) commercial data that cannot simply be published, so the reporting must be aggregate and independently verifiable; and (5) a threshold chosen by the customer, which means the error rate is a curve rather than a number.

## Target Customer
Data science and policy leadership, regulated customers, evaluation bodies and researchers, and biometric vendors whose components are evaluated but whose pipelines are not.

## Impact If Solved
The evaluation methodology exists and stops at the algorithm. Extending it to the deployed pipeline — capture, document, database and threshold — is where the people who cannot verify are actually excluded.
