# Lineage: SEO Tooling Vendors

**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** WebPosition Gold — a desktop program whose Reporter module fired a site's target keywords at each search engine and logged the page's position in the results, alongside a doorway-page generator and a submission scheduler
**Builder:** FirstPlace Software
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

In the late 1990s nobody could see where a page ranked without typing the query.

A webmaster trying to be found on AltaVista, Excite, Infoseek, Lycos and the rest had a list of phrases and a handful of engines, each with its own ranking behaviour and each re-indexing on its own schedule. Checking position meant searching every phrase on every engine by hand, paging through results, and writing the number down — then doing it again next week to see whether the last change had worked. For a consultant with several clients, the checking crowded out the optimising.

The engines of the period ranked largely on on-page text, which made the loop tempting: change a page, resubmit it, measure the rank, repeat. What was missing was the measuring instrument.

## What Got Built

A Windows program that did the typing. **WebPosition Gold** bundled several modules: a *Reporter* that queried the engines for a list of keywords and recorded where the site appeared; a *Page Critic* that compared a page's keyword use against pages already ranking; a *Page Generator* that produced keyword-tuned "doorway" pages; an upload manager; a submission scheduler; and a traffic analyser.

The Reporter is the artefact that survived. It turned rank into a number that could be tracked over time and put in front of a client, and it established the category's basic unit of account — **one keyword, one engine, one position, one date.** Every rank tracker since has kept that row structure.

## Who Built It, And Why Them

**Brent Winters**, founder, president and chief architect of **FirstPlace Software**, which published WebPosition Gold. Reviewers of the period describe it as available by 1997 and among the oldest site-promotion tools; one secondary source says the underlying application was developed in 1996 by a firm called Code Gurus — a claim this note could not corroborate.

Why a small independent software house and not a search engine or an agency? Because the engines had no reason to publish rank data — rank was their product, and a tool that measured it was a tool for gaming it — and agencies of the time were not software publishers. A shrink-wrapped desktop program sold to thousands of webmasters could amortise the work of keeping up with every engine's result-page format, which no single consultant could. The tool's design also shows the commercial bet: it sold the measurement *and* the manipulation (doorway pages) in one box, because the customer wanted both.

FirstPlace sold WebPosition to NetIQ, owner of WebTrends, in 2004; Winters went on to a billing-assurance product.

## What It Cost

**The measurement ran on someone else's servers without permission.** Every report was hundreds of automated queries against a search engine that had not agreed to answer them.

By January 2002 Winters was saying publicly that Google "don't like any product, not just WebPosition Gold, querying their service." Google's webmaster guidelines went further and named it — "Google does not recommend the use of products such as WebPosition Gold™ that send automatic or programmatic queries to Google" — by trade-press accounts, the only product singled out that way. After Google discontinued its SOAP Search API in December 2006, rank tracking had no sanctioned route at all. Reports in August 2008 had WebPosition's Google checks failing outright.

The industry kept the unit of account and moved the scraping into server farms, which is why rank data remains an observation made from outside, against the terms of the thing observed.

## What You Still Touch

Every SEO dashboard still opens on a table of keyword, position and date — the WebPosition row. It is now accurate and nearly meaningless where a generated answer sits above position one.

- [[problems/seo-tooling-vendors/high-impact|🔴 Rank Stopped Being a Proxy for Anything]]
- [[problems/seo-tooling-vendors/worker-life-1|🟢 The SEO Explaining a Traffic Drop They Did Not Cause]]
- [[problems/seo-tooling-vendors/low-impact-1|🟡 Search Volume and Difficulty Sold as Facts]]
- [[niches/seo-tooling-vendors/generative-visibility-measurement/profile|Generative Visibility Measurement]]
- [[niches/seo-tooling-vendors/causal-attribution-of-change/profile|Causal Attribution of Visibility Change]]

**Sources:** InfoWorld, "Avoid a search engine ban", 22 January 2002 (Winters as FirstPlace president; the Google quote; doorway pages); searchengineworkshops.com, "What's Brent Winters Been up to Since Selling WebPosition Gold?" (Winters as founder; sale to NetIQ/WebTrends in 2004; SureTime billing-assurance product); evolt.org review and reseller pages at win.net (module list; "since at least 1997"); aimclear, "Google makes it Official: WebPosition Gold is Dead", 11 June 2007 (guideline wording; SOAP API discontinued December 2006); Search Engine Roundtable, 6 August 2008 (Google checks failing from 5 August 2008); this vault's `history/seo-tooling-vendors.md` (context only, not independent corroboration). ⚠️ **Not established:** WebPosition's exact first-release year and FirstPlace Software's location; the 1996 "Code Gurus" origin appears in a single search-result summary and is unconfirmed. ⚠️ **Sources disagree** on when Google's guidelines first named WebPosition: aimclear presents it as a June 2007 update, while forum threads suggest earlier wording — hence no date given above. The NetIQ purchase price was not found.
