# Lineage: Digital Goods Marketplaces

**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the DMCA takedown notice — the six-element notice defined in 17 U.S.C. § 512(c)(3), with its designated agent and 10–14 business-day counter-notice clock
**Builder:** US Congress
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The question was not how to stop copying. It was who pays when a stranger's upload infringes.

In the early 1990s a bulletin board, Usenet server or web host stored files it had never looked at. If each exposed the host to liability, hosting was uninsurable. If none did, rights holders had no one to ask.

That tension reached court in *Religious Technology Center v. Netcom*. Dennis Erlich had posted L. Ron Hubbard's copyrighted writings to `alt.religion.scientology`, and the rights holder sued Netcom, whose servers carried the copies, as well as him. On **21 November 1995** Judge Ronald Whyte in the Northern District of California held that Netcom was not a direct infringer — some element of volition was required — but left open contributory liability **if Netcom knew** and did nothing.

Knowledge became the hinge. What hosts lacked was a defined way of *being told*.

## What Got Built

A form, written into statute.

Title II of the Digital Millennium Copyright Act was signed on **28 October 1998**. Section 512(c) gives a provider a safe harbour for material stored at a user's direction, on conditions. It must designate an agent to receive complaints. And when it receives a notice containing six elements, it must act expeditiously to remove or disable access to the material.

The six elements are the tool: a signature of someone authorised to act for the owner; identification of the work infringed; identification of the infringing material **with information reasonably sufficient to permit the service provider to locate it**; contact details; a statement of good-faith belief that the use is unauthorised; and a statement, under penalty of perjury, that the sender is authorised.

A counter-notice path runs the other way. If the uploader objects, the provider restores the material after 10 to 14 business days unless the claimant files suit.

## Who Built It, And Why Them

**US Congress** — but the shape was negotiated, not designed.

Courts had not converged on a single standard for intermediary liability after *Netcom*, and both sides needed uniformity. Congress brought online service providers and copyright owners into direct negotiation, and § 512 is the settlement. Contemporary accounts called it a win for the telecom and internet industry groups, with concessions to rights holders.

Why a statute and not a contract: neither party could bind the other. Only law could trade a procedure for a liability shield across every provider at once. The trade is visible in the design: the host gets certainty in exchange for a mailbox and prompt removal, and the rights holder gets a remedy **that costs them the work of finding every copy**.

## What It Cost

The notice is addressed to a location — material the provider can find on its own system, one host at a time. That fit 1998. It fits a marketplace creator badly, because a sold template can be reposted to a hundred hosts, and each is a separate notice to a separate agent.

The burden of discovery was assigned to the party least able to carry it at scale. The statute removes; it does not prevent. A file taken down under one name can go back up under another the next day, and nothing in § 512 obliges a host to stop it.

A marketplace reviewer handling a notice between two creators is not deciding copyright. They are administering a clock, with no standard for the hard cases.

## What You Still Touch

A US-facing "report infringement" form asks for a work, a location, a good-faith statement and a signature under penalty of perjury because those are § 512(c)(3)'s elements, and a host that wants the safe harbour has reason to collect them. The creator filling it in for the fortieth time is doing the discovery work the 1998 settlement assigned to them.

- [[problems/digital-goods-marketplaces/high-impact|🔴 Unauthorised Redistribution as Direct Substitution]] — a location-by-location remedy for a good that copies everywhere at once
- [[problems/digital-goods-marketplaces/worker-life-1|🟢 Takedown and Copyright Reviewer]] — the person administering the clock
- [[niches/digital-goods-marketplaces/redistribution-response/profile|Redistribution Response]]
- [[niches/digital-goods-marketplaces/asset-fingerprinting-at-scale/profile|Asset Fingerprinting at Web Scale]] — the discovery step the statute left to the claimant
- [[niches/digital-goods-marketplaces/the-copyright-reviewer/profile|The Copyright Reviewer]]

**Sources:** Wikipedia, *Online Copyright Infringement Liability Limitation Act* (signing 28 October 1998; six notice elements quoted from § 512(c)(3); designated agent; 10–14 business-day counter-notice window; characterisation as a victory for telecom and internet groups with concessions to copyright owners); Wikipedia, *Religious Technology Center v. Netcom On-Line Communication Services, Inc.* (decided 21 November 1995, N.D. Cal., Judge Ronald M. Whyte; Erlich postings to alt.religion.scientology; volition requirement; contributory liability turning on knowledge); Justia, 907 F. Supp. 1361 (N.D. Cal. 1995); Copyright Alliance, *20 Years of the DMCA: Notice & Takedown in Hindsight* and search-result summaries of *Iowa Law Review* and NYU JLPP articles (Congress convening negotiations between service providers and content owners; courts' failure to converge on a standard) — read as secondary summaries, not full texts. ⚠️ **Not established:** the names of the negotiating parties and the dates of the 1998 negotiating sessions; I did not reach a primary legislative-history source (e.g. H.R. Rep. 105-551 or S. Rep. 105-190) this session. The claim that marketplace report forms collect these elements is inferred from the statute's requirements, not from a survey of any platform's forms.
