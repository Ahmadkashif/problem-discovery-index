# Lineage: SMB Marketing Agencies

**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the UTM parameters — `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content` — the campaign labels on a link, named for Urchin, the traffic analyser that became Google Analytics
**Builder:** Urchin Software Corporation
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A web shop that builds a client's site gets asked the same question every month: is it working?

In the mid-1990s the only record of what a website did was the server's log file — one line per request, written for the machine that served it. And even a count answered the wrong question. The log could say a page had been requested. It could say, sometimes, which page the visitor had come from. It could not say which of the client's promotions had produced the visit, because a banner, an email and a paid search listing that all pointed at the same page looked identical once they arrived.

For a firm whose revenue depended on the client renewing, that gap was the business problem. Work that cannot be shown to have produced anything is work that gets cut.

## What Got Built

Two things, one on top of the other.

First, **Urchin**: software that read a web server's log files and turned them into traffic reports in a web interface — pageviews, referrers, hits. The first commercial "Pro" version shipped in January 1998, for $199.

Second, **the Urchin Tracking Module convention**: a set of named parameters added to the end of a URL. The link in an email carries `utm_medium=email`; the link in a paid ad carries `utm_medium=cpc` and the keyword in `utm_term`. The destination page ignores them, but the analytics software reads them, so visits that would otherwise look identical arrive already labelled by source, channel and campaign. Five parameters, no infrastructure.

Google bought Urchin Software Corporation in April 2005 and made it the basis of Google Analytics, which it gave away free. The parameters came with it, prefix and all.

## Who Built It, And Why Them

**Urchin Software Corporation** — which began not as an analytics company but as a San Diego web shop.

Paul Muret and Scott Crosby started it in 1995 building and hosting business websites for local clients; Scott's brother Brett Crosby joined in 1997 and Jack Ancone joined as CFO. The company traded first as Web Depot and then as Quantified Systems before it took the Urchin name. By a history compiled from the founders' own accounts, Muret wrote a simple log-file analysis system to show how the firm's clients' sites were performing, and that in-house reporting tool became the first Urchin.

**That is why it was a web shop and not a database or advertising company.** The builders were the people who had to answer a client every month, holding the raw logs because they hosted the sites. The reporting was the thing the client paid attention to, so the reporting became the product. The campaign parameters follow the same logic: they solve attribution the cheapest way a service firm could, by getting whoever wrote the link to label it.

## What It Cost

**The label only exists if a person types it.** Nothing validates a UTM value. `Email`, `email` and `e-mail` are three different channels in the report, and an untagged link is lost into "direct" or "referral". The trade was near-zero cost for dependence on the discipline of every account manager, freelancer and client staffer who ever posts a link.

**It records the last click.** A tagged link says which link was clicked on this visit. It says nothing about the three ads the buyer saw earlier, which is why last-touch reporting became the default measure that agencies spend years arguing clients out of.

And when Google made the report free, the agency's measurement moved onto a platform owned by a company that also sold the ads being measured.

## What You Still Touch

Every link an agency posts still ends in `?utm_source=`, and the client's monthly report starts from whatever those strings say.

- [[problems/marketing-agencies-smb/high-impact|🔴 Campaign Performance Attribution Across Channels for SMB Clients]] — the last-click inheritance
- [[problems/marketing-agencies-smb/low-impact-1|🟡 Client Reporting Automation with Business Context]] — the monthly report Urchin was born to write
- [[problems/marketing-agencies-smb/worker-life-1|🟢 Account Manager Client Communication Overload]]
- [[niches/marketing-agencies-smb/client-reporting-attribution/profile|Client Reporting and ROI Attribution]]
- [[niches/marketing-agencies-smb/marketing-mix-modelling-consultancies/profile|Marketing Mix Modelling Consultancies]] — the discipline for what the last click cannot see

**Sources:** Wikipedia, *Urchin (software)* (initial release 1998; Google acquisition April 2005, forming Google Analytics; sales ended March 2012) and *UTM parameters* (introduced by Urchin; the five parameters and their meanings); tracking-garden.com, "Urchin — the first Google Analytics" (founders Muret and Crosby, San Diego, 1995; Web Depot and Quantified Systems names; hosting and site-building for local clients; Muret's log-analysis tool for client sites; Pro version January 1998 at $199; move to software only) — this source states it makes "no claim to correctness", and it is the only one read for the client-reporting origin; Scott Crosby's own essay on urchin.biz was found in search but could not be fetched. ⚠️ **Not established:** the date UTM parameters were introduced. One glossary site gives 1996, which predates the 1998 first release and was not corroborated; Wikipedia gives no date. The 1999 EarthLink deal appears only in tracking-garden.com and is left out of the body. The exact date Google Analytics launched was not checked against a primary source; the body says only that Google made it free after the 2005 acquisition.
