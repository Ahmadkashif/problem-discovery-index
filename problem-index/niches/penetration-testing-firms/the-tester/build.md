# Build: Capture While Testing

**Niche:** The Tester
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A capture layer that records evidence, requests and reasoning as the tester works, so the report is assembled from the engagement rather than reconstructed from memory a fortnight later.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #transfer-learning #automation #worker-facing #workflow-orchestration
**Contested on:** Whether the write-up is work the schedule makes room for, or unpaid evening labour squeezed between back-to-back engagements.

## The Problem

A tester finds an authorisation flaw on Tuesday of week one. They understand it completely in that moment: the request, the manipulated parameter, the response proving access, the reason the control fails, the conditions required to reproduce it, the realistic impact.

They write it up eleven days later, in the evening, during a different engagement. What remains is a screenshot, a line in a notes file, and a memory that has to be reconstructed. The reconstruction takes twenty minutes per finding, produces a description slightly less precise than what they understood at the time, and occasionally requires going back to the target — which may no longer be accessible, since the engagement window has closed.

Multiply by forty findings and the write-up is days of work re-deriving understanding that was complete at the moment of discovery. This is the largest single inefficiency in the delivery of a penetration test, and the raw material that would eliminate it — the proxy history, the tool output, the exact requests and responses — is sitting in the tester's own tooling, unused.

## Why Nobody Has Built This

**Testers resist anything that interrupts flow.** The work requires sustained concentration, and a tool demanding structured input at the moment of discovery breaks exactly the state that produces findings. Every note-taking discipline imposed on testers has failed for this reason, which means capture has to be near-passive with a very light annotation step.

**Evidence is sensitive.** Proxy history from an engagement contains credentials, session tokens, exploit payloads and client data. Building a product that ingests and retains it creates a serious handling obligation and a security review that a security firm will conduct thoroughly.

**Firms do not perceive the cost.** Write-up time is unbilled and unmeasured. It does not appear in the utilisation report, so the problem has no number attached and competes poorly for investment against anything that does.

**Report formats vary per client.** A capture-to-report pipeline has to emit into many different templates, which makes the last mile harder than the capture itself.

**Testers own the prose.** The narrative and the impact assessment are where a tester's judgement shows, and anything perceived as generating their analysis will be rejected regardless of quality. The scope has to be capture and assembly, not authorship.

## What to Build

**Passive capture from the tools already in use.** Proxy history, tool output, terminal sessions and screenshots, ingested automatically. The tester changes nothing about how they work — this is the constraint that determines adoption and every previous attempt has failed by violating it.

**A one-key annotation.** At the moment of discovery, a single action marks the preceding request-response pair as evidence for a finding, with an optional sentence of context. Two seconds, no context switch. Everything else — the request, the response, the timestamp, the surrounding traffic — is already captured and attaches automatically.

**Reconstruct reproduction steps from traffic.** The minimal sequence of requests required to demonstrate the finding, derived from the captured history rather than retyped. This is the most tedious part of a write-up and is entirely mechanical given the log.

**Redact automatically and by default.** Credentials, tokens and personal data stripped at capture, with the tester able to reveal where necessary. This has to be the default because the alternative is a report containing a live session token, which happens.

**A firm-level finding library.** The firm's accumulated descriptions for recurring finding classes, offered as a starting point the tester edits. Every firm has written the insecure direct object reference paragraph hundreds of times and starts from nothing each time.

**Assemble, do not author.** Findings as structured objects with evidence bound to them, rendered into whichever client template is required. The tester writes the claim and the impact; the system supplies everything around it — which is the same separation that works in [[niches/penetration-testing-firms/report-production/profile|⚡ Report Production]].

**Structure that serves the other opportunities.** Findings captured as classified objects with evidence are exactly what coverage measurement and remediation tracking need, so the capture layer pays for itself twice.

## Target Customer

Testing firm practice leadership, sold on delivery speed and tester retention rather than on report quality — the argument is that write-up time is a large unmeasured cost and the firm's scarcest resource is spending a third of its effort on it.

Individual testers are the actual adopters and the ones who will veto anything that gets in the way, so the product has to win on their experience first and the firm-level case second.

## Impact If Built

The write-up stops being a reconstruction. Capturing understanding at the moment it is complete, rather than re-deriving it eleven days later, is worth days per engagement and produces a better description.

Reports arrive faster, which directly reduces the staleness problem — every day saved between the last test day and delivery is a day of relevance retained.

And it removes the specific working pattern that drives good testers out of the profession, in an industry where operator scarcity is the binding constraint on everyone's growth.
