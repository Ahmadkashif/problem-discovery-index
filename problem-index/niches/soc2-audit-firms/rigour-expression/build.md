# Build: A Report That Says What Was Done

**Niche:** Rigour Expression
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured, comparable statement of testing depth, scope exclusions and challenge attached to the attestation, so a relying party can tell one audit from another.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #descriptive-statistics #hypothesis-testing #revenue-impact
**Contested on:** Whether a report can convey how searching the audit was.

## The Problem

An enterprise vendor risk team receives two SOC 2 reports from two suppliers. Both are clean. Both cover the same trust services criteria. Both are issued by firms they have heard of.

One audit tested every change ticket in the period, examined all three cloud accounts including the one the client would rather have excluded, and pushed back twice on the system description. The other sampled twenty-five items per control, accepted a scope covering the primary account only, and took the description as written.

The reports are the same. Not similar — the same artefact, saying the same thing, with the same weight in the vendor risk process.

So the first firm's additional work is invisible and unrewarded. The client who commissioned it paid more and received an identical deliverable. And the relying party, who would absolutely prefer the first, has no way to express that preference because they cannot detect it.

The information exists. The firm knows its population sizes, its sample sizes, what was excluded from scope, and where it challenged the description. It is in the workpapers and it is not in the report.

## Why Nobody Has Built This

**The buyer does not want it.** The company paying for the audit wants a clean report. A report disclosing that scope excluded a subsidiary or that testing was minimal is a worse product for the purchaser.

**The first mover is penalised.** A firm disclosing testing depth invites comparison against competitors who do not, and the disclosure itself looks like a weakness until enough of the market does it.

**The report format is fixed by standard.** Attestation reports have a prescribed structure. Adding material is possible and changing the core is not, which means the standards bodies are the route.

**Relying parties do not ask.** Enterprise vendor risk teams process these reports at volume, accept them as binary, and have never requested depth information — largely because they do not know it varies.

**Comparability requires a standard.** Individual firms disclosing differently produces information that cannot be compared, which is barely better than none.

**The firms competing on price would resist.** Making rigour visible is directly against the interest of the segment competing on speed and cost, which is a substantial share of the market.

## What to Build

**A standard supplementary disclosure.** Population and sample size per control, testing method, scope exclusions with reasons, and the number of description amendments the auditor required. Structured, comparable, attached to the report.

**Define it as a standard, not as a firm's initiative.** The value is entirely in comparability, which means a standards body, an industry group or a coalition of relying parties has to define it. A single firm's format is not a signal.

**Build the demand side first.** A group of large enterprise vendor risk teams stating that they will require the disclosure changes the market immediately, because their suppliers' auditors will produce it. The demand side is where this is winnable.

**Make it machine-readable.** Vendor risk teams process these at volume. A structured format they can ingest and compare across suppliers is what turns the disclosure into something they actually use.

**Report scope exclusions prominently.** What was outside the boundary and why is frequently the most informative thing in an audit and is currently buried in the system description.

**Publish firm-level statistics.** Aggregate testing depth by firm, across engagements, published. This is what would let a market price rigour, and it is the endpoint the disclosure enables.

**Start with the firms who would benefit.** Firms that already test thoroughly have an interest in the comparison existing, and are the natural coalition to push for it.

## Target Customer

Enterprise vendor risk teams at large buyers, who are the relying parties, process these reports at scale, and have the leverage to require a disclosure from every supplier.

Standards bodies, who own the report format and are the only parties who can change the core artefact.

Audit firms that already test thoroughly, for whom the disclosure converts invisible investment into a commercial advantage, and who are therefore the supply-side coalition.

## Impact If Built

The market acquires the ability to price rigour, which is the missing mechanism that has driven competition toward speed and price.

A demand-side coalition of large buyers is the realistic route, because they can require it of their suppliers immediately without waiting for any standard to change.

And machine-readable disclosure is what makes it usable, since vendor risk teams process hundreds of these reports and will only act on information they can compare at scale.
