# Delta Checks That Fire on Every Dialysis Patient

**Niche:** [[niches/clinical-laboratories/autoverification-result-review/profile|Autoverification & Result Review]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** A dialysis patient's potassium and creatinine swing between draws by design, so a fixed delta check holds every result and technologists release them all by reflex.
**Tags:** #change-point-detection #feature-engineering #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to take routine result review off technologists' hands, and whoever cuts technologist review minutes per thousand results with no rise in corrected reports takes the account.

## The Problem
Delta checks compare a result with the patient's previous one and hold large changes, catching mislabelled tubes. But dialysis, chemotherapy, transfusion and post-surgical patients change legitimately. Fixed thresholds hold their results again and again, teaching technologists to click release, which is when a genuine wrong-blood-in-tube slips through.

## Why It's Still Broken
Delta rules are set per analyte, not per patient context, and the LIS rarely knows that a draw was pre- or post-dialysis or after a transfusion.

## What a Fix Looks Like
Make delta checks context-aware: pull dialysis schedules, transfusion records and recent procedures from the EHR, and set thresholds by context using the lab's own history. Measure each delta rule's release-unchanged rate monthly and retire or retune the worst.

## Who Feels the Pain
Technologists drowning in predictable holds, dialysis units waiting for results, and patients whose real mislabel is lost in the noise.

## Impact If Fixed
Fewer reflexive releases and more attention on the holds that matter. Cutting delta holds in known-context patients by half on a lab holding ~300 such results a day (estimate) saves over two technologist-hours daily.
