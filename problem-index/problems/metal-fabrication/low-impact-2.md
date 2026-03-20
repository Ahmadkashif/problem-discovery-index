# Weld Distortion Prediction for Pre-Compensation Planning

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Finite element analysis tools can simulate weld distortion, but require hours of setup per assembly by an FEA engineer — while fabrication shops need a fast, practical distortion prediction that a welder or fitter can use to set up pre-bend angles and welding sequence for a new assembly before it distorts and requires straightening.
**Tags:** #gradient-boosting #gaussian-processes #linear-regression #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #bayesian-optimization #tacit-knowledge-ml

## The Problem

Weld distortion — the deformation of a fabricated assembly caused by differential thermal expansion and contraction during welding — is one of the most expensive problems in structural fabrication. A weldment that warps out of tolerance during welding requires either straightening (heat straightening or press straightening, adding 1-4 hours of rework) or rejection as scrap. For large structural assemblies, distortion that requires field correction at installation adds cost that dwarfs the fabrication price.

Experienced welders and fabricators know from years of practice how a specific assembly will distort — they pre-bend components in the opposite direction of expected distortion, optimize welding sequence to balance heat input, and use pre-heat and interpass temperature controls to minimize shrinkage. This pre-compensation knowledge lives entirely in the heads of senior fabricators, is not documented in any job router, and is not transferable to junior welders through any current training.

## What Already Exists

Commercial FEA software (Simufact Welding, ESI SYSWELD) can simulate weld distortion accurately, but requires 2-8 hours of setup by an FEA engineer per assembly and is not accessible to a typical job shop. Rule-of-thumb tables (expected angular distortion per kJ/mm of heat input for a given thickness) exist in welding engineering references but don't account for assembly geometry, constraint conditions, or welding sequence.

## The Customisation Gap

A practical shop-floor distortion prediction tool needs: (1) simplified geometry feature extraction — key parameters that drive distortion (plate thickness, joint type, weld sequence, restraint conditions, preheat); (2) a surrogate model trained on FEA simulation results across the assembly parameter space — capturing the physics without requiring the engineer setup time; (3) pre-compensation recommendations in terms a welder or fitter can act on (pre-bend this plate 3/16" before tack; weld this side first). The surrogate model approach — training ML on FEA outputs rather than on experimental data — is the gap current tools don't bridge.

## Impact If Solved

Reduces weld distortion rework rate from 8-15% of fabricated assemblies to under 5% for shops with predictable assembly types. For a $5M/year fabricator with current 10% rework rate driven by distortion, reducing rework by half saves $250,000 annually in labor and scrap. Makes distortion pre-compensation knowledge accessible to junior welders, reducing the dependence on senior fabricators for every complex assembly.
