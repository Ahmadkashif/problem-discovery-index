# Care Instruction Handoff Failures

**Niche:** [[niches/pet-services/medical-senior-sitting/profile|Specialized Pet Sitting (Medical/Senior)]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Fix (Pain Point)
**One-liner:** Medical pet care instructions are communicated verbally and via unstructured text messages, leading to missed details, dosage errors, and emergency situations that could have been prevented.
**Tags:** #automation #data-integration #workflow-orchestration #worker-facing

## The Problem
A pet owner leaving a diabetic dog with a sitter communicates the care protocol through some combination of: a 20-minute verbal walkthrough during the meet-and-greet (sitter takes notes on phone), a long text message with medication details (buried in a text thread within 2 days), a handwritten note on the kitchen counter, and sticky notes on the medication bottles. By day 3 of a week-long sitting, the sitter is cross-referencing 4 different information sources, unsure if the evening insulin dose is 3 units or 4, and whether the backup medication is for low blood sugar or high blood sugar.

## Why It's Still Broken
Pet owners are not medical professionals — they communicate their pet's care the way they remember it, which is often incomplete, ambiguous, or contradictory across sources. Sitters don't have a standardized intake process because they're solo operators without operational infrastructure. The meet-and-greet (the only in-person handoff) happens when both parties are relaxed, not during the stressful moment when the sitter actually needs the information. No one thinks to document "what to do if the dog refuses food before the insulin dose" because it hasn't happened yet — until it does, at 10pm on a Saturday.

## What a Fix Looks Like
A structured care handoff template that walks the pet owner through every category of care: medications (name, dose, timing, administration method, what to do if pet refuses), feeding (brand, amount, timing, restrictions), medical monitoring (what to check, how often, what's normal vs. concerning), emergency scenarios (specific symptoms and specific actions), and contact priority (owner, emergency vet, regular vet, neighbor with spare key). The completed template becomes the sitter's single source of truth — searchable, checkable, and always accessible on their phone.

## Who Feels the Pain
Pet sitters who carry the stress of medical responsibility with incomplete information, and pet owners who discover mid-trip that their communication was inadequate when the sitter calls with a question they should have anticipated.

## Impact If Fixed
Eliminates the 2-3 "clarification calls" per medical sitting engagement, prevents medication errors caused by ambiguous instructions, and reduces sitter anxiety — a major factor in sitter availability for medical pet care.
