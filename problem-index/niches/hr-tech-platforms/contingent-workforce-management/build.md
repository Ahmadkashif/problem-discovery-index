# One View of Everyone Doing Work

**Niche:** [[niches/hr-tech-platforms/contingent-workforce-management/profile|Contingent Workforce Management]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An organisation's people are recorded in the HCM system, accounts payable, a vendor management system, several purchase orders and a services contract, and nobody can produce a single list.
**Tags:** #data-integration #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in contingent workforce software is fighting to give an employer one accurate view of everyone doing work for it, employee or not — and whoever can state total workforce and its classification exposure takes the account.

## The Problem
An executive asks how many people work on a particular product. The answer assembles forty-one employees from the HCM system, and then stalls: there are contractors billing through two agencies, three individual consultants paid on invoice, an offshore team of unknown size under a fixed-price services contract, and two people who were contractors and became employees at some point this year and may be counted twice. Headcount planning, cost analysis, access review, classification risk and business continuity all depend on a number nobody can produce. Every piece of it exists in a system the company runs.

## Why Nobody Has Built This
The population is split across two functions with different systems, different vocabularies and different objectives — procurement manages spend against suppliers, HR manages people against roles — and the entity in the middle, a person who is not an employee, belongs to the data model of neither. Vendor management systems address the agency labour slice for organisations large enough to buy one and leave individual contractors and services contracts untouched. And the diffusion of ownership is not accidental: assembling the view creates obligations — classification review, access governance, co-employment management — that nobody has been assigned.

## What to Build
A worker identity resolved across every system where work is recorded. People are resolved from HCM records, vendor management timesheets, accounts payable invoices, contractor onboarding records and system access provisioning, into a single worker entity with an engagement history — which may include periods as a contractor and as an employee, through different suppliers, at different rates. Engagement attributes are captured deliberately: who directs the work, where it is performed, what equipment is used, how it is paid and how long it has run, because those are the attributes classification turns on and they are currently not recorded anywhere. From that, the organisation gets total workforce by function, true cost including contingent spend, tenure distribution across the contingent population, and a classification risk view that updates as engagements extend. The resolution is the hard part and is the same entity resolution problem that appears throughout this vault, with the added difficulty that the source systems were never designed to identify a person.

## Target Customer
Large and mid-size employers with substantial contingent populations, vendor management and procurement vendors extending into workforce visibility, and HCM vendors for whom total workforce is a natural extension of a headcount system.

## Impact If Built
Total workforce visibility is the precondition for managing classification exposure, access risk and true functional cost, and a surprising number of substantial organisations cannot produce it. The engagement attribute capture is the element with the most direct value, because it converts classification from an assertion made on a form at engagement into a continuously assessable property.
