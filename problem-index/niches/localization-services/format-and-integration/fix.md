# The File That Came Back Broken

**Niche:** [[niches/localization-services/format-and-integration/profile|File Format & Integration Engineering]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Fix (Pain Point)
**One-liner:** The translated file corrupted the layout in four languages and nobody noticed until the client opened it.
**Tags:** #quick-win #automation #data-integration #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get content out of a client's systems and back again without an engineer handling every format by hand, and whoever automates that takes the account.

## The Problem
A translated file is delivered and is broken: markup mangled, placeholders lost, encoding wrong, layout destroyed by text expansion, a right-to-left language rendering incorrectly. Nobody at the agency checks, because checking requires opening the file in the client's own application and reading a language nobody there speaks. The client discovers it, frequently at the worst moment, and the agency's competence is judged on a class of failure that is entirely mechanical.

## Why It's Still Broken
Nothing verifies the output — a delivery process that checks the translation and never opens the file cannot notice that the file is broken, and the only party who can is the client. Checking requires the client's tooling. The failure looks like a translation problem. And it happens late enough to be an incident rather than a process.

## What a Fix Looks Like
Verify the file mechanically before delivering it. Validate every delivered file structurally — well-formedness, encoding, placeholder integrity, tag balance — which is the fix and catches most of the class automatically. Check length expansion against any constraints in the format, since text growth is the commonest layout break and is predictable per language. Render the file and compare against the source rendering where the format allows, which catches what structural checks miss. Verify placeholders and variables survived, as those break functionality rather than appearance. Test bidirectional and non-Latin scripts specifically, which fail in ways Latin-script testing never surfaces. Round-trip a sample through the client's own tooling where possible. Block delivery on a failed validation rather than reporting it afterwards. Record which formats and languages fail most, which directs the filter work. Give the client a validation report with the delivery, which changes the relationship. And treat a structural failure as a process defect rather than an incident.

## Who Feels the Pain
Clients opening a broken file at a bad moment; agencies judged on a mechanical failure; linguists whose work is blamed for a format problem; and the release, delayed for a fix that takes minutes.

## Impact If Fixed
A delivery process that checks the translation and never opens the file cannot notice the file is broken, and only the client can. Structural validation before delivery catches most of the class automatically.
