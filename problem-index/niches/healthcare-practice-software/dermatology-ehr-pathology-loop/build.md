# The Specimen Loop as a Tracked State Machine

**Niche:** [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/profile|Dermatology EHR — the Pathology Loop]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No dermatology platform models a specimen as an object with a lifecycle, so the practice's actual safety net against a lost melanoma result is a spreadsheet maintained by a medical assistant.
**Tags:** #hidden-markov-models #survival-analysis #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #automation #worker-facing
**Contested on:** Every serious competitor in dermatology EHR is fighting to close the biopsy loop — specimen out, result back, matched to the exact lesion it came from, patient told, treatment scheduled — and whoever closes it with the fewest open ends takes the account.

## The Problem
Ask a dermatology practice manager how they ensure every biopsy comes back and gets acted on, and the answer is a log. Someone writes the specimens down when they leave, crosses them off when reports arrive, and checks the uncrossed lines periodically. It works until the person maintaining it is on leave, or until a lab's courier misses a pickup and nobody notices the specimen never reached the lab at all. The EHR contributes a results inbox, which shows what arrived. The thing the practice needs to see is what did not arrive, and the product has no representation for it.

## Why Nobody Has Built This
Modelling a specimen properly means creating an object that lives outside the encounter, outside the order, and outside the result — with its own states, its own timers, and its own escalation behaviour. EHR data models are encounter-centric and this cuts across them, so it never fits in a sprint. The clinical safety framing also works against it: an explicit overdue-specimen queue creates a documented record of known-unreviewed results, which vendors' counsel reliably reads as new liability rather than as the mitigation it is. So the log stays on the medical assistant's desk, where it is nobody's product risk.

## What to Build
A specimen object with an explicit lifecycle: collected, labelled, in transit, accessioned, resulted, matched to lesion, reviewed by physician, communicated to patient, treatment scheduled, closed. Each transition carries a timestamp and an expected duration learned from the practice's own history with that lab, so overdue is computed from real distributions rather than from a guessed constant. Anything that stalls escalates on a schedule that reflects the stakes, with malignant and non-diagnostic results on their own track. Matching to lesion is inference over the requisition text, the lesion map and the procedure record, proposed with a confidence rather than assigned silently. The output the practice has never had is a single board showing every open specimen in the building and how long it has been open.

## Target Customer
Dermatology groups from single-site practices upward, with the sharpest need at multi-site and private-equity-backed groups where no one person can hold the log in their head, and the vendors selling to them.

## Impact If Built
The loop stops depending on an individual. Practices that instrument it for the first time generally find a small number of genuinely open specimens they did not know about, which is the entire point — the value is the tail, not the average. It also converts the practice's largest malpractice exposure from an unmeasured risk into a dashboard number, which is the form in which a malpractice carrier will actually price it.
