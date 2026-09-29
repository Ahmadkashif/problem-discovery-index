# History: Restaurant Tech Platforms

**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Origin Parent:** *None of this vault's eighteen origins names restaurant technology as a child.* A search of every `origins/*/legacy.md` file for "restaurant" returns nothing. The nearest adjacency — supermarket chains' Wave 2 itemised-transaction lineage — is real but indirect, and this file treats it as prose context rather than a formal parent link, in the same spirit the plan flags electric-utilities→agtech-platforms and process-manufacturing→metal-fabrication as adjacency, not transplant.
**Episode Tier:** 1
**Transferable Pattern:** A platform can own the transaction and the interface completely and still not own the number that determines whether the restaurant survives the week — because that number is set by a marketplace on the other side of an API the restaurant did not build and cannot negotiate.

## Before

A kitchen ran on a paper ticket, a carbon-copy guest check, and an expediter calling out orders by voice. The first genuinely computerised restaurant order system predates almost everything else in this vault's Wave 6 cohort by decades: in 1974, **William Brobeck and Associates built a microprocessor-controlled ordering system for McDonald's using the Intel 8008**, with individual station displays showing a complete order and up to eight devices linked for centralised management. This sits alongside, but is distinct from, IBM's **3650/3660 store systems (August 1973)** — the first commercial client-server retail terminals, deployed at Pathmark supermarkets and Dillard's department stores by 1974 — which is [[series/eras/wave-02-departmental-item-level|Wave 2]]'s general itemised-transaction lineage, not a restaurant-specific one.

## The Origin Event — three moments, not one

No single founding fight opens this industry. Three separate, verifiable moments built the product this vault's hub note describes.

