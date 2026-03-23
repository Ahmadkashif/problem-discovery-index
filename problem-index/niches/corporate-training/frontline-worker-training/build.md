# On-Floor Skill Verification System

**Niche:** [[niches/corporate-training/frontline-worker-training/profile|Frontline Worker Training]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform today verifies whether a frontline worker actually applies trained skills on the job — completion data shows they watched the module, but nobody knows if the barista actually improved their drink preparation speed or the warehouse picker reduced error rates.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #worker-facing

## The Problem
A QSR chain trains 50,000 workers on a new food preparation procedure via mobile microlearning. Completion rates are 85%. But six weeks later, mystery shoppers report that only 40% of stores are executing the procedure correctly. The L&D team has no data between "completed the module" and "mystery shopper visit" to understand where execution broke down — was the training content ineffective, did managers not reinforce it, or did workers learn it but revert to old habits under time pressure?

## Why Nobody Has Built This
Verifying skill application requires observing the worker performing the task in the actual work environment — not in a simulation or quiz. For physical tasks (food preparation, shelf stocking, equipment operation), this means either manager observation checklists (which are inconsistently completed) or computer vision systems (which raise privacy concerns and require specialized camera infrastructure). For customer-facing tasks (service interaction quality), verification requires either customer feedback correlation or audio/video analysis of interactions.

## What to Build
A skill verification layer that connects training modules to observable job performance indicators: (1) for physical tasks, a lightweight manager observation protocol (3-click mobile checklist completed during routine floor walks) with automated scheduling and aggregation; (2) for process compliance, integration with existing operational sensors (POS timing data, warehouse management system error rates, quality inspection results) to correlate training completion with performance metric changes; (3) for customer-facing skills, integration with customer feedback systems (NPS, survey scores) at the individual-worker level.

## Target Customer
Operations Directors at retail chains, QSR franchises, and warehouse operators with 1,000+ frontline workers who spend $1M+ annually on training but cannot demonstrate that training produces observable behavior change on the floor.

## Impact If Built
Closes the "training-to-behavior" gap that makes frontline training budgets indefensible. Organizations can identify which training modules actually change floor behavior (estimated at only 30-40% of current content) and reallocate investment accordingly — improving operational performance while reducing training waste by 40-60%.
