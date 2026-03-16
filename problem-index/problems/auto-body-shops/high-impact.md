# Hidden Damage Prediction from Visible Impact

**Industry:** [[auto-body-shops|Auto Body Shops]]
**Type:** High Impact
**One-liner:** Every estimate accounts for what's behind the panel before the panel comes off — because experienced estimators already know, and now the model does too.
**Tags:** #cnn #regression #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
When a car arrives with front-end collision damage, an experienced estimator looks at the external deformation pattern — the depth of crush, the direction of impact, the way the bumper cover folded, the gap misalignment between panels — and mentally predicts what's damaged behind the visible surface. They know that a 15mph offset frontal impact on a 2019 Camry typically bends the radiator support, cracks the condenser, and tweaks the upper rail — even before touching the vehicle. This tacit knowledge developed over thousands of teardowns means their initial estimates are 80-90% accurate. A new estimator writes for what they can see, missing 30-50% of actual damage, triggering supplements that delay repairs by 3-7 days.

## Why It's Unsolved
The knowledge is geometric and vehicle-specific: how force propagates through the specific crush structures of each make/model/year. An experienced estimator has internalized these deformation patterns across hundreds of vehicles, but the reasoning is visual and intuitive, not rule-based. Capturing this requires paired data — pre-teardown photos linked to post-teardown damage discoveries — which collision shops generate daily but never systematically record. OEM repair databases document procedures but not the impact-to-damage correlations that estimators learn through experience.

## What a Solution Looks Like
A computer vision system that ingests photos of visible collision damage, identifies the vehicle make/model/year, analyzes the impact geometry (angle, estimated speed, point of impact), and predicts hidden damage with line-item specificity: "radiator support — bent (85% confidence), condenser — cracked (72% confidence), right upper rail — tweaked (61% confidence)." Output is a supplemented estimate that accounts for predicted hidden damage from day one, reducing supplement cycles from 2-3 rounds to 0-1.

## Impact If Solved
Reduces average supplement amount by 40-60% by front-loading hidden damage into initial estimates. Cuts average cycle time by 2-4 days by eliminating supplement approval delays. Improves insurance DRP scores by reducing supplement frequency. Enables accurate repair planning from day one, improving parts ordering and scheduling.
