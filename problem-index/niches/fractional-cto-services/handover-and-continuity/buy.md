# Buy: Architecture Decision Records for Advisors

**Niche:** Handover & Continuity
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Architecture decision records already solve capturing why a technical choice was made and are built for teams documenting themselves, not for an advisor writing for successors they will never meet.
**Tags:** #large-language-models #bert #word-embeddings #data-integration #workflow-orchestration #automation #worker-facing
**Contested on:** Whether the reasoning behind a technical direction survives the departure of the person who set it.

## The Problem

The engineering profession solved this problem for itself a decade ago. An architecture decision record is a short document capturing the context, the options considered, the decision and its consequences, written at the time of the decision and kept beside the code. Where the practice is followed, an engineer joining three years later can understand why the system is shaped as it is.

The advisory profession, whose entire structural problem is that its reasoning leaves the building with its author, has essentially not adopted it. Advisory deliverables are decks and reports; decisions appear as conclusions with a supporting argument aimed at approval, not as records aimed at a successor.

The adaptation needed is not conceptual — the format is right and proven. It is that the tooling assumes a team documenting its own ongoing work in its own repository, and an advisor is a temporary outsider writing for people who will inherit the consequences.

## What Already Exists

The ADR pattern itself is well established, with widely used templates (Nygard's original, MADR, the Y-statement form) and tooling: `adr-tools` for filesystem-based records, Log4brains for a browsable ADR site, and native support or conventions in Backstage, Confluence, Notion and most documentation platforms. Backstage in particular has a strong position as an engineering catalogue where decisions can live beside the services they concern.

Adjacent: meeting transcription and summarisation platforms (Otter, Fireflies, Granola, and the native transcription in the major conferencing tools) now reliably capture and structure what was said in a meeting. Knowledge management platforms handle storage, search and permissions. Interim executive transition planning has mature handover practice in the general management world.

## The Customization Gap

**Authorship is inverted.** ADR tooling assumes the author will be around to maintain the record and that readers share context with them. An advisory ADR is written by someone leaving, for readers with less context, and has to carry background the team version can safely omit.

**Assumptions are not modelled.** Standard ADRs capture context and consequences. They do not capture the specific external facts a decision depends on, as checkable statements with thresholds. This is the gap that matters most, because the failure mode is always a silent assumption becoming false, and no existing template makes that visible.

**No revisit triggers, no owners.** ADRs record that a decision was made. They do not record when it should be reopened or who is responsible for noticing. Adding a trigger with an owner turns a document into a mechanism.

**Capture is manual, at the end.** Tooling assumes an author who sits down to write. The advisory constraint is that rationale must be captured in the meeting where the decision happens, which is where the transcription platforms come in — the technology to draft a decision record from a recorded architectural discussion is now good enough, and nothing has combined the two.

**Where does it live.** ADRs sit in the client's repository, which the advisor may not have write access to, and which the advisor's own practice cannot retain for its corpus. A dual-home model — the client's copy, and a de-identified copy in the practice's own record per [[niches/fractional-cto-services/assessment-calibration/profile|🎯 Assessment Calibration]] — is a tenancy question no ADR tool considers.

**Nothing addresses adoption by the inheritor.** The hardest part is that someone who did not write the records reads them a year later. A walkthrough workflow, an onboarding path through the decision set, and question capture against specific decisions are all absent.

## Target Customer

Backstage-adjacent vendors (Spotify's commercial plugins, Roadie, Cortex, OpsLevel) are the natural home — they already hold the service catalogue decisions attach to, and an advisory edition extends them into a market they do not currently serve.

Documentation platforms with strong client-facing usage — Notion and Confluence — are the low-friction alternative, since advisory practices already deliver into them.

The buyers are fractional CTO practices and interim technology leaders, who would use it as a differentiator in pitches, and client organisations that have already been stranded once.

## Impact If Solved

A proven format reaches the profession with the most acute version of the problem it solves. Advisory work has a harder continuity problem than internal engineering and a decade less practice at addressing it.

Meeting-capture technology makes the unpaid part nearly free, which is the specific change that turns this from a good idea practitioners agree with into something that actually happens.

And the practice's own corpus grows as a by-product, since a structured decision record is exactly the extraction target that makes calibration possible.
