# The Missed Punch Resolved a Week Later

**Niche:** [[niches/payroll-platforms/time-to-payroll-handoff/profile|Time-to-Payroll Handoff]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An employee forgets to clock out on Monday and the correction is made by a manager on the following Thursday from memory, which is both an inaccurate record and the most common cause of a pay dispute.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in the time-to-payroll seam is fighting to surface the exceptions that will break a run days before the deadline rather than on the afternoon of it — and whoever moves detection earliest takes the account.

## The Problem
An employee's shift ends and they leave without clocking out. The system records an open punch. Nobody notices until the timesheet is reviewed at the end of the period, at which point the manager — who was not there — asks the employee what time they left, or applies the scheduled end time, or applies a default. The record is now an estimate presented as a measurement, the employee may be paid for less or more than they worked, and if the estimate is systematically low it is an underpayment repeated every time it happens. Missed punches are the single most common time exception in every hourly workforce.

## Why It's Still Broken
Exception detection is batched to the timesheet review because that is when a manager looks at the timesheet, and nothing prompts at the moment the exception occurs. The employee, who knows exactly when they left and is the best available source, is not asked until days later. And the default-application practice is convenient and quietly consequential: applying the scheduled end time to every missed clock-out systematically ignores the overtime an employee actually worked, which is a wage and hour pattern that accumulates.

## What a Fix Looks Like
Detect the exception when it happens and ask the person who knows. An open punch at a time that is implausible for the shift generates a prompt to the employee within minutes — a message on a phone asking what time they finished, which they can answer accurately because it just happened. The manager approves rather than reconstructs. Where no response is obtained, the correction requires an explicit decision with a recorded basis rather than a silent default, and the default itself should not be the scheduled time by convention, since that choice has a systematic direction. Track the correction pattern: an employee or a location with frequent missed punches usually has a clock placement, coverage or process problem, and the rate is a diagnosis rather than a discipline matter. And show the employee their own corrections, so a systematically low reconstruction is visible to the person it affects rather than only to the person making it.

## Who Feels the Pain
Employees whose hours are reconstructed from memory by someone who was not there; managers asked to estimate a time they cannot know; and payroll specialists resolving the same exceptions every period.

## Impact If Fixed
Prompting at the moment of the exception replaces reconstruction with recollection while the recollection is reliable, which is both a better record and a faster close. The correction-rate diagnosis is the useful by-product, because frequent missed punches almost always indicate something fixable about where the clock is or how the shift ends rather than anything about the employee.
