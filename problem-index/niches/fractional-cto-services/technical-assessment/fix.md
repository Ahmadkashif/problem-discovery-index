# Fix: The Assessment That Leaves With the Assessor

**Niche:** Technical Assessment
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** Every assessment a practice produces is written, delivered and forgotten, so the firm's hundredth engagement starts with exactly as much accumulated knowledge as its first.
**Tags:** #bert #large-language-models #evaluation-metrics #k-means-clustering #data-integration #word-embeddings #automation
**Contested on:** Whether the advisor's picture of the system is built from evidence the organisation already produces or from reading and asking.

## The Problem

A boutique advisory practice with eight practitioners running four engagements a year each produces roughly thirty assessments annually. Each one contains a structured account of a real company's technical situation, the practitioner's reasoning, and a set of recommendations. Each is delivered as a document, filed in a client folder, and never read again by anyone.

The consequence is that the practice owns nothing. When a practitioner joins, they bring their own pattern library and build a new one from scratch on the firm's clients. When a practitioner leaves, the firm loses everything they learned in it. The partner who has seen sixty assessments knows things the associate does not, and there is no mechanism by which that knowledge reaches the associate other than working alongside them.

It also means there is no reference class. When a practitioner concludes that a rebuild will take nine months, the question "what happened the last four times someone in this firm said nine months" cannot be asked, because the last four times are in four PDFs in four client folders with no index and no follow-up. The firm sells calibrated judgement and has never calibrated anything.

## Why It's Still Broken

**Confidentiality is the stated reason and a partial one.** Assessments contain client-identifying material under NDA, and the reflex is to treat the whole document as untouchable. The reflex is broader than the obligation — the pattern ("a payments system with this coupling profile and this team size took this long to stabilise") is not the client's confidential information once the client is not named, and most engagement letters permit exactly that abstraction. Almost no practice has done the work to establish where the line is, so the default is that nothing is reused.

**Nobody's job.** The assessment is billable; the write-up into a reusable form is not. In a practice where utilisation is the operating metric, unbilled knowledge work loses every time it competes with an engagement, and there is no partner whose compensation depends on the firm's corpus existing.

**The documents are prose.** They are written to persuade a specific board of a specific decision, so their structure serves the argument rather than any comparison across engagements. Extracting a comparable record from thirty bespoke narratives is real work, and the obvious shortcut — a rigid template — makes the documents worse at the job they are actually paid for.

**The outcome is missing.** The assessment says what should happen. Whether it happened, and what resulted, is on the other side of a wall that closes when the engagement ends. Recommendations are almost never followed up, so even a perfectly indexed corpus of assessments would record predictions with no results attached — which is why the indexing feels pointless to the people who would have to do it.

**The practice's self-image resists it.** Codifying the pattern library is close to admitting the pattern library could be held by the firm rather than the person, which affects who has leverage in a compensation conversation. Senior practitioners are rarely enthusiastic, and they are the ones who would have to supply the material.

## What a Fix Looks Like

Start with structured extraction rather than a new template. Run the existing assessment documents through extraction that pulls a consistent record out of each — company shape, system characteristics, the problems identified, the recommendations made, the estimates given, the risks flagged — leaving the narrative document untouched and building the comparable layer beside it. Redaction and entity replacement happen at extraction, so the corpus that accumulates is already in the form the engagement letter permits.

Add outcome capture as a light, contractual habit: a short structured follow-up at six and eighteen months, offered as a free check-in, which most clients accept because it is useful to them. What was executed, what was not, what happened. Ten minutes on a call, recorded against the original assessment. That single addition converts the corpus from a filing system into a record of predictions with results.

Then make it queryable at the point of need. When a practitioner is scoping a new engagement, the firm's own prior work on similar shapes surfaces — comparable systems, what was recommended, what actually followed. When an estimate is being written, the distribution of the firm's past estimates against actuals appears next to it. Not a recommendation engine; a reference class.

Finally, make maintaining it somebody's compensated responsibility, because every version of this that depends on practitioner goodwill has failed.

## Who Feels the Pain

The junior practitioner most acutely. They are sent into situations senior colleagues have seen many times and given no access to that experience except by asking, which costs social capital and returns an anecdote. Their assessments are worse than they need to be for want of a reference class that exists in the building.

The practice owner feels it commercially. The firm's valuation rests on relationships and named individuals rather than any asset, and when a senior practitioner leaves for a competitor or an operating role, the loss is total. There is no enterprise value in a consultancy whose knowledge walks out at six each evening.

The client feels it without knowing. They are buying calibrated judgement and receiving one person's recollection of their own last few projects, priced as though it were the firm's collective experience.

## Impact If Fixed

A practice with a queryable corpus of its own assessments and their outcomes can do something no competitor can: answer the client's hardest question — "how confident should I be in this?" — with evidence. Of the last eleven times we made a recommendation of this shape, here is what happened.

It changes the economics of hiring. A capable engineer without a decade of advisory pattern recognition becomes productive faster when the firm's pattern library is a resource rather than a colleague's memory, which widens the hiring pool a growth-constrained industry has always treated as fixed.

And it converts an accumulated career of pattern recognition into an asset the firm owns, which is the difference between a practice and a group of individuals sharing a brand.
