# History: Work Collaboration Tools

**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-11-covid-dislocation|11 — The COVID Dislocation]]
**Origin Parent:** Native birth — no origin parent. See below.
**Episode Tier:** 1
**Transferable Pattern:** The platform your product must beat is not always a competitor — sometimes it is a purchasing decision the buyer already made when they bought something else, and a better product does not overturn "already paid for."

> **Origin Parent — there genuinely is none.** Enterprise chat and work-tracking software did not descend from a pre-computer industry this vault tracks. It grew directly out of internet-era software teams' own internal needs, which makes it, like observability and no-code, a native Wave 6 birth.

## Before

Coordinating work meant email, meetings, and phone calls, none of which kept a searchable, shared record of what had actually been decided. Enterprise chat had been tried before and had not stuck at scale — internal tools like Lotus Sametime, and later Yammer (2008) and HipChat (2010) — none of which became the default interface to a company's work the way this industry's leaders eventually did. The absence was not technical. Persistent group chat was old technology by the 2010s. What was missing was a version of it built around search, integrations, and channels rather than the ephemeral, one-to-one shape instant messaging had inherited from consumer IM.

Neither of the earlier attempts survived as independent products, which is worth noting before the main contest below: Microsoft bought Yammer in 2012 and folded it into the Office estate rather than let it compete as a standalone product, and Atlassian's HipChat was discontinued in 2019 as part of a deal in which Atlassian took a stake in Slack and pointed its own customers there instead of continuing to compete. By the time Microsoft Teams arrived, one of Slack's earlier rivals for this exact niche had already been absorbed by the company building the tool that would go on to beat Slack on distribution. This detail is reported consistently in industry coverage of the deal; I did not re-verify the exact terms against a primary source in this session and note that rather than presenting the specifics with false precision.

## The Origin Event

**Slack began as an internal tool at Tiny Speck**, the company Stewart Butterfield co-founded to build an online game called Glitch. When Glitch failed to find a sustaining audience and the company wound the game down around October 2012, Butterfield's team repurposed the communication tooling they had built for their own use into a standalone product. **Slack launched publicly in August 2013**, and gained roughly 8,000 signups in its first 24 hours.

The "accidental byproduct of a failed game" framing is broadly accurate and worth keeping, with one caution: it can make the pivot sound passive, when the available account is of a deliberate choice to extract, polish and ship an internal tool rather than simply shutting the company down. The tool was a byproduct of the game; the company that resulted from it was not an accident.

Growth from there was fast by any standard: roughly 135,000 paying customers across 60,000 teams by February 2015; 750,000 daily active users by April 2015; over 1 million daily active users by late 2015; over 8 million daily active users by May 2018. Slack completed a direct public listing on the NYSE in June 2019 at a $19.5 billion valuation.

## What Became Cheap

**A searchable, persistent, cross-team communication record that any company, of any size, could turn on the same afternoon it heard about it** — no server, no IT deployment, no training beyond "it's like texting." This is Wave 6's mechanism applied to internal communication rather than a system of record: the product spread the way SaaS products spread when there is no capital decision standing between a team and trying it.

## The Contest

Microsoft announced Teams on 2 November 2016 and shipped it generally on 14 March 2017. From the start it was included as part of Microsoft 365 enterprise subscriptions — not a separate purchase decision, a feature of a suite most large organisations already owned — with a standalone free tier added later, on 12 July 2018.

The trajectory this produced is documented in both companies' own disclosures. Slack reported over 10 million daily active users at its April 2019 IPO filing. Microsoft reported Teams at 13 million daily active users that same July, already ahead of Slack's last major disclosed figure, and growing before the pandemic gave it a second, much larger push: 20 million (November 2019), 44 million (19 March 2020), 75 million (29 April 2020) as offices closed, 145 million (April 2021), and past 250 million monthly active users from mid-2021 onward. Salesforce announced its acquisition of Slack on 1 December 2020 for approximately $27.7 billion, closing 21 July 2021 — after which Slack stopped disclosing standalone user metrics as a public company data point, which is itself worth noting: the comparison this file draws becomes harder to make cleanly past 2021 because one side simply stopped publishing.

The crossover in disclosed daily-active-user counts predates COVID; the pandemic then widened a gap that had already opened. The mechanism is not disputed by the companies themselves in any serious way: Teams was distributed as something enterprises already had, while Slack had to be bought. In July 2023 the EU Commission opened a formal antitrust investigation into this bundling, and in June 2024 formally charged Microsoft over it; in August 2023, before the formal charges, Microsoft had already announced it would unbundle Teams from the Microsoft 365 suite in the EU. A regulator taking bundling seriously enough to charge a company over it is closer to an independent verdict on the mechanism than this vault can usually cite for a competitive claim of this kind.

## The Binding Constraint

The constraint that decided this contest was not a technical one. It was a procurement fact: a company already paying for Microsoft 365 licences was choosing between "a tool we already have" and "a new line item," and that comparison does not require the incumbent tool to be better, only to be free at the margin. No amount of product polish on Slack's side changed what was, for the buyer, an accounting question rather than a user-experience question.

## The Graveyard — There Isn't One

Slack lost the platform-distribution fight by any DAU comparison available, and it is tempting to write this file the way this vault writes a corpse. That would misstate what actually happened. Slack was acquired for $27.7 billion — a rich outcome by almost any measure, and one many venture-backed companies would count as the goal rather than the failure. The honest framing: Slack lost the race to be the default communication layer for the largest number of organisations, and won a highly profitable exit for its founders and investors regardless. Losing a platform war and having a good outcome are not mutually exclusive, and this file should not flatten that into a simpler story than the numbers support.

## What's Still Open

- [[problems/work-collaboration-tools/high-impact|🔴 Status Is Typed, Not Observed]] — the gap between what these tools record and what they infer
- [[niches/work-collaboration-tools/work-status-inference/profile|Work Status Inference]]
- [[niches/work-collaboration-tools/attention-and-notification/profile|Attention and Notification]] — the tax nobody in the stack is accountable for
- [[niches/work-collaboration-tools/cross-tool-dependency-graph/profile|Cross-Tool Dependency Graph]]
- [[niches/work-collaboration-tools/invisible-contribution-work/profile|Invisible Contribution Work]]

## The Transferable Pattern

> **Before crediting a product win to product quality, check what was already paid for. A tool bundled into something the buyer owns anyway does not need to win a feature comparison — it only needs to be in the room when the decision gets made, and most decisions of this kind get made by whoever is already in the room.**

**Sources:** Wikipedia, *Slack (software)*, *Microsoft Teams*; Salesforce press release, Slack acquisition (1 Dec 2020, closed 21 July 2021); European Commission press releases on the Teams bundling investigation (July 2023 opening, June 2024 charges) and Microsoft's announced EU unbundling (August 2023); this vault's `industries/work-collaboration-tools.md` and `series/eras/wave-11-covid-dislocation.md`.
