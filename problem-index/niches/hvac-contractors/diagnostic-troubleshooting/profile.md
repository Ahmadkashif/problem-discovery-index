# Diagnostic Troubleshooting

**Parent Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (embedded in service revenue across all HVAC niches)
**Share of Parent Industry:** Embedded function — diagnostic troubleshooting is performed on every service call across residential, commercial, and refrigeration HVAC. The cost of misdiagnosis (unnecessary parts, repeat visits, customer churn) represents $5-8B in annual industry waste.
**Digital Adoption:** Low — Manufacturer-specific diagnostic tools exist (Trane TechAssist, Carrier Aero, Daikin Intelligent Equipment) but are brand-locked, cover only that manufacturer's equipment, and require connectivity that's often unavailable in attics and crawlspaces. No cross-manufacturer diagnostic platform exists.
**Target Buyer:** HVAC service manager, training director, or owner of a service company with 5+ technicians including apprentices and journeymen
**Automation Potential:** Very High — HVAC diagnosis follows a structured pattern (symptoms + measurements = probable cause) that is a classic multiclass classification problem, but the training data has never been systematically collected

## What Makes This a Distinct Niche
Diagnostic troubleshooting is the single most consequential tacit knowledge task in HVAC. It is the moment where an experienced technician's judgment creates or destroys value. The experienced tech arrives at a no-cooling call, puts her hand on the suction line ("too warm"), checks superheat ("15°F high"), checks subcooling ("2°F low"), listens to the compressor ("laboring"), checks amperage ("running 20% over rated load amps"), and in 3-4 minutes has determined: low refrigerant charge, probably a leak at the evaporator coil. A junior technician with the same tools and the same readings doesn't know what the readings mean in combination. Superheat of 25°F could indicate low charge, a restricted metering device, or a failing compressor — the differentiation comes from reading multiple parameters together in the context of the specific system type, age, and environmental conditions. This is pattern recognition developed over thousands of service calls, and it cannot be taught in a classroom. Misdiagnosis costs the industry $5-8B annually: unnecessary part replacements ($200-800 per wrong part), repeat truck rolls ($150-300 each), warranty callbacks, and customer churn when the "fixed" system fails again within weeks.

## Current Tools & Gaps
Manufacturer diagnostic apps (Trane TechAssist, Daikin Intelligent Equipment, Mitsubishi Diamond Contractor app) provide fault codes and basic troubleshooting trees for that manufacturer's equipment only. A technician servicing a Goodman system can't use Trane's diagnostic app. The Measurequick app helps technicians take and interpret refrigerant measurements (superheat, subcooling, target temperatures) but doesn't diagnose — it validates whether the system is operating within spec, not what's wrong when it isn't. HVAC training platforms (Interplay Learning, SkillCat) teach diagnostic methodology through simulation but don't assist in real-time field diagnosis. No tool crosses manufacturer boundaries, ingests multi-parameter measurements, and produces a ranked differential diagnosis with verification procedures.

## Problems
- [[niches/hvac-contractors/diagnostic-troubleshooting/build|🔨 Build: HVAC Diagnostic AI from Symptom + Measurement Data]]
- [[niches/hvac-contractors/diagnostic-troubleshooting/buy|🛒 Buy: Manufacturer Diagnostic Tools Are Brand-Specific]]
- [[niches/hvac-contractors/diagnostic-troubleshooting/fix|🔧 Fix: Junior Technician Misdiagnosis Rate]]
