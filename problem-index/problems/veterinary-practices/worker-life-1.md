# After-Hours Triage Decision Support for On-Call Vets

**Industry:** [[veterinary-practices|Veterinary Practices]]
**Type:** Worker Life Changing
**One-liner:** The vet on call at 11pm gets a structured triage summary — symptom history, species, age, relevant conditions — before they pick up the phone, and an AI-assisted urgency assessment that helps them decide "see now, see tomorrow morning, or home care instructions" without relying entirely on an anxious owner's description.
**Tags:** #large-language-models #gradient-boosting #feature-engineering #transfer-learning #evaluation-metrics #worker-facing

## The Problem
After-hours on-call is one of the most stressful and disruptive aspects of veterinary practice. The vet receives a call from a panicked pet owner who may be unable to accurately describe or assess their pet's symptoms — "he's not acting right," "she seems uncomfortable," "his breathing looks off" — and must make a triage decision with minimal information and no visual assessment. The stakes are real: missing a true emergency (urinary obstruction in a male cat, GDV in a large breed dog, respiratory distress) can be fatal, but sending every anxious owner to an emergency hospital at midnight is both unnecessary and damages the client relationship. Experienced vets have developed triage scripts and question patterns through years of calls, but newer vets are essentially improvising under pressure in the middle of the night.

## Why It Matters to the Worker
After-hours calls disrupt sleep and personal time — vets may receive 2-5 calls per on-call night, with variable quality of information from callers. The cognitive burden of making a high-stakes medical decision when suddenly awakened, with incomplete information, about a patient the vet has never met, is genuinely difficult. Junior associates bear a disproportionate share of on-call responsibility. Having a structured intake tool that collects the caller's information via SMS/app before the callback — species, age, symptoms, duration, behavior changes — and generates a preliminary urgency score gives the vet a structured briefing rather than a cold call.

## What a Solution Looks Like
A pet owner-facing triage intake app or SMS flow that collects structured symptom information (guided by species-specific question trees), along with the option to upload a short video. The collected information is structured into a triage brief for the vet and scored against known high-urgency symptom patterns (male cat + straining to urinate + no urine production = emergency; dog + distended abdomen + retching = emergency). The vet receives a notification with the brief and score before deciding whether to call back, escalate to an emergency hospital, or send home care instructions. The system doesn't replace vet judgment — it informs it.

## Impact If Solved
Reduces cognitive load and call back time on after-hours calls by 40-60%. In true emergency cases, faster owner action (prompted by a clear "go to emergency hospital now" recommendation) improves patient outcomes. Reduces the after-hours call burden on junior associates and improves sustainability of independent practice employment.
