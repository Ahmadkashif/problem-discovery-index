# Moisture Migration Prediction and Scope Accuracy

**Industry:** [[insurance-restoration|Insurance Restoration]]
**Type:** High Impact
**One-liner:** Restoration contractors stop losing $5K-$15K per job from underscoped water damage because a model predicts where moisture has migrated behind walls and under floors before demo begins — eliminating the cycle of scope supplements, carrier pushback, and absorbed costs.
**Tags:** #cnn #gradient-boosting #regression #computer-vision #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
When a water loss occurs — burst pipe, appliance failure, storm intrusion — visible damage is only part of the picture. Water wicks through drywall, migrates along floor joists, travels through insulation, and pools in cavities that are invisible without destructive investigation. An experienced restoration technician walks into a water loss, looks at the visible damage, considers the building's construction type (slab vs. crawlspace, balloon frame vs. platform frame), estimates elapsed time since the loss, notes ambient humidity and temperature, and predicts where moisture has traveled. They know that a second-floor bathroom overflow in a balloon-frame home means water has reached the basement. They know that water on a concrete slab migrates laterally 3-5 feet beyond visible damage. They know that 72 hours of standing water in a Category 1 loss can escalate to Category 3 contamination.

This tacit knowledge — reading visible damage and construction cues to predict invisible moisture migration — is the single most valuable skill in restoration. Technicians without it underscope jobs (missing affected areas that develop mold weeks later, requiring costly re-mobilization) or overscope them (triggering carrier audits and jeopardizing preferred vendor status). The initial scope sets the Xactimate estimate, which determines the carrier-approved budget. Getting it wrong in either direction has severe financial consequences.

## Why It's Hard

**Data collection challenge:** Capturing this expertise requires pairing initial site conditions (photos, moisture readings, construction details, loss type, elapsed time) with the actual discovered damage after demolition. This means prospectively documenting what the technician predicted versus what was found — a documentation burden that doesn't exist in current workflows. Each job's "ground truth" isn't known until selective demo reveals the full extent of damage.

**Labeling challenge:** Experienced technicians disagree on scope. A 20-year veteran may scope a 3-foot moisture migration buffer based on construction type, while another equally experienced tech scopes 5 feet. Both may be right for different buildings. The "correct" scope is only verified after demolition, and even then, the decision of when to stop demolishing is itself a judgment call.

**Deployment challenge:** The model must produce predictions fast enough to inform the initial scope — ideally during the first site visit. It must be more consistent (not necessarily more accurate) than the average technician to reduce scope variability. And it must present predictions as a heat map overlay on a floor plan, not just a number, so the project manager can communicate the scope to the carrier adjuster with visual evidence.

## What a Solution Looks Like
A mobile application used during the initial inspection. The project manager photographs visible damage, inputs construction type (from observation or property records), records initial moisture readings on a digital grid, and enters loss details (water source, category, elapsed time, HVAC status). The model outputs a predicted moisture migration map overlaid on the floor plan — showing where water likely traveled, confidence levels by area, and recommended probe points for verification. The scope estimate auto-generates Xactimate line items based on the predicted affected area.

## Implementation Path
Training data comes from pairing initial inspection documentation (photos, moisture readings, construction details) with final scope documentation (actual affected areas discovered during demo). A restoration company processing 50+ water losses per month can accumulate 1,000+ training examples within 2 years. The model combines a CNN for visual damage assessment with gradient-boosted regression for moisture migration distance prediction based on tabular features. Initial deployment targets the most common loss types (supply line failures, appliance overflows) in the most common construction types (platform frame, slab-on-grade) and expands from there. Integration with Xactimate via API enables automated line-item generation from predicted scope.
