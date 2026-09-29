# Build: Findings as Objects, Reports as Renders

**Niche:** Report Production
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system where a finding is a structured object carrying its own evidence, and every deliverable — full report, executive summary, client template, ticket export — is rendered from it.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #transfer-learning #automation #workflow-orchestration #worker-facing
**Contested on:** Whether the document is assembled from structured findings captured during the engagement, or retyped into a different client's template every time.

## The Problem

The testing is done. What remains is production, and production consumes a quarter to a third of the effort in a typical engagement.

The specific work: writing out each finding in prose, largely reproducing a description the firm has written hundreds of times for the same weakness class. Placing screenshots and request-response pairs by hand. Retyping affected host and endpoint lists. Redacting credentials from evidence manually. Writing the executive summary, then rewriting it when a severity changes during review. Producing a second, shorter document for a board audience. Reformatting everything into this client's required template, which is arbitrarily different from the last one.

None of it requires the person doing it, and all of it is done by that person, because it is entangled with content that is still moving. And this is where the errors are — the mismatched severity, the host list that was not updated, the screenshot with a live session token, the finding described against a system that changed.

The raw material to eliminate most of it exists: the tester's proxy history, tool output and evidence captures, sitting in their own tooling, unread by any reporting process.

## Why Nobody Has Built This

**Reporting platforms exist and small firms have not adopted them.** This is the key fact. The category is real — Dradis, PlexTrac, AttackForge, Ghostwriter — and adoption is concentrated at larger firms. The reasons are setup cost, workflow rigidity, and that testers resist tools that constrain how they write. Any new entrant has to be dramatically lighter rather than incrementally better.

**Testers guard the prose.** The finding narrative and the impact assessment are where judgement shows. Anything perceived as generating the analysis will be rejected outright, which narrows the buildable scope to capture, assembly and consistency — less impressive than it sounds in a pitch and more valuable in practice.

**Client templates are genuinely varied and defended.** Enterprise clients specify formats, sometimes contractually. A system that imposes one structure sells to nobody; one that renders arbitrary templates is a harder build.

**Evidence binding requires capture during testing.** For findings to carry their evidence, something must have captured it at the moment of discovery, which is the dependency on the build in [[niches/penetration-testing-firms/the-tester/profile|🟣 The Tester]].

**The saving is unmeasured and unbilled.** Write-up time appears nowhere, so the business case is an anecdote and competes badly against anything with a number.

## What to Build

**Findings as structured objects.** Class, location, affected assets, evidence with source, severity with its basis and assumptions, reproduction steps, remediation guidance, impact. The tester writes the claim and the impact in their own words; the structure carries everything around it.

**Bind evidence by reference, live.** A host list, an affected endpoint count, a request-response pair is a reference to captured data, not typed text. When the tester adds a twelfth affected host on day nine, every mention updates. This alone removes the most common class of error in these documents.

**Render, do not template.** One finding set produces the full report, the executive summary, the board version, the client's required format and a structured export for the client's vulnerability management platform. Editing a finding changes all of them at once, which ends the divergence problem that makes late changes so expensive.

**A firm finding library with real language.** The firm's accumulated description for each recurring class, offered as an editable starting point and improved over time. This is where most of the writing time goes and it is the most straightforwardly recoverable.

**Redact at capture, automatically.** Credentials, tokens and personal data stripped from evidence by default, with deliberate reveal. A security firm shipping a live token in a report is a real and recurring embarrassment and is entirely preventable.

**Consistency checking as a release gate.** Severity agreement between summary and body, affected-asset lists matching evidence, every summary finding present in the body, no residual text from a previous client, every claim evidenced. Ten seconds, mechanical, and it catches the failures that actually damage a firm's credibility.

**Structured export as a first-class output.** Findings as data for the client's platform, which solves the receiving engineer's retyping problem in [[niches/penetration-testing-firms/the-security-engineer/profile|🟣 The Security Engineer Receiving the Report]] and makes the firm's deliverable more useful than a competitor's PDF.

**Light enough to adopt in an afternoon.** The category's adoption failure is the main lesson available. Setup measured in hours, no workflow imposed, and useful on the first engagement.

## Target Customer

Boutique and mid-size testing firms — the segment the existing platforms have not reached, where report volume is high enough for the saving to matter and there is no operations function to run an implementation.

Independent testers are a volume market at a much lower price point, reachable only if setup is genuinely trivial.

## Impact If Built

Days recovered per engagement, on the largest unbilled cost in the industry, going directly to the working pattern that drives testers out of the profession.

Reports arrive faster, which reduces the staleness that undermines their usefulness — every day between the last test day and delivery is a day of relevance lost.

And structured output makes the deliverable act on: a report that arrives as data the client's platform can ingest is worth more than the same findings in a PDF, and no firm currently competes on that.
