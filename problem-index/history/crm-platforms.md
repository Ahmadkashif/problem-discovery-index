# History: CRM Platforms

**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Origin Parent:** [[origins/telecom-carriers/profile|Telecom Carriers]]
**Episode Tier:** 1
**Transferable Pattern:** The record-keeping system and the predictive science an industry needs frequently arrive from two unrelated lineages that are never joined inside the product — so the system ships with a trusted ledger and an untrusted forecast, forever.

## Before

Enterprise customer records were kept the way Wave 4 kept everything: on a server the buyer owned, running software the buyer had licensed for a large upfront fee and then paid a systems integrator to configure for the better part of a year. Siebel Systems, founded in 1993 by Thomas Siebel and Patricia House — both formerly of Oracle — sold exactly this. By the late 1990s it was the category's dominant vendor, reaching a peak of roughly 45% market share in 2002, named Fortune's fastest-growing US company in 1999, and past $1 billion in revenue by 2000.

The product this bought a company was real and valuable: one place where every account, contact and opportunity lived, replacing the rolodexes and personal notebooks salespeople had kept before. But it was purchased the way a mainframe or an ERP suite was purchased — a capital decision, made once every several years, by a company large enough to carry it. A twelve-person sales team was not a Siebel customer. It could not have been.

## The Origin Event

**Salesforce was founded on 8 March 1999** by Marc Benioff (another Oracle veteran), Parker Harris, Dave Moellenhoff and Frank Dominguez, with early backing from Larry Ellison and Halsey Minor. Its prototype shipped that November. The pitch was not a better CRM feature set — Siebel's was more complete for years — it was a different way to buy one: a browser, a login, a monthly per-seat fee, no server and no implementation project.

Benioff staged this as a fight from the beginning. Salesforce's marketing literally picketed a Siebel user conference with actors carrying "No Software" signs. This was theatre, but it named the real axis of competition precisely: not features, but who carries the fixed cost and how long the buyer is committed before they see value.

*(Myth on record elsewhere in this vault, worth repeating here because this is the industry it is most often misattributed to: Salesforce did not coin "software as a service." The term is in print by February 2001, in an SIIA whitepaper, two years after Salesforce's founding. Salesforce popularised the model; it did not name it.)*

## What Became Cheap

**Giving a sales team a shared, always-current record of every account, without a server, an IT department, or a six-figure services engagement.** Wave 6's general mechanism — AWS turning the fixed cost of compute into a meter — is what let Salesforce, and later HubSpot, Pipedrive and Zoho, sell this to the exact customer Siebel structurally could not reach: the small business for whom a capital software purchase was never going to be rational.

## The Contest

This is the cleanest head-to-head this vault has for Wave 6: a real product, a real incumbent, and a documented shift in the two companies' fortunes, though the record supports a narrower claim than "Salesforce killed Siebel."

Salesforce's revenue climbed from $5.4 million in 2000 to $22.4 million in 2001 and past $1 billion by 2009 — a small-business beachhead building slowly into a company that could eventually contest the mid-market, not an overnight rout of the enterprise incumbent. Siebel, meanwhile, had genuinely won the category it was competing in; nothing in the available record shows Salesforce taking enterprise accounts away from Siebel directly during Siebel's peak years. What the record does show is Oracle announcing its acquisition of Siebel on **12 September 2005**, for **$5.8 billion**, closing the following year. Siebel's own product survived inside Oracle for years afterward as its on-premise CRM offering, while Oracle built a separate cloud CX line; there is no clean end-of-life date on record for the original Siebel codebase, and no evidence in Siebel's own history of the internal turmoil — accounting trouble, leadership crisis, a botched product cycle — that would let this file claim a dramatic collapse. Siebel was not toppled. It was acquired into a company that was consolidating enterprise software broadly that same year (Oracle bought PeopleSoft in January 2005, itself sitting on top of JD Edwards), a wave of M&A that had more to do with Oracle's roll-up strategy than with anything Salesforce did.

The honest version: Salesforce did not defeat Siebel in the market Siebel dominated. It created and won a different, initially much smaller market — the SMB and mid-market buyer priced out of Siebel entirely — and grew into the incumbent's territory over the following decade, by which point Siebel's independent corporate existence had already ended for unrelated reasons. The lesson for an FDE is sharper for being narrower: **a disruptive pricing model does not need to beat the incumbent's product. It only needs to be sold to the customer the incumbent's cost structure excludes, and to wait.**

## How It Was Actually Solved — Two Inheritances That Never Met

The architecture of a CRM — accounts, contacts, opportunities, stages, one record per relationship — is Wave 4's inheritance: the client–server data model Siebel built, which Salesforce re-hosted rather than reinvented. That is why every CRM still looks like a rolodex with a pipeline bolted on.

The *predictive* science this industry actually needs arrived from somewhere else entirely, and considerably earlier. [[origins/telecom-carriers/legacy|Telecom carriers' legacy file]] documents that the propensity score — the idea that a customer's own recorded behaviour, joined across systems built for other purposes, predicts what they will do next — was demonstrated on a 47,000-subscriber wireless dataset (Mozer et al., IEEE Trans. Neural Networks, 2000) a full generation before it became a CRM feature. Every "health score" and "deal risk" field in a modern CRM is that result, repackaged as a dropdown.

These two lineages were never joined inside the product. The CRM inherited Siebel's record structure and, separately, inherited telecom's predictive method as a bolt-on feature — but the number the industry actually trusts for forecasting revenue is neither: it is the sales representative's manually chosen pipeline stage and self-reported close date, a field the platform's own hub note observes is "trusted less than a regional VP's gut." The behavioural exhaust that would let a CRM forecast the way a telecom carrier forecasts churn — calls, email response latency, meeting cadence, buying-committee breadth — sits in the same database, unused for this purpose, because nobody joined it to the outcome the way Mozer's team joined billing, usage, credit and complaint records in 1999.

## What's Still Open

- [[problems/crm-platforms/high-impact|🔴 Forecast Accuracy the Sales Leader Will Actually Use]] — closing exactly the gap this file traces to 1999
- [[niches/crm-platforms/enterprise-sales-forecasting/profile|Enterprise Sales Forecasting]]
- [[niches/crm-platforms/revenue-intelligence-capture/profile|Revenue Intelligence Capture]] — the category that grew up to do what the CRM's own data could have done
- [[niches/crm-platforms/activity-graph-capture/profile|Activity Graph Capture]] — the behavioural exhaust, uncaptured
- [[niches/crm-platforms/account-data-hygiene/profile|Account Data Hygiene]] — Wave 4's record model, still the shape of the problem

## The Transferable Pattern

> **When a system's most expensive input is also the one whose author has no incentive to make it accurate, look for the predictive science the industry already solved somewhere else, on data collected for a different reason — and check whether anyone ever actually joined it to the record everyone still trusts by habit instead.**

An FDE arriving at a CRM-shaped business should not start by asking how to build a better forecasting model. The model has existed, proven, since 1999. The question is why a company still asks a salesperson to guess instead.

**Sources:** Wikipedia, *Siebel Systems*, *Salesforce*; Oracle press release, Siebel acquisition announcement (12 September 2005); SIIA, *Strategic Backgrounder: Software as a Service* (Feb 2001); this vault's `industries/crm-platforms.md`, `origins/telecom-carriers/legacy.md` (Mozer et al., IEEE Trans. Neural Networks 11(3), 2000).
