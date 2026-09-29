# Build: The Boundary, Derived

**Niche:** Scope & System Description
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Derive the system's actual boundary from observed data flows and infrastructure, compare it against the described one, and make the difference part of the engagement.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #change-point-detection #compliance #data-integration #automation
**Contested on:** Whether the boundary of the audit is derived from where the data actually goes, or drawn in a document the audited party writes.

## The Problem

The description says the system comprises the production application, its primary cloud account, and a named set of supporting services. Two third-party processors are carved out. A subsidiary acquired last year is not mentioned.

The auditor reviews it, asks some questions, and accepts it. Testing then covers what the description defined.

Whether the description is complete is the whole question, and the auditor's basis for judging it is conversation. They ask whether anything else processes customer data and are told no. They may look at a network diagram the client produced. They do not independently establish where the data actually goes.

It is observable. The cloud provider knows which accounts exist and which are connected. The identity system knows which third parties hold access. Network egress shows where data leaves. A data map, if the client has one, shows the flows. Comparing the described boundary against any of those would reveal the systems in the path that the description omits.

Nobody performs the comparison, so the boundary remains the client's assertion, and an assertion drawn by the party whose interest is a smaller audit.

## Why Nobody Has Built This

**The description is the client's deliverable by design.** The attestation model has management assert and the auditor examine, which puts the description on the client's side of the line.

**Challenging scope loses engagements.** A firm that pushes hard on boundaries is harder to work with than one that does not, in a market where the client selects the auditor.

**Deriving the boundary requires access.** Cloud inventories, identity data and network telemetry are the client's systems, and an auditor requesting them for scope verification is asking for something outside the normal evidence pattern.

**The reader cannot reward the effort.** A firm that verified the boundary produces the same report as one that did not.

**Exclusions are frequently legitimate.** Many carve-outs are proper and well founded, which makes it harder to argue that verification is necessary — though the legitimate ones would survive verification easily.

**Nobody tracks scope over time.** A boundary that quietly narrowed between periods is not flagged anywhere, so the drift is invisible even to a returning auditor.

## What to Build

**Derive the estate from the client's own systems.** Cloud account inventory, identity grants, egress destinations, data platform lineage. This produces an observed picture of what exists and what connects.

**Compare the observed estate to the described boundary.** Systems in the path that the description does not mention, third parties holding access that are not disclosed, accounts and environments outside the stated scope. This comparison is the product and it is a diff.

**Ask the client to explain the difference.** Every item observed and not described should have a reason — legitimately out of scope, no customer data, carved out with disclosure. Requiring the reason is the substantive change and most of the time the reasons are fine.

**Track the boundary across periods.** A scope that narrowed between this year and last should be flagged and explained, which is currently invisible.

**Record the challenges.** How many amendments the auditor required to the description, recorded in the workpapers and ideally disclosed. This is a direct measure of how hard the auditor pushed and is exactly what the reader cannot currently see.

**State exclusions prominently.** What is outside the boundary should be at the front of the report, not inferred from what the description does not say.

**Verify the carve-outs.** Subservice organisations carved out should be listed with what they do and what the client relies on them for, so the reader knows what the opinion does not cover.

## Target Customer

Audit firms wanting a defensible quality position, for whom boundary verification is concrete, evidenced and genuinely distinguishing — and who would need the reporting change to be rewarded for it.

Enterprise relying parties, who care most about scope of anything in the report and currently examine it least, and who could require exclusion disclosure from their suppliers.

Standards bodies, who could require observed-boundary verification or prominent exclusion disclosure, which is the collective fix.

## Impact If Built

The boundary becomes evidence rather than assertion, which matters because the boundary determines what the opinion covers and is currently set by the party with an interest in it being small.

The observed-versus-described diff is the artefact, it is a comparison rather than a model, and it uses data the client already has.

And tracking the boundary across periods would catch the quiet narrowing that nobody currently sees, in a report the reader assumes covers the same thing it did last year.
