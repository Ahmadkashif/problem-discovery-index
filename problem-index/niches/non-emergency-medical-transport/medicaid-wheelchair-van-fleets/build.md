# Wheelchair-Patient-Vehicle Configuration Matcher

**Niche:** [[niches/non-emergency-medical-transport/medicaid-wheelchair-van-fleets/profile|Medicaid Wheelchair Van Fleets]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system automatically matches a patient's wheelchair type, dimensions, and weight to a vehicle with the correct lift capacity, floor layout, and securement hardware.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #automation #compliance

## The Problem
A scheduling coordinator receives a trip request for a wheelchair patient and must determine: Is this a standard manual wheelchair, a power wheelchair, or a bariatric wheelchair? Does the vehicle's lift handle the combined weight (patient + chair can exceed 500 lbs for bariatric patients)? Does the vehicle's floor layout accommodate the wheelchair's turning radius? Are the securement tie-downs rated for this weight class? Today, this matching is done from memory or by calling the driver to measure the vehicle. Mismatches result in failed pickups — the driver arrives, cannot load the patient, and must call dispatch for a replacement vehicle while the patient misses their appointment. Failed pickups trigger broker penalties and patient complaints.

## Why Nobody Has Built This
Vehicle configurations vary even within the same model — operators customize floor layouts, install different lift brands, and modify securement points over time. No standardized database of vehicle-to-wheelchair compatibility exists. Patient wheelchair specifications are often incomplete in the scheduling system (listed as "wheelchair" with no further detail), and patients may switch between manual and power wheelchairs without notifying the provider. Building a matcher requires digitizing the fleet's vehicle configurations at the individual VIN level and capturing patient equipment details that change over time.

## What to Build
A configuration matching engine that maintains a detailed profile for each vehicle (lift capacity in pounds, lift platform dimensions, floor layout with securement point positions, door clearance height) and each patient (wheelchair type, dimensions, combined weight, special equipment like oxygen tanks or IV poles). When a trip is scheduled, the engine filters available vehicles to only those physically compatible with the patient's equipment, eliminating impossible assignments before dispatch. The system learns from failed pickup reports to flag configuration mismatches it was not previously aware of.

## Target Customer
NEMT operators with 15+ wheelchair vans who experience 5-10% failed pickups due to vehicle-wheelchair incompatibility, each failure costing $50-$150 in wasted driver time and broker penalties.

## Impact If Built
Reduces wheelchair-related failed pickups by 80-90%, saving $30K-$100K annually per fleet in wasted dispatch, broker penalties, and patient rescheduling costs. Improves patient satisfaction scores that directly affect broker contract retention.
