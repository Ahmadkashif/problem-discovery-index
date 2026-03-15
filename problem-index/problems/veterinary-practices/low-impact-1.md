# Species- and Weight-Specific Drug Dosing Safety Layer

**Industry:** [[veterinary-practices|Veterinary Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic drug reference tools exist (Plumb's, VIN) but aren't integrated into the prescribing workflow as a real-time calculation and interaction check calibrated to the species, breed, and weight of the specific patient being treated.
**Tags:** #tabular-ml #binary-classification #compliance #automation

## The Problem
Veterinary pharmacology is species-specific in ways that have no human medicine parallel: many drugs that are safe for dogs are toxic for cats (NSAIDs, certain antibiotics), drug metabolism rates differ dramatically by species and breed (sighthound breeds metabolize barbiturates differently; brachycephalic breeds have different anesthetic profiles), and dosing calculations for exotic species (rabbits, birds, reptiles) require subspecialty knowledge that general practitioners access through references rather than memorized dosing ranges. In emergency situations — a seizing dog, a cat in acute respiratory distress — dosing errors occur under pressure. The current workflow is: reach for Plumb's Veterinary Drug Handbook, look up the drug, do the weight-based calculation manually, double-check, then draw up the dose. Each step is manual and error-prone.

## What Already Exists
Plumb's Veterinary Drug Handbook (print and app) is the gold standard reference — comprehensive, authoritative, and widely used. VIN (Veterinary Information Network) provides drug reference databases. Some practice management systems have basic drug calculators. None of these are integrated into the active patient record as a real-time guardrail — they are reference tools consulted separately, not embedded in the prescribing or treatment workflow in a way that prevents errors before they happen.

## The Customisation Gap
What's needed is a dosing calculation engine that runs inside the EHR/practice management system: when a vet prescribes or administers a drug, the system automatically pulls the patient's species, breed, weight, and age, calculates the dose range, flags if the prescribed dose falls outside the safe range for that specific patient profile, and checks the prescribed drug against the patient's known drug list for species-relevant interactions. The species-specificity layer (cats ≠ dogs ≠ rabbits ≠ birds) and the exotic-animal coverage are the customization gap that no general pharmacy tool addresses.

## Impact If Solved
Prevents dosing errors that range from subtherapeutic (the patient doesn't recover) to life-threatening (drug toxicity at correct-for-dog doses given to a cat). In a practice seeing 30-40 patients per day, even a 0.5% dosing error rate on the most dangerous drug categories represents a meaningful patient safety improvement. Reduces the cognitive load on vets under emergency pressure.
