# Build: The Gap That Will Cost You the Answer

**Niche:** Pre-Incident Evidence Readiness
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An assessment that maps an organisation's actual logging configuration against the questions a breach investigation must answer, and ranks the gaps by which ones would make notification unanswerable.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #survival-analysis #compliance #automation #data-integration
**Contested on:** Whether an organisation can be told, before anything happens, which of its logging gaps will make the notification question unanswerable.

## The Problem

Organisations receive logging advice constantly. Enable audit logging. Retain logs for a year. Monitor endpoints. Turn on cloud trail. It arrives as best practice, it is generic, it competes with every other security priority, and it is partially implemented on a budget.

The advice does not say what it is for in terms anyone acts on. Turn on file access auditing is a recommendation. Without file access auditing on this share, if an intrusion reaches it, you will be unable to establish which records were read, and your notification will have to assume all of them is an entirely different statement — and it is the one a general counsel will fund.

The firms that could make that statement are the ones that spend their working lives discovering which gaps mattered. Every investigation ends with a list of questions that could not be answered and the specific evidence that would have answered them. Across thousands of engagements that is the most valuable dataset in the industry about what logging actually matters, ranked by how often its absence was consequential.

It is not collected. Each engagement's unanswerable list lives in that engagement's report, and the firm's accumulated knowledge of which gaps recur is held informally by practitioners.

## Why Nobody Has Built This

**Selling prevention is hard.** The return appears only if an incident occurs, which is the standard difficulty with every preventive security investment and is particularly acute for something that improves the investigation rather than preventing the breach.

**It is a different buyer and a different sale.** Incident response is sold to an insurer panel or activated on a retainer under crisis conditions. Readiness is a consulting engagement sold to a CISO in a budget cycle, which is a sales motion most response firms are not built for.

**The recommendations cost money the firm does not receive.** Enabling cloud audit logging and extending retention has real ongoing cost, paid to the cloud provider and the logging vendor rather than to the firm making the recommendation.

**The corpus is not collected.** Each engagement's evidence gaps are recorded in its own report under privilege, and nobody aggregates across engagements.

**Detection assessment already exists and looks similar.** Organisations that buy a coverage assessment believe the question is addressed, and detection coverage is a genuinely different question from investigative coverage.

**Retention advice runs into cost immediately.** The honest recommendation is frequently expensive, and an assessment whose output is a large logging bill is a hard conversation.

## What to Build

**Aggregate the unanswerable lists.** Across the firm's own engagements, which questions could not be answered and which evidence would have answered them, de-identified. This is a corpus the firm already generates and discards, and it is the foundation.

**Map the organisation's actual configuration.** What logging is enabled, at what retention, covering what systems — read from cloud configuration, endpoint deployment, SIEM ingestion and identity provider settings rather than from a questionnaire.

**Model against realistic scenarios.** Not a generic best-practice gap list but: for an intrusion of the shape that actually happens to organisations like this, entering this way, these questions would be answerable and these would not.

**Rank by consequence, in notification terms.** The output is ordered by which gap most expands the notification population if exploited. A gap that turns a two-thousand-record notification into a two-million-record one is the first item, and expressing it that way is what makes it fundable.

**Cost the remediation honestly.** Each recommendation with its ongoing cost, so the organisation can trade a logging bill against a notification exposure. This is the trade they are implicitly making and nobody has ever laid it out.

**Check retention against dwell time, not policy.** Retention should exceed the realistic dwell time for the scenarios that matter, and most retention periods are set by cost and convention. Stating the actual dwell time distribution from the firm's own engagements makes the gap concrete.

**Separate detection coverage from investigative coverage.** An organisation may have excellent detection and poor investigability, which is a common and under-recognised combination — and the assessment should say which it has.

## Target Customer

CISOs and general counsel jointly, since the argument is about notification exposure rather than about security posture and lands better with the two of them in the room.

Cyber insurers, who are the best-aligned buyer of all: an insured with better investigative coverage produces a narrower, cheaper, faster-resolved claim, and insurers have the leverage to require or incentivise it.

Forensics firms as the provider, for whom this monetises a corpus they already generate and creates a relationship before the crisis rather than during it.

## Impact If Built

The advice becomes specific and consequential. Generic logging guidance is ignored; a statement that this gap will make your notification decision unanswerable is acted on.

Ranking by notification consequence expresses the recommendation in the currency the buyer actually cares about, which is the difference between a security recommendation and a business one.

And insurers are positioned to make this standard, because an insured with better evidence produces a materially cheaper claim — which is the mechanism most likely to make this a market rather than a niche service.
