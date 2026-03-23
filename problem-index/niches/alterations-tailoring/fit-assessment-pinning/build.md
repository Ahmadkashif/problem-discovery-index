# Computer Vision Fit Assessment Assistant

**Niche:** [[niches/alterations-tailoring/fit-assessment-pinning/profile|Fit Assessment & Pinning Workflow]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool uses computer vision to analyze how a garment fits on a body and identify specific fit issues — the skill that takes tailors 3-5 years to develop by eye and is the industry's deepest tacit knowledge.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #pose-estimation

## The Problem
An experienced tailor looks at a client wearing a jacket and sees: the left shoulder seam is sitting 1cm too far forward, creating diagonal wrinkles from the chest toward the armhole; the collar is gapping at the back of the neck because the back length is 0.5cm too short; the waist suppression is insufficient, creating excess fabric that pools at the sides. They see all of this simultaneously, in under a minute, and translate it into specific alteration instructions. A new tailor sees "it doesn't look right" but can't identify the specific issues or their causes. This visual assessment skill is the single highest-value tacit knowledge in the alterations industry.

## Why Nobody Has Built This
Building a CV fit assessment requires: (1) a labeled dataset of garments on bodies with expert annotations of every fit issue present ("collar gap: 0.5cm, cause: insufficient back length"), (2) a model that understands the relationship between fabric drape patterns and underlying fit issues (wrinkle direction indicates which seam needs adjustment), (3) pose estimation to separate body position artifacts from actual fit problems, and (4) garment type awareness (a suit jacket and a casual blazer have different fit criteria). No such dataset exists, and collecting one requires instrumenting expert tailor fittings with cameras and detailed annotation.

## What to Build
A camera-based assessment system where the tailor (or consumer) photographs the garment from front, back, and sides. The system identifies fit issues: shoulder alignment, collar gap, chest tightness, waist suppression, sleeve length, hem balance, back pitch, and button pull. For each issue, it suggests the specific alteration and estimated adjustment amount. For experienced tailors, this validates their assessment; for apprentices, it teaches them what to see; for consumers, it tells them what's possible before visiting a shop.

## Target Customer
Alteration shops training new staff (reducing the 3-5 year apprentice timeline), consumers assessing fit of online purchases, and tailors seeking a "second opinion" confirmation of their visual assessment.

## Impact If Built
Reduces fit assessment training time from 3-5 years to 1-2 years for apprentices, enables consumer self-assessment (growing the alteration market by reaching people who don't know they need alterations), and captures the tacit knowledge of expert tailors in a scalable digital system before it's lost to retirement.
