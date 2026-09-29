# Fix: A Clean Report Is Not a Clean System

**Niche:** Assessment Assurance
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Everyone in the transaction knows a clean report means two weeks of sampling, and the document is written so that it reads as an assessment of the system.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing #revenue-impact
**Contested on:** Whether a test report states what its clean results actually mean, or leaves the client to read two weeks of sampling as evidence of security.

## The Problem

The tester knows what the engagement established. The client's security engineer usually knows too. Between them there is no confusion at all.

The confusion begins the moment the report leaves that conversation. It goes to a security leader who summarises it for a board. It goes into a customer security questionnaire as evidence that annual penetration testing is performed. It goes to an auditor, an insurer, a prospective enterprise customer, a procurement team. At each step the nuance the tester would have supplied verbally is absent, and the document — which lists what was found and says nothing about what was looked at — reads unambiguously as an assessment.

Nobody lies. The tester writes an accurate list of findings. The security engineer accurately reports that a test was performed and the findings were addressed. The security leader accurately tells the board the system was tested by an external firm. And the board concludes something that none of the three would endorse if asked directly.

The failure is in the artefact. A document that contains no statement of its own limits will be read as unlimited, and the people who understand the limits are not in the room when it is read.

## Why It's Still Broken

**Nobody in the chain is harmed until something happens.** The tester is paid, the engineer has their evidence, the leader has their assurance, the auditor has their artefact. The cost of the misreading is borne only in the breach that follows, by which point the report is a disclosure item rather than an operating document.

**Caveats are competitively punished.** A report opening with a substantial scope-limitation section reads as a weaker deliverable in a procurement comparison against one that does not. Firms that have tried it report losing bids on exactly that basis.

**The buyer often wants the ambiguous version.** A meaningful share of testing is procured to satisfy a requirement. For that buyer a clean report that reads as assurance is the product, and a report full of honest limitations is actively less useful to them.

**Testers raise it verbally and it evaporates.** Most good testers say the important things in the debrief. Debriefs are not minuted, are attended by two or three people, and do not travel with the document.

**Methodology sections describe intent, not execution.** Naming PTES or OWASP says what the approach is meant to cover. It is routinely read as a statement of what was covered, and it is not one.

**No standard exists to point at.** An individual firm adding coverage language is making an idiosyncratic claim. A profession-wide convention would make its absence conspicuous instead, which is why this is a standards problem more than a product one.

## What a Fix Looks Like

**A mandatory scope and limitations section, at the front.** What was in scope, what was excluded, what was in scope and not reached, and what a clean result in each area is worth. At the front, because appendices do not travel. This costs a page and is the single highest-value change available to any firm today, with no new technology whatsoever.

**An explicit untested list.** The areas nobody reached, stated plainly, with the reason — time, access, a blocked dependency, a scope exclusion. This is the information clients most need and currently never receive, and testers are usually relieved to have somewhere to put it.

**Separate the executive summary from the assurance statement.** The summary says what was found. A short, deliberately unglamorous assurance statement says what the engagement can and cannot support — written to be quoted, because it will be. If the sentence that gets extracted into a board pack is written by the tester rather than assembled by a reader, most of the misreading disappears.

**Say what it would take.** For each partially covered area, an estimate of the effort required for meaningful coverage. This converts an awkward admission into a commercial conversation and is why honest coverage reporting should increase revenue rather than reduce it.

**Minute the debrief into the document.** The caveats testers already give verbally, written down. They are being said; they simply are not travelling.

**Push for a convention, not unilateral virtue.** The accreditation and methodology bodies are the right home. A standard scope-and-limitations section, adopted across the profession, removes the competitive penalty for the firm that would otherwise go first — and this is one of the few problems in this vault where the fix is genuinely blocked on collective action rather than on capability.

## Who Feels the Pain

The organisation that believed it was tested, in the area nobody reached, until something happened there.

The tester, who understands the gap between the document and its reading better than anyone and has no field in which to record it.

The security engineer, who knows the report is being over-read up the chain and cannot correct it without appearing to undermine a result their own leadership is pleased with.

And the firms doing genuinely deep work, who lose bids to thinner competitors because the artefact makes the two look identical.

## Impact If Fixed

A front-page scope and limitations section, with an untested list, closes most of the misreading at the cost of a page. There is almost nothing else in this industry with that ratio.

It would reprice the market. Once buyers can see how much of their estate a given engagement reached, depth becomes comparable, and firms doing thorough work stop competing on day rate against firms producing the thinnest acceptable deliverable.

And it turns the industry's least comfortable conversation — what we did not get to — into its most commercially productive one.
