# Two-Way Reconciliation Against the Carrier's Own Position

**Niche:** [[niches/hr-tech-platforms/benefits-carrier-connectivity/profile|Benefits Carrier Connectivity]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An employer sends a carrier an eligibility file every month and never asks the carrier what it currently believes, so the two records drift and the employee discovers it at a pharmacy counter.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #data-integration #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in benefits administration is fighting to detect that a carrier's record of an employee has diverged from the employer's before the employee is turned away — and whoever finds divergence first takes the account.

## The Problem
An employee has a child in March and adds the dependent through the benefits portal within the enrolment window. The change is recorded in the employer's system. The eligibility file that month either omits it because of a processing rule nobody remembers, or includes it and the carrier's load rejects the record for a formatting reason and continues with the rest. Nothing reports the rejection to anyone. In June the child needs care and the claim is denied, the employee spends two weeks on the phone between HR and the carrier, and the resolution is retroactive if they are fortunate. The employer's system has been correct throughout. The carrier's has not. Nobody compared them.

## Why Nobody Has Built This
The integration was designed as a one-way feed and the architecture has been inherited for thirty years. Carriers produce discrepancy or error reports of varying quality and frequently do not return a full position file, which is the thing reconciliation actually requires — and asking for one is a contractual conversation the benefits administration vendors have not collectively had. There is also a diffusion of responsibility that keeps it unowned: the employer assumes the vendor handles it, the vendor assumes the carrier confirms it, the carrier assumes the file is authoritative, and the employee is the control mechanism.

## What to Build
Reconciliation against the carrier's own position, on a cadence. The carrier's full eligibility position is obtained — by file, by API where available, or by contractual requirement where neither exists — and compared record by record against the system of record. Breaks are classified by consequence: missing member, missing dependent, wrong plan or tier, wrong effective date, terminated member still active, each with a different severity and a different remedy. Severity drives the response, because a missing dependent on a medical plan is urgent and a stale address is not. Transmission and load failures are monitored as first-class events rather than inferred from a discrepancy months later. Ageing and escalation apply, since the breaks that persist are the ones that hurt someone. And the affected employee is notified when a break concerning them is found, which no current product does and which is the difference between a control that protects the employer and one that protects the person.

## Target Customer
Benefits administration vendors, HCM platforms, brokers and third-party administrators, and large self-insured employers who bear both the cost and the employee relations consequence.

## Impact If Built
The failure mode here is a person being denied medical care because two systems disagree, which is a severe consequence from an entirely mechanical cause. Routine reconciliation converts it from an employee-detected event into a break on a list, and the first reconciliation run at any employer of scale reliably finds discrepancies affecting real people who do not yet know.
