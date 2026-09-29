# Fix: The Disposition Is Whatever Closed the Ticket

**Niche:** Precision Verification
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The field that would measure whether threat intelligence works is filled in by a tired analyst choosing the option that lets them move to the next alert.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #hypothesis-testing #workflow-orchestration #compliance
**Contested on:** Whether, when an indicator fires, anyone can establish that the activity it flagged was genuinely malicious.

## The Problem

An alert fires at eleven at night. The analyst investigates: an internal host connected to an address on a threat feed. The address belongs to a hosting provider. The connection was a single HTTPS request. There is no other suspicious activity on the host. The user was working late.

Is it a true positive? The indicator matched something real — that connection happened. Was it malicious? Probably not, but the analyst cannot prove it was not, and proving it would take another hour they do not have with nine alerts in the queue.

They select false positive and close it. Or benign. Or, at some organisations, true positive with no impact, because the indicator did match. The choice depends on the organisation's conventions, the analyst's habit, and how the dropdown is worded.

Multiply by every alert in every organisation. The resulting dataset is the ground truth on which any measurement of threat intelligence quality must rest, and it is produced by people optimising for queue throughput against a taxonomy that does not describe what they actually concluded.

The analyst is not doing anything wrong. They reached the right operational decision — no action needed — and recorded it in the only vocabulary available.

## Why It's Still Broken

**The taxonomy does not fit the conclusion.** Analysts routinely conclude "matched, investigated, no evidence of harm, not certain" and have to record it as true or false. The most common real outcome has no category.

**Disposition is for closing tickets.** It exists so the case management system can close a case. Nobody designed it as a measurement instrument, and it is used as one by default.

**Throughput pressure is real and constant.** Time spent refining a disposition is time not spent on the next alert, and the analyst is measured on the queue.

**No feedback ever arrives.** An analyst never learns whether their disposition was right, so there is no mechanism by which their classification improves.

**Conventions vary and are undocumented.** Two organisations, and frequently two analysts, use the same categories differently, which makes the data non-comparable even before it is aggregated.

**The ambiguous majority determines the answer.** How unresolved cases are recorded drives any precision figure computed from this data, which means the measurement is largely a measurement of local convention.

## What a Fix Looks Like

**Add an unresolved category and make it respectable.** A disposition for investigated, no evidence of harm found, not conclusively benign. This is the most common real outcome and having nowhere to record it is the single largest source of noise in the data. Making it an acceptable answer rather than an admission also relieves the analyst.

**Capture investigation depth automatically.** Time spent, sources consulted, actions taken — derived from the case record rather than asked for. It costs the analyst nothing and lets any downstream analysis weight confident dispositions above rushed ones.

**Define the categories and publish the definitions.** Written definitions with examples, so two analysts classify the same alert the same way. This is a page of documentation and it is missing almost everywhere.

**Measure agreement on a sample.** Have two analysts independently classify the same alerts periodically. The agreement rate is the reliability of the entire dataset and nobody has ever computed it.

**Adjudicate contested cases.** A standing route for genuinely ambiguous alerts to receive a second opinion, without a throughput penalty. This improves the data and gives the analyst somewhere to take uncertainty other than a guess.

**Give the analyst something back.** Show them, periodically, how their dispositions compared with adjudicated outcomes and with peers. Analysts currently receive no feedback on the judgement that constitutes most of their job.

**Never use disposition data for individual performance.** The moment it is used to evaluate analysts it will be gamed, and the measurement will be worth nothing. This has to be explicit and credible.

## Who Feels the Pain

The analyst, forced to record a binary conclusion about an ambiguous situation, under time pressure, in a vocabulary that does not describe what they found.

Every downstream measurement — detection tuning, feed evaluation, precision estimates — all of which rest on this field and none of which knows how noisy it is.

The security leader, reporting false positive rates that are substantially an artefact of local convention.

And the intelligence vendors, whose product cannot be evaluated because the ground truth is generated under conditions that guarantee it is noisy.

## Impact If Fixed

Adding an unresolved category and defining the terms costs a page of documentation and a configuration change, and would remove the largest source of noise in the data this entire measurement problem depends on.

Capturing investigation depth automatically lets any analysis weight by confidence at no cost to the analyst, which is a rare free improvement.

And measuring inter-analyst agreement once would tell an organisation how reliable its own alert data is — a number that everything from detection tuning to vendor renewal currently assumes and nobody has checked.
