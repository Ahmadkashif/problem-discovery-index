# Fifty State Workflows Under a Two-Week Clock

**Niche:** [[niches/hr-consultants/unemployment-claims-management/profile|Unemployment Claims Management]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fifty agencies, fifty deadline rules, fifty portals, and a missed response forfeits the case outright.
**Tags:** #workflow-orchestration #ocr #data-integration #automation #compliance

## The Problem
Every state runs its own unemployment system with its own forms, its own portal or fax or mail intake, its own response window, its own appeal deadlines, and its own rules about what tolls a clock. A national firm operates in all of them simultaneously.

A missed deadline is not a delay. It forfeits the employer's right to contest, raises their tax rate, and is the firm's liability. So the operation runs on deadline discipline: intake, calendar, chase documentation from the employer, draft, file, confirm — across fifty rule sets, at high volume, with the documentation chase being the part that most often runs out of time.

The systems supporting it are case management platforms with state variations bolted on over years, maintained by whoever understands a given state's quirks.

## What Already Exists
Case management and workflow platforms with SLA tracking, deadline calendars, document management, and escalation are mature and plentiful — legal case management, claims administration, and BPM suites all cover this ground competently.

## The Customization Gap
Generic SLA management assumes a service target. This is a statutory forfeiture.

**Deadlines as jurisdiction-specific legal rules.** Calculated from the notice date under that state's own counting convention — business days or calendar, mailing rules, holidays, what tolls and what does not. This is legal logic, it changes when states amend procedure, and it must be versioned so the firm can later show which rule it applied. Generic SLA fields cannot express any of it.

**Backward planning from the deadline.** The binding constraint is usually the employer's response to a documentation request, not the firm's drafting. Work should be scheduled backward from the filing deadline with the employer's own historical responsiveness built in — a client who takes six days to send a termination letter needs to be asked on day one.

**Intake from documents that arrive any way at all.** State notices come as portal messages, PDFs, and paper. Extracting claimant, employer account, separation date, and — critically — the response deadline is the highest-stakes extraction in the operation, and getting the deadline wrong loses the case.

**Fifty filing paths as one orchestration.** Portal submission, upload, fax, and mail, each with its own confirmation semantics. Proof of timely filing is the thing that matters and it looks different in every state.

**Rule changes as a monitored input.** States amend procedures and portals regularly, and the current mechanism is an analyst noticing something has changed. A stale rule silently produces a wrong deadline on every claim in that state.

## Target Customer
Chief Operating Officer or VP of Technology at a national UI claims firm, running high volume against fifty procedural regimes where the failure mode is total.

## Impact If Solved
Missed deadlines are rare and catastrophic, and the effort spent preventing them is enormous and invisible. Encoding the rules properly makes the rare failure rarer while freeing the manual vigilance currently doing that job — and backward planning from the employer's real responsiveness attacks the single most common cause of a late filing.
