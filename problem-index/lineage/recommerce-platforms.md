# Lineage: Recommerce Platforms

**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the StockX green authentication hangtag — a plastic tag clipped to every item that passes StockX's intake check, sold to buyers as "Verified Authentic" and renamed "StockX Verified" in 2022
**Builder:** StockX
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A used item has no price until someone decides what it is.

On the peer-to-peer web the buyer did that deciding. In sneakers that meant eBay auctions: every listing a unique lot, every buyer of a four-figure pair authenticating from a seller's photos. Reputation systems — see [[lineage/online-marketplaces|Online Marketplaces]] — told you whether a *seller* was honest. They said nothing about whether *this pair* was.

That is the constraint this industry exists to absorb. A managed platform takes the unit in, decides what it is, and stands behind the decision. The decision then has to travel with the object to a buyer who never saw the inspection.

## What Got Built

A tag, and a rule that made the tag possible.

The rule came first. StockX, launched in February 2016, accepted **deadstock only** — new, unworn product — and listed each item not as a unique lot but as a fungible stock-keeping unit: one model, one colourway, one size. Buyers placed bids, sellers placed asks, and a trade cleared at a public price with a visible history. The load-bearing move was refusing to grade condition. If everything is "new", there is nothing to grade, and one unique unit becomes one of many identical units with a market price.

The tag carried the remaining judgement. Sellers do not ship to the buyer; they ship to a StockX authentication centre. An authenticator checks box, labels, construction and accessories — TechCrunch describes it as a roughly 100-point checklist — and an item that passes leaves with a **green plastic hangtag** clipped through the laces and a receipt calling it authentic. The hangtag is the intake verdict compressed into an object the buyer can hold.

## Who Built It, And Why Them

Josh Luber, and the reason is that he started with the price data rather than the product.

Luber, then an IBM consultant, founded **Campless** in 2012 as a sneaker price guide built by scraping millions of completed eBay auctions. That dataset showed a large secondary market whose prices were real but whose units were unverified. Dan Gilbert — the Quicken Loans founder — acquired Campless, and with Luber, Greg Schwartz and Chris Kaufman founded StockX in **March 2015**, relocating the operation to Detroit.

**Why them and not eBay:** eBay's model was not to hold inventory. StockX's pricing thesis only worked if every unit on one product page was interchangeable, and that could only be guaranteed by physically handling every unit. A pure marketplace cannot promise that; an operator that routes goods through its own building can. The tag is what that routing produces. Luber has said there was no sneaker-authenticator job to hire for, so StockX created one. It started with four authenticators in 2016 and had nearly 300 across nine centres by 2021.

## What It Cost

**The tag promised more than a checklist can deliver.** In May 2022 Nike amended an existing lawsuit to allege it had bought counterfeit pairs on StockX, each wearing the "Verified Authentic" hangtag and a receipt reading "100% Authentic". In November 2022 StockX replaced "Verified Authentic" with "StockX Verified", saying verification was "the new authentication" — and disclosing that fakes were only 14% of its rejections; the rest were wrong sizes, damaged boxes, defects and wear. In March 2025 a federal judge found StockX liable for selling 37 counterfeit pairs. The parties settled on confidential terms in August 2025.

The deeper cost is scope. The deadstock rule makes pricing tractable by excluding exactly the goods the rest of the industry handles: worn, graded, one-of-a-kind items. The tag is a pass/fail signal. It has no grade, so it cannot price condition.

## What You Still Touch

Managed resale now sells a verdict that travels with the object — a tag, card or certificate saying someone qualified looked. Buyers pay the fee for that promise; authenticators carry the judgement behind it.

- [[problems/recommerce-platforms/low-impact-2|🟡 Authentication in High-Value Categories]] — the judgement the tag compresses
- [[problems/recommerce-platforms/worker-life-2|🟢 Authenticator Making the Call]]
- [[problems/recommerce-platforms/high-impact|🔴 Pricing One Unique Unit at Scale]] — the problem deadstock-only sidestepped
- [[niches/recommerce-platforms/authentication-systems/profile|Authentication Systems]]
- [[niches/recommerce-platforms/condition-grading/profile|Condition Grading]] — what a pass/fail tag cannot express

**Sources:** Wikipedia, *StockX* (founders, March 2015 founding, February 2016 launch, Campless acquisition and Detroit move); Wikipedia, *Josh Luber*, and Crunchbase/TED profiles (Campless 2012, eBay-auction price guide); TechCrunch, "Authentication and StockX's global arms race against fraudsters", 5 Apr 2021 (four authenticators in 2016, ~300 across nine centres, green tag, 100-point checklist); Highsnobiety interview with Luber (authenticator career path); OPB/NPR, 12 May 2022, and The Fashion Law timeline (May 2022 amended complaint, "Verified Authentic" hangtag); sneakermarket.ro, 16 Nov 2022 ("StockX Verified" rename, 14% statistic); SGB Media, 2025 (March 2025 liability ruling, August 29 2025 settlement). ⚠️ **Not established:** the date the green hangtag was first used — I could not confirm it shipped at the February 2016 launch rather than later; treat its introduction date as unverified. The 100-point checklist figure is StockX's own description via TechCrunch, not independently audited.
