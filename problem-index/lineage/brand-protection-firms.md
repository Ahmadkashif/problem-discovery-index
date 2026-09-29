# Lineage: Brand Protection Firms

**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** eBay's Verified Rights Owner (VeRO) Program and its Notice of Claimed Infringement (NOCI) form
**Builder:** eBay
**Builder in vault:** [[industries/online-marketplaces|Online Marketplaces]]
**Verification:** partial — see Sources

## The Problem That Came First

A counterfeit used to have an address. It sat in a shop, a warehouse or a street stall, and a brand's lawyers sent an investigator, then a letter, then a raid.

An online auction dissolved the address. The seller was a username, the goods were a photograph, and the listing would end within days whether anyone acted or not. A brand could not sue ten thousand pseudonymous sellers, and the venue — the one party who could actually make a listing disappear — insisted it was not the seller and could not tell a real Tiffany bracelet from a fake one by looking at a JPEG.

So the expensive step was not detecting a fake. It was converting a brand's suspicion into the removal of a specific listing, fast enough to matter, without either party taking legal responsibility for the judgement.

## What Got Built

A form, and a promise about how quickly the form would be acted on.

Under VeRO, a rights owner with a good-faith belief that a listing infringed its copyright or trademark submitted a **Notice of Claimed Infringement**. eBay staff checked the notice for accuracy — not the item for authenticity — and removed the listing. As the Second Circuit recorded in 2010, eBay's practice was to remove within **twenty-four hours**, and it in fact deleted **70–80% within twelve hours**. If bidding was still open, eBay cancelled the bids and told the seller why; if it had closed, eBay cancelled the transaction retroactively and refunded its own fees. Repeat offenders were warned and then suspended. Rights owners could also publish an "About Me" page on eBay stating their legal position.

VeRO sat alongside a detection layer eBay built later: by May 2002 a rules-and-models "fraud engine" screened listings, including about 90 Tiffany-specific keywords, replacing earlier manual keyword searches.

## Who Built It, And Why Them

**eBay**, and the reason is liability.

The late-1990s legal settlement for online intermediaries ran through notice: a platform that acted on specific notices of infringement could argue it had no knowledge of the rest. VeRO is commonly said to date from **1998**, the year the Digital Millennium Copyright Act created notice-and-takedown for copyright. Trademark law had no equivalent statute, and eBay built the same mechanism for trademarks voluntarily. The shape follows from eBay's position: it had the only lever over the listing, the least knowledge of whether the item was genuine, and a business built on unvetted sellers it could not afford to vet one by one.

The design was tested in **Tiffany (NJ) Inc. v. eBay Inc.**, filed in 2004. The district court ruled for eBay on 14 July 2008; the Second Circuit affirmed on 1 April 2010, holding that generalised knowledge that counterfeiting occurred was not enough for contributory liability — eBay needed to know of specific listings, and when told, it acted. That holding turned VeRO from a courtesy into the legal template.

## What It Cost

**The burden of finding counterfeits moved permanently onto the brand.**

After Tiffany, a platform that removed what it was told about was largely safe, so the brand had to do the telling — at the scale of every listing on every marketplace. That is the job brand protection firms sell. And the unit of VeRO is the listing, not the seller: a notice removes one page, while the operator behind it relists under another account. A takedown is easy to count and says nothing about whether counterfeit sales fell. The evidence standard is a rights owner's good-faith belief, not a finding, so an authorised reseller can be removed by the same form as a counterfeiter.

## What You Still Touch

Every marketplace rights-owner portal, and every takedown dashboard a brand protection vendor reports from, is a descendant of the NOCI: one notice, one listing, removed on a clock.

- [[problems/brand-protection-firms/high-impact|🔴 Takedowns Counted, Effect Unmeasured]] — the listing as the unit of work
- [[problems/brand-protection-firms/low-impact-2|🟡 Enforcement Routing and Notice Operations]] — a VeRO-style form per platform
- [[problems/brand-protection-firms/worker-life-2|🟢 The Brand Manager Handling the Reseller Who Was Wrongly Removed]] — good-faith belief as the evidence standard
- [[niches/brand-protection-firms/operator-attribution/profile|Operator Attribution]]
- [[niches/brand-protection-firms/the-wrongly-actioned-seller/profile|The Wrongly-Actioned Seller]]

**Sources:** *Tiffany (NJ) Inc. v. eBay Inc.*, 600 F.3d 93 (2d Cir. 2010), abridged opinion at cyber.harvard.edu (read directly: VeRO as "notice-and-takedown" system maintained "for nearly a decade"; NOCI form and good-faith standard; 24-hour removal practice, 70–80% within 12 hours; bid and transaction cancellation, fee refunds; fraud engine by May 2002 with ~90 Tiffany keywords; "About Me" pages; Trust and Safety staffing; knowledge holding); Wikipedia, *Tiffany (NJ) Inc. v. eBay Inc.* (amended complaint 15 July 2004; district court 14 July 2008; Second Circuit 1 April 2010). ⚠️ **Not established:** VeRO's 1998 start date comes only from secondary sources (IPWatchdog, seller-education sites); the only primary source found says "nearly a decade" as of 2010, which is consistent with about 2000 as much as 1998. I found no primary source naming the eBay staff who designed VeRO or stating its motive; the liability rationale above is inferred from the programme's structure and the Tiffany holding, not from an eBay statement.
