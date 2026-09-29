# Knowledge Manager Against the Product Roadmap

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Type:** Worker Life Changing
**One-liner:** The one person maintaining the knowledge base stops discovering product changes from a customer complaint, because shipped changes surface the articles they invalidated.
**Tags:** #bert #word-embeddings #large-language-models #change-point-detection #transformers #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
Most support organisations have one knowledge manager, sometimes a fraction of one. They own a corpus of hundreds or thousands of articles describing a product that engineering, product and marketing change continuously without telling them.

There is no notification mechanism. Release notes exist and are written for customers. Product changes ship in the app. The knowledge manager finds out that an article is wrong when an agent mentions it, when a customer complains, or when they happen to open the article for another reason.

Their working method is therefore reactive and arbitrary: fix what someone reported, work through a review backlog by age, and write new articles for whatever product asked for. There is no way to know which articles are currently wrong, and the corpus is far too large to audit.

Generative deflection made this considerably worse. The corpus is now answering customers directly and at volume, which means the manager's backlog has become the company's error rate, and they were not given more resource when that happened.

## Why It Matters to the Worker
The role is structurally impossible and is usually held by someone conscientious, which is a bad combination. They are accountable for the accuracy of a corpus describing a product they do not control, with no mechanism to learn about changes.

It is also isolated. Knowledge management sits inside support, reports to a cost centre, and has no standing with product or engineering. Asking a product manager to notify them of changes is a favour, not a process, and favours do not survive a busy quarter.

The work is invisible when it goes well and highly visible when it does not. Nobody notices a correct article. Everybody notices when an automated answer tells a customer something false.

And they know which articles are probably wrong — the ones for the areas that changed most — but have no evidence, so prioritisation is instinct.

## What a Solution Looks Like
Change linkage. Release notes, changelogs, configuration changes and even UI string changes can be mapped to the articles that reference them, so a shipped change produces a specific review queue rather than silent invalidation. This is the single highest-value fix and is entirely mechanical.

Behavioural staleness signals, ranked. Articles viewed and then followed by a ticket on the same topic. Agents contradicting an article in their replies. Generative answers on a topic that were rejected or escalated. Each of these is observable and each identifies a probably-wrong article with evidence.

Coverage gaps from ticket clustering: topics generating volume with no article are the corpus's missing pieces and are identifiable without anyone guessing.

Drafting assistance, so writing an article means editing something grounded in the resolutions agents actually gave rather than starting from an empty page.

And an error rate. The knowledge manager should be able to state how accurate the corpus is, from sampled adjudication, because that number is the only way the role gets resourced proportionally to what now depends on it.

## Impact If Solved
The knowledge base became load-bearing when generative answering shipped, and it is maintained by one person with no visibility into what changed. Linking product changes to affected articles and surfacing behavioural staleness gives that person, for the first time, a defensible way to spend their week.
