# Clean Scanning Is a Pattern in the Data and Nobody Models It as One

**Niche:** [[niches/auto-repair-shops/state-inspection-program-operators/profile|State Vehicle Inspection Program Operators]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fraud in inspection programmes is committed by a small number of stations in recognisable ways, and it is caught by rules and audits.
**Tags:** #gradient-boosting #graph-neural-networks #evaluation-metrics #change-point-detection #compliance

## The Problem
Inspection fraud is the programme's central integrity risk. A station passes a vehicle that should have failed — by testing a different, compliant vehicle in its place, by manipulating the connection, or simply by recording a result that did not happen. The motorist gets a sticker, the vehicle keeps polluting, and the programme's entire purpose is defeated.

Operators run controls: rule-based flags on implausible results, covert audits, station visits, and statistical outlier reports on pass rates. These work on the obvious cases.

They are poorly suited to the rest. Rules are static and fraud adapts to them. Pass-rate outliers confound fraud with legitimate variation — a station in an affluent suburb testing newer cars should have a high pass rate. Covert audits are expensive and therefore rare, which makes them a deterrent rather than a detection method.

What the operator has, and does not exploit, is a census with structure. Vehicles move between stations over time. Technicians move between stations. Analyser units have identities. Test sequences have timing. Fraudulent behaviour leaves signatures across those relationships — a vehicle whose readings change implausibly between cycles, a technician whose results differ from colleagues on the same equipment, a station whose failures collapse the week after an audit.

## What Already Exists
Fraud analytics platforms are mature in payments and insurance, and graph analytics tooling is commodity. Anomaly detection over transaction streams is a solved problem class. Some inspection programmes have deployed statistical screening.

None of it maps directly. Payments fraud models assume a high base rate, immediate labels and a tolerant loss function; inspection fraud is rare, labels arrive only from expensive audits, and a false accusation against a small business has legal and political consequences a payments decline does not. Generic anomaly detectors flag outliers without distinguishing fraud from a station that specialises in older vehicles.

## The Customization Gap
**The label is scarce and expensive and must drive the sampling.** Confirmed fraud comes from audits. The model's job is to make the next audit maximally informative — which is an active sampling problem, not a scoring problem, and it is what a generic platform does not express.

**The graph is the discriminator.** Vehicles, stations, technicians, analysers and time form a network, and the strongest signals are relational: the same vehicle producing incompatible readings at two stations, technicians clustering across stations, equipment reassignment preceding a pass-rate shift.

**Legitimate variation must be modelled, not suppressed.** Fleet mix, neighbourhood vehicle age and station specialisation explain much of the pass-rate variance and have to be conditioned out before anything is called anomalous.

**Adaptation is the operating condition.** Detection changes behaviour, so patterns decay after enforcement. Drift monitoring on the detection model itself is a requirement, not a refinement.

**Evidence, not scores.** An enforcement action against a station is a legal proceeding. The output must be an explainable case file with the underlying records, not a risk number.

**Political sensitivity is a design input.** These are state contracts and station operators are constituents. False positives carry costs a payments system never faces, which sets the threshold and the escalation path.

## Target Customer
Director of Programme Integrity or VP of Analytics at an inspection programme contractor.

## Impact If Solved
Programme integrity is the criterion on which these contracts are ultimately judged, because a programme with visible fraud loses political support entirely. Turning detection from static rules and expensive covert audits into relational modelling with audit-guided sampling raises detection at lower cost — and directly supports the effectiveness analysis above, which is meaningless if a share of the underlying records are fabricated.
