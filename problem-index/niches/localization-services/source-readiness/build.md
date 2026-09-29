# Checking the Source Before Thirty Languages Do

**Niche:** [[niches/localization-services/source-readiness/profile|Source Readiness]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A defect in the source is a defect in every target language at once.
**Tags:** #automation #large-language-models #evaluation-metrics #data-integration #workflow-orchestration #compliance #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to catch the defects that were created in the source content before they enter thirty language pipelines and multiply — and whoever checks the source takes the account.

## The Problem
Source content is written by people with no localisation training and enters the pipeline unchecked. A string concatenated from fragments cannot be translated grammatically into languages with different word order. A date format hardcoded in text breaks in half the world. An idiom has no equivalent. A string with no context is ambiguous. Each of these produces a query or a defect in every target language, and the cost is attributed to translation rather than to authoring.

## Why Nobody Has Built This
The source is owned by a different team with different priorities, and the cost of its defects lands elsewhere. Localisation is downstream and has no standing to reject input. Checking would slow authoring. And the defects surface as translation problems, so nobody traces them back.

## What to Build
Check the source automatically where it is written and attribute the cost back. Run automated source checks at authoring — concatenation, hardcoded formats, idioms, ambiguous references, length constraints, missing context — which is the core and catches the multiplying defects before they multiply. Require context for every string, since an ambiguous string is the single largest source of queries and the context exists in the author's head at the moment of writing. Flag text embedded in images, which is expensive in every language and trivially detectable. Check for strings reused in different grammatical contexts, which is a common and damaging pattern in software. Attribute downstream query and defect cost back to source defects, which is the evidence that gets authoring to change. Provide the feedback to authors in their own tools rather than as a report to another team. Score source readiness before accepting content into the pipeline, which gives localisation a basis for a conversation it currently cannot have. Estimate the multiplied cost of each defect by the language count, which makes the argument concrete. Educate through the tooling rather than through training sessions. And make the check part of the content pipeline rather than a gate the localisation team operates.

## Target Customer
Enterprise content and product teams, language service providers, content and localisation platform vendors, and technical writing functions.

## Impact If Built
A defect in the source is a defect in every target language at once, and the cost is attributed to translation. Automated checking at authoring, with cost attributed back, catches it where it is one defect rather than thirty.
