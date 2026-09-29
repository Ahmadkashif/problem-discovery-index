# The Employee Cannot See the Calculation

**Niche:** [[niches/payroll-platforms/garnishment-wage-attachment/profile|Garnishment & Wage Attachment]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An employee subject to a wage attachment sees a deduction on their pay statement and has no way to check the exemption applied, the priority used or the remaining balance — in a situation where an over-withholding is immediately serious.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in garnishment processing is fighting to turn a court order into a correct deduction — right priority, right disposable income base, right exemption limit — without a person reading the document, and whoever automates that correctly takes the service line.

## The Problem
An employee has a garnishment. Their pay statement shows a deduction with a code. They do not know what disposable income figure was used, which exemption limit was applied, whether the state limit that would have protected more of their pay was considered, how much of the underlying debt remains, or when the order will end. They are, by definition, someone under financial pressure, and the amount taken from their pay is determined by a calculation they cannot see and by a document they may never have received a copy of. If it is wrong against them, they are the only person with any incentive to notice and the only person without the information.

## Why It's Still Broken
Garnishment processing was designed around the employer's obligations to the court and the creditor, both of whom receive information. The employee is a subject of the process rather than a party to it in the system's design, and their notice requirement is satisfied by the order itself. Exposing the calculation has not been requested by the buyer, because the buyer is the employer. And there is an uncomfortable reality that should be named: an employee who can see the calculation is an employee who can challenge it, which creates work.

## What a Fix Looks Like
Show the employee their own calculation. Disposable income as computed, with the deductions that produced it. The exemption limit applied, with the authority — federal or state — and a plain statement that the more protective governs, which is a right many affected employees do not know they have. The priority sequence where there are multiple orders. The remaining balance and the projected end date, which is the single piece of information an employee under a wage attachment most wants and almost never has. A copy of the order itself. And a route to raise a question that goes somewhere, with the arithmetic attached, rather than a call to a payroll line that cannot explain it. None of this is difficult; all of it exists in the processing system; the only reason it is absent is that nobody specified it for the person it concerns.

## Who Feels the Pain
Employees under wage attachment who cannot verify a deduction from their own pay; payroll support staff fielding questions they cannot answer without escalating; and anyone over-withheld, whose only recourse depends on information they do not have.

## Impact If Fixed
Showing the calculation costs nothing and addresses an asymmetry that falls on people already in financial difficulty. The remaining balance and projected end date alone would materially change the experience of being garnished, and the exemption disclosure informs employees of a protection that exists specifically for them and that they are currently expected to assert without being told it applies.
