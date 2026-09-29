# History: Marketing Attribution Vendors

**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Primary Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** [[origins/ad-holding-companies/profile|Ad Holding Companies]]
**Episode Tier:** 1
**Transferable Pattern:** A measurement convention adopted because a tool could compute it, not because anyone believed it was correct, will outlive every attempt to sell a better one — if the buying system that spends the money was built to read the convention it replaced.

## Before the Convention

Advertisers have wanted to know which spend caused which sale for as long as there has been more than one channel to spend on. John Wanamaker's apocryphal complaint about not knowing which half of his advertising was wasted predates computing by a century. What did not exist before the 1990s was a *machine-readable trail* of individual exposures a computer could join to an individual purchase. Measurement before then meant aggregate correlation — sales lifted after a campaign ran — assessed by the same kind of consulting houses that built early **marketing mix modelling** for consumer packaged goods manufacturers from the late 1980s, because CPG firms were the ones with reliable, syndicated sales and marketing spend data to model against. Mix modelling is the older of this industry's two lineages, and it never went away — it went dormant while the web offered something that looked more precise.

## The Origin Event

**June 1994.** Netscape engineer **Lou Montulli** invents the HTTP cookie, initially to solve a shopping-cart statelessness problem for an e-commerce client. **DoubleClick, founded in February 1996**, is among the first to repurpose the cookie for advertising: a small file that persists in a browser and lets a server recognise the same visitor across page loads.

The cookie could do one thing reliably for attribution purposes: **record which ad a given browser had most recently been served or clicked before a conversion happened on that same browser.** It could not reliably reconstruct an entire path of exposures across publishers, across sessions, or across devices — the technical means to do that, at internet scale, in 1996, did not exist. So the industry built its measurement convention around what the tool in hand could actually report.

> **Myth, already killed elsewhere in this vault and worth restating here because this is the industry it created.** "Google decided last-click attribution" does not survive the timeline. DoubleClick's cookie tooling could only reliably capture the last touch; agency practice entrenched the convention through the late 1990s; Google popularised it at scale after acquiring DoubleClick in 2008; and the **IAB** — the trade body whose own founding year is 1996 — folded it into industry measurement guidance over the following decade. Nobody sat in a room and chose last-click over first-click or fractional credit on the merits. The convention is the shape of what the cookie could see.

