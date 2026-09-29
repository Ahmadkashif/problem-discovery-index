# Lineage: Fractional CTO Services

**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Joel Test — twelve yes/no questions about a software team's practices ("Do you use source control?" through "Do you do hallway usability testing?"), scored out of 12, published 9 August 2000
**Builder:** Joel Spolsky
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Judging a software team from outside took longer than anyone who needed the judgement had.

The formal instruments were built for a different buyer: process-maturity assessments of the Software Engineering Institute kind served large contractors and took an audit's worth of time. A founder, an investor or a new technical lead had days, and access to people rather than to evidence.

What was missing was a *cheap* test an outsider could run in a conversation.

## What Got Built

A list.

Spolsky published it on his blog, *Joel on Software*, as "The Joel Test: 12 Steps to Better Code." Every question is binary and concrete:

1. Do you use source control?
2. Can you make a build in one step?
3. Do you make daily builds?
4. Do you have a bug database?
5. Do you fix bugs before writing new code?
6. Do you have an up-to-date schedule?
7. Do you have a spec?
8. Do programmers have quiet working conditions?
9. Do you use the best tools money can buy?
10. Do you have testers?
11. Do new candidates write code during their interview?
12. Do you do hallway usability testing?

The scoring rule was blunt: "A score of 12 is perfect, 11 is tolerable, but 10 or lower and you've got serious problems," and "most software organizations are running with a score of 2 or 3." He introduced it as "my own, highly irresponsible, sloppy test to rate the quality of a software team," whose virtue is that "it takes about 3 minutes." He contrasted it explicitly with SEMA, "a fairly esoteric system for measuring how good a software team is."

The shape is the argument. Each question asks about a *practice that leaves evidence* — a repository, a build script, a bug tracker — rather than about quality, which an outsider cannot see in three minutes.

## Who Built It, And Why Them

Joel Spolsky, a Microsoft Excel program manager from 1991 to 1994, later at Juno Online Services in New York.

In 2000 he and Michael Pryor founded Fog Creek Software in New York — founded, per its Wikipedia history, **as a consulting company** — and that same year he started *Joel on Software*, described as one of the first blogs set up by a business owner. The test is keyed to Spolsky rather than Fog Creek because it was published under his own byline on his own site; this note did not establish whether Fog Creek was incorporated before or after 9 August 2000.

**Why him:** he had worked inside the team that scored 12 — the article cites Microsoft as running "at 12 full-time" — and then walked out into a market of teams scoring 2 or 3. A person who has seen both, and who needs to size up clients and hires quickly, is the person who compresses the difference into twelve questions.

## What It Cost

It measures process, not architecture. A team can score 12 on a system that must be rewritten, and the test says nothing about the codebase, the data model or the debt — which is precisely the question a fractional CTO is hired to answer.

It is also self-reported, which is tolerable over coffee and dangerous in due diligence. And it ages: "daily builds" and "the best tools money can buy" were pointed in 2000 and are nearly free in a world of hosted CI.

## What You Still Touch

The first-week checklist a fractional CTO walks through — is there source control, a one-step deploy, a bug tracker, tests, a written plan — is the Joel Test's shape: practices that leave evidence, asked of people rather than read from the code.

- [[problems/fractional-cto-services/high-impact|🔴 Forming a Consequential Technical Opinion in Three Weeks From Interviews]] — the three-minute test stretched to three weeks, still built on interviews
- [[problems/fractional-cto-services/low-impact-1|🟡 Technical Due Diligence Under Deal Timelines]] — where self-reported answers meet an interested management team
- [[niches/fractional-cto-services/technical-assessment/profile|Technical Assessment]]
- [[niches/fractional-cto-services/evidence-extraction/profile|Evidence Extraction]] — reading the evidence the questions only ask about

**Sources:** joelonsoftware.com, "The Joel Test: 12 Steps to Better Code," 9 August 2000 (twelve questions, scoring passage, "sloppy test … 3 minutes", SEMA and Microsoft references — read directly); Wikipedia, *Joel Spolsky* (Microsoft Excel team 1991–94, Excel Basic and VBA strategy, Juno from 1995, Fog Creek and the blog both 2000, "one of the first blogs set up by a business owner"); Wikipedia, *Glitch, Inc.* (Fog Creek "founded in 2000 as a consulting company by Joel Spolsky and Michael Pryor"). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs only. ⚠️ **Not established:** the month Fog Creek was founded, and therefore whether the test predates the firm; any documented use of the Joel Test in formal technical due diligence — the link to fractional-CTO practice is this note's argument, not a sourced claim; the characterisation of SEI-style assessments as audit-length is general background, not verified this session.
