# Build: Report Assembly From the Evidence

**Niche:** Assessment Deliverable Production
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A deliverable system where findings are structured objects carrying their own evidence, and the report, the board summary and the appendix are all rendered from them.
**Tags:** #large-language-models #bert #evaluation-metrics #word-embeddings #workflow-orchestration #automation #worker-facing
**Contested on:** Whether the report that carries the engagement's judgement is assembled from the evidence that produced it or retyped from scratch.

## The Problem

A practitioner finishes the analysis on day six of a ten-day assessment. The findings exist: in their notes, in a spreadsheet of metrics, in screenshots, in a half-written summary, in their head. Days seven through nine are spent turning that into a document.

The work is transcription and reconciliation. Each finding is written out in prose. Each number is retyped from wherever it was computed, which means it can be and sometimes is wrong. Each chart is rebuilt in the presentation tool. The executive summary is written last and has to agree with a body that has been edited since. Then the board version is made by copying and cutting, after which the two documents begin to diverge and every subsequent edit has to be applied twice.

Three days of a senior practitioner at an advisory rate is a meaningful fraction of the engagement's economics, spent on a task with no judgement in it. And the errors it produces are the embarrassing kind — a figure that does not match, a severity that changed in one place and not the other, a stale number from the previous client left in a reused template.

## Why Nobody Has Built This

**It looks like a formatting problem.** Framed as "a better template", it attracts no serious investment, and every attempt at that framing has produced something practitioners abandon within two engagements because the constraint is worse than the saving.

**Practitioners guard the prose.** The document is where judgement is expressed and where the practitioner's voice lives. Any system perceived as generating the narrative will be rejected, which means the product has to automate assembly, evidence and consistency while leaving the argument entirely to the author — a narrower and less impressive-sounding scope than most builders want.

**Every practice's format is idiosyncratic and defended.** House style is a real differentiator in a market where quality is otherwise unobservable, so a system imposing a structure sells to nobody, and one supporting arbitrary structures is much harder to build.

**The evidence and the document live in different worlds.** For findings to carry their evidence, something must have structured the evidence — which is the [[niches/fractional-cto-services/evidence-extraction/profile|🎯 Evidence Extraction]] problem. Without it the report system has nothing to assemble from, and with it the report system is mostly a rendering layer. The dependency is why this rarely gets built standalone.

**The buyer is small and the saving is indirect.** Recovered practitioner days convert to revenue only if there is demand to fill them, which in a small practice is not automatic.

## What to Build

**Findings as objects, not paragraphs.** Each finding is a record: the claim, the severity with its basis, the supporting evidence with its source and window, the recommendation, the estimated cost, the confidence. The practitioner writes the claim and the argument in their own words; the structure carries everything around it.

**Evidence bound to the finding, live.** A metric cited in a finding is a reference to the computed value, not a typed number. When the analysis is rerun — which happens constantly during an engagement as access improves — the figures in the draft update. This single property eliminates the most common class of error in advisory documents.

**Render, don't template.** One finding set produces the full report, the board summary, the technical appendix and the investment committee memo, each including the findings at the depth that audience needs. Editing a finding changes every document at once, which is the end of the divergence problem.

**Consistency checking as a release gate.** Before delivery: does every severity in the summary match the body, is every number consistent, is every finding in the summary present in the body, are there residual references to a previous client, does every claim have evidence attached. This is mechanical, it is where reports actually fail, and no current process does it at all.

**A firm-level language library.** Recurring findings — key-person concentration, unsupported framework versions, absent disaster recovery testing — get the firm's accumulated phrasing as a starting point, refined over time. The practitioner edits rather than composes, and the firm's reports become consistent across practitioners, which is itself a quality improvement.

**Structured output feeds the corpus.** Findings as objects are exactly the extraction target [[niches/fractional-cto-services/assessment-calibration/profile|🎯 Assessment Calibration]] needs, so the practice's record accumulates as a by-product of producing the deliverable rather than as an extra task. This is the argument that makes the whole thing worth building rather than buying a template pack.

**Output where clients expect it.** A polished document and deck, matching house style precisely. A web-delivered report is a strictly better artefact and clients in this market want a file, so the rendering has to be excellent rather than clever.

## Target Customer

Boutique advisory and diligence practices of five to fifty practitioners, where report volume is high enough for the saving to be material and there is an operations function to own the templates. Diligence practices are the sharpest case — highest volume, hardest deadlines, most formulaic structure, and a client base that reads many reports and notices inconsistency.

Independent practitioners are a volume market at a much lower price point, reachable only if setup is trivial.

## Impact If Built

Two to three senior days returned per engagement. For a practice running a hundred engagements a year that is a large number, and it converts directly to capacity.

The error class disappears. Live evidence binding and mechanical consistency checking remove the failures that most damage a firm's credibility, and they are failures of process rather than of skill.

And the practice's corpus builds itself, which is the thing every practice wants and none will do as separate work.
