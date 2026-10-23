# Survey Readiness Computed From the Work Record

**Niche:** [[niches/facilities-management-firms/healthcare-facility-operations/profile|Healthcare Facility Operations]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The evidence a surveyor will ask for already exists in work orders and vendor reports, and nobody can say on a given morning which elements of performance it fails to cover.
**Tags:** #large-language-models #bert #gradient-boosting #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep a hospital survey-ready on any given day, with every life-safety test, inspection and deficiency documented the way a surveyor reads it, and whoever walks out of an unannounced survey with no Environment of Care or Life Safety findings takes the account.

## The Problem
A plant director preparing for an unannounced survey has to show, for every applicable element of performance, that tests and inspections happened on frequency, that failures were corrected, and that alternative equipment maintenance decisions are justified. The records are spread across the CMMS, vendor PDFs, generator logs, fire drill reports and construction files. Readiness is judged by a mock survey a few times a year.

## Why Nobody Has Built This
The standards are written in prose with frequency and documentation rules referenced from NFPA codes, and mapping operational records to them required people. Healthcare compliance vendors built for clinical standards, and CMMS vendors built for scheduling.

## What to Build
A readiness engine that encodes the EC and LS elements of performance and their referenced NFPA frequencies for each hospital's systems, classifies every work order, vendor report and log entry against them, and shows daily which elements are fully evidenced, which have gaps and which deficiencies are open past their allowed time. A model trained on past survey findings across hospitals ranks the gaps by likelihood of citation, so the team fixes what a surveyor would actually find.

## Target Customer
Hospital facilities directors and healthcare FM providers responsible for accreditation outcomes across many hospitals.

## Impact If Built
Readiness becomes continuous rather than a pre-survey scramble, and the most-cited chapters stop being the most-cited for the hospitals that use it.
