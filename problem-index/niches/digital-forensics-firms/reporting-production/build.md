# Build: The Report Assembled From the Record

**Niche:** Reporting & Deliverable Production
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Findings as structured objects bound to their evidence and their reasoning, with every deliverable — technical report, executive summary, insurer version, expert report — rendered from the same record.
**Tags:** #bert #large-language-models #word-embeddings #graph-theory #evaluation-metrics #automation #workflow-orchestration #compliance
**Contested on:** Whether the report is assembled from the investigation's own record, or written from memory during the next engagement.

## The Problem

The investigation produced a great deal of structured material. A timeline in a tool. Evidence items with hashes and provenance. Correlated events. Inferences and their bases, where anyone recorded them.

The report is written in a word processor, from notes and memory, weeks later. The timeline becomes a narrative paragraph. The evidence exhibits are copied in by hand with their references retyped. The findings are described from recollection of work done a fortnight earlier by someone who has since started another engagement.

Then it is produced again for each audience — an executive summary, a version for counsel, a version for the insurer — each a copy with parts removed, which then diverge as edits are applied to one and not the others.

The cost is days of exhausted senior time per engagement. The risk is worse: this is where inconsistencies enter, where a finding gets stated more strongly than the evidence section supports, and where a caveat present in the technical report fails to appear in the summary that everyone will actually read.

Everything needed to assemble most of it exists in the investigation's own record and is not connected to the document.

## Why Nobody Has Built This

**Findings are prose because investigation is narrative work.** The profession writes, and structuring findings as objects feels like reducing analysis to a form.

**Practitioners guard the narrative.** The report is where judgement is expressed, and anything perceived as generating the analysis will be rejected — which narrows the buildable scope to assembly, evidence binding and consistency.

**Structured findings require investigation-time capture.** For a report to assemble itself, the findings and their bases must have been recorded during the engagement, which is the practice change in [[niches/digital-forensics-firms/evidence-bounded-inference/profile|🎯 Evidence-Bounded Inference]].

**Evidentiary rigour raises the bar.** A report that may be used in litigation needs exhibit integrity, provenance and defensibility, which makes automated assembly a higher-stakes engineering problem than in most document domains.

**Audience formats are genuinely different.** An insurer, a regulator, a board and a court want different documents, and rendering all of them well from one source is more than a templating exercise.

**The cost is unmeasured.** Report production time is absorbed into the engagement and is not tracked, so the business case is an anecdote.

## What to Build

**Findings as structured objects.** Claim, supporting evidence with provenance, confidence, the timeline events it rests on, and the caveats. The practitioner writes the claim and the reasoning in their own words; the structure carries everything else.

**Bind evidence by reference.** Exhibits, hashes, timeline events and log excerpts referenced rather than copied, so a late correction propagates and the exhibit numbering cannot drift.

**Render every audience from one source.** Technical report, executive summary, insurer version and expert report generated from the same finding set, each including what that audience needs. Editing a finding changes all of them, which ends the divergence problem.

**Carry the caveats into every rendering.** A qualification attached to a finding appears wherever that finding appears, including the summary. This is the specific failure that produces overstatement downstream and it is fixed by binding rather than by discipline.

**Check consistency mechanically.** Figures agreeing across documents, every summary finding present in the body, every claim carrying evidence, no residual text from a previous engagement. Seconds, and it catches what tired writing produces.

**Preserve the chain of custody through the pipeline.** Evidence provenance carried into the document, so an exhibit's integrity is demonstrable without reconstructing it.

**Draft from the record, let the practitioner write the judgement.** The factual sections — timeline, evidence inventory, systems examined, actions taken — can be assembled. The findings and their interpretation are written, and the tool should not pretend otherwise.

## Target Customer

Forensics firms, sold on recovered senior time and on reducing the error class that damages credibility in litigation.

Firms with expert witness practices, where evidentiary rigour and defensibility are worth more than the time saving and where a report assembled from a provenance-tracked record is a stronger artefact.

Cyber insurers, who receive these reports in volume and would benefit from consistent structure across a panel.

## Impact If Built

Days of exhausted senior time returned per engagement, on work that requires none of the seniority spent on it.

Binding caveats to findings so they appear in every rendering fixes the specific mechanism by which qualifications disappear between the technical report and the summary the board reads.

And a report assembled from a provenance-tracked investigation record is materially more defensible in litigation than one written from memory a fortnight later.
