# Lineage: Collections Agencies

**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** the predictive dialer — US Patent 4,858,120, *System for regulating arrivals of customers to servers*
**Builder:** International Telesystems Corp
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A collector's only product is a conversation, and almost nobody picks up.

Dial, sit through four rings, get a busy signal, a dead line, an answering machine. Reach rates on consumer debt are structurally low: the people most worth calling are the people most motivated to be unreachable. A collector spent most of a paid hour listening to a telephone ring.

**That idle time was not a nuisance. It was the industry's entire cost structure.** An agency is paid on contingency — a share of what it recovers — so its margin is the ratio of talking minutes to salaried minutes. Everything the trade tried before the mid-1980s attacked the other half of the problem: better scripts, better skip tracing, better collectors. None of it touched the dial tone, and the dial tone was where the money went.

## What Got Built

A machine that deliberately places more calls than it has people to answer.

Autodialers already existed: they worked a list one number at a time and handed the result to whoever was free. The missing piece was arithmetic. **US Patent 4,858,120, filed 18 March 1987 and granted 15 August 1989, describes a system that estimates in real time how long agents will stay on their current calls and what fraction of outbound attempts will reach a live human — then launches new calls *ahead* of agents coming free**, so the connection lands at the moment a collector hangs up.

Read the title: there is no telephone in it. This is a queueing result — a continuously updating estimator, built to stay stable when conditions shift underneath it — pointed at a phone switch. What it produces is the **overdial ratio**: attempts per available agent, held above one, tuned by the hour.

## Who Built It, And Why Them

International Telesystems Corporation, a small Virginia firm founded in 1984. The inventor named on the patent is Douglas A. Samuelson, an operations researcher rather than a telephony engineer.

**That is the explanation.** The switch vendors owned the telephony and had no commercial reason to want fewer, longer calls. The agencies owned the pain but employed collectors, not queueing theorists. The binding constraint was never how to place a call; it was how to forecast a distribution of call outcomes well enough to bet money on it, and keep that forecast honest when a list went cold mid-afternoon.

The economics also closed for only one kind of buyer. Two points of agent occupancy is a rounding error in most businesses. In contingency collections it *is* the business — which is why the capital purchase closed here, and for telemarketers, before anywhere else.

## What It Cost

**The abandoned call.** Overdialling works by being wrong on purpose: sometimes the consumer answers, no collector is free, and they get silence and then a click.

The agency's saved minutes were not created. They were moved — off the payroll and onto the person called, in three-second increments, millions of times a day. That externality is why this artefact has been regulated ever since by people who never bought one.

The deeper cost is structural. Once a dial cost effectively nothing, *frequency* became the strategy rather than a side effect. The FDCPA of 1977 governed what a collector could say. It had no vocabulary for a machine that could say it forty times before lunch.

## What You Still Touch

The pause after you say hello. That is an overdial ratio, tuned by a 1987 estimator, resolving against you.

And the CFPB's Regulation F, effective 30 November 2021, caps the same machine at seven calls in seven days per account — a rule whose entire substance is a number the dialer has no reason to respect.

- [[problems/collections-agencies/high-impact|🔴 Debtor Contactability & Payment Propensity Scoring]] — the successor question, now that dialling more is capped
- [[problems/collections-agencies/worker-life-2|🟢 Non-Contact Time Reduction]] — the 1987 problem, still open at the collector's desk
- [[problems/collections-agencies/worker-life-1|🟢 Collector Emotional Burnout Shield]] — the bill for filling every minute with conversation
- [[niches/collections-agencies/dialer-platform-analytics/profile|Contact Platform Analytics Teams]]
- [[niches/collections-agencies/phone-number-reputation-consent-data/profile|Phone Number Reputation & Consent Data]] — carriers labelling the dialer's output before it rings
- [[niches/collections-agencies/compliance-audit-automation/profile|Compliance Audit Automation]] — proving the seven-in-seven count

**Sources:** Google Patents, US 4,858,120 — *System for regulating arrivals of customers to servers*, inventor Douglas A. Samuelson, assignee International Telesystems Corp, filed 18 March 1987, granted 15 August 1989 (read directly); D. A. Samuelson, "Predictive Dialing for Outbound Telephone Call Centers," *Interfaces* 29(5), 1999, 66–81 (citation confirmed; full text behind a 403 this session, so the paper's own account of first deployments is **not** read here); CFPB Regulation F, 12 CFR 1006, effective 30 November 2021 (seven-calls-in-seven-days presumption); FDCPA, Pub. L. 95-109 (1977). ⚠️ **Not established:** that the patent itself was written for debt collection — the specification names telemarketing, call distribution and traffic control, and **does not mention collections at all**; the collections-first framing comes from trade retrospectives (TCN, Ameyo, Call Center Advisor), which are secondary and mutually derivative. ⚠️ **Contested and unresolved:** commercial primacy. Digital Systems International of Redmond, Washington is credited in several retrospectives with shipping a predictive dialer before ITC's patent was granted; I could not date that product against a primary source. This note claims ITC built the patented pacing algorithm, not that it shipped the first box.
