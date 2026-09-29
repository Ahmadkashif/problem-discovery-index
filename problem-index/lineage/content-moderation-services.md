# Lineage: Content Moderation Services

**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** PhotoDNA — a robust image hash matched against NCMEC's database of known child sexual abuse images
**Builder:** Microsoft
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The worst images on the internet were not new. They were the same images, uploaded again.

By the early 2000s child sexual abuse material was spreading across every large platform. In **2003** Attorney General John Ashcroft convened technology executives and asked them to propose a way to remove it. By Hany Farid's account, between 2003 and 2008 they did nothing effective, and the reason offered was scale. At a 2008 meeting the attendees agreed that any automated system would have to analyse an image in under two milliseconds, wrongly flag no more than one image in 50 billion, catch at least 99%, and never extract or share identifiable image content. No classifier could meet that, then or since, Farid argues.

What remained was human review — people looking at each image. And every image a person looked at, they looked at in full.

## What Got Built

A fingerprint that survives the platform's own processing.

The idea came from a fact NCMEC's then-CEO Ernie Allen mentioned in that meeting: NCMEC held millions of images already reviewed and confirmed as abuse, and those same images kept recirculating for years. If you could not recognise new abuse automatically, you could at least recognise the old.

An ordinary cryptographic hash such as MD5 would not work: Facebook, for example, resized, recompressed and stripped metadata from every upload, and any change produces a completely different MD5. PhotoDNA instead converts an image to grayscale, downsizes it to 400 × 400 pixels, applies a high-pass filter to emphasise salient structure, partitions the result into a grid, and extracts simple statistics from each cell into a feature vector. Two images match when the Euclidean distance between their vectors falls below a threshold. The hash is stable to resizing, recompression, colour changes and overlaid text — and it never requires anyone to look at the uploaded image to decide.

## Who Built It, And Why Them

**Microsoft**, through Microsoft Research, working with **Hany Farid**, then a computer scientist at Dartmouth, and with **NCMEC**, which supplied the reference database. Microsoft and NCMEC invited Farid to the 2008 meeting. After a year and a half of development it launched in **2009** on Microsoft's SkyDrive and Bing, and was then made available to other platforms.

Why Microsoft: it was both a host with the problem — a search engine and a consumer storage service — and a research lab able to build the answer, and, with NCMEC, it was the party that brought Farid in. Why a hash rather than a classifier: the design meets the engineering constraints by refusing to understand images at all. It does not recognise a child, an age, or explicitness; it recognises a picture someone has already classified. Farid reports Facebook deploying it network-wide in 2010, Twitter in 2011 and Google only in 2016; he also reports that in 2016, with about 80,000 NCMEC hashes, it removed more than 10 million images. Microsoft offered it as a cloud service from 2014, and in 2016 Facebook, Twitter, Google and Microsoft announced a shared hash approach for extremist content.

## What It Cost

**It only catches what a human has already seen.**

Every hash in the database exists because a person reviewed the original. The tool removes the second through millionth viewing, not the first. New material, altered beyond the threshold, or in a category nobody has hashed, still routes to a human queue — which is precisely the queue moderation vendors are paid to staff. The hash also carries no context: it matches pixels, so the policy question of what belongs in the database is decided entirely upstream of the tool.

## What You Still Touch

Upload a photo to almost any large platform and it is hashed and compared before a person could see it. What reaches a vendor's reviewer is the residue the hash could not decide — the novel, the ambiguous, the unhashed languages and categories.

- [[problems/content-moderation-services/worker-life-1|🟢 The Reviewer]] — the human who sees what the hash has not yet seen
- [[problems/content-moderation-services/low-impact-2|🟡 Coverage in Languages Nobody Built For]] — where no reference set exists to match against
- [[niches/content-moderation-services/exposure-management/profile|Reviewer Exposure Management]]
- [[niches/content-moderation-services/exposure-triage/profile|Exposure Triage]]

**Sources:** Hany Farid, "Reining in Online Abuses", *Technology and Innovation* 19 (2018) 593–599, doi 10.21300/19.3.2018.593 (read directly: Ashcroft 2003; 2003–2008 inaction; 2008 invitation by Microsoft and NCMEC; the four engineering requirements; Ernie Allen's two facts; MD5 failure and Facebook's resizing; grayscale, 400 × 400, high-pass, quadrant statistics, Euclidean threshold; 2009 launch on SkyDrive and Bing; Facebook 2010, Twitter 2011, Google 2016; ~80,000 hashes and 10 million removals in 2016 — all Farid's own account, a participant's, not independent); Wikipedia, *PhotoDNA* (Microsoft Research and Farid from 2009; Azure offering 2014; 2016 extremist-content announcement). ⚠️ **Conflict, not resolved:** Farid dates Facebook's deployment to 2010; press coverage (iTnews) and secondary sources date Facebook's adoption to May 2011. **Not established:** the date and terms of Microsoft's donation to NCMEC — a secondary summary gives 15 December 2009, not confirmed against a Microsoft or NCMEC primary source. I found no source naming the Microsoft Research engineers who co-developed it, and none is asserted. Microsoft is keyed as builder because it co-developed, launched, owns and licenses the tool; Farid is the named algorithm co-designer and could argue for a joint key.
