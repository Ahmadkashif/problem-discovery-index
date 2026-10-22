# Home-Cage Video That Turns Observations Into Data

**Niche:** [[niches/biotech-research-firms/discovery-in-vivo-pharmacology/profile|Discovery In Vivo Pharmacology]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clinical observations of animals are scored by a technician once or twice a day, by eye, unblinded, when the animal's behaviour is continuous and could be recorded objectively.
**Tags:** #cnns #lstms-and-grus #object-detection #change-point-detection #tacit-knowledge-ml #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make a non-GLP efficacy study trustworthy enough to move a programme — randomised, blinded and completely recorded — and whoever makes the efficacy signal reproduce in the next study takes the account.

## The Problem
Technicians check each cage, score posture, activity, grooming and body condition, and decide when an animal has reached a humane endpoint. Experienced technicians notice a sick mouse before the scores change, but that read is not recorded, differs between people and shifts with workload. Efficacy readouts that depend on behaviour inherit the same variability.

## Why Nobody Has Built This
Home-cage monitoring needs special racks and cameras that many vivaria lack. Models trained in one facility's lighting and strains transfer poorly. Labelled data — the experienced technician's judgement paired with video — has never been collected systematically.

## What to Build
Overhead video on standard racks with models for activity, posture, feeding and social behaviour per animal, change-point alerts when an animal departs from its own baseline, and a labelling loop in which technicians confirm or reject alerts so the model learns their read. Readouts are blinded to dose group and attached to the study record.

## Target Customer
Heads of in vivo sciences at biotechs with their own vivaria; discovery CROs selling reproducibility.

## Impact If Built
Objective, continuous measures replace once-a-day scores, which cuts variability, shrinks group sizes and catches humane endpoints earlier.
