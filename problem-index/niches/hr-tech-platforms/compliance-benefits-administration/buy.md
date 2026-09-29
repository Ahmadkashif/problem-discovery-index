# Reconciliation Practice From Financial Operations

**Niche:** [[niches/hr-tech-platforms/compliance-benefits-administration/profile|Compliance & Benefits Administration]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Financial operations reconciles every account against an external statement as a matter of routine and has done for a century, and HR systems exchange eligibility files with carriers monthly and reconcile nothing.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #data-integration #compliance #automation #workflow-orchestration
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A bank account is reconciled monthly against a statement, item by item, with breaks investigated and cleared — this is elementary financial control and nobody would run a business without it. An employer sends a benefits eligibility file to a carrier monthly, receives nothing back that it compares, and discovers a discrepancy when an employee is turned away. The same organisation would never treat its cash that way.

## What Already Exists
Reconciliation as a discipline — matching two independent records, classifying breaks, ageing them, investigating and clearing — is entirely standard in financial operations, with mature software, established control frameworks and a large body of practice. Data quality and observability tooling provides the technical machinery cheaply. Benefits carriers accept and produce standard file formats. Every component required is available and the practice is a century old in an adjacent function inside the same company.

## The Customization Gap
The adaptation is to an eligibility record rather than a monetary balance. It requires: (1) obtaining the carrier's own view, which is the foundational obstacle — many carriers send files and receive files without ever returning a full position statement, and asking for one is a contractual and commercial matter as much as a technical one; (2) break classification specific to benefits — an employee missing entirely, a dependent dropped, a plan or tier mismatch, an effective date discrepancy, a terminated employee still active — each of which has a different consequence and a different remedy; (3) severity by consequence rather than by count, since a dropped dependent on a medical plan is an emergency and a stale address is not; (4) ageing and escalation, because these breaks are currently discovered and cleared ad hoc and the ones that persist are the ones that hurt someone; and (5) employee notification as part of the clearing process, which financial reconciliation has no analogue for and which is what distinguishes a control that protects the employer from one that protects the employee.

## Target Customer
Benefits administration vendors, HCM platforms, large employers and the brokers and third-party administrators who sit between them and the carriers.

## Impact If Solved
Reconciliation is elementary control practice applied to a record that determines whether people can get medical care, and its absence is a genuine anomaly in an otherwise well-controlled function. Getting a position statement from carriers is the hard part and is a commercial negotiation the larger employers and brokers could win if they asked collectively.
