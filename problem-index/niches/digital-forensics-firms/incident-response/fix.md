# Fix: Day One Is Spent on Access

**Niche:** Incident Response Engagements
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The most expensive practitioners in the firm spend the most valuable days of the engagement waiting for credentials from a client who is also managing a crisis.
**Tags:** #workflow-orchestration #evaluation-metrics #compliance #worker-facing #automation #confidence-intervals
**Contested on:** Whether the first week of an engagement is spent investigating or spent obtaining access and building an inventory.

## The Problem

The engagement begins. The responder needs read access to the directory, the endpoint platform, the cloud accounts, the SIEM and several SaaS applications.

Nobody can grant it quickly. The identity team is handling the incident. The approval path for an external party is unclear and was never designed for this. The cloud accounts have different owners, one of whom is on leave. The SIEM administrator is the person currently doing containment. And a reasonable question arises that nobody has an answer to — should a forensic team be provisioned through a directory that may be compromised.

So the first day produces a request list. The second produces partial access. By the third or fourth there is enough to work with, and the fifth is spent on the accounts that were missed.

Meanwhile the clock runs. Statutory notification deadlines are counting. Telemetry is ageing out of retention. The attacker may still have access. And the client is paying senior day rates for a team that is largely waiting.

Everyone finds this normal. It happens on most engagements, it is billable, and the alternative — arranging access before an incident — is a conversation nobody has.

## Why It's Still Broken

**Nobody has the conversation in advance.** Retainers cover availability and rates. Access is discussed at activation because that is when it becomes urgent.

**Standing external access is a genuine exposure.** A dormant privileged account for an external firm is a real risk, and the objection is legitimate. The answer is a designed break-glass model, and nobody has designed one.

**The client has never done this.** Most organisations experience one serious incident. They have no procedure because they have never needed one, and they are learning it under the worst conditions.

**The delay is billable.** A week of waiting is a week of engagement, which removes the commercial pressure to fix it.

**Provisioning through a compromised directory is a real dilemma.** The question is correct and the answer — an out-of-band path agreed in advance — requires preparation nobody did.

**Insurer panel activation starts at the incident.** Where the relationship begins with the claim, no preparation was possible.

## What a Fix Looks Like

**Agree the access model before the incident, as part of the retainer.** Which accounts, what scope, what approval path, activated on declaration and expiring automatically. A page, agreed calmly, in a security review with time in it. This is the fix.

**Design for the compromised-directory case explicitly.** An out-of-band access path — separate credentials, a separate identity source, or a pre-agreed emergency mechanism — so the question has an answer before it is asked at two in the morning.

**Name the people and the backups.** For each platform, who can grant access and who can if they cannot. Most delay is finding the person, not the decision.

**Write the export procedures down in advance.** Per platform, the specific steps to export the logs a responder will need. Written once, calmly, by someone who is not in a crisis.

**Rehearse it annually.** Execute the access path and a test collection. Preparation that has never been tested fails, which is the consistent finding in every emergency discipline.

**Insurers should require it.** The parties funding the response have the leverage to make readiness a condition, and the claim cost difference between a day-one and a day-six start is substantial and directly measurable.

**Measure and report time to first evidence.** From engagement start to the first collected data. Firms that track it will improve it, and clients comparing firms would find it a more informative number than anything currently in a proposal.

## Who Feels the Pain

The client, paying senior rates for a waiting team while the statutory clock runs and their evidence ages out.

The responder, unable to start the work they were called for and spending their first days on access requests.

The client's own security team, handling containment and simultaneously fielding provisioning requests, which is the worst possible time to ask them.

And the investigation, which begins after several days of evidence has expired and after the attacker has had several more days inside.

## Impact If Fixed

A pre-agreed access model recovers several days of the most valuable week in an engagement, and it costs one conversation held in advance.

Designing the compromised-directory case beforehand answers the question that most reliably stalls provisioning, and it is a design decision rather than a technology.

And measuring time to first evidence would give firms something real to compete on and clients something meaningful to compare — in a market where proposals currently compete on credentials and rates.
