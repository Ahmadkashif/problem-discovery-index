# Lineage: Web Data Extraction Firms

**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** robots.txt, the Robots Exclusion Protocol: a plain-text file at a site's root listing which user-agents may not fetch which paths
**Builder:** Martijn Koster
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

In early 1994 a program that fetched web pages automatically could knock a server over, and the server had no way to say no.

The web was small, hosted on institutional machines with thin connections. A human browsing fetched a page every few seconds. A crawler could fetch as fast as the network allowed, and the first generation of crawlers was written by individuals experimenting. None of them had any convention for asking what a site wanted fetched. A site operator's only defence was to block by address after the damage, if they could work out who it was.

The need was not to stop crawling, which people wanted for indexing. It was a way for a site to publish its wishes *before* the visit, cheaply enough that any crawler would bother to read them.

## What Got Built

A text file at a fixed address.

A site places `/robots.txt` at its root. Each record names a `User-agent` and lists `Disallow` path prefixes that agent should not fetch. A polite crawler reads the file first and skips what it is asked to skip. The proposal was initially called `RobotsNotWanted.txt`.

Nothing enforces it. The file does not authenticate the crawler, block anything or carry legal terms. It is a request. **By June 1994** it had become a de facto standard that most crawlers followed, including those behind the search engines WebCrawler, Lycos and AltaVista.

It stayed informal for twenty-five years. On **1 July 2019** Google announced a proposal to make the Robots Exclusion Protocol an IETF standard. **RFC 9309**, by Martijn Koster, Gary Illyes, Henner Zeller and Lizzi Sassman, was published in **September 2022** as a Proposed Standard.

## Who Built It, And Why Them

**Martijn Koster**, who proposed it in **February 1994** on `www-talk`, then the main mailing list for web development, while working at **Nexor** in the UK.

Why him: he was on the receiving end. Charles Stross, later known as a novelist, says he provoked the proposal. He had written a badly behaved crawler that inadvertently caused a denial of service on Koster's server. Emails from Stross to Koster are dated from 7 March 1994. Stross also wrote the first crawler known to comply, CharlieSpider/0.3.

Why a mailing-list convention and not a product: in 1994 there was no firm with an interest in owning the answer. There was also no authority that could impose one on anonymous crawler authors. The only thing that could spread was something trivially cheap for both sides. A site operator needed only a text editor, and a crawler author needed only one extra GET. Koster's design is exactly that cheap, and it is exactly as weak as that implies.

He is keyed as an individual because the standard came out of an informal list consensus, not a Nexor product. I found no evidence that Nexor sponsored it as a company project.

## What It Cost

**Consent was reduced to a voluntary signal.** robots.txt says what a site asks. It cannot say *why*, for *what purpose*, under what terms, or for how long. It has no legal force in most jurisdictions, though it carries weight as evidence of intent.

That was adequate when the only question was "may you index me". It is inadequate now that the question is "may you take my prices, my listings, or my text to train a model". From the 2020s, sites began using the file to refuse AI training crawlers. In 2023, blocking OpenAI's GPTBot became common among news sites such as the BBC and *The New York Times*. The file was being asked to carry a licensing decision with a syntax built for load management.

## What You Still Touch

An extraction firm's compliance check starts by fetching `robots.txt`, because nothing better exists at the protocol level. Then it goes to lawyers, because the file answers almost none of the questions the lawyers need answered.

- [[problems/web-data-extraction-firms/low-impact-1|🟡 Collection Governance and Permission Tracking]]: the permission layer the 1994 file never became
- [[problems/web-data-extraction-firms/worker-life-2|🟢 Compliance Reviewer on a Collection Request]]
- [[niches/web-data-extraction-firms/collection-governance-record/profile|Collection Governance Record]]
- [[niches/web-data-extraction-firms/the-compliance-reviewer/profile|The Compliance Reviewer]]

**Sources:** Wikipedia, *Robots.txt* (Koster at Nexor; February 1994 proposal on www-talk; `RobotsNotWanted.txt`; Stross's claim and emails dated from 7 March 1994; CharlieSpider/0.3; de facto standard by June 1994 including WebCrawler, Lycos, AltaVista; Google's 1 July 2019 IETF proposal; RFC 9309 authors and September 2022 publication; 2020s AI-crawler blocking and 2023 GPTBot blocking by BBC and *New York Times*); Wikipedia, *Martijn Koster*, via search summary. Koster's own retrospective, "Robots.txt is 25 years old" (greenhills.co.uk), refused the fetch (HTTP 403), so his first-hand account was not read. The "no legal force in most jurisdictions / evidence of intent" characterisation is the vault's `industries/web-data-extraction-firms.md`, cited as vault material, not independent corroboration. ⚠️ **Not established:** whether Nexor formally sponsored the work. The individual key rests on the absence of evidence that it did. The "why a convention" argument is inference.
