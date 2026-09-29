# Property-Based Testing for Earnings Engines

**Niche:** [[niches/payroll-platforms/regular-rate-premium-calculation/profile|Regular Rate & Premium Calculation]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Property-based testing exists for systems with combinatorial input spaces, an earnings engine with multiple interacting premiums across jurisdictions is the canonical example of one, and it is tested with scenarios a person wrote.
**Tags:** #combinatorics-and-counting #hypothesis-testing #evaluation-metrics #confidence-intervals #automation #compliance #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in wage calculation is fighting to compute the regular rate and every premium correctly for every jurisdiction an employer operates in — and whoever can prove a configuration matches the law takes the account.

## The Problem
Testing an earnings configuration means constructing example timesheets and checking the resulting pay. The combinations — jurisdictions, shift patterns, differential eligibility, bonus periods, consecutive days, daily and weekly thresholds, meal premium triggers — are vastly more numerous than any hand-built suite, and the defects live in the interactions nobody constructed. The same problem in insurance rating, described elsewhere in this vault, has the same answer and neither industry uses it.

## What Already Exists
Property-based and generative testing frameworks are mature and free in every major language, developed precisely for combinatorial input spaces. Model-based testing handles stateful sequences such as a bonus period spanning multiple pay periods. Metamorphic testing addresses cases where the correct output is unknown but the relationship between outputs is knowable — which describes a great deal of wage calculation. The techniques are established and the tooling costs nothing.

## The Customization Gap
The adaptation is to wage law's own invariants. It requires: (1) domain invariants stated explicitly — total pay is monotonic in hours worked, adding an overtime hour never decreases overtime pay, a non-discretionary bonus never decreases the regular rate, premium pay in a state that requires it is never zero when the trigger condition holds — which is the intellectual work and which a payroll compliance specialist can supply once asked in these terms; (2) a timesheet generator producing realistic rather than uniformly random patterns, since real shift patterns concentrate probability where real defects live; (3) cross-jurisdiction metamorphic relations, comparing the same timesheet under two jurisdictions whose rules differ in exactly one respect, which isolates configuration errors that no single-output test can find; (4) multi-period sequence generation for bonus allocation and retroactive recalculation, which is where the most expensive defects are; and (5) failure shrinking presented as a minimal timesheet, so a found defect arrives as a reproducible scenario a payroll specialist can read.

## Target Customer
Payroll providers' engineering and compliance teams, employers running payroll in house, and the audit and consulting firms who verify payroll configurations manually.

## Impact If Solved
Property-based testing finds interaction defects that hand-built suites structurally cannot, and in this domain each defect is an underpayment repeated across every affected employee and period. The invariants are a fortnight of a specialist's time and have never been asked for, which makes this among the highest-leverage unspent efforts in the industry.
