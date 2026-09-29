# The Mechanism: What "Meaningful Use" Actually Made a Hospital Compute

**Origin:** [[origins/hospital-systems/profile|Hospital Systems]]
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #worker-facing #tacit-knowledge-ml

> Every other mechanism file in this vault's origins asks "what did the system compute to win a competitive advantage." This one asks a different question, because hospitals were not competing: **what did the system have to compute to satisfy a regulator, and what did that requirement leave out?**

## The Attestation Problem

HITECH did not simply pay hospitals to buy software. It paid them to *attest*, annually, that their EHR use crossed specific numeric thresholds defined by CMS — for example, a minimum percentage of patients with an electronically maintained problem list, a minimum percentage of prescriptions issued electronically, a minimum percentage of patients given electronic access to their own records. Fail to clear the threshold and the payment did not arrive; from 2015, fail to clear it and a Medicare payment *penalty* began instead.

This turns a clinical software adoption question into a **measurement-and-reporting problem**: for each of dozens of criteria, count the qualifying events, count the denominator, compute the percentage, and hold the evidence for audit. The EHR vendor's job was substantially to make that computation and its audit trail correct, because getting it wrong put the hospital's incentive payment — and later its Medicare revenue — at risk.

## What Got Optimised, and What Did Not

**Structured data capture was optimised hard**, because it was directly measured. Problem lists, medication lists and computerised physician order entry (CPOE) became close to universal, because "percentage of orders entered via CPOE" was a Stage 1 and 2 criterion with a hard threshold.

**Clinical documentation quality was not measured the same way, and it degraded in a specific, well-documented direction.** The fastest way to clear a structured-data threshold is a template the clinician clicks through rather than a note they compose, and hospitals overwhelmingly built for the metric. The result — extensively reported in physician-burnout literature since — is a shift of documentation labour onto the clinician at the keyboard, producing notes that are more machine-countable and frequently less clinically legible than what they replaced.

**Interoperability was measured weakly relative to its stated importance.** Stage 2's health-information-exchange criteria could be satisfied by demonstrating the *capability* to send a summary-of-care record for a threshold percentage of transitions — not by demonstrating that the receiving system did anything useful with it, or even that the receiving clinician read it. A hospital could clear the bar by transmitting a document nobody on the other end opened.

## The Transferable Pattern

> **When a regulator (or a manager) sets a numeric proxy for a capability it actually wants, the organisation being measured will very reliably optimise the proxy. This is not a failure of compliance — attesting correctly against the stated criteria is the rational response to the stated incentive. The gap between the proxy and the goal is where the real work still has to happen, later, unfunded.**

Hospital systems are the cleanest instance of this in the vault because the proxy and the incentive were both explicit, public and dated. An FDE evaluating any KPI-driven rollout — a sales team hitting a quota metric, a support team hitting a resolution-time SLA, a model team hitting an offline accuracy number nobody has connected to a downstream outcome — is meeting the same shape of problem HITECH created at national scale.

**Sources:** CMS and ONC, *Meaningful Use* Stage 1/2/3 final rules and criteria; ONC-Certified EHR Technology (CEHRT) certification requirements; 21st Century Cures Act (2016), information-blocking rule, as the regulatory acknowledgment that HIE criteria under Meaningful Use had not produced working interoperability; physician documentation-burden literature following EHR mandates (AMA and JAMA Internal Medicine surveys on EHR-associated burnout, post-2012).