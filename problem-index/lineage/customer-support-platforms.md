# Lineage: Customer Support Platforms

**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the KCS article — Knowledge-Centered Support's structured record of issue, environment, resolution and cause, written during the case and moved through Work in Progress, Not Validated, Validated and Archived states
**Builder:** Customer Support Consortium
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Technical support solved the same problem thousands of times and remembered it zero times.

An engineer closed a case; the fix lived in their head and in the case notes. The next customer with the same fault reached a different engineer, who solved it again. The obvious remedy — a knowledge base — kept failing the same way: a separate team wrote articles after the fact, the product moved, the articles went stale, and engineers stopped searching a corpus they did not trust.

**The cost of knowing something was a second job nobody was paid to do.**

## What Got Built

A method, and a record format that makes the method work.

The Consortium's name for it has shifted — Solution-Centered Support, then Knowledge-Centered Support, and since 2016 Knowledge-Centered Service — but the mechanism is constant. The engineer searches the knowledge base at the start of the case ("search early, search often"). If nothing matches, they write the article *while solving*, in a fixed structure: **issue, environment, resolution, cause**. The article enters as Work in Progress or Not Validated and becomes Validated through use. The v6 Practices Guide calls the principle "reuse is review": every time someone uses an article, they are expected to fix it.

The practices split into a Solve Loop — Capture, Structure, Reuse, Improve — and an Evolve Loop covering content health, process integration, performance assessment and leadership.

## Who Built It, And Why Them

A consortium of support organisations, started in Seattle in 1992 by Symbologic, with Shelly Benton as founding executive director.

The history is the argument. From 1992 to 1994 members talked mostly about technology — features for a tool that would capture knowledge as a by-product of work. From 1994 to 1996 they concluded the tool was not the constraint; behaviour was. That finding pulled the work away from the vendor. In 1996 Greg Oxton, then a member, joined the staff to make it member-funded, and in January 1997 it became an independent 501(c)(6) — the Customer Support Consortium. The first Practices Guide, by Livia Wilson and John Chmaj, followed in 1999.

**Why a consortium and not a software company:** the answer members reached was a workflow discipline that any tool could host, and no vendor profits from telling buyers the tool is secondary. Support organisations, sharing results across company lines, could. The Consortium kept the tools downstream: in 2005 it introduced KCS Verified, a set of functional requirements knowledge-base vendors must meet.

## What It Cost

**KCS moves authorship into the case and trades polish for currency.** Articles are short, structured, and written by whoever is solving. That keeps them fresher than an editorial team could, and it only works if the queue pays for it — which is where it collides with handle-time targets that count the minutes an engineer spends writing as lost.

It also assumes a human in the loop at every reuse. "Reuse is review" means a wrong article gets corrected when an engineer notices. When the reader is a chatbot answering the customer directly, no one is reviewing, and the correction loop KCS depends on disappears.

## What You Still Touch

The help-centre article you get from a support widget, the "was this helpful?" button beneath it, the flag for an article to be updated — all are KCS's evolve loop in a vendor's interface. Generative deflection reads the same corpus without the engineer who used to fix it.

- [[problems/customer-support-platforms/high-impact|🔴 Knowledge Decay Under Generative Deflection]] — reuse without review
- [[problems/customer-support-platforms/worker-life-1|🟢 Agent Metrics and the Queue]] — handle time against the minutes KCS asks for
- [[niches/customer-support-platforms/knowledge-generative-deflection/profile|Knowledge & Generative Deflection]]
- [[niches/customer-support-platforms/b2b-technical-support/profile|B2B & Technical Support]]

**Sources:** Wikipedia, *Knowledge-centered support* (1992 start; Symbologic and Seattle; Shelly Benton; 1992–94 technology phase and 1994–96 shift to people and culture; Greg Oxton 1996; January 1997 incorporation as a 501(c)(6) called the Customer Support Consortium; Wilson and Chmaj 1999 Practices Guide; HDI 2003; KCS Verified 2005; versions 4.1 2006, 5.0/5.1 2011, 5.3 2012, 6.0 2016; earlier name Solution-Centered Support); Consortium for Service Innovation, *KCS v6 Practices Guide* (library.serviceinnovation.org; Solve and Evolve loops, eight practices, article states, "search early search often", "reuse is review", issue/environment/resolution/cause; v6 released 21 April 2016); serviceinnovation.org *About Us* (KCS Academy formed 2011, name retired 2022). ⚠️ **Not established:** the date the Customer Support Consortium became the Consortium for Service Innovation, and whether "Customer Support Consortium" was also the pre-1997 name — the key uses the name recorded at incorporation; the Consortium's own About page shows its timeline only as an image. WebSearch was unavailable this session (session cap reached); research ran on WebFetch against known URLs.
