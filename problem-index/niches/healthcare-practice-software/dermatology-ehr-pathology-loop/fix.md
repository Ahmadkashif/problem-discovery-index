# The Result Nobody Told the Patient About

**Niche:** [[niches/healthcare-practice-software/dermatology-ehr-pathology-loop/profile|Dermatology EHR — the Pathology Loop]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** A dermatology practice can prove a result arrived and was reviewed, and usually cannot prove the patient was told what it meant or that the recommended treatment was ever scheduled, which is where the loop actually breaks.
**Tags:** #survival-analysis #evaluation-metrics #descriptive-statistics #hypothesis-testing #compliance #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in dermatology EHR is fighting to close the biopsy loop — specimen out, result back, matched to the exact lesion it came from, patient told, treatment scheduled — and whoever closes it with the fewest open ends takes the account.

## The Problem
The report comes back as a basal cell carcinoma. The physician reviews and signs it. A staff member is asked to call the patient. The patient does not answer. A voicemail is left, or not, because the practice is careful about what it leaves on voicemail. A portal message is sent to a patient who has never logged in. Weeks pass. The chart shows a reviewed result and a note saying "patient notified" typed by someone who left a message. Nobody scheduled the excision. This sequence is the most common shape of a dermatology malpractice claim, and every step of it looks compliant in the record.

## Why It's Still Broken
"Notified" is modelled as a checkbox, so the record cannot distinguish a conversation from an unanswered call. Scheduling lives in a separate module with no link to the result that required it, so an unscheduled excision is invisible unless someone remembers. The portal is treated as delivery, which is a legal fiction in a population where portal activation is far from universal and skews by age exactly against the patients most likely to have a skin cancer. And there is no report anywhere in the category that asks the obvious question: of malignant results in the last six months, how many have a documented patient conversation and a scheduled or completed treatment.

## What a Fix Looks Like
Replace the checkbox with a state and make the report. Distinguish attempted contact from confirmed contact, and require the latter to be anchored to something real — an answered call logged by the phone system, a portal message that was opened, a returned acknowledgement. Link the result to the treatment it recommends so that "scheduled" is a state the system knows rather than a thing someone remembers. Escalate on the clock, with malignant results on a short one. Then publish the standing report: open malignant results by days since resulting, contact attempts by channel and outcome, and unscheduled recommended treatments. None of this requires a model; it requires a practice to be willing to look at the number, which is the actual obstacle.

## Who Feels the Pain
The medical assistant making the fourth unanswered call and deciding what is safe to say on a voicemail; physicians who signed a result and have no way to know what happened next; and practice owners whose largest liability is recorded as a checkbox.

## Impact If Fixed
Practices that run the report for the first time find open malignant loops measured in weeks. Making contact a state rather than a checkbox also changes staff behaviour immediately, because an attempt that does not close is visible to someone. This is the highest-stakes, lowest-technology fix in the specialty and the one most likely to be resisted, since the first output is an uncomfortable list.
