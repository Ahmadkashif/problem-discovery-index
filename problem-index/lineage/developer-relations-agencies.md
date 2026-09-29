# Lineage: Developer Relations Agencies

**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Orbit Model — a published framework that places each community member in one of four numbered orbit levels by the commitment and frequency of their activity, and scores the whole community by "gravity", the rate at which member involvement is changing
**Builder:** Orbit
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A developer advocate's budget was defended in a language that did not describe the work.

In a growth-stage software company, community and advocacy usually reported into marketing, and marketing's job was to fill a funnel for sales. So the question asked of every meetup, talk and forum was the funnel's question: how many leads did it produce?

For developer work that question has no honest answer. A developer who watches a talk, reads a sample and joins a chat server carries no identifier across those touches, and the purchase arrives months later. The advocate could report member counts — which rise just as happily when a community fills with unanswered questions and people who leave.

## What Got Built

A vocabulary, published as a document anyone could fork.

The Orbit Model replaced the funnel with a gravity well. Every member sits at an **orbit level**, numbered so that "Orbit 1" always means the inner circle: Orbit 4 *Exploring* (newcomers and passive readers), Orbit 3 *Participating*, Orbit 2 *Contributing*, Orbit 1 *Leading*. Placement is driven by two signals — the commitment level of a member's activities and how often they participate.

A member's involvement is scored as **love** (presence, frequency, recency) and their influence as **reach**; the community-level score is **gravity**, defined arithmetically:

> Gravity = Change in Weighted Commitment / # of Members

The point of that formula is its denominator. A community that doubles in size while nobody moves inward has *falling* gravity. That is exactly the case the member-count report hid.

The model went onto GitHub in November 2019 under the MIT licence, with a talk titled "Communities aren't funnels" at DevRelCon in December 2019.

## Who Built It, And Why Them

Josh Dzielak and Patrick Woods, who founded a company called Orbit in 2019 to sell software implementing it.

The model's history page is plain about the motive: its authors built it "to scratch our own itch as community leaders at high-growth companies," where "we had to report metrics and secure budget." The repository's README dates first use of the model to 2014. Dzielak's own site lists a 2014 WIRED feature on Keen IO in his timeline; this note does not establish what role he held there or whether the model was first used at Keen.

**Why them rather than an analytics vendor:** the people who could define the unit were the people who had been asked to justify themselves in the wrong one. A marketing-analytics firm would have extended the funnel; practitioners who had lost the funnel argument designed the instrument that let them stop having it. Open-sourcing the framework first meant the vocabulary reached buyers ahead of the vendor — the model was the marketing for the software.

## What It Cost

The model measures involvement, not adoption. It gives an advocate a defensible number for community health, but it still does not connect a member's orbit level to a signed contract. The attribution gap the funnel exposed is renamed, not closed.

It also requires identity. Scoring love means joining one person's activity across GitHub, a chat server, a forum and product sign-up — the same cross-platform linking that raises the privacy questions the rest of the industry now works on.

And the company that stewarded it did not stay independent: Dzielak's timeline records Orbit's acquisition by Postman in 2024, and the GitHub repository now states the project is no longer under active development.

## What You Still Touch

Every community dashboard that buckets members into tiers — newcomer, active, champion — and reports movement between them rather than headcount is working in the grammar the Orbit Model published.

- [[problems/developer-relations-agencies/high-impact|🔴 The Function Cannot Prove It Works and Is Cut First Because of It]] — the budget argument the model was built to win, still not won
- [[problems/developer-relations-agencies/low-impact-1|🟡 Community Health and Question Triage]] — the member-count problem the gravity denominator exists to catch
- [[niches/developer-relations-agencies/community-health/profile|Community Health]]
- [[niches/developer-relations-agencies/adoption-attribution/profile|Adoption Attribution]]
- [[niches/developer-relations-agencies/identity-and-privacy/profile|Identity Linking & Privacy Design]] — the price of scoring one person across many platforms

**Sources:** github.com/orbit-love/orbit-model — README ("first used in 2014 and put on GitHub in November 2019", MIT licence, "no longer under active development"), `pages/about.mdx` (model origins quotation; Orbit founded by Josh Dzielak and Patrick Woods in 2019; history list incl. DevRelCon December 2019), `pages/love/orbit-levels.mdx`, `pages/glossary.mdx` and `pages/gravity/measure.mdx` (gravity formula) — read directly from the repository archive; joshed.io (Dzielak's personal timeline: 2014 WIRED on Keen, 2020 a16z investment in Orbit, 2021 Series A, 2024 Postman acquired Orbit); Software Engineering Daily episode page, 25 March 2021 (Dzielak and Woods as Orbit co-founders). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs only. ⚠️ **Not established:** Dzielak's or Woods's role and employer when the model was first used; the repository's own pages disagree on the start date (README "first used in 2014", about page "since 2016"); the orbit.love blog post "Why Orbit is Better Than Funnel for Developer Relations" returned an error and was not read; the Postman acquisition date is from Dzielak's own site only.
