# Minutes Logged by Stopwatch and Lost on Audit

**Niche:** [[niches/physician-practices/chronic-care-management-programs/profile|Chronic & Advanced Primary Care Management Programs]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Care managers type minutes into a field after each call, the 20-minute threshold invites rounding, and an audit finds the time logs do not match the phone records.
**Tags:** #data-integration #descriptive-statistics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep enrolled Medicare patients in monthly care management the practice can bill, and whoever keeps the most patients billable every month with documentation that survives audit takes the account.

## The Problem
CCM bills only when staff time reaches 20 minutes in the calendar month. Time is logged by hand: a call, a chart review, a pharmacy call, a message. Patients at 17 minutes on the 29th get a last call. Some logs are rounded up and some legitimate time is never logged.

## Why It's Still Broken
Phone systems, EHR activity and care-management software each hold part of the time record and are not joined. Vendors paid per billable month have little reason to tighten logs that pass the threshold. Practices have no tool to reconcile them before billing.

## What a Fix Looks Like
Time assembled automatically from phone-system call records, EHR audit trails of chart work and documented messages, attached to each patient-month with the evidence. Months below threshold are flagged early enough for genuine outreach, and no minute is billed without a matching system record.

## Who Feels the Pain
Care managers who reconstruct logs; compliance officers who sign attestations; practice owners facing extrapolated recoupment when an audit sample fails.

## Impact If Fixed
System-backed time could raise billable months by ~5% from minutes now unlogged (estimate) and remove the rounding that drives audit failure. Extrapolated CCM recoupments can reach six figures for a mid-sized programme (estimate).
