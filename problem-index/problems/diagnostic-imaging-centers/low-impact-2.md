# MRI Schedules Built on Average Slot Lengths

**Industry:** [[diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Scheduling software books every MRI into a fixed 30- or 45-minute slot and treats every no-show as random, when exam length and attendance are both predictable from the protocol, the patient and the referral.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #monte-carlo-methods #optimization-fundamentals #time-series-forecasting #automation #revenue-impact

## The Problem
A 1.5T or 3T MRI is the centre's most expensive asset and its revenue ceiling. Schedulers build templates of fixed slots by body part (a brain in 30 minutes, a prostate or cardiac study in 45–60) and book into them first come, first served. Real exam times vary widely. A claustrophobic patient needs a break. An implant needs a modified, slower protocol. A contrast study adds IV start time. A breast MRI with a biopsy follow-up runs over. A knee finishes early. Overruns push the afternoon late and pay technologist overtime, and early finishes leave a magnet idle.

Attendance is just as uneven. In one published outpatient series, 19.3% of MRI appointments were no-shows before a gradient-boosting model and targeted phone calls brought it to 15.9% (AJR). The risk concentrates in long-wait bookings, patients rescheduled before, and certain referral sources. Yet most centres overbook by gut feel or not at all, and fill late gaps only when a scheduler happens to have a waitlist in front of them.

## What Already Exists
RIS scheduling modules (from DeepHealth, Merative, Fujifilm, AbbaDox and others) with slot templates and reminder calls; patient-engagement platforms such as Luma Health that send texts and run waitlists; generic no-show prediction and reminder tools covered under [[scheduling-booking-platforms|Scheduling & Booking Platforms]]; and capacity optimisation sold to hospitals for operating rooms and infusion chairs, analysed under [[general-hospitals|General Hospitals]].

## The Customisation Gap
Imaging needs scheduling that knows the exam. Slot length has to come from the protocol, field strength and coil, contrast and IV time, the patient's history of incomplete scans or sedation, and the technologist's experience. Overbooking has to be priced on the value of the specific slot and the cost of an overrun into the next contrast study. Resource constraints the generic tools ignore must be modelled: a radiologist or qualified physician on site during contrast hours, an anaesthesia-supported block for sedated patients, MR-safety screening time for implant patients, and limited breast or cardiac coils. Waitlist fill also has to respect authorization windows. A patient whose approval expires before the open slot cannot simply be moved up.

## Impact If Solved
Each recovered MRI slot is worth several hundred dollars of technical fee (estimate). A four-magnet centre that fills two more slots per scanner per day, through better slot lengths and priced overbooking, adds roughly $1M–$1.5M a year of completed exams with no new equipment (estimate). It also ends the daily overrun that sends technologists home an hour late.
