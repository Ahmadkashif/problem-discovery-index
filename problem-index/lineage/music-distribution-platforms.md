# Lineage: Music Distribution Platforms

**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the DDEX Electronic Release Notification (ERN) message — the XML format in which a release's tracks, metadata, rights and deal terms are delivered to a digital music service
**Builder:** DDEX
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Selling a song online meant describing it, over and over, in somebody else's format.

A physical record ships with its information printed on it. A digital track is a file plus everything a store needs to sell it and pay for it: title, artist, the recording's identifier, who owns it, in which territories it may be sold, at what price, from what date. By the mid-2000s record companies were sending that description to a growing set of download and subscription stores, and each store defined how it wanted to receive it.

So every label maintained a delivery variant per store, and every store wrote ingestion code per label. The same cost ran back the other way: sales reports came to labels and rights societies in each store's own layout. Nothing about the music differed between stores. Only the paperwork did, and it was paid for many times over.

## What Got Built

**A shared message for announcing a release.** DDEX's first four standards, announced in October 2006, were the **Electronic Release Notification Message Suite** — telling a digital service what content exists and on what terms — the **Digital Sales Report** message for reporting sales back, a **Data Dictionary** of agreed terms, and the **DDEX Party Identifier** for the companies involved.

The ERN is the one a distributor lives in. A release goes out as one structured XML message listing its resources and their identifiers, the release they compose, and the deals under which the service may sell or stream it. A service that accepts ERN can take a release from any sender that produces it.

## Who Built It, And Why Them

**DDEX**, the Digital Data Exchange consortium, formed in May 2006.

Its charter members, per its first-standards announcement, were the four major record companies of the day — EMI Music, Sony BMG, Warner Music Group and Universal Music Group — alongside the rights organisations ASCAP, the Harry Fox Agency, the MCPS-PRS Alliance, SGAE and SACEM, and the digital services AOL, Apple, Microsoft and RealNetworks. ASCAP's Chris Amenita chaired it.

**That membership is the explanation.** The cost of incompatible formats fell on both ends of every delivery: the few companies owning most catalogue, and the few services selling it. Each had enough volume for the waste to show, and together they covered almost every connection in the chain. Rights societies came because the same metadata determined whose composition had been sold.

**No independent distributor appears among the charter members.** The services that now put a self-released track onto every platform in days inherited a format designed for label-to-store deliveries of professionally prepared catalogue. What a distributor's upload form collects is, in large part, the list of fields an ERN message needs.

## What It Cost

**A standard format is not a standard interpretation.** ERN defines the message; each receiving service still publishes its own choreography, validation rules and style requirements. The vault's own industry note calls those per-service quirks "the actual work". Standardisation moved incompatibility down a layer rather than removing it.

**It carries whatever the sender typed.** The message can describe a release completely and still be wrong. Its schema can be satisfied by an artist name spelled three ways, a featured artist in the title field, or a composition credit missing entirely — and the recording and the underlying composition are identified by different codes, ISRC and ISWC, with no authoritative join between them. A delivery format built by parties who already held clean catalogue took accuracy of input for granted. Self-service distribution removed exactly that assumption.

## What You Still Touch

When a distributor rejects your release because a field is missing, or a store lists your track under the wrong artist page, you are touching an ERN message and the choices of the companies that designed it in 2006.

- [[problems/music-distribution-platforms/low-impact-1|🟡 Release Delivery and DSP Specification Compliance]] — the per-service layer ERN did not remove
- [[problems/music-distribution-platforms/high-impact|🔴 The Unmatched Pool]] — metadata that validates but does not match
- [[problems/music-distribution-platforms/worker-life-2|🟢 The Metadata Operations Reviewer]]
- [[niches/music-distribution-platforms/dsp-delivery-and-ingestion/profile|DSP Delivery & Ingestion]]
- [[niches/music-distribution-platforms/metadata-capture-at-upload/profile|Metadata Capture at Upload]]
- [[niches/music-distribution-platforms/recording-to-composition-matching/profile|Recording-to-Composition Matching]]

**Sources:** GlobeNewswire, "First Digital Data Exchange Standards Established and Agreed to by Digital Music Service Providers, Record Companies and Music Rights Societies", 18 October 2006 (the four first standards; charter, contributing and participating members; Chris Amenita, ASCAP, chair); ddex.net, "About DDEX" (formed 2006; not-for-profit membership organisation; the need for a common metadata format delivered in a common way); search-result summary of MacDailyNews, 4 May 2006 (formation in May 2006; Apple, Microsoft and the major labels) — not read in full; Wikipedia, *DDEX* — its member list includes Spotify and Google as "charter members", which conflicts with the 2006 press release and was not relied on; this vault's `industries/music-distribution-platforms.md` (per-service quirks; ISRC/ISWC link not authoritative) — vault material, not independent corroboration. ⚠️ **Not established:** whether individual stores' pre-2006 delivery formats were each distinct in the way described — the press release speaks only of inefficient information sharing across the supply chain, and no named pre-DDEX format was found. Which ERN version is current, and whether early independent distributors helped shape later versions, were not checked; the twelve unnamed contributing members of 2006 were not identified. The claim that distributor upload forms mirror ERN fields is inference from the format's purpose, not a sourced finding.
