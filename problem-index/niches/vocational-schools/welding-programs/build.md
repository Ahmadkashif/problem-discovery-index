# Vision-Based Weld Quality Progression Tracking

**Niche:** [[niches/vocational-schools/welding-programs/profile|Welding & Skilled Trades Programs]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A camera-based system that photographs every student weld, scores quality dimensions automatically, and tracks skill progression across the full certification path — replacing subjective instructor eyeballing with consistent, documented assessment.
**Tags:** #cnn #multiclass-classification #computer-vision #tacit-knowledge-ml #worker-facing

## The Problem
Welding instructors assess student work by visual inspection — checking bead width consistency, undercut depth, porosity, spatter, and overall appearance. An experienced instructor processes these cues in seconds, but the assessment is never recorded digitally, varies between instructors, and provides no progression data over time. Students have no objective record of their improvement trajectory, and programs cannot demonstrate competency development to accreditors or employers with anything beyond pass/fail tallies.

## Why Nobody Has Built This
Capturing the visual assessment that experienced welding instructors perform tacitly requires training a computer vision model on thousands of labeled weld images with multi-dimensional quality scores — data that doesn't exist because no school currently photographs student welds systematically. The labeling challenge is severe: instructors disagree on marginal welds, and the same instructor may grade the same weld differently on different days. Building ground truth requires multi-instructor consensus labeling at $50-100/hour per evaluator.

## What to Build
A workstation-mounted camera system that captures high-resolution images of each student's completed weld coupon. A CNN model trained on consensus-labeled weld images classifies quality across 4-6 dimensions (bead appearance, penetration indicators, undercut severity, porosity, spatter, overall acceptability). Results feed a student progression dashboard showing improvement curves by weld position (1G-6G) and process (SMAW/GMAW/GTAW), with weekly progress reports for instructors and accreditation-ready competency documentation.

## Target Customer
Private welding schools and community college welding programs with 50+ active students seeking consistent assessment, accreditation documentation, and instructor productivity improvement.

## Impact If Built
Reduces instructor assessment time by 40-60% per student per session. Provides the first objective, longitudinal competency record for welding students — improving employer confidence in graduates and strengthening accreditation self-study evidence with quantified skill progression data.
