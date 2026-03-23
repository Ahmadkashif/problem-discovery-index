# Incoming Device Condition Assessment System

**Niche:** [[niches/medical-device-mfg/legacy-device-remanufacturers/profile|Legacy Device Remanufacturers]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No standardized system exists to assess incoming used device condition and automatically route to the correct refurbishment procedure — experienced technicians make this determination by visual inspection and manual testing, and their judgment cannot be easily transferred to new hires.
**Tags:** #cnns #multiclass-classification #tacit-knowledge-ml #worker-facing

## The Problem
When a used endoscope, surgical instrument, or electrosurgical device arrives for remanufacturing, an experienced technician inspects it to determine: (1) is it remanufacturable at all, or is it beyond repair? (2) which specific refurbishment procedures are needed (lens replacement, cable repair, housing refinish, seal replacement)? (3) which components must be replaced versus refurbished? This assessment takes 15-45 minutes per device and is the highest-skill task in remanufacturing — a technician with 5+ years of experience can assess a device in half the time and with 3x fewer errors than a new hire, because they recognize wear patterns, corrosion signatures, and damage indicators that indicate specific underlying failures.

## Why Nobody Has Built This
The incoming device population is heterogeneous — hundreds of device models in varying states of wear and damage. Each model has different assessment criteria. The assessment depends on visual cues (discoloration patterns, surface wear, seal condition) combined with functional test results (light transmission, articulation range, electrical continuity) that together form a diagnosis. This multi-modal assessment has not been formalized into rules — it lives in the technician's head.

## What to Build
A tablet-based assessment tool that guides the technician through a structured inspection workflow per device model, captures photos at standardized inspection points, uses a CNN model to pre-classify condition (corrosion severity, wear grade, seal integrity) from images, combines visual assessment with functional test inputs, and recommends the refurbishment procedure routing and cost estimate. The system learns from the experienced technician's assessment decisions, gradually encoding their judgment into the model.

## Target Customer
Operations managers at remanufacturing facilities processing 50+ devices per week. Approximately 100-150 US medical device remanufacturers. Average contract value: $30-60K/year.

## Impact If Built
Assessment time drops by 30-40% per device. New technician ramp-up time decreases from 12-18 months to 3-6 months. Refurbishment routing accuracy improves by 20-30%, reducing rework from incorrect initial assessment.
