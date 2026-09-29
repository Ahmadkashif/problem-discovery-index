# Fix: A Week of Eight Getting Access

**Niche:** Engagement Operations
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** An eight-week engagement routinely loses its first week to arranging the system access it cannot start without, and the negotiation begins from nothing at every client.
**Tags:** #workflow-orchestration #compliance #automation #data-integration #worker-facing
**Contested on:** Whether the administrative shell around an engagement is set up once and reused or rebuilt for every client.

## The Problem

The engagement starts Monday. The practitioner needs to read the code, see the issue tracker, look at the cloud spend and be in the engineering Slack. None of that exists yet.

So Monday is spent asking. The CEO says yes and forwards it to the head of engineering, who is not sure what permission level to grant and asks what exactly is needed. The answer — read access to these repositories — triggers a question about whether a third party can have code access, which triggers a security review nobody scheduled. Someone asks for a signed NDA that was already signed and is in an email thread. Cloud access is refused entirely because the only role anyone knows how to grant is administrator. Slack access arrives Thursday. Tracker access arrives the following Tuesday, after the person who owns it returns from leave.

Ten working days into a forty-day engagement, the practitioner can finally see the system they were hired to assess. They have spent the interval doing interviews, which is the part that works without access and is the part least improved by starting early.

Nothing about this is anyone's fault. The client has never provisioned an external technical advisor before and has no template for it. The practitioner has done it forty times and still starts each one with an email saying "here's what I'll need."

## Why It's Still Broken

**No standard exists.** There is no agreed specification of what a technical advisor needs, at what permission level, with what justification. Every engagement negotiates it from first principles, on both sides, with neither party knowing what is reasonable.

**The client's security posture is built for employees and vendors.** A guest advisor fits neither category. Employee onboarding is too heavy and assumes a contract type they do not have; vendor integration assumes a procurement process and a systems integration. The advisor falls into a gap, and the default answer when a request does not fit a category is delay.

**The practitioner underplays it in the sale.** Raising access provisioning during the pitch makes the engagement sound complicated. So it is mentioned lightly and discovered fully on day one, when the clock has already started.

**Nobody owns it on the client side.** Access spans the head of engineering, IT, security and whoever administers each individual system. There is no single person whose job it is, so it proceeds at the speed of the slowest thread.

**Over-provisioning is the shortcut and it is worse.** The fast path is often administrator access to everything, because it avoids thinking about roles. That is bad for the client, uncomfortable for the practitioner, and almost never revoked afterwards.

**The cost is borne by the practitioner and hidden from the client.** The engagement is fixed-fee or fixed-day, so the lost week compresses the work rather than extending the bill. The client never sees a cost and therefore never has a reason to fix it.

## What a Fix Looks Like

**Publish a standard access package.** A documented specification — read-only repository access to these kinds of repositories, tracker export, read-only billing, no production data, no customer data, duration bounded by the engagement — with the security justification written out in a form a client's security team can evaluate in a single pass. Published as an open standard for the profession rather than held by one practice, because its value is entirely in becoming the thing both sides recognise.

**Move it into the contracting stage.** The access schedule is an annexe to the engagement letter, agreed before the start date, so the security conversation happens during contracting when there is time and not on day one when there is not. This single change recovers most of the lost week and costs nothing.

**Name an owner on the client side.** One person accountable for provisioning, named in the engagement letter, with the list in front of them. Most delay is coordination rather than objection.

**Provide the lowest-privilege recipe per platform.** Practitioners know exactly which GitHub, Jira, AWS and GCP roles give what they need without giving more, and clients do not. A short, concrete guide — grant this role, not that one — converts a risk conversation into a configuration task and is the thing that most often turns a refusal into a yes.

**Degrade gracefully and say so up front.** Tell the client what the assessment can and cannot conclude at each access level, so the choice to withhold is informed rather than accidental. A client who understands that cloud cost analysis is impossible without billing read will usually grant billing read.

**Revoke at close, verifiably.** A close-down checklist covering every grant made, with confirmation. The practitioner benefits from not holding access they should not have, and the client benefits from an exposure closing that would otherwise stay open for years.

## Who Feels the Pain

The practitioner, losing a week of a short engagement and then compressing the remaining work to compensate, which lands on the quality of the assessment.

The client, who paid for eight weeks of senior attention and received seven, and whose engineering lead spent the first week on provisioning instead of the assessment.

The client's security team, handed an unfamiliar request under time pressure by someone who wants it approved today, which is the condition under which bad access decisions get made.

And every future engagement at that company, which starts the negotiation again because nobody wrote down what was granted last time.

## Impact If Fixed

A week of an eight-week engagement recovered — twelve per cent of the work — for the cost of writing a schedule and attaching it to the contract. There are very few interventions in this vault with that arithmetic.

Security posture improves rather than degrades. A standard package specifying least privilege is a much better outcome than the administrator-access shortcut that currently happens when time runs short.

And the profession gets a shared artefact. A published access standard that client security teams come to recognise turns the hardest recurring conversation in fractional work into a formality, and it benefits every practitioner including the ones who did not write it.
