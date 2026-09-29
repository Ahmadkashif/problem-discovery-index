# Lineage: Digital Accessibility Firms

**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** WCAG 1.0 — the W3C Web Content Accessibility Guidelines, with prioritised checkpoints rolled up into the conformance levels A, Double-A and Triple-A
**Builder:** W3C
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Nobody could say whether a web page was accessible, because there was nothing to measure it against.

In the mid-1990s a blind user with a screen reader, a user who could not work a mouse and a deaf user facing an uncaptioned clip each hit different barriers, and each advocacy group, university lab and vendor had its own advice. A site owner who wanted to do the right thing had no list to check, and a site owner who did not had no standard to be held to. The expensive step was agreement: turning many disabilities' needs into one set of statements a web developer could act on.

## What Got Built

A list of checkpoints, each with a priority, and a rule for adding them up.

The W3C published **WCAG 1.0 as a Recommendation on 5 May 1999**: fourteen guidelines, each broken into checkpoints. Every checkpoint carried a priority, defined by consequence. Priority 1 was something a developer "must" satisfy, "otherwise, one or more groups will find it impossible to access information"; Priority 2 "should", or access would be "difficult"; Priority 3 "may", or it would be "somewhat difficult".

Conformance was the roll-up: **Level "A"** meant all Priority 1 checkpoints met, **"Double-A"** all Priority 1 and 2, **"Triple-A"** all three. The document even specifies that the levels are spelled out in words "so they may be understood when rendered to speech".

## Who Built It, And Why Them

**The W3C's Web Accessibility Initiative**, launched as an international programme office in 1997, led by domain leader **Judy Brewer**, with technical manager **Daniel Dardailler**. The Web Content Guidelines Working Group was co-chaired by **Gregg Vanderheiden**, director of the Trace Research & Development Center at the University of Wisconsin — a research lab, not a standards body, which is the point.

**Why the W3C and not a government or a vendor** is visible in the funder list: the US National Science Foundation, the Department of Education's disability research institute, the European Commission, the Government of Canada, and IBM, Lotus, Microsoft and NCR. No one of those could issue a standard the others would adopt. A consortium that already owned HTML could. Vanderheiden said so at launch: the W3C provided "a unique forum" to bring together industry, research and practice "in a way that has not been possible before". Vice President Al Gore's testimonial credited the White House as a "catalyst".

The measuring instrument arrived first. **Bobby**, a free online checker from the Center for Applied Special Technology (CAST), was released in 1996 and became known for its "Bobby Approved" badge; it later checked against WCAG 1.0 and Section 508, passed to Watchfire and then IBM, and was closed in 2008.

## What It Cost

**It measures the page, not the person.**

A checkpoint list is testable against markup — alt attribute present, form label attached, contrast ratio met — and that testability is why it could become law and contract language. The price is that conformance is a property of code, while access is a property of a disabled user finishing a task. A page can meet every Priority 1 checkpoint and still be unusable in a screen reader because the order of operations makes no sense.

The A/AA/AAA ladder then became a procurement target. WCAG 2.0 (December 2008) rewrote checkpoints as testable success criteria but kept the three levels, and Double-A became the default contractual bar — a pass line, not a usability measure.

## What You Still Touch

Every accessibility audit report, VPAT and overlay vendor's compliance badge is a checkpoint tally in the 1999 format, descended from Bobby's badge.

- [[problems/digital-accessibility-firms/high-impact|🔴 Conformance Is Measured and Task Completion Is Not]] — the checkpoint roll-up, measuring code
- [[problems/digital-accessibility-firms/low-impact-1|🟡 Automated Scanning Coverage and False Positives]] — Bobby's descendants
- [[problems/digital-accessibility-firms/worker-life-1|🟢 The Auditor Doing the Manual Pass]]
- [[niches/digital-accessibility-firms/conformance-auditing/profile|Conformance Auditing]]
- [[niches/digital-accessibility-firms/task-outcome-measurement/profile|Task Outcome Measurement]]
- [[niches/digital-accessibility-firms/overlay-claims/profile|Overlay & Quick-Fix Claims]]

**Sources:** W3C, *Web Content Accessibility Guidelines 1.0*, w3.org/TR/WCAG10 (priority definitions, conformance levels, "rendered to speech" note); W3C press release, "W3C Issues Web Content Accessibility Guidelines as a Recommendation", 5 May 1999 (date, funders, Brewer, Dardailler, Vanderheiden and Trace, Vanderheiden and Gore quotes); Wikipedia, *Web Content Accessibility Guidelines* (fourteen guidelines, 1997 WAI programme office, WCAG 2.0 December 2008); Wikipedia, *Bobby (software)*, and Jim Thatcher's and Deque's tool histories (CAST, 1996, badge, Watchfire, IBM, closure 1 February 2008). ⚠️ **Not established:** the full editor list of WCAG 1.0 (not stated in the sources retrieved; not asserted). Bobby predates WCAG 1.0, so its original 1996 rule set cannot have been WCAG — what it checked against at launch was not found. Sources disagree on whether Watchfire acquired Bobby in 2002 or 2004. The claim that Double-A is the "default contractual bar" is industry practice as described in this vault's problem notes, not a sourced statistic; Section 508's adoption of WCAG 2.0 AA was not re-verified this session and is not dated here.
