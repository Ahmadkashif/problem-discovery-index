# The Order Read and Applied Without a Processor

**Niche:** [[niches/payroll-platforms/garnishment-wage-attachment/profile|Garnishment & Wage Attachment]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A wage attachment is a document with a jurisdiction, a type, an amount and a set of rules that determine exactly how much may be withheld, and it is turned into a deduction by a person reading it and consulting a reference table.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in garnishment processing is fighting to turn a court order into a correct deduction — right priority, right disposable income base, right exemption limit — without a person reading the document, and whoever automates that correctly takes the service line.

## The Problem
An employee already subject to a child support order receives a creditor garnishment and a state tax levy in the same month. The processor must determine each order's type and jurisdiction, compute disposable income on the correct base for each, apply the priority sequence, apply the exemption limit that is most protective of the employee where federal and state differ, respect the aggregate cap, and decide whether the later orders can be satisfied at all. The rules for all of this are published. The calculation is deterministic. It is performed by a person reading a document under time pressure, for an employee whose financial situation is already difficult and for whom an over-withholding is immediately serious.

## Why Nobody Has Built This
The documents are genuinely varied — thousands of issuing courts and agencies with their own forms — and until recently extraction from them was unreliable. The calculation rules are jurisdiction-specific and have never been assembled as executable content, which is the same content gap that recurs across this vault. And the service line is profitable as a labour business: providers charge per garnishment and staff accordingly, which means the automation displaces revenue as well as cost, and that has been enough to keep the status quo.

## What to Build
Order intake as extraction and the calculation as executable rules. Extraction identifies the order type, the issuing jurisdiction, the amounts, the effective and termination dates and any order-specific instructions, with confidence per field and human review below threshold — the stakes make conservative gating correct rather than cautious. The calculation engine encodes, per jurisdiction and order type, the disposable income definition, the exemption limits, the priority sequence, the aggregate cap and the permitted administrative fee, with effective dates. Concurrent orders are resolved by the engine rather than by a processor's judgement. Every calculation produces a traceable derivation: this base, less these deductions, against this limit, under this authority — which is what makes it checkable by the employer, the issuing authority and, critically, the employee. Termination and balance tracking is automatic, since orders that should have ended and did not are a real and under-detected error class.

## Target Customer
Payroll providers operating garnishment service lines, specialist garnishment processors, and the employers who administer attachments in house.

## Impact If Built
The calculation is deterministic and is currently performed manually at volume for a population who cannot absorb an error. Automating it with a traceable derivation reduces both directions of error, and the termination tracking alone addresses a category — orders withheld past their end — where the money taken was never owed and the person affected is the least equipped to notice.
