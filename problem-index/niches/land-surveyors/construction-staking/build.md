# Real-Time Digital Staking for Contractor Tablets

**Niche:** [[niches/land-surveyors/construction-staking/profile|Construction Staking]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool gives a contractor real-time, AR-overlay spatial guidance on a tablet — "dig here, this deep, this wide" — eliminating the need for physical stakes that get destroyed, buried, or misread.
**Tags:** #cnn #pose-estimation #computer-vision #multimodal #ai-platform

## The Problem
The construction staking workflow has a fundamental disconnect: the surveyor places precise markers that the contractor interprets approximately. A stake with "C 3.2" written on it means "cut 3.2 feet to reach finish grade" — but the contractor may misread the notation, work past the stake, or not understand the cut direction. Stakes get run over by equipment, buried by grading, pulled out by subcontractors, and rained into illegibility. A $50,000 surveyor places information that a $200/hour excavator operator can't reliably use. The physical-stake paradigm assumes the contractor will stand next to the stake and know what to do — but modern construction sites have dozens of concurrent activities and workers who weren't present when the surveyor explained the staking.

## Why Nobody Has Built This
Consumer GPS (phone-based) is accurate to 2-3 meters — useless for construction. Survey-grade GPS requires $15K+ receivers and surveyor training. Augmented reality requires centimeter-accurate positioning (which GPS can't provide indoors or near buildings) and a rendering engine that understands construction drawings. The intersection of survey-grade accuracy and contractor-friendly AR interface hasn't been achieved at a price point contractors can afford. Some machine control systems (Trimble SiteVision) offer AR on tablets but at $30K+ and only for specific Trimble hardware ecosystems.

## What to Build
A contractor-facing tablet application that displays the design surface and staking points overlaid on the real-world camera view using RTK-corrected GPS or local robotic total station tracking. The contractor points the tablet at the ground and sees: "dig here, 3.2 feet deep, 4 feet wide, utility clearance 2 feet left." The surveyor uploads the design model and staking points to the cloud; the contractor accesses them in real-time. Position updates in real-time as the contractor moves. Works with consumer-grade tablets using an affordable external RTK GPS antenna ($2-3K). The surveyor can verify remotely that the contractor is working to the correct positions.

## Target Customer
General contractors and site superintendents on commercial and residential construction projects. Secondary market: survey firms that can offer "digital staking" as a premium service.

## Impact If Built
Eliminates 60-70% of re-staking visits (estimated at $500-1,500 per visit). Reduces contractor interpretation errors that cause rework (estimated 3-5% of construction rework is staking-related). Enables the surveyor to support more concurrent projects by reducing physical site visits.
