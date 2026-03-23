# Tailor's Knowledge Capture System

**Niche:** [[niches/alterations-tailoring/custom-tailoring-bespoke/profile|Custom Tailoring & Bespoke]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system captures the tacit knowledge of master tailors — how they read a body, predict fabric behavior, and make pattern adjustments based on decades of visual-spatial expertise that will be lost when they retire.
**Tags:** #cnn #regression #computer-vision #tacit-knowledge-ml #multimodal

## The Problem
A master tailor looks at a client standing in a partially-constructed jacket and sees what no one else can: the right shoulder is slightly higher, creating a collar roll that will worsen as the fabric settles; the back pitch needs 3mm adjustment to accommodate forward arm carriage; the chest drape indicates the front dart should shift 1cm toward the side seam. This assessment takes the master tailor 30 seconds and takes an apprentice 10 years to learn. There are fewer than 5,000 true master tailors in the US, with an average age over 60. When they retire, their knowledge — the relationship between what they see and what they do — retires with them.

## Why Nobody Has Built This
Capturing tacit visual-spatial knowledge requires: (1) a master tailor willing to articulate what they see and why they make each adjustment (most can't — they "just know"), (2) a structured data collection process that pairs visual observations (photos/video of the fitting) with the specific adjustments made, (3) enough annotated examples across body types, garment types, and fabric types to train a model, and (4) a deployment form that's useful to less experienced tailors. The data collection is the hardest part — it means instrumenting the fitting process of master tailors willing to participate in knowledge capture.

## What to Build
A fitting documentation system where the master tailor is photographed during the fitting process: photos of the garment on the body from standardized angles, the tailor's pinning and marking decisions captured visually, and the tailor's verbal assessment recorded and transcribed. Over hundreds of fittings, the system builds a dataset linking body/garment images to specific pattern adjustments. The near-term output is a searchable case library: "show me fittings where the client had forward shoulder posture — what adjustments did the master make?" The long-term output is a predictive model that suggests adjustments to less experienced tailors.

## Target Customer
Master tailors in their 50s-70s who want their knowledge to survive them, bespoke shops with apprentice programs, and tailoring schools seeking to preserve craft knowledge before it's lost.

## Impact If Built
Preserves craft knowledge that would otherwise be lost to retirement (estimated 2,000+ master tailors will retire in the next decade), accelerates apprentice development from 10-15 years to 5-7 years, and creates a compounding knowledge asset for the bespoke tailoring industry.
