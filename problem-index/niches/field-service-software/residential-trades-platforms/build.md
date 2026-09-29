# Diagnosis Prediction from Symptom and Service History

**Niche:** [[niches/field-service-software/residential-trades-platforms/profile|Residential Trades Platforms]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendor holds millions of symptom-to-diagnosis-to-parts-to-outcome records across every equipment make in the country and dispatches a technician based on a customer's sentence and a dispatcher's memory.
**Tags:** #gradient-boosting #large-language-models #bert #k-nearest-neighbors #confidence-intervals #evaluation-metrics #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in residential trades software is fighting to predict what the job actually is before the truck leaves, and to match the technician and the parts to it — and whoever moves first-time fix rate most takes the account.

## The Problem
A customer calls: the upstairs is not cooling, there is a humming sound, it started yesterday. The call taker records a vague description in a free-text field. The dispatcher assigns whoever is nearest and available. The technician arrives, diagnoses a failed capacitor on a fourteen-year-old unit of a make he has not worked on much, does not have the right one on the truck, and returns Thursday. The information that would have prevented this exists: the same symptom on the same make and age of equipment resolves to a small set of diagnoses with known part requirements, thousands of times a year, in the vendor's own data.

## Why Nobody Has Built This
The symptom text is poor and getting poorer — call takers are measured on call duration, so descriptions are short and non-standard — which makes the input side weak until someone decides to improve it. The outcome labels are also imperfect: the invoice records parts and a flat-rate task code, which is a proxy for diagnosis rather than the diagnosis itself, and the callback linkage that would define failure is frequently not recorded as a callback at all. Both are fixable and neither has been fixed, because vendors have competed on workflow breadth and a prediction that is wrong in front of a customer is a product risk that a scheduling module is not.

## What to Build
A pre-dispatch prediction that returns a ranked set of likely diagnoses with probabilities, conditioned on the reported symptom, the equipment make, model and age where known, the property's service history, the season and the local weather. From that follow the two decisions that matter: which technician — matched on demonstrated success with this equipment and this diagnosis class rather than on a skills checklist somebody filled in — and which parts should be on the truck. The call-taking interface is part of the product, because a small number of structured questions asked at intake improves the prediction far more than any modelling on free text: the system should ask the caller the two questions that most reduce uncertainty, chosen dynamically. Every prediction is checked against the technician's actual diagnosis, which gives continuous calibration and is the feedback loop the category has never closed.

## Target Customer
Residential field service platforms with a large cross-contractor corpus, and directly the larger residential HVAC and plumbing contractors for whom a point of first-time fix is worth several hundred thousand dollars a year.

## Impact If Built
First-time fix improvements of several points are the realistic range, and each point removes return visits that consume a slot, a drive and a customer's goodwill. For the vendor it is the first capability in the category that depends on a corpus rather than on features, which is the only durable position in a market where every competitor can copy a workflow in a quarter.