**Former IAB president Greg Stuart** has since called last-click attribution "a big mistake" — a striking admission from the industry body whose own standards work helped cement the convention it now disavows. *(I could not independently re-verify the primary source or exact date of this quote in this session — the trade article carrying it returned an access error to WebFetch. It is carried here from this vault's own prior, sourced research in `history/programmatic-ad-platforms.md` and `history/affiliate-networks.md`, both of which cite it; treat the quote as attributed but not re-verified this session, and confirm before it appears in a script.)*

## What Became Cheap

**Computing a plausible-looking causal answer to "what caused this sale" from data that was already sitting in a server log.** Before the cookie, answering that question meant a lift study or a mix model — commissioned work, weeks of turnaround, aggregate rather than individual. After it, any advertiser with a tag on their site could see, for free, which last link a converting visitor had clicked. That answer arrived instantly and felt precise because it pointed at an individual event rather than a statistical correlation. **Precision and correctness are not the same property, and this entire industry exists in the gap between them.**

## How It Was Actually Solved — three methods, none sufficient alone

**Single-touch and multi-touch attribution (MTA)** assign credit along an observed sequence of touchpoints — all of it to the last touch, or fractionally across several, by equal weighting, time decay, or an algorithmic model trained on converting versus non-converting paths. Every version of MTA shares the same structural weakness: it is built entirely from *observational* data, describing correlation between a touchpoint's presence and a conversion, never establishing that the touchpoint caused it. A shopper who was already going to buy and happened to click a retargeting ad on the way looks, to an MTA model, identical to a shopper the ad genuinely persuaded.

**Marketing mix modelling (MMM)**, the older lineage, returned as the field's answer to that weakness once cross-site cookie identity began to erode — because MMM never depended on individual-level tracking in the first place, only aggregate spend and sales by channel and time period. Its own weakness is underdetermination: channel spends move together, adstock decay curves and saturation functions are specification choices an analyst makes, and the resulting attribution can shift substantially depending on assumptions the client never sees argued.

**Incrementality testing** — geo holdouts, randomised experiments withholding a channel from part of the audience — is the one method that actually measures a causal effect rather than inferring one. It is also the one method this industry treats as an occasional supplement rather than the foundation, because it costs money, takes weeks, and at most advertisers' scale can only detect large effects.

**The consequence, stated in this vault's own hub note for the industry:** two vendors modelling the same business return materially different channel contributions, and the client is advised to "triangulate" between methods with unknown, uncharacterised biases. Triangulation among three uncalibrated instruments is not a methodology. It is a way of avoiding the admission that nobody in the room can say which number is right.

## The Trade-Off

**MTA and MMM outputs are bought, presented, and then routinely ignored by the systems that actually allocate the money.** This is the trade worth stating plainly rather than softening, because it is the honest answer to why this industry exists at the scale it does without having solved its central problem.

A programmatic demand-side platform's bidding algorithm optimises against the signal it can observe in real time — historically the click, increasingly a platform-reported conversion event — regardless of what a mix model or an MTA report concluded about that channel's true incremental value. The measurement layer and the spending layer are different systems, built by different vendors, on different timelines, updated at different speeds. **A marketing scientist can correctly diagnose that a channel is being over-credited, present the finding in a quarterly business review, and watch the automated bidder that actually spends the budget continue optimising against the metric it always used**, because nobody wired the finding back into the machine that spends the money.

This vault's own hub note names the honest inversion nobody sells: treat every model as an interpolator between experiments, continuously validated against the next randomised test it failed to predict, rather than treating experiments as an occasional check on a model presumed correct by default. That product is buildable from tools that already exist. It has not been built at category scale, because the vendor who ships it first makes visible — to its own clients, in its own dashboard — how often its previous answer was wrong.

## The Binding Constraint

The deeper limit is not statistical, it is architectural, and it long predates this industry: **the conversion record itself is now partial, consent-dependent, and modelled by each platform in its own favour.** Apple's App Tracking Transparency (iOS 14.5, April 26 2021) and the broader retreat from third-party cookies removed the deterministic cross-site identity that MTA was built on. Server-side tagging, conversion APIs and "modelled conversions" have partly replaced it — but a modelled conversion is, definitionally, an estimate the reporting platform makes about its own performance, filled in wherever a real one is missing. **An attribution vendor now sits downstream of an input that the platform being measured is permitted to estimate.**

## What's Still Open

- [[problems/marketing-attribution-vendors/high-impact|🔴 Selling a Causal Answer With No Way to Check It]] — this file's central finding, as the vault's own top problem for the industry
- [[niches/marketing-attribution-vendors/validation-and-ground-truth/profile|Validation & Ground Truth]] — the inversion nobody has shipped: experiments as the foundation, models as interpolators
- [[niches/marketing-attribution-vendors/mix-modelling/profile|Mix Modelling]] — the older lineage, and the specification choices reported as if the data produced them
- [[niches/marketing-attribution-vendors/reconciliation-and-triangulation/profile|Reconciliation & Triangulation]] — three uncalibrated methods, and the client asked to pick
- [[niches/marketing-attribution-vendors/the-marketing-scientist/profile|The Marketing Scientist]] — defending a number they know is less certain than the chart implies
- [[niches/marketing-attribution-vendors/conversion-data-plumbing/profile|Conversion Data Plumbing]] — the partial, modelled input every method above now depends on

## The Transferable Pattern

> **A measurement convention that survives for thirty years after its own inventors call it a mistake is not surviving on its merits — it is surviving because something downstream was built to consume it. Selling a better measurement does nothing until the thing that spends the money is rewired to read it.**

An FDE arriving at a business where "everyone agrees the metric is wrong" should treat that agreement as informative but not sufficient. The next question is mechanical: **what system currently reads this metric to make a decision, and who owns the authority to change what it reads?** If the answer is "the bidding algorithm, and it belongs to a different vendor than the one selling the correction," you have found why the correction, however statistically sound, keeps not shipping. This is the same shape [[history/programmatic-ad-platforms|programmatic ad platforms]] documents at the level of the auction itself; this industry is the business built entirely around selling the fix, decade after decade, to a machine that was never told to listen.

**Sources:** Wikipedia, *HTTP cookie* (Lou Montulli, June 1994; Netscape Mosaic 0.9beta, October 13 1994); Wikipedia, *Interactive Advertising Bureau* (founded 1996); Wikipedia, *Multi-touch attribution* (definitions, single-touch versus algorithmic models, correlational limits versus incrementality testing); Wikipedia, *Marketing mix modeling* (Neil Borden and the "marketing mix," c.1949; Hudson River Group 1989 and Marketing Management Analytics 1990 as early commercial MMM practitioners; CPG origin); Apple developer documentation, App Tracking Transparency (iOS 14.5, April 26 2021); this vault's `industries/marketing-attribution-vendors.md`, `history/programmatic-ad-platforms.md`, `history/affiliate-networks.md` and `origins/ad-holding-companies/` files (last-click chronology, Greg Stuart attribution, IAB codification). *(The Greg Stuart quote and the specific 2004/2009 IAB codification dates are carried from this vault's own prior sourced research and could not be independently re-verified against a primary source this session — the trade-press URL was blocked. Flagged for re-verification before use in a script.)*
