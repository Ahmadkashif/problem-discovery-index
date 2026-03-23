# NPI Process Parameter Predictor from Historical Program Data

**Niche:** [[niches/electronics-contract-mfg/high-mix-low-volume-ecms/profile|High-Mix Low-Volume EMS Providers]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product predicts optimal SMT process parameters (reflow profile, stencil aperture ratios, placement speeds) for a new customer program by analyzing the BOM's similarity to previously successful programs — forcing process engineers to start from generic parameters and tune empirically over 3-6 months.
**Tags:** #gaussian-processes #gradient-boosting #tacit-knowledge-ml #revenue-impact

## The Problem
When an HMLV EMS provider launches a new customer program, the process engineer must establish SMT process parameters: reflow profile (zone temperatures, conveyor speed), stencil design (aperture sizes and shapes for each pad), placement machine settings (speed, force, nozzle selection per component), and solder paste specifications. An experienced process engineer looks at the BOM — component mix, package types, thermal mass distribution, board characteristics — and draws on hundreds of prior programs to estimate starting parameters. A junior engineer starts from the component manufacturer's generic recommendations and iterates empirically, producing 5-15% higher scrap during ramp. This experiential judgment is the most valuable and least transferable knowledge in HMLV electronics manufacturing.

## Why Nobody Has Built This
The prediction requires a structured representation of BOM characteristics (component package mix, thermal mass per board zone, moisture sensitivity levels) correlated with optimal process parameters and yield outcomes across hundreds of historical programs. This data exists in MES and ERP but has never been organized for ML training — BOM data is stored as line-item lists, not as a feature vector of thermal and mechanical properties. Building the feature engineering pipeline (BOM characteristics → process parameter prediction) requires deep domain expertise in SMT process physics.

## What to Build
A recommendation engine that accepts a new BOM and board specification, computes thermal mass distribution, component sensitivity profile, and board characteristics, finds the most similar historical programs in the facility's production history, and recommends starting process parameters (reflow profile, stencil design rules, placement settings) with confidence intervals. Where the model is uncertain (novel component combinations), it flags the specific parameters needing empirical validation. Integrates with MES to capture yield feedback and refine predictions continuously.

## Target Customer
NPI directors and process engineering managers at HMLV EMS providers launching 20+ new programs per year. Approximately 300-400 US HMLV EMS providers at this scale. Average contract value: $75-150K/year.

## Impact If Built
NPI first-pass yield improves by 3-8% (from typical 85-90% to 93-95%). NPI ramp time decreases from 3-6 months to 1-2 months. Scrap cost during NPI decreases by $50-200K per year for a typical HMLV provider, with corresponding improvement in customer satisfaction and contract retention.
