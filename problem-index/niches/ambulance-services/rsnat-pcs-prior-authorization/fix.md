# PCS Forms Returned Without Credentials or Dates

**Niche:** [[niches/ambulance-services/rsnat-pcs-prior-authorization/profile|PCS & RSNAT Prior Authorization for Scheduled Transports]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** A signed PCS comes back without the physician's credentials or with a date outside 60 days, nobody notices until the MAC's letter, and another 7-day cycle starts.
**Tags:** #large-language-models #transformers #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep each repetitive patient's Medicare transports paid without prepayment review, and whoever has the fewest RSNAT claim lines denied per 1,000 scheduled round trips takes the account.

## The Problem
CMS's top reasons for non-affirmation are mostly clerical: incomplete PCS sections, a signature from someone other than the attending physician, missing credentials, a date more than 60 days before the start, and notes that do not support the PCS or that come from the ambulance supplier rather than the patient's clinician (CMS MLN6805343). 27.6% of completed FY2024 requests were not provisionally affirmed (CMS statistics).

## Why It's Still Broken
The PCS specialist handles dozens of faxed forms a day, and the defects are small and easy to miss on a scanned page. Nothing checks a returned form before it goes into the packet.

## What a Fix Looks Like
Read every returned PCS and note as it arrives. Check each required section, the signer against the attending physician on file, the credential field and the date window. Check that the notes come from the clinician and describe the patient's condition at the time of transport, and send defects back to the physician's office the same day with the exact field to fix.

## Who Feels the Pain
PCS specialists redoing packets; patients who receive non-affirmation letters at home; and billing directors watching transports go to prepayment review.

## Impact If Fixed
If half of the 7,948 non-affirmed FY2024 requests (28,836 completed less 20,888 affirmed) were clerical defects caught before submission (an estimate), ~4,000 cycles of 7 days each would be saved nationally.
