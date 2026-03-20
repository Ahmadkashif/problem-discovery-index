# SOAP Note Generation from Examination Room Audio

**Industry:** [[veterinary-practices|Veterinary Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Ambient AI documentation tools exist for human medicine but aren't trained on veterinary clinical language, multi-species terminology, or the specific documentation patterns of a vet managing an uncooperative patient while narrating findings aloud.
**Tags:** #large-language-models #transformers #seq2seq #attention-mechanisms #transfer-learning #loss-functions #automation #worker-facing

## The Problem
Veterinary documentation has a unique challenge that human medical scribing tools aren't designed for: the patient is often struggling, vocalizing, or uncooperative throughout the physical examination, making continuous dictation difficult. Vets narrate findings as they examine — "heart sounds clear, no murmur, lungs clear bilaterally, abdomen soft, no pain response on palpation" — while simultaneously restraining the patient, which means audio quality is variable and the narration is non-linear. The clinical terminology is species-specific (a "BCS of 5/9 in a canine patient" means something precise), and the documentation must capture diet, vaccination status, parasite prevention, and follow-up plan — fields that generic medical scribing tools don't structure for.

## What Already Exists
Nuance DAX, Abridge, and DeepScribe serve the human medical documentation market and are reaching strong adoption. They are not designed for veterinary use — their training data is human clinical encounters, their output templates are human SOAP formats, and their terminology models don't cover veterinary diagnoses (VENOM coding, common vet abbreviations like "BAR," "QAR," species-specific clinical terms). A vet using a human medical scribing tool would get a transcript, not a structured vet note.

## The Customisation Gap
A veterinary-specific ambient documentation tool needs: (1) ASR models fine-tuned on vet clinical audio, specifically handling species names, drug names, and clinical abbreviations used in veterinary practice; (2) output templates structured for veterinary SOAP notes including vaccination records, parasite prevention status, and dental scoring; (3) multi-species awareness so that "heart murmur grade 3/6" in a 14-year-old feline generates appropriate follow-up considerations vs. the same finding in a 2-year-old canine. This is a targeted fine-tuning and template problem, not a fundamental research problem.

## Impact If Solved
Returns 1-2 hours per shift of documentation time to the vet — directly translating to 3-5 additional patient slots or, more likely, reduced after-hours burden and improved work-life balance, which is a major driver of veterinary profession attrition.
