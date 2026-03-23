# Computer Vision Cleanliness Scoring

**Niche:** [[niches/cleaning-companies/quality-inspection-automation/profile|Quality Inspection Automation]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system can look at a photo of a cleaned room and objectively score cleanliness — detecting streaks on glass, residue on surfaces, or debris on floors.
**Tags:** #cnn #semantic-segmentation #computer-vision #tacit-knowledge-ml #automation

## The Problem
Cleaning quality is judged by subjective human inspection. An experienced quality manager can walk into a room and immediately spot issues — streaks on glass, dust on horizontal surfaces, vacuum tracks missing from carpet, soap residue in sinks. This tacit visual pattern recognition takes years to develop and can't be scaled. Operators with 50+ buildings can't afford to have a quality manager inspect every building every shift, so most buildings go uninspected most of the time, and quality degrades until a client complains.

## Why Nobody Has Built This
"Clean" vs. "not clean" is surprisingly hard for computer vision. The model must detect subtle visual cues (streaks visible only at certain angles, thin dust layers, water spots on chrome) in variable lighting conditions across diverse room types. Training data requires expert labeling — an experienced inspector must annotate thousands of images with specific deficiency types and locations. The model also needs to be robust to baseline room differences (an old carpet always looks dirtier than a new one).

## What to Build
A mobile app where the crew or inspector photographs each area from standardized angles. Computer vision analyzes images for cleanliness deficiencies: streaks on glass, dust on surfaces, debris on floors, smudges on fixtures, restocking gaps (empty soap dispensers, low paper towels). Each image gets a cleanliness score (0-100) and flagged deficiencies with bounding boxes. Scores aggregate into a building-level quality dashboard tracked over time.

## Target Customer
Large cleaning companies managing 20+ commercial buildings who currently inspect fewer than 30% of buildings per month and lose contracts to undetected quality degradation.

## Impact If Built
Enables 100% inspection coverage (vs. current 20-30%), reduces quality-related contract losses (worth $50,000-$200,000 per lost building contract), and makes quality objective rather than disputed.
