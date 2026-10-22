# The Fire Panel That Failed After Cut-Over

**Niche:** [[niches/telecom-resellers/pots-line-replacement/profile|Legacy POTS Line Replacement]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** A line passes a dial-tone check on install day, but the alarm panel's signals don't reach the central station reliably over the new path, and nobody finds out until the next test or the next fire.
**Tags:** #change-point-detection #logistic-regression #feature-engineering #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to inventory every copper line at a multi-site customer and replace each with a service that passes the attached device's own test (fire-alarm signalling, the elevator emergency phone, the fax), and whoever certifies each line working takes the portfolio.

## The Problem
Alarm communicators and older fax and modem devices send tones that compressed voice paths can distort. A technician installs the replacement, hears dial tone, places a test call and leaves. Days later the central station starts logging missed test signals from that site, or nobody notices at all. Elevator phones fail the same way at the next inspection, with the building owner facing the inspector.

## Why It's Still Broken
The installer's job ends at dial tone, and the alarm contractor's job starts at the panel. Nobody owns the end-to-end test, and the central station's view of missed signals doesn't flow back to the reseller who changed the line.

## What a Fix Looks Like
Close out each life-safety line only after a device-level test: a signal received at the central station, an elevator phone answered at the monitoring centre. Record the evidence against the line. Then watch each line's periodic test-call pattern on the replacement device and flag a change when expected test calls stop or fail, before the central station or an inspector does.

## Who Feels the Pain
Building owners failing inspections; alarm contractors chasing missed signals; resellers carrying liability for lines they replaced.

## Impact If Fixed
Life-safety lines are proven working at cut-over and monitored after it, which removes the failure buyers fear most about leaving copper.
