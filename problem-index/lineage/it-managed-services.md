# Lineage: IT Managed Services

**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** ConnectWise's professional services automation system (ConnectWise Manage, now ConnectWise PSA) — one database joining a service ticket, the time logged against it and the client agreement that decides whether that time is billable
**Builder:** ConnectWise
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A small IT services firm sold hours, and lost them between three systems.

A client called about a broken printer. Someone wrote it in a helpdesk tool, or a notebook. A technician fixed it and wrote the time on a timesheet. At month end someone else read the timesheets against the client's contract to decide which hours were covered, which were billable and at what rate, and typed an invoice into the accounting package.

Every hand-off leaked. For a firm whose only product was labour, **the gap between work done and work invoiced was the margin.** Moving from break/fix hourly billing to a fixed monthly fee per user or per device made it worse, because now the firm also had to prove to itself which work the fee had already paid for.

## What Got Built

The PSA: a single database for a services firm, where the unit of work, the unit of time and the unit of contract are joined.

In ConnectWise's form, a request becomes a **ticket** on a service board; technicians log **time entries** against the ticket; the client's **agreement** — hours bank, per-device fee, covered and excluded work — decides what each entry does to the invoice. Service-level clocks run on the ticket. Reporting to the client, utilisation reporting to the owner, and the month-end invoice all read the same rows.

Its sibling in the MSP stack is the **RMM agent**, which counts and watches the client's machines. The oldest dated one I could confirm is **Kaseya's Virtual System Administrator**, from a company founded in California in **2000** by Mark Sutherland and Paul Wong. ConnectWise later owned an RMM too — by **11 February 2015** it was buying ScreenConnect to strengthen its RMM product, LabTech.

## Who Built It, And Why Them

ConnectWise, founded in **1982** by Arnie Bellini.

The commercial reason is that the buyer and the builder had the same problem. A generic helpdesk vendor sells ticket closure; a generic accounting vendor sells invoices. Only a firm that itself **sold technician hours under contracts** feels the join between them as money, and so builds the agreement into the ticket rather than bolting billing on afterwards.

The account usually told in the channel is exactly that: that the Bellinis ran an IT services business and built the software to run their own shop before selling it to firms like theirs. **I could not confirm that account against an independent source this session**, nor the year the PSA product first shipped. What is established is the outcome: ConnectWise grew to over 1,200 employees and about $250 million in annual recurring revenue, and was sold to Thoma Bravo in **2019 for $1.5 billion**.

The term "professional services automation" was in book titles by 2002; who coined it was not established.

## What It Cost

**The PSA made the contract the source of truth and the device count an input someone types.** Per-device agreements bill from a quantity in the PSA; the machines themselves are counted by the RMM, a separate product with its own database. The two drift, and the drift is unbilled revenue or over-billing — the reconciliation problem this industry still names.

It also made every piece of work a ticket. That is what allowed billing to be proven, and it is why a password reset carries the same administrative weight as a server rebuild: triage, routing, time entry and closure, all by a person.

## What You Still Touch

Every MSP service manager exporting ticket and time data into a client SLA report, and every month-end device-count reconciliation between PSA and RMM, is working the joins of a system designed so that a services firm could invoice its own labour.

- [[problems/it-managed-services/low-impact-2|🟡 PSA/RMM Data Reconciliation for Accurate Billing]] — the contract in one database, the devices in another
- [[problems/it-managed-services/worker-life-2|🟢 Service Manager Timesheet and SLA Reporting Drudgery]]
- [[problems/it-managed-services/high-impact|🔴 Ticket Triage, Routing, and Automated Resolution for L1 Issues]] — every request a ticket
- [[niches/it-managed-services/billing-reconciliation/profile|Client Billing Reconciliation and Contract Compliance]]
- [[niches/it-managed-services/rmm-psa-vendor-data-teams/profile|RMM & PSA Vendor Data Teams]]

**Sources:** Wikipedia, *Arnie Bellini* (founded ConnectWise 1982; 1,200 employees and $250M ARR; sold to Thoma Bravo in 2019 for $1.5B); Wikipedia, *ConnectWise ScreenConnect* (acquisition announced 11 February 2015 to improve LabTech RMM); Wikipedia, *Kaseya* (founded 2000 in California by Mark Sutherland and Paul Wong; VSA as its RMM web application); Wikipedia, *Professional services automation* (2002 Melik book as earliest reference). ⚠️ **WebSearch was unavailable this session (session cap reached)**; research was by direct fetch only. ConnectWise's own About page carried no history, and there is no Wikipedia article on ConnectWise itself (404). ⚠️ **Not established:** that ConnectWise originated as an IT services firm building for its own use (widely repeated, unconfirmed); the year the PSA product first shipped; the involvement and role of David Bellini; who coined "PSA". The ticket–time–agreement description reflects the current product's documented structure, not a dated first release.
