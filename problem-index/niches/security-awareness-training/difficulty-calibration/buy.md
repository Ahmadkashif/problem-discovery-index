# Buy: Item Banking From Educational Testing

**Niche:** Difficulty Calibration
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** High-stakes testing built calibrated item banks, equating and exposure control because a score that depends on which form you sat is worthless, and phishing simulation has exactly that score.
**Tags:** #bayesian-inference #maximum-likelihood-estimation #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #automation
**Contested on:** Whether a simulation's difficulty is a measured property, so that click rates can be compared.

## The Problem

Educational and professional testing faced this problem and solved it comprehensively, because the stakes made an uncalibrated score intolerable.

The apparatus is complete. Item response theory estimates item difficulty and candidate ability jointly. Item banks hold calibrated items with known parameters. Equating procedures make scores from different test forms comparable. Exposure control manages how often an item is used, because a widely-seen item stops discriminating. Differential item functioning analysis detects items that behave differently for different groups. And the whole thing is maintained continuously as items are added and retired.

Phishing simulation has a template library with difficulty labels and no calibration, no equating, no exposure control and no group-difference analysis. It produces a score that depends on which templates you happened to receive, which is precisely the situation testing abandoned.

The data required is already collected. Every simulation platform holds a large response matrix of people against templates, which is the exact input the entire testing apparatus consumes.

## What Already Exists

Psychometric method: item response theory in its standard forms, Rasch modelling, test equating and linking, differential item functioning, and adaptive testing — all documented in detail with open-source implementations.

Assessment platforms: the systems used by testing organisations, with calibrated item banks, exposure control and ability reporting.

Psychometric services: consultancies and academic groups who calibrate item banks professionally, for whom this would be routine work.

Adaptive testing: selecting the next item based on the estimated ability, which would make simulation campaigns both more informative and shorter.

Simulation platforms: template libraries, scheduling and click tracking.

## The Customization Gap

**The response matrix is sparse and non-random.** Testing administers a planned set of items. Simulation sends campaigns to whole populations on an operational schedule, so the matrix has a different structure — handled by standard sparse calibration methods and requiring deliberate design.

**Learning happens between administrations and is the point.** Testing generally assumes a stable ability during a test. Here the intervention is meant to change the ability, which means a longitudinal model rather than a single calibration — well established in growth modelling and not the default.

**Exposure effects are stronger and faster.** A phishing template circulates through an organisation by word of mouth within hours, which makes exposure control more urgent here than in a proctored test.

**Adaptive campaigns have no equivalent and would be valuable.** Sending each person a template near their estimated susceptibility produces far more information per message and fewer messages overall, which also reduces the harm surface.

**Group-difference analysis is unused and matters.** Differential item functioning would reveal templates that unfairly disadvantage particular roles, language groups or shift patterns — which is a fairness question in a programme with consequences attached.

**The stakes framing is different and should not be.** Testing built this because scores had consequences. These scores have consequences too — training assignment, lists, occasionally disciplinary action — and the discipline has not followed.

## Target Customer

Simulation vendors, for whom a psychometric partnership is a modest investment producing the category's first defensible measurement.

Psychometric service providers and assessment vendors, for whom calibrating a phishing template bank is routine work in an adjacent market with no incumbent capability.

Large enterprise security organisations and insurers, as the demand side that would ask for a calibrated scale once one exists.

## Impact If Solved

A complete, mature apparatus for exactly this problem exists next door, and the required data is already being collected at scale.

Adaptive campaign design would produce more information from fewer messages, which simultaneously improves measurement and reduces how often employees are deceived.

And differential item functioning analysis would surface templates that systematically disadvantage particular groups — a fairness question in a programme whose results are attached to individuals and currently entirely unexamined.
