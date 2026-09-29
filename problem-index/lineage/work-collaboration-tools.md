# Lineage: Work Collaboration Tools

**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Basecamp — the hosted project page, launched 5 February 2004, that put one client project's messages, to-do lists and milestones at a single web address both the agency and its client could open
**Builder:** 37signals
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A web design firm's work is a set of small projects, each with a client who wants to know how it is going.

Around 2003 that knowledge lived in email threads and spreadsheets. The state of a project was whatever the last message said, held in the inbox of whoever had received it. A client asking "where are we?" triggered a search, a reply-all and, often, a discovery that two people on the same team believed different things.

Jason Fried's own description of 37signals at the time is blunt: "We were disorganized, we were dropping balls, and stuff was slipping." The traditional answer — desktop project-management software built around Gantt charts and resource levelling — assumed a trained project manager to keep it current. A small design shop did not have one.

## What Got Built

A web page per project. On it: a message board for discussion, to-do lists that anyone on the project could tick off, milestones with dates, and — crucially — a login for the client. The launch post said the tool prioritised "two-way communication, conversation, simple scheduling, and to-do lists" over tracking, and was aimed at freelancers and small teams without dedicated project managers.

Two details show whose problem it was built for. The project site could be fully branded to the agency — "There's no mention of 37signals" — so a firm could hand it to a client as its own. And it was sold as a hosted subscription: one project free, the Basic plan at roughly 65 cents a day.

## Who Built It, And Why Them

**37signals**, a Chicago web design consultancy founded in 1999 by Jason Fried, Carlos Segura and Ernest Kim. Development began in **2003** as an internal tool for the firm's own client work; clients who saw it asked to use it; the firm polished it and launched it on **5 February 2004**. Within about a year, by the company's own account, Basecamp earned more than the design business, and the firm stopped taking design work.

**Why a design agency and not a software company?** Because the agency was the customer. Established project software was written for the person running the plan; 37signals was the person being asked for status, with a client on the other end. That position dictates the artefact: shared access for outsiders, a to-do list instead of a dependency network, and a conversation thread instead of a report.

A by-product outlasted the product category. David Heinemeier Hansson extracted **Ruby on Rails** from his work building Basecamp and released it as open source in **July 2004**.

## What It Cost

**The tool recorded what people said about the work, not the work.** A to-do list is ticked when someone remembers to tick it; a milestone is on time until someone admits it is not. Basecamp removed the project manager as a bottleneck and in the same move made every team member the typist of their own status.

37signals' later method book, *Shape Up*, concedes the point. It observes that to-do lists grow as work is discovered, so a count of finished tasks misleads, and introduces the **hill chart** — each piece of work placed "uphill" while it is still being figured out and "downhill" once it is execution — so that managers can "judge what's in motion and what's stuck" without asking. It is still a position someone drags by hand.

## What You Still Touch

Every task card with a status dropdown, every "@mention for an update", and every client guest seat in a work-management tool is a Basecamp decision: shared page, human-entered state.

- [[problems/work-collaboration-tools/high-impact|🔴 Status Is Typed, Not Observed]] — the bill for recording what people said
- [[problems/work-collaboration-tools/worker-life-1|🟢 Project Manager Status Chasing]]
- [[niches/work-collaboration-tools/work-status-inference/profile|Work Status Inference]]
- [[niches/work-collaboration-tools/external-collaboration/profile|External Collaboration]] — the client login, grown up

**Sources:** Jason Fried, "Basecamp Launches," *Signal v. Noise* (5 February 2004, signalvnoise.com/archives/000542.php) — launch date, positioning, branding and pricing quotes; basecamp.com/about (Fried's "dropping balls" quote; clients asking for access; the product out-earning the design business within about a year); Wikipedia, *37signals* (1999 founding in Chicago, founders, 2003 development) and *Basecamp (software)* (internal-tool origin; messaging, to-dos, milestones); Wikipedia, *Ruby on Rails* (extraction from Basecamp, July 2004 release); 37signals, *Shape Up*, chapter "Show Progress" (hill-chart passages quoted). This vault's `history/work-collaboration-tools.md` covers Slack and Teams and was not used as a source here. ⚠️ **Not established:** the launch-day price in dollars per month (the post gives "about 65 cents a day"); the year hill charts shipped in the product. WebSearch was unavailable this session (session cap reached); research used WebFetch on known URLs only.
