# Refrigerant System Diagnosis from Manifold Gauge Readings

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Type:** High Impact
**One-liner:** Experienced HVAC technicians who diagnose refrigerant system faults by reading the interplay of suction pressure, discharge pressure, superheat, and subcooling measurements — a multi-variable pattern recognition skill that takes 5-8 years to develop — get that diagnostic reasoning replicated by an ML model that interprets the gauge readings and returns a ranked differential diagnosis before the junior tech makes a costly misdiagnosis.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem #probability-distributions #tacit-knowledge-ml #revenue-impact

## The Problem

A residential split-system air conditioner has a refrigerant circuit where a trained technician reads four primary measurements from their manifold gauge set: suction-side pressure, discharge-side pressure, suction-line temperature (for superheat calculation), and liquid-line temperature (for subcooling calculation). These four numbers, combined with ambient temperature and indoor return air temperature, encode the state of the refrigerant system — compressor health, refrigerant charge level, metering device (TXV/piston) performance, and evaporator/condenser airflow adequacy.

An experienced technician interprets this 6-8 dimensional measurement set against a mental model of how each fault condition shifts the pressure-temperature relationships. Compressor valve failure drops discharge pressure and raises suction pressure simultaneously. Low refrigerant charge reduces both pressures with elevated superheat. TXV restriction raises superheat and lowers suction pressure. These patterns overlap and interact, requiring the technician to reason about the joint state of all measurements — not just individual readings.

A junior technician misreading this pattern makes the most expensive diagnostic errors in HVAC: adding refrigerant to a system with a restricted TXV (making it worse), condemning a compressor that has a capacitor failure (unnecessary $1,200 replacement), or misdiagnosing an airflow problem as a refrigerant problem (replacing charge on a dirty evaporator coil).

## Why It's High Impact

Diagnostic errors in HVAC have direct, large costs:
- A misdiagnosed compressor replacement: $1,200–$2,500 avoidable cost to the customer
- Refrigerant added to a system with a TXV restriction: further refrigerant system damage + return trip
- Repeated callbacks (technician returns to a system they "repaired" that fails again): callback rate is a primary quality metric for HVAC firms; each callback costs the firm a second truck roll with no additional revenue

Beyond error costs, diagnostic speed determines call capacity per day. An experienced tech who diagnoses a system correctly in 15 minutes versus a junior tech who takes 45 minutes means the experienced tech can complete 6-7 calls per day versus 4-5. Multiplied across a fleet of technicians, diagnostic speed and accuracy are the primary drivers of billable call volume.

## What a Solution Looks Like

A mobile app where the technician inputs their gauge readings (suction pressure, discharge pressure, superheat, subcooling) plus the system parameters (refrigerant type, system capacity, ambient temperature, indoor return temperature). The model returns:
1. Ranked differential diagnosis: most likely fault condition, second most likely, third most likely — with probability scores
2. The specific measurement pattern driving each diagnosis (explaining the reasoning)
3. Next diagnostic steps to narrow to confirmed root cause (e.g., "check capacitor microfarad against nameplate rating to distinguish compressor from capacitor fault")
4. Parts and labor estimate for each diagnosis scenario (technician can begin preparing parts quote before completing the diagnostic)

The model behaves as the experienced technician's "diagnostic double-check" — a second opinion before committing to a repair recommendation.

## Competitive Landscape

OEM diagnostic tools (Carrier's diagnostic app, Trane's diagnostic guide) provide static lookup tables — "if suction pressure is low, check for X." These are not probabilistic models; they don't reason about the joint state of all measurements and don't produce ranked differential diagnoses. No existing commercial product for residential HVAC does probabilistic diagnosis from gauge readings.

## Implementation Path

Training data: refrigerant system diagnostic records with gauge readings and confirmed diagnoses. Large HVAC service companies running ServiceTitan with structured diagnostic data codes have this — every confirmed repair code (compressor replaced, capacitor replaced, refrigerant added, TXV replaced, coil cleaned) paired with the gauge readings from the service call is a training example. A gradient boosting classifier on the gauge reading feature set, trained on 10,000–30,000 labeled diagnostic calls, is achievable in 8-12 weeks once data is assembled. The feature engineering (computing superheat, subcooling, pressure ratio from raw readings) is domain knowledge that defines the model's input representation.
