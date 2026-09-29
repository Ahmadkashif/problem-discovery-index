# The Analyst Decided What an Ambiguous Instruction Meant and Wrote Code

**Niche:** [[niches/accounting-firms-smb/tax-software-content-teams/profile|Tax Software Content & Compliance Teams]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Tax instructions are frequently unclear, somebody resolves the ambiguity every season, and the resolution survives only as an implementation.
**Tags:** #tacit-knowledge-ml #large-language-models #compliance #evaluation-metrics #worker-facing

## The Problem
A meaningful share of tax content work is interpretation. An instruction is silent on an interaction. Two provisions conflict. A state conforms to a federal definition "as amended" and the amendment created a case the state clearly did not consider. A worksheet's arithmetic implies something its text does not say.

Somebody decides. A senior content analyst reads the authority, considers how the authority has behaved before, sometimes calls the department, and reaches a position. That position is implemented in code and shipped to every firm using the product.

What is recorded is the implementation. The reasoning — what was ambiguous, what the alternatives were, what evidence supported the choice, how confident the analyst was, and what would change the position — is not captured in any structured form. Sometimes there is a comment. Often there is nothing.

Three consequences. Consistency across jurisdictions is unmeasured: the same ambiguity resolved differently in two states by two analysts is invisible until a customer notices. Defensibility is reconstructive: when a firm challenges a computation, or an authority does, somebody reverse-engineers the reasoning from the code. And succession is a live risk in an area where the expertise is specific, senior and thin — a content analyst who has covered a state for fifteen years holds a decade of resolved ambiguities that exist nowhere else.

It also blocks the automation above. A model proposing content changes needs examples of how ambiguous instructions were resolved. The resolutions exist; the reasoning does not.

## Why It's Still Broken
The season leaves no slack. Interpretation happens under the same clock as everything else, and documentation is the first thing dropped.

The artefact is code because code is what ships. Every downstream consumer — the engine, the test suite, the release — is satisfied by the implementation.

And there is a real liability instinct. A written record of an analyst weighing two readings and choosing the more favourable one is a document that would be uncomfortable in a dispute over a firm's returns. That instinct also prevents the vendor demonstrating that its interpretations are considered and consistent, which is its own exposure.

## What a Fix Looks Like
**Record the position, not an essay.** For each resolved ambiguity: the authority, the ambiguity, the position taken, the alternative rejected, the basis, and what would change it. Minutes, on decisions that already take hours.

**Store the "what would change this" field deliberately.** It converts monitoring from general watchfulness into a specific trigger — the next season's change detection can be told exactly what evidence to look for.

**Make positions retrievable across jurisdictions.** The same ambiguity recurs across states, and an analyst covering one state should see how the same question was resolved in four others. This is immediately useful, which is what makes the habit hold.

**Track authority contact.** Where a position rests on a conversation with a department, record it. Verbal guidance is common in this work and evaporates entirely.

**Report cross-jurisdiction consistency.** Where positions on equivalent questions diverge, surface it. Divergence is sometimes correct and should always be deliberate.

**Settle the discoverability question with counsel first.** The current default of recording nothing also means the vendor cannot show a rigorous process, which is a worse position in a dispute, not a better one.

## Who Feels the Pain
Senior content analysts who are the interpretation and cannot cover two states at once; junior analysts inheriting a codebase full of decisions with no rationale; accounting firms whose returns rest on interpretive positions they cannot see or evaluate; and the vendor, whose product claim is correctness and whose interpretive consistency has never been measured.

## Impact If Fixed
The vendor's deepest asset is a body of accumulated interpretation about ambiguous tax authority, and it is stored as source code. Recording the reasoning makes consistency measurable, makes positions defensible when challenged, and creates the labelled corpus without which no automation of tax content work is possible at all.
