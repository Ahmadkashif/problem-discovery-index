# Wave 5 — The Commercial Web (1993–2004)

**Trigger:** NCSA Mosaic 1.0, April 22 1993; first SSL-secured credit-card purchase Aug 11 1994; Netscape Navigator 1.0 Dec 1994; Amazon founded 1994; Google incorporated Sept 4 1998; AdWords launched Oct 23 2000
**What went to ~zero:** the cost of **distribution and discovery**
**Failure class produced:** the **declined join** is born here — and it is born by accident

## What Was True The Day Before

Reaching a customer required physical presence or purchased attention: a shop on a street, a listing in a directory, a slot in a broadcast. Distribution was the scarce asset, and whoever controlled it — the retailer, the wholesaler, the network — took the margin. A good product with no shelf was not a business.

## The Trigger

The browser made publishing free and made every business, anywhere, one URL from every customer. The 1994 SSL transaction closed the loop by making it safe to hand over a card.

Then the harder problem: with distribution free, **discovery** became the scarce asset. Yahoo's curated directory did not scale with the web. Google's PageRank scored pages by weighted inbound-link authority rather than keyword density, which worked at web scale, and AdWords monetised it through a self-serve keyword auction. *(Link-analysis ranking was contemporaneous research — Kleinberg's HITS among others. Google's edge was execution and scale, not sole invention.)*

## The Competitive Fight

**Amazon versus Barnes & Noble** is the cleanest case, and the usual telling gets the mechanism wrong. Amazon's advantage was not "being online." It was inventory-free scale against physical-store economics, an unbounded catalogue, patented checkout friction reduction (1-Click), and reviews and recommendation data that compounded. Barnes & Noble was **not** as late as the usual telling suggests — **bn.com launched in May 1997**, roughly two years behind Amazon, not the four or five a casual account implies. *(Corrected at H5; this file previously said "1999–2000", which was wrong.)* It was under-resourced against Amazon's focus, ran chronic stockouts, and ultimately retreated to competing on physical experience — the café model — rather than out-executing on logistics.

**And the tidy lesson does not survive a second case.** **Borders outsourced its entire e-commerce operation to Amazon from 2001 to 2007** — the opposite choice — and **went bankrupt in February 2011 anyway.** One bookseller built its own channel late and lost; the other rented its rival's and lost. Owning the online channel was not the determining variable, which is precisely why "they were slow to go online" is an inadequate explanation of what happened to bookselling.

Then it ended. NASDAQ peaked at **5,048.62 on March 10 2000** and bottomed at **1,114.11 on Oct 9 2002** — a **78% fall** erasing roughly **$5 trillion**. The businesses that survived were the ones whose unit economics worked without the next funding round.

## What It Broke — and this is the important part of this wave

**Last-click attribution.** Every "declined join" in this vault descends from a decision nobody made.

DoubleClick, founded Feb 1996, pioneered cookie-based ad serving. A cookie reliably captures one thing: the last touch before a conversion. So last-click became the measurement the infrastructure *could* produce — **not** what anyone believed was correct. Google Analytics and AdWords adopted it as default for simplicity and low compute. The IAB then codified click-based measurement (impression guidelines 2004, click guidelines 2009), formalising a shortcut that was already universal.

Greg Stuart, a former IAB president, is widely reported to have called it **"a big mistake."**

> ⚠️ **Provenance: unverified, and actively searched for.** This quote and the IAB codification dates (impressions 2004, clicks 2009) trace to a single trade-press page that now returns 403. An H5 verification pass checked mi-3.com.au, Wikipedia, iab.com's insights listing and IAB Europe's site search and **found no corroboration.** `series/failures/last-click-attribution.md` is written deliberately **without** them. **The argument does not need the quote** — last-click's origin in DoubleClick's 1996 cookie tooling is independently documented. Do not put the quote in a script.

It persists because of simplicity, cookie-tech compatibility, and institutional inertia — agency reporting, billing and dashboards were all built on it — despite marketing-mix and multi-touch research repeatedly showing it misattributes credit to bottom-funnel touches. Amazon Associates (July 1996) used the same last-click logic at the affiliate level, and affiliate networks still do.

**The lesson for an FDE, and the thesis of the series in miniature:** a measurement convention was set by what the *tooling* happened to be able to observe, everyone built on it, and thirty years later an entire industry reports a number it knows is wrong because the honest number would be harder to compute and smaller to report. Nobody chose this. Everybody now defends it.

*(Myths: last-click was not "decided by Google" — DoubleClick's cookie tooling and agency practice preceded and shaped Google's adoption. Amazon did not invent affiliate marketing; PC Flowers & Gifts predates it. Amazon scaled the model.)*

