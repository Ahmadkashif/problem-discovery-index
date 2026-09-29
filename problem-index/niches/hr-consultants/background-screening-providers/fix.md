# Every Dispute Is a Labelled Error and They Are Filed as Tickets

**Niche:** [[niches/hr-consultants/background-screening-providers/profile|Background Screening Providers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The company generates thousands of adjudicated examples of its own mistakes every year and files each one as a closed ticket.
**Tags:** #tacit-knowledge-ml #anomaly-detection #data-integration #worker-facing #compliance

## The Problem
When a candidate disputes a report, the firm must investigate and resolve it within a statutory window. A compliance specialist pulls the record, checks the source, contacts the court, and either corrects the file or confirms it. Then the ticket closes.

Each of those is a fully adjudicated determination of whether the firm's process got it right, produced by trained people at real cost. Thousands a year. They are stored in a service desk system, indexed by ticket number and candidate, searchable by nothing anyone would want to ask — which jurisdiction, which record type, which matching path, which failure mode.

So the same failures recur. A county whose disposition codes are routinely misread. A record type that a rule mishandles. A researcher whose adjudications skew one way. The specialists resolving disputes see the repetition clearly and have nowhere to record the observation except a ticket that will be closed and never read again.

## Why It's Still Broken
The function is measured on cycle time. Statutory deadlines are hard, volume is high, and the metric that matters is whether disputes are resolved in time. Nothing in that measurement rewards understanding why the dispute happened, and doing so takes longer than closing it.

Organizationally, disputes sit in compliance and matching sits in operations or engineering. The people who see every error and the people who could prevent them are in different reporting lines, meeting quarterly, exchanging counts rather than cases.

And there is the same defensive instinct that runs through this whole business: a structured, queryable record of adjudicated errors is a document. The legal reflex is not to build one — which leaves the firm unable to see a pattern until it arrives as a class action, at which point the same records get produced anyway, unanalyzed.

## What a Fix Looks Like
Treat the dispute file as the company's most valuable dataset, because it is.

**Structured resolution records.** Every dispute closed with a coded cause: source record error, match error, disposition misread, outdated record, stale data, candidate error. The specialist already determines this to resolve the case; it currently goes in a free text field.

**Linked back to the decision path.** Which search was run, which source returned it, which rule or reviewer matched it, which reportability logic passed it. Without this a dispute says something went wrong; with it, the dispute says exactly where.

**Automatic pattern surfacing.** Disputes clustering by jurisdiction, record type, source, or reviewer are a signal the current process cannot see. Three disputes in a month from one county's disposition codes is a fixable defect and today is three unrelated tickets.

**A feedback loop with a named owner.** Weekly, the dispute patterns should reach the people who own matching and sourcing, as cases rather than counts. This is an organizational fix as much as a technical one and it is the part that actually changes outcomes.

**Reviewer calibration.** Ambiguous matches routed to humans produce decisions that vary by reviewer, and disputes reveal which way each one leans. Feeding that back is straightforward and nobody does it.

## Who Feels the Pain
Compliance specialists, resolving the same failure repeatedly with no way to say so. Operations, unable to distinguish a systemic defect from noise. The general counsel, who learns about patterns from plaintiffs' lawyers. And candidates, who lose jobs over errors the firm has already made and corrected for someone else.

## Impact If Fixed
Dispute volume is a direct cost — investigation labour, corrections, and the litigation tail — and a fraction of it is systemic and fixable. More than that, this is the only ground truth the business has about whether its core product is accurate. Turning it from a ticket queue into a measured feedback loop is what makes every other improvement in this niche possible, and it is built entirely from work the firm is already paying to do.
