# Lease Survival Computed From Production Data

**Niche:** [[niches/oil-and-gas-producers/lease-obligations-hbp/profile|Lease Obligations & HBP Tracking]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a lease is still alive is a rule applied to production, units and shut-in status, and nobody computes it continuously.
**Tags:** #large-language-models #survival-analysis #feature-engineering #workflow-orchestration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to keep every signed lease in force until the operator chooses to release it, and whoever loses the fewest net acres to a missed rental, shut-in payment or continuous-development deadline takes the account.

## The Problem
Lease analysts know which leases are past their primary term, but not, at any moment, which are held, by which well or unit, and what deadline comes next. They check by pulling production reports and unit plats when a question arises, and drilling schedule changes are not checked against obligations until someone notices.

## Why Nobody Has Built This
The data sits in three systems (land, production, drilling schedule) owned by three departments, and the clauses that matter were never abstracted.

## What to Build
A lease-status engine: clause extraction from each lease and amendment into rules; links from tracts to wells and units; monthly production, shut-in and operations data from the production system; and a computed status and next deadline per lease, refreshed monthly. When the drilling schedule moves a well, it shows which leases lose their continuous-development protection, and it drafts shut-in payment and release notices.

## Target Customer
Land departments at operators holding tens of thousands of net acres across many lease forms.

## Impact If Built
At Permian acreage values of thousands of dollars per net acre (estimate), keeping even one 160-net-acre lease a year from lapsing pays for the system many times over. It also turns a quarterly scramble into a monthly report.
