# Discharge Instruction Generation Tailored to Urgent Care Diagnoses

**Industry:** [[urgent-care|Urgent Care Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic patient education tools produce discharge instructions that are hospital-level verbose and not calibrated to the 15-minute urgent care context — leaving patients confused and driving unnecessary return visits.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
After diagnosing and treating a patient, the urgent care provider is responsible for discharge instructions — what to watch for, when to return, how to take medications, and when to follow up with a primary care doctor. The current workflow is either choosing from a library of pre-written PDF handouts (accurate but generic) or quickly verbalizing instructions that the patient may not retain. Neither approach calibrates the instructions to the patient's specific presentation, their level of health literacy, or their specific prescription. A patient discharged with a diagnosis of "viral pharyngitis" and a prescription for dexamethasone gets a handout written for a general population, not one that explains why they received a steroid for a sore throat and what to watch for.

## What Already Exists
Patient education libraries (Krames, Healthwise) integrate with most EHRs and provide well-written general education materials. Large EHRs like Athenahealth have some instruction templating capability. LLM-based tools for patient communication are emerging. What doesn't exist is a system that reads the visit's final diagnosis, medications prescribed, patient demographics, and generates 5 bullet points of specific, plain-language instructions relevant to this exact visit — and calibrates the reading level to the patient's documented language preference.

## The Customisation Gap
Urgent care has a specific instruction context that differs from primary care and the ED: the patient is unlikely to have a PCP they're returning to, they came in for acute symptom relief, and the key message is always "this is when to come back vs. when to go to the ER." The instructions need to include specific return-to-urgent-care criteria vs. go-to-ER criteria, which generic education tools blur together. Medication-specific instructions (take this with food, this will make you drowsy, finish the full course) should be auto-integrated from the prescription. None of the existing tools do this for the urgent care context specifically.

## Impact If Solved
Reduces unnecessary return visits (estimated 8-12% of return visits are for reassurance that discharge instructions didn't provide) and reduces patient anxiety and after-hours call volume. For staff, it eliminates 2-4 minutes of manual instruction selection per complex discharge.
