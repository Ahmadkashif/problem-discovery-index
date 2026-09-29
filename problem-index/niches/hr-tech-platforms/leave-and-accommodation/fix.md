# Intermittent Leave Reconciled by Hand

**Niche:** [[niches/hr-tech-platforms/leave-and-accommodation/profile|Leave & Accommodation]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Intermittent leave is taken in hours across months against an entitlement measured in hours, and it is tracked by a leave administrator comparing timesheets to a spreadsheet, which is where both employer disputes and employee shortfalls originate.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in leave and accommodation software is fighting to run an individual's case as an entitlement with a statutory clock rather than as an email thread — and whoever makes the interactive process trackable takes the account.

## The Problem
An employee has certified intermittent leave for a chronic condition, entitling them to a number of hours over a twelve-month period. They take two hours on a Tuesday, a full day three weeks later, an hour for an appointment, and so on across months. Each absence must be coded correctly by a manager or by the employee, deducted from the correct entitlement, and reconciled against the timesheet. In practice absences are coded inconsistently, some are recorded as ordinary sick time and never deducted, others are deducted twice, and the running balance is maintained by a leave administrator in a spreadsheet reconciled monthly. Both errors matter: an employee who is denied leave they still have is harmed, and an employer that cannot evidence its tracking is exposed.

## Why It's Still Broken
Intermittent leave crosses three systems — time and attendance, the leave record and payroll — and the reconciliation between them is nobody's automated job. Coding depends on a manager or an employee selecting the right absence type at the moment of an absence that may be unplanned and unwell, which is the least reliable possible capture point. And the entitlement arithmetic is genuinely fiddly, with rolling periods, hourly increments and concurrent entitlements, which is exactly the kind of thing a spreadsheet does badly and a system does well.

## What a Fix Looks Like
Automate the reconciliation and show the balance to both parties. Absences flow from time and attendance into the leave case automatically, with the coding proposed rather than requested — an absence during a period with certified intermittent leave, for a duration consistent with the certification, defaults to that leave type with the employee able to correct it. The entitlement engine computes the rolling balance in the correct increments against the correct period basis. Discrepancies between timesheet, leave record and payroll are detected and queued rather than discovered at the monthly reconciliation. The employee sees their own balance with the absences that consumed it, which is the single most useful thing this process can give someone managing a chronic condition and is currently unavailable. And the standing report is coding accuracy — how many absences were recoded after the fact — which is the measure of whether the process is working and which no employer computes.

## Who Feels the Pain
Employees managing a chronic condition who cannot tell how much protected leave they have left; leave administrators reconciling three systems by hand every month; and employers whose intermittent leave tracking would not survive scrutiny.

## Impact If Fixed
Automated reconciliation across the three systems removes the most error-prone manual process in leave administration, and it corrects errors in both directions — employees denied leave they had, and entitlements consumed twice. Showing the employee their own balance is the part that most directly helps the person the entitlement exists to protect.
