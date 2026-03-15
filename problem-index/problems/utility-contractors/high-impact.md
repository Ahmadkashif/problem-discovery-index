# Underground Utility Detection and Depth Estimation from Ground-Penetrating Radar Data

**Industry:** [[utility-contractors|Utility Contractors]]
**Type:** High Impact
**One-liner:** Experienced utility locators who interpret GPR (ground-penetrating radar) B-scan imagery to identify buried utility depth and routing — reading hyperbolic reflection patterns that take years of training to interpret correctly — get an ML model that identifies utilities in GPR scans and returns depth and routing estimates, reducing utility strikes during excavation.
**Tags:** #cnn #object-detection #regression #signal-processing #tacit-knowledge-ml #revenue-impact

## The Problem

Ground-penetrating radar (GPR) is the most accurate available tool for detecting subsurface utilities before excavation. A GPR unit generates a B-scan image — a cross-sectional view of the subsurface where buried utilities appear as hyperbolic reflection signatures. An experienced GPR operator reads these hyperbolas to identify: which reflections are utilities vs. soil anomalies, the utility's depth from the hyperbola vertex, the utility type (plastic vs. metal affects the reflection signature), and the routing direction.

This visual interpretation skill — reading GPR B-scan imagery — takes 2-3 years of supervised practice to develop reliably. Operators who misread GPR data produce utility maps that lead to excavation strikes: the excavator digs where the locator said it was clear, and hits a gas main or fiber optic cable that the GPR showed but the operator misinterpreted.

## Why It's High Impact

Utility strikes are catastrophic:
- A natural gas main strike can cause explosion and fire: fatalities, property destruction, and criminal liability
- A high-voltage cable strike: electrocution risk and outages affecting thousands of customers
- Fiber or telecom: service disruption affecting hospitals, emergency services, or financial systems

The liability per major strike is $500,000 to $10 million. The frequency of utility strikes in the US is approximately 400,000 per year — most are minor, but hundreds per year are major incidents. Improving the accuracy of GPR interpretation is among the highest-impact safety interventions available in underground utility work.

## What a Solution Looks Like

A ML model integrated with GPR software (GSSI SIR-4000, Mala Ground Explorer, or equivalent) that processes the B-scan imagery in real time and identifies:
1. Hyperbolic reflections indicating buried objects
2. Depth estimate per detected object from hyperbola geometry
3. Object type classification (metallic pipe, non-metallic pipe, cable, structural void) from reflection characteristics
4. Confidence score per detection

The operator reviews the model's overlay on the B-scan display, confirms detections, and marks utilities. The model catches signatures the operator might dismiss as noise, and flags ambiguous areas for additional passes.

## Implementation Path

GSSI and Mala have large archives of labeled GPR B-scans from their field service operations — utilities confirmed by excavation provide ground truth labels. A CNN trained on labeled GPR B-scans with hyperbola annotations: 12-18 months for a commercial-quality model. GSSI or a large utility contractor (Quanta, MYR Group) is the natural development partner — they have data, distribution, and the financial incentive to reduce strike liability.
