# Fifty-Two Jurisdictions Publish PDFs and Somebody Reads All of Them

**Niche:** [[niches/accounting-firms-smb/tax-software-content-teams/profile|Tax Software Content & Compliance Teams]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Finding what changed on a form, and working out what that means for the calculation, is a reading exercise performed thousands of times between October and January.
**Tags:** #transformers #large-language-models #cnns #workflow-orchestration #data-integration

## The Problem
The season starts with discovery. Every jurisdiction publishes its forms, instructions, schemas and rate tables on its own schedule, in its own format, with revisions arriving through the season. Somebody has to notice every change, decide whether it affects the product, and translate it into a specification for the engineering team.

Change detection is the first job and it is partly mechanical and partly not. A line renumbered is trivial and cascades into every cross-reference. A threshold changed is trivial and easy to miss. A new instruction sentence can alter a calculation without changing any line on the form at all — and that is the change that produces the defect nobody catches.

The second job is harder: mapping a change onto the affected calculation logic. That requires knowing which forms feed which, which worksheets are shared across states, and where the engine's implementation of a rule lives. It is done by analysts who know the codebase and the forms, and it is the bottleneck.

The volume is not stable. State conformity decisions after federal changes, retroactive provisions, and late legislative sessions all compress work into the weeks before the season opens.

## What Already Exists
Document comparison tooling is commodity. Language models read regulatory and instructional text well. Some vendors in adjacent regulatory domains offer change tracking against published sources. PDF extraction has improved enormously.

None produces the required output. Generic diffing shows textual change; it does not say that a changed instruction sentence implies a revised worksheet in three states. Regulatory tracking services report that a document changed, which is the beginning of the work, not the end. And nothing off the shelf knows the vendor's own mapping from a form line to a calculation module, which is where the entire value sits.

## The Customization Gap
**The output is a change to a calculation, not to a document.** Emitting "this instruction revision affects these three worksheets and these two state conformity implementations" requires the vendor's own form-to-logic map as the target — an asset nobody else has.

**Instructions matter more than forms.** The dangerous changes are prose, not layout. Detecting semantic change in instructional text, per jurisdiction, is the core language problem.

**Cross-references are a graph.** Forms feed forms, worksheets are shared, and states conform to federal definitions selectively. Blast radius is graph traversal over the vendor's own content model.

**Jurisdiction conventions differ and must be learned separately.** Each state has its own drafting habits, publication schedule and revision practice, and the vendor has decades of prior seasons per state to adapt on.

**Confidence must route, not decide.** A missed change is a production defect; an over-flagged change is analyst time. The system's job is ranked triage with the source passage attached.

**Late and retroactive changes are the design case.** The system must handle a change arriving after implementation has begun and correctly identify what has to be revisited.

## Target Customer
Director of Compliance Engineering or VP of Tax Content at a tax software vendor, owning both the analyst workforce and the content model.

## Impact If Solved
Change discovery and impact mapping is the pacing item of the entire season and the source of the defects that matter. Turning it from reading into reviewing ranked, scoped, evidence-linked change proposals is what lets a fixed team absorb a growing volume of legislative change against a date that never moves.
