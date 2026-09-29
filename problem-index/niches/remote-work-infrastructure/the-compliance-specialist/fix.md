# Fix: The Jurisdiction Leaves When the Specialist Does

**Niche:** [[niches/remote-work-infrastructure/the-compliance-specialist/profile|The Compliance Specialist]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** One person knows how the platform handles a country, they resign, and the knowledge goes with them.
**Tags:** #compliance #descriptive-statistics #workflow-orchestration #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #quick-win #worker-facing
**Contested on:** Whether the knowledge a specialist holds personally will be written down before they leave.

## The Problem

A compliance specialist covers a set of jurisdictions. Over two or three years they accumulate a great deal that is not in the wiki: which local counsel is reliable and which is slow, how the authority in that country actually behaves versus what the statute says, which of the platform's clients have unusual arrangements there and why, what the answer was to a question that came up eighteen months ago, and which parts of the guidance they wrote are confident and which are best guesses.

They resign. There is a handover of two weeks, largely spent on in-flight cases. The accumulated judgement leaves.

The next person inherits a wiki whose confident pages and uncertain pages look identical, no record of past determinations and their reasoning, and no map of which relationships work.

## Why It's Still Broken

The knowledge is tacit and writing it down is unrewarded work competing with a live queue. Nobody has ever been given time for it.

The wiki also has no place for it. It holds statements of the rules, not the metaknowledge about them — which parts are uncertain, which came from which source, what the authority actually does, who to call.

And the risk is invisible until it materialises. A platform with eight specialists covering sixty jurisdictions has eight single points of failure and has never named them as such.

## What a Fix Looks Like

Capture the metaknowledge continuously and make the handover structured.

Add confidence and provenance to every guidance page. How certain is this, where did it come from, what is uncertain about it. Three fields, filled in when the page is written, and they convert a uniform wiki into one where a reader knows what to trust.

Keep a determination log per jurisdiction. The question, the facts, the answer and the reasoning, for every non-routine determination. This is the case law of the platform's own practice and it is the single most useful artefact for a successor. It accumulates as a by-product of the work if there is a field for it.

Record the relationships and the observations. Which local counsel, what they are good at, response times, cost. How the authority actually behaves. Which clients have unusual arrangements and the history behind them. A page per jurisdiction, updated when something is learned.

Map the coverage and name the single points. Which jurisdictions have exactly one person who knows them, as a standing risk register. Naming it is what gets a second person assigned.

Cross-cover deliberately. A second specialist reviewing a sample of determinations in a jurisdiction they do not own builds transferable familiarity and produces the consistency measurement at the same time.

And make the handover structured when it comes. A checklist per jurisdiction — guidance state, open questions, uncertain areas, relationships, clients with history, pending changes — rather than two weeks of conversation about in-flight work.

## Who Feels the Pain

Specialists, carrying jurisdictions personally with no ability to take leave without the coverage degrading, and leaving with knowledge they would happily have written down given time. Their successors, inheriting a wiki with no map of what to trust. Clients, whose determinations in that country are made by someone six months into learning it. And the platform, whose jurisdictional coverage is a set of undocumented single points of failure.

## Impact If Fixed

The metaknowledge that determines whether guidance can be trusted gets captured in three fields as the guidance is written. The platform's own determination history becomes an artefact rather than a memory. And the single points of failure get named, which is the step that precedes doing anything about them.