## Children in This Vault

The largest cohort in the vault after Wave 6 — 45 industries whose existence presupposes free distribution.

**Primary:**
- [[industries/affiliate-networks|Affiliate Networks]]
- [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
- [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
- [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
- [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
- [[industries/edge-cdn-providers|Edge & CDN Providers]]
- [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
- [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
- [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
- [[industries/online-marketplaces|Online Marketplaces]]
- [[industries/print-on-demand-platforms|Print on Demand Platforms]]
- [[industries/recommerce-platforms|Recommerce Platforms]]
- [[industries/digital-audio-platforms|Digital Audio Platforms]]
- [[industries/digital-native-publishers|Digital Native Publishers]]
- [[industries/music-distribution-platforms|Music Distribution Platforms]]
- [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
- [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
- [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
- [[industries/localization-services|Localization Services]]
- [[industries/ux-research-agencies|UX Research Agencies]]
- [[industries/language-schools|Language Schools]]
- [[industries/vocational-schools|Vocational Schools]]
- [[industries/identity-verification-vendors|Identity Verification Vendors]]
- [[industries/lending-marketplaces|Lending Marketplaces]]
- [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
- [[industries/indie-game-studios|Indie Game Studios]]
- [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
- [[industries/personal-injury-law|Personal Injury Law Firms]]
- [[industries/news-media-local|Local News Media]]
- [[industries/trade-associations|Trade Associations]]
- [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
- [[industries/digital-bpo-operations|Digital BPO Operations]]
- [[industries/freelance-marketplaces|Freelance Marketplaces]]
- [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
- [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
- [[industries/staffing-agencies|Staffing Agencies]]
- [[industries/short-term-rentals|Short-Term Rentals]]
- [[industries/ecommerce-sellers|E-Commerce Sellers]]
- [[industries/it-staffing-firms|IT Staffing Firms]]
- [[industries/software-dev-agencies|Software Development Agencies]]
- [[industries/moving-companies|Moving Companies]]
- [[industries/brand-protection-firms|Brand Protection Firms]]
- [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
- [[industries/content-moderation-services|Content Moderation Services]]
- [[industries/penetration-testing-firms|Penetration Testing Firms]]

**Secondary:**
- [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
- [[industries/rv-dealerships|RV Dealerships]]
- [[industries/api-infrastructure-providers|API Infrastructure Providers]]
- [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
- [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
- [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
- [[industries/subscription-commerce|Subscription Commerce]]
- [[industries/newsletter-media|Newsletter Media]]
- [[industries/developer-relations-agencies|Developer Relations Agencies]]
- [[industries/technical-content-agencies|Technical Content Agencies]]
- [[industries/mortgage-brokers|Mortgage Brokers]]
- [[industries/tax-prep-firms|Tax Prep Firms]]
- [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
- [[industries/game-hosting-providers|Game Hosting Providers]]
- [[industries/virtual-economy-operators|Virtual Economy Operators]]
- [[industries/customer-support-platforms|Customer Support Platforms]]
- [[industries/hotels-boutique|Boutique Hotels]]
- [[industries/immigration-law|Immigration Law Firms]]
- [[industries/small-law-firms|Small Law Firms (Solo and 2-10 Attorney Practices)]]
- [[industries/customs-brokers|Customs Brokers]]
- [[industries/freight-brokerage|Freight Brokerage]]
- [[industries/last-mile-delivery|Last-Mile Delivery]]
- [[industries/independent-publishers|Independent Publishers]]
- [[industries/podcasting-networks|Podcasting Networks]]
- [[industries/virtual-assistant-services|Virtual Assistant Services]]
- [[industries/auto-dealers-independent|Independent Auto Dealers]]
- [[industries/independent-retailers|Independent Retailers]]
- [[industries/medical-supply-retail|Medical Supply Retail]]
- [[industries/funeral-homes|Funeral Homes]]
- [[industries/security-awareness-training|Security Awareness Training]]
- [[industries/proptech-platforms|Proptech Platforms]]

**Sources:** Wikipedia, *NCSA Mosaic*, *Netscape Navigator*, *Dot-com bubble*, *Timeline of Google Search*, *Affiliate marketing*, *Timeline of online advertising*; Retail Relates and Vice (first secure online purchase, Aug 11 1994); grokipedia.com, *DoubleClick*; mi-3.com.au (last-click attribution history; Greg Stuart / IAB); Knowledge@Wharton (Amazon vs Barnes & Noble); Amazon Seller Central (Associates programme).
