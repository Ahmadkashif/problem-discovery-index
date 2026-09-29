# A Time-Boxed Sample Reported as an Assessment

**Industry:** [[penetration-testing-firms|Penetration Testing Firms]]
**Type:** High Impact
**One-liner:** Two weeks against an estate that would take months produces a list of what was found, and nothing in the report says what was never looked at.
**Tags:** #bayesian-inference #confidence-intervals #probability-distributions #graph-neural-networks #gradient-boosting #evaluation-metrics #hypothesis-testing #compliance

## The Problem
A penetration test has a fixed duration and a scope agreed before anyone has looked at the system. Within that window a tester explores, finds what they find, and writes it up. The report lists findings with severities and recommendations.

What the report does not contain is coverage. How much of the application's functionality was exercised, which components were reached, which attack classes were attempted and which were not, how much of the estate was examined at all. A clean report and a report from a test that ran out of time before reaching the interesting half look identical.

Clients read the absence of findings as evidence of security. Testers know it is evidence of a fortnight. The industry is aware of the gap — reports carry disclaimers saying exactly this — and the disclaimer does not change how the document is used, because the buyer needs a security assertion and this is the artefact they were sold.

The consequence compounds through the procurement chain. Enterprise customers ask suppliers for a clean penetration test, insurers ask for one, compliance frameworks require one, and none of them can distinguish a thorough engagement from a shallow one because neither report states its coverage. That drives price competition toward the thinnest acceptable deliverable, which is the opposite of what any of those parties want.

And the firm cannot demonstrate otherwise. A firm doing genuinely deeper work has no way to show it in the artefact, so the market cannot reward it.

## Why It's Unsolved
Coverage is genuinely hard to define for security testing. Code coverage is measurable and does not mean much about security; attack surface coverage requires an enumeration of the surface, which is exactly what a test is partly trying to establish; and attack class coverage requires agreeing a taxonomy of what should have been tried. None of these is impossible and none is standard.

The commercial incentives run against it. A report that states it examined forty percent of the application is a harder sell than one that lists findings and says nothing, particularly against competitors who say nothing. The first firm to report coverage honestly looks worse than the firms that do not, which is the same first-mover problem that appears throughout this vault.

Remediation outcomes are withheld by default. Clients do not report back whether findings were fixed, partly because nobody asks and partly because the answer is frequently uncomfortable. So the firm cannot measure the one thing that would demonstrate its value.

And compliance demand actively rewards the shallow version. Where the purchase exists to satisfy an audit item, the buyer's need is a document, and a firm that produces a more honest and more alarming document is solving a problem the buyer did not have.

## What a Solution Looks Like
Instrument the test. What was reached, what was attempted, what was deferred and why is recordable during an engagement with modest tooling — and reporting it converts a list of findings into an assessment with a stated scope. Testers largely keep this information informally already, in notes and in their heads.

Report residual uncertainty. Given the coverage achieved, the technology stack and the firm's historical finding rates for comparable systems, the expected number of remaining findings is estimable — and a statement that a fortnight on this stack typically surfaces about half of what a month would is far more useful to a client than a disclaimer.

Build the remediation loop. Asking clients for remediation status and retesting outcomes, as a standard part of the engagement rather than as a separate sale, gives the firm the data to say which finding types get fixed, which recur, and which remediation advice actually works. Most clients would agree to this if it were framed as included assurance.

Define coverage per attack class and make it a deliverable. Which classes were attempted against which components, with the ones not attempted named, is achievable, auditable and would let a buyer compare two engagements for the first time.

## Impact If Solved
This industry sells a document whose meaning its buyers systematically misread, and the misreading drives the market toward cheaper and shallower work. Coverage reporting plus residual estimates give a buyer something comparable, which is the precondition for depth being rewarded; the remediation loop gives the firm the first real evidence about which of its advice works. Both are achievable with instrumentation and a clause, and both would be resisted for exactly the reason they are needed.
