# Thermal Image Interpretation for Electrical Panels

**Niche:** [[niches/electrical-contractors/panel-inspection-diagnostics/profile|Panel Inspection & Diagnostics]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** FLIR and Fluke thermal cameras capture beautiful heat maps of electrical panels, but interpreting what constitutes a dangerous hot spot vs. normal operating temperature requires experience that most electricians and inspectors lack — an AI interpretation layer turns thermal images into actionable findings with severity ratings.
**Tags:** #cnns #semantic-segmentation #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #worker-facing

## The Problem
Thermal imaging is widely used in electrical maintenance and inspection — an infrared camera pointed at a closed panel reveals hot spots indicating loose connections, overloaded circuits, or failing breakers. The problem is interpretation: a breaker carrying 80% of rated load at 140°F in a 75°F ambient environment is normal operating temperature, but the same breaker at 140°F carrying 20% load is a serious concern. A loose bus bar connection might show as a 30°F temperature rise above ambient — dangerous — but so might a fully loaded circuit breaker — normal. Experienced thermographers understand these distinctions because they've interpreted thousands of images in context (load conditions, ambient temperature, connection type). Most electricians have a FLIR camera on their phone but lack the training to correctly interpret what they see, leading to both missed hazards (false negatives) and unnecessary alarm (false positives).

## What Already Exists
FLIR and Fluke sell thermal cameras ranging from $200 phone attachments to $5,000 professional units. FLIR's software (FLIR Tools, FLIR Ignite) provides basic temperature measurement and report generation. Some cameras include "high temperature alerts" at fixed thresholds. NETA (InterNational Electrical Testing Association) publishes thermal imaging guidelines with temperature rise severity tables. None of these tools interpret the image in context — they show temperatures but don't say "this is a problem."

## The Customization Gap
The gap is between image capture (solved by FLIR/Fluke) and expert interpretation (currently requires a Level II thermographer certification and field experience). An AI interpretation layer would: (1) segment the thermal image to identify individual components (breakers, bus bars, wire terminations, neutrals) using a CNN trained on annotated thermal images of electrical panels; (2) measure temperature rise above ambient for each component, accounting for the panel's overall temperature distribution; (3) correlate temperature anomalies with component type and expected operating characteristics — a gradient-boosted model classifies each anomaly as normal/watch/caution/critical based on component type, temperature rise magnitude, and distribution pattern; (4) generate a findings report matching NETA standards with severity ratings, recommended actions, and re-inspection intervals. The key training data is pairs of thermal images with expert thermographer interpretations, which industrial facilities with annual thermographic inspection programs have accumulated over decades.

## Target Customer
Electricians who own thermal cameras but lack Level II thermographer training, home inspectors offering thermal scans as an add-on service, industrial facilities performing annual thermographic surveys with in-house electricians rather than certified thermographers.

## Impact If Solved
Brings Level II thermographer-quality interpretation to any electrician with a $200 FLIR phone attachment, expanding the effective thermographic inspection workforce by 10-20x. Reduces false negatives (missed hazards) from 30-40% for untrained users to under 10%. Reduces false positives (unnecessary alarm) from 50%+ for untrained users to under 15%, saving follow-up investigation costs.
