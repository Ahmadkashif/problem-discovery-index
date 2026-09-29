# Fix: Untested and Tested-Clean Look Identical

**Niche:** Coverage Measurement
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** An area nobody reached and an area that was probed hard and held produce exactly the same thing in a report — nothing — and the difference is the most important information the client never receives.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing
**Contested on:** Whether an engagement can state how much of the attack surface it actually reached, by what technique and at what depth.

## The Problem

A report lists findings. Silence about an area is therefore ambiguous in the worst possible way. It could mean the tester spent a day on that subsystem, tried everything they know, and it held — genuinely good news. It could mean they ran an automated pass and moved on. It could mean the area never came up, because the authentication for it was broken until Wednesday, or because the client's asset list did not include it, or because by the time they got there two days remained and something else looked more promising.

The client cannot distinguish these. Neither can the security leader summarising the report, the auditor filing it, or the insurer pricing against it. All four treat silence as a clean result, and in one of the three cases it is the opposite — an area with no evidence at all, presented indistinguishably from an area with strong evidence.

This is the single most consequential ambiguity in the industry's deliverable, and closing it requires no technology. It requires a list.

Testers know the list. At the end of every engagement a competent tester could write down, in ten minutes, the areas they did not get to and why. They are not asked to, there is no section for it, and raising it unprompted in the debrief sounds like apologising for not finishing.

## Why It's Still Broken

**It reads as an admission of failure.** A section titled "what we did not test" looks, to a buyer comparing two proposals, like a confession. The firm that omits it appears to have done more work. This is the whole obstacle and it is a procurement artefact rather than a technical one.

**Nobody is asked for it, so nobody supplies it.** Report templates have no field. Quality review checks findings, severity and evidence. The absence is invisible because nothing looks for it.

**Scope exclusions get conflated with coverage gaps.** Reports often list what was out of scope, which is a contractual statement agreed in advance. In-scope-but-not-reached is a completely different thing and almost never appears, though it is the category that actually misleads.

**Time pressure hits exactly when it would be written.** The gaps are clearest at the end of the engagement, which is when the tester is already late on the write-up and starting the next job.

**Fear of the follow-up question.** Stating that a third of the estate was unreached invites "why did you not test it", which feels like a conversation about competence rather than about scope and budget — though it is actually the second, and it is a selling opportunity.

**No convention to point at.** A firm adding the section alone bears the competitive cost. If the profession's accreditation bodies specified it, its absence would become the conspicuous thing instead.

## What a Fix Looks Like

**Add the section and make it mandatory in quality review.** In-scope areas not reached, with the reason: time, access blocked, dependency broken, deprioritised in favour of a more promising path. Ten minutes of tester time, at the front of the report where it will travel. This is the entire fix and it is available to any firm this week.

**Separate three categories explicitly.** Out of scope by agreement. In scope and not reached. In scope, tested, nothing found — with the depth stated. Three headings, unambiguous, and the reader can no longer collapse them.

**State depth where something was tested.** Even coarsely: automated only, manually examined, deeply tested. Without this, "tested, nothing found" carries an unknown amount of assurance and will be read as carrying a lot.

**Cost the gap.** For each unreached area, an estimate of the effort to cover it properly. This reframes the whole section from an apology into a proposal, which is both more honest and commercially better — clients buy more testing when they can see what is uncovered, and firms consistently find this once they try it.

**Capture it during, not after.** A running note of deferred areas kept through the engagement, so the list is assembled by the time the work ends rather than reconstructed by a tired person at the deadline.

**Make the client's procurement ask for it.** The demand side can fix this faster than the supply side. A security leader who requires an in-scope-not-reached section in every proposal gets one, and if enough buyers require it the competitive penalty for supplying it disappears.

## Who Feels the Pain

The client, who allocates budget and attention away from areas that appear fine and are simply unexamined.

The tester, who knows exactly which parts of the estate got no attention, has no field in which to say so, and carries the professional exposure if something surfaces there later.

The security engineer, who receives the report and cannot tell which of its silences are evidence and which are absence — and who is the person asked when a breach occurs in an area the report did not mention.

And the firms doing thorough work, whose reports are compared against thin ones on a basis that cannot show the difference.

## Impact If Fixed

A ten-minute list closes the largest interpretive gap in the industry's core deliverable. There is no other intervention in this vault with a better ratio of effort to consequence.

It changes how testing gets bought. A client who can see the uncovered portion has a concrete reason to fund more, which is why honest coverage reporting should grow the market rather than shrink any individual firm's share of it.

And it lets a report finally distinguish its two kinds of silence, which is the distinction everything else in assessment assurance is built on.
