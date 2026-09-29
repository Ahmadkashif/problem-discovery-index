# Positions Are Published Without the Reasoning Behind Them

**Niche:** [[niches/hr-consultants/employment-law-content-publishers/profile|Employment Law Compliance Content Publishers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** An attorney spends a day deciding how an ambiguous statute applies, and the company keeps the conclusion and discards the day.
**Tags:** #tacit-knowledge-ml #large-language-models #word-embeddings #worker-facing #compliance

## The Problem
Much of employment law is ambiguous at the edges. A new state leave statute does not say how it interacts with an existing local ordinance. A threshold is defined without saying whether part-time employees count. A notice requirement does not specify the trigger date.

Someone has to decide, because the publisher's product is a definite position — a policy paragraph, a guidance article, a compliance answer. An attorney or senior analyst reads the statute, the legislative history, any agency guidance, comparable provisions in other states, and whatever practitioner commentary exists, and forms a view. That takes hours to a day, and it is the highest-value work the company does.

What gets published is the position. The reasoning, the alternatives considered, the confidence level, and the specific ambiguity that forced the call are not recorded anywhere retrievable. Three years later, when an agency issues contrary guidance or a court rules, nobody can find which of the publisher's positions depended on the reading that just changed.

The same ambiguity also recurs across jurisdictions — the third state to pass a similar statute presents the same interaction question — and the analyst who resolved it for the first two may not be the one drafting the third.

## Why It's Still Broken
The output format has no room for it. Customers want a clear answer, and a policy template with hedging in it is a worse product. So the deliverable is confident prose, and everything behind the confidence is stripped out on the way to publication.

Editorial workflow reinforces it. Research happens in an analyst's own documents and notes, review happens on the draft, and the artefact that enters the content management system is the final text. The system's unit is a published item; there is no object representing a legal position with a rationale attached to it.

And the risk calculation cuts the wrong way. A written record saying "we considered the alternative reading and chose this one" looks, to a cautious general counsel, like a document that could be used against the company — even though publishing a position with no recorded basis is the more exposed posture.

## What a Fix Looks Like
Make the interpretive position an object, not a paragraph.

**Positions with structure.** The question, the authority relied on, the reasoning, the alternatives rejected, the confidence, who decided, and when. Attached to every piece of content that depends on it — which is what makes the corpus queryable by the question an analyst actually has.

**Monitored dependencies.** A position resting on the absence of agency guidance should flag itself the moment guidance appears. A position drawn by analogy to another state should surface when that state's courts rule. The publisher already monitors those sources for content; nothing connects the monitoring to the positions that would be affected.

**Reuse across jurisdictions.** When the same ambiguity appears in a new state, the analyst should see how the firm resolved it before, with the reasoning. This is the single largest efficiency in the research function and it currently depends on someone remembering.

**Confidence recorded internally.** Not published — but the firm should know which of its positions are settled and which are judgment calls, because that is the map of where it is exposed, and it does not currently exist in any form.

## Who Feels the Pain
Analysts and attorneys, re-deriving reasoning colleagues already worked out. The content leader, who cannot answer which positions are affected when the law moves. And customers, who receive confident guidance with no indication of which parts are settled law and which are one reasonable reading among two.

## Impact If Fixed
The interpretive corpus is the only thing this business owns that a competitor cannot buy — statutes are free and anyone can read them. Storing the reasoning turns years of expensive legal analysis into a compounding asset, makes the firm able to respond in hours rather than weeks when a court or agency moves, and directly compresses the research cost of every new jurisdiction that passes a law someone else already passed.