**1974** gave the industry its first computerised order system (McDonald's, above) — proof that a restaurant's order flow could be digitised at all. **1977** gave it its first durable commercial vendor: **MICROS Systems, incorporated that year as Picos Manufacturing and renamed Micros Systems in 1978**, went on to hold an estimated **35% share of the restaurant point-of-sale market by 2003** before **Oracle acquired it in June 2014 for $68 a share, roughly $5.3 billion** — the company operating independently for thirty-six years before becoming Oracle Food and Beverage. **1986** gave the category its interface paradigm, and arguably its most durable legacy: **Gene Mosher's ViewTouch, demonstrated at Comdex in Las Vegas that year, was the first commercially available point-of-sale software with a colour, widget-driven touchscreen** — running on an Atari 520ST. Every tablet-based POS screen a restaurant uses today, forty years later, is still that idea.

## What Became Cheap

MICROS-era point of sale was proprietary hardware, an enterprise sales cycle, and a large upfront licence — the same fixed-cost arithmetic [[series/eras/wave-06-cloud-saas|Wave 6]] describes generally. **Square, founded 2009, and Toast, founded 2012 by Steve Fredette, Aman Narang and Jonathan Grimm**, replaced that model with commodity tablets, cloud backends, and integrated payments priced per transaction rather than per licence — the same interchange-plus logic this vault's `history/payment-processors.md` describes generally, applied to a single-location independent restaurant that MICROS's sales model was never built to reach economically. Toast went public in September 2021 at close to a $20 billion market capitalisation and reported operating across roughly 120,000 US restaurants by mid-2024.

## The Binding Constraint

**Getting online meant a delivery marketplace, and the marketplace's commission is a rate no individual restaurant sets or negotiates.** Litigation brought against the major delivery platforms — the 2020 antitrust suit *Davitashvili v. Grubhub Inc.*, naming DoorDash and Uber Eats alongside Grubhub — alleged commissions **ranging from 13% to 40% of order revenue**, against a restaurant industry whose average profit margin runs **3% to 9% of revenue**. At the upper end of that documented range, a delivery order can be break-even or loss-making for the restaurant at full menu price, before counting the marketing and packaging costs layered on top, and the restaurant cannot individually negotiate the rate any more than a cardholder can negotiate an interchange fee.

Several US cities are widely reported to have moved against this during 2020–21 — this vault could verify, from primary or near-primary sources in this session, only two concrete actions: **Montgomery County, Maryland's investigation, announced October 2020, into its authority to force lower delivery fees**, and **the City of Chicago's August 2021 lawsuit against DoorDash and Grubhub over allegedly unfair and deceptive practices during the pandemic**. Reporting on specific percentage caps enacted elsewhere — New York City and others are frequently cited at figures near 15% — could not be independently confirmed against a primary source in the time available this session, and this file declines to assert those specifics as verified fact. The general shape — municipalities responding to marketplace leverage over a captive merchant base during 2020–21 — is well attested even where the individual ordinances are not confirmed here.

## What Became Cheap, and What Still Isn't — the join underneath the constraint

Beneath the commission dispute sits a plumbing problem this vault's own hub note describes precisely: **menu items must be mapped consistently across the POS, three or more delivery marketplaces, a website and a kiosk, each with a different modifier structure**, and every new location still has a human build the same menu five times because no channel models a modifier the same way. **Invoice lines from distributors never automatically match the recipe ingredients they are meant to cost** either — invoice capture is solved, recipe costing is solved, and the join between the two is done by hand, forever, at every location, per this vault's own analysis. Neither gap is a hard computational problem. Both persist because no single vendor in the stack owns both ends of either join, which is this vault's own most repeated finding, restated once more in a new industry.

## The Graveyard — a thesis, not a corpse, in the marketplace layer

**Just Eat Takeaway completed its acquisition of Grubhub on 15 June 2021 for $7.3 billion in stock.** In January 2025, it completed the sale of Grubhub to Wonder Group for **$650 million**, recording a loss of more than **$6.5 billion** on the position — roughly 91% of the original purchase price gone in three and a half years. Grubhub itself did not disappear; the thesis that justified paying $7.3 billion for it — that delivery marketplaces would consolidate into durable, globally-scaled platforms commanding lasting pricing power — is the thing that did not survive, in this specific instance, at this specific price. It is the same shape of failure this vault records for Klarna's 2021–22 valuation collapse in `history/bnpl-providers.md`: the company lived: the price the market was willing to pay for the story did not.

## What's Still Open

- [[problems/restaurant-tech-platforms/high-impact|🔴 High Impact: Store-Level Demand Forecasting for Labour and Prep]]
- [[niches/restaurant-tech-platforms/digital-ordering-middleware/profile|Digital Ordering Middleware]] — the menu-mapping join across channels
- [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/profile|Invoice-to-Recipe Costing]] — the second unjoined pair
- [[niches/restaurant-tech-platforms/independent-fsr-forecasting/profile|Independent FSR Forecasting]] and [[niches/restaurant-tech-platforms/labor-scheduling-availability/profile|Labor Scheduling & Availability]]
- [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|FSR POS Operations]] and [[niches/restaurant-tech-platforms/multi-unit-chain-operations/profile|Multi-Unit Chain Operations]]
- [[niches/restaurant-tech-platforms/kitchen-staff-tools/profile|Kitchen Staff Tools]]
- [[niches/restaurant-tech-platforms/ghost-kitchen-commissary/profile|Ghost Kitchen & Commissary]] — a format built entirely inside the marketplace-commission constraint this file describes

## The Transferable Pattern

> **Owning the point of sale is not the same as owning the take rate.** A restaurant can run the best-instrumented, most cloud-native, most fully-integrated point-of-sale stack in this vault's Wave 6 cohort and still hand over 13–40 cents of every delivery dollar to a party whose commission it cannot negotiate, because the marketplace, not the POS vendor, controls the channel that generates the order in the first place. The technology solved capture. It did not solve leverage, and no version of the technology, built by the restaurant's own vendors, can — the leverage sits one layer up, in [[series/eras/wave-08-mobile-gps|Wave 8]]'s matching-market economics, not in this industry's own stack.

An FDE evaluating a merchant's technology stack should separate, explicitly, the costs the merchant's own software controls from the costs set by a counterparty on the other end of an API. The first category is where efficiency tooling helps. The second is where it cannot, no matter how well built.

**Sources:** Wikipedia, *Point of sale*, *MICROS Systems*, *Toast, Inc.*, *DoorDash*, *Grubhub*, *Food delivery*; *Davitashvili v. Grubhub Inc.* (2020 antitrust litigation, as reported); City of Chicago v. DoorDash and Grubhub (filed August 2021); Montgomery County, Maryland delivery-fee investigation (announced October 2020); this vault's `industries/restaurant-tech-platforms.md` and `history/bnpl-providers.md`.
