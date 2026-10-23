# Client Setup Generated From the Prior Provider's Records

**Niche:** [[niches/professional-employer-organizations/peo-operating-platforms/profile|PEO Payroll, Benefits & HR Operating Platforms]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every new client arrives with its configuration already expressed in someone else's payroll registers, benefit summaries and handbook, and a PEO implementer re-enters it field by field.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #automation #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to run payroll, benefit deductions, payroll tax and workers' comp reporting for thousands of small co-employed clients on one multi-tenant system, and whoever lets a PEO take on a new client and run its first payroll and benefit deductions correctly with the fewest manual configuration steps takes the account.

## The Problem
Configuring a 30-person client means setting up earnings codes, deduction codes, pay schedules, departments, work locations, tax jurisdictions, workers' comp class assignments, accrual policies and benefit plans with contribution rules. All of it already exists implicitly in the client's last few payroll registers from its previous provider, its benefit summaries and its policies. Implementers translate it by hand, and mistakes surface on the first payroll.

## Why Nobody Has Built This
Every prior provider formats registers differently, and the mapping from "what the old system did" to "how our platform must be configured" sits in implementers' heads. Platform vendors have focused on processing, not intake.

## What to Build
An intake engine that reads prior registers, year-to-date reports, tax filings and benefit documents, and infers the configuration: earning and deduction codes with tax treatment, accrual rules, work-location tax setups, likely workers' comp classes and benefit contribution formulas. It proposes a complete client setup in the PEO's platform with a confidence level on each element, then runs a parallel payroll against the prior provider's last register and explains every difference before go-live.

## Target Customer
Implementation leaders at PEOs onboarding hundreds of clients a year, and the platform vendors that could embed it.

## Impact If Built
Setup time per client cut from days to hours (estimate), and the first payroll, the moment clients judge the PEO by, right the first time.
