# Lineage: Mobile Game Publishers

**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** In App Purchase — Apple's StoreKit payment API, added in iPhone OS 3.0 for paid apps and opened to free apps on 15 October 2009
**Builder:** Apple
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

When the App Store opened on **10 July 2008** with around 500 applications, a game could make money one way: a player paid once, up front, before playing.

That model put the whole commercial decision at the moment the player knew least. A browsing player saw an icon, five screenshots and a price, and had to guess whether the game was any good. Most chose the free alternative. The publisher's workaround was the **Lite version** — a separate, cut-down free app that advertised the paid one — which meant building, submitting and maintaining two products, and hoping the player remembered to come back and pay.

And the one payment was the last. A player who loved the game and would happily have spent more had nothing to spend it on. **Revenue was capped at the purchase price and collected before any value was delivered.**

## What Got Built

**A payment call inside the app.** iPhone OS 3.0, announced **17 March 2009** and released **17 June 2009**, added In App Purchase through the StoreKit framework: an app could list products, present Apple's payment sheet, charge the card already on the user's iTunes account, and receive a receipt it could verify. At first it was restricted to paid apps.

The decisive change was a short developer notice on **15 October 2009**: "Now you can use In App Purchase in your free apps to sell content, subscriptions, and digital services." Apple spelled out two reasons. Developers could ship "a single version of your app" and eliminate "the need to create Lite versions," and verifiable purchases could "help combat some of the problems of software piracy."

**That notice is the free-to-play mobile game's founding document.** The download became free, and the purchase moved to whatever point in play the designer chose.

## Who Built It, And Why Them

**Only the store owner could build a frictionless payment inside an app**, because only Apple held the player's card on file. A third-party payment form inside a game meant typing a card number on a phone keyboard, which almost nobody did. Apple's version was one confirmation against an account the player had already set up to buy apps and music.

Apple's reasons were commercial and stated. It took a 30% share of what the store sold, so every purchase moved inside an app was a purchase Apple collected on. Lite versions cluttered the store with duplicate listings. Piracy of paid apps on jailbroken devices was a known leak; a purchase verified by receipt was harder to steal than a binary.

The model it enabled was not new. Nexon had run free-to-play in South Korea since 1999, and Western MMOs were converting. **What Apple contributed was the payment rail on a device in hundreds of millions of pockets**, and the rule that let the first download cost nothing.

## What It Cost

The model rewards very few players. Wikipedia reports that free-to-play revenue overtook premium revenue on the App Store in 2011; the money under it is concentrated in the small share of players who spend heavily, which makes a game's economics a tail-estimation problem rather than a pricing one.

It also made **the first days of play the product test**. When the download is free, a game lives or dies on whether players come back and whether a few of them pay — so publishers kill prototypes on early retention numbers, because that is the only signal fast enough to act on.

And every purchase passes through a 30% toll whose owner writes the rules.

## What You Still Touch

The "Buy 500 gems" button, the confirmation sheet with your account on it, and the free game that is really a storefront are StoreKit's shape. So is the publisher's habit of deciding a game's fate on day-three retention: a free download means the player's first session, not the price, is the gate.

- [[problems/mobile-game-publishers/high-impact|🔴 Killing Most Prototypes on Three Days of Data]]
- [[problems/mobile-game-publishers/worker-life-2|🟢 The Product Manager Who Knows Where the Revenue Comes From]] — the tail the model created
- [[niches/mobile-game-publishers/hybrid-monetisation-balance/profile|Hybrid Monetisation Balance]]
- [[niches/mobile-game-publishers/offer-and-bundle-configuration/profile|Offer & Bundle Configuration]]
- [[niches/mobile-game-publishers/early-signal-modelling/profile|Early Signal Modelling]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. Apple Developer News, *In App Purchase Now Available for Free Apps*, 15 October 2009 (primary — all quotations above); Wikipedia, *iPhone OS 3* (announced 17 March 2009, released 17 June 2009, in-app purchase support); Wikipedia, *App Store (Apple)* (opened 10 July 2008 with ~500 apps; 70/30 split); Wikipedia, *Free-to-play* (Nexon QuizQuiz October 1999; free-to-play revenue overtaking premium on the App Store in 2011). ⚠️ **Not established:** the Apple engineers or product managers who designed StoreKit — no source checked names them. The "paid apps only" restriction before October 2009 is inferred from Apple's own notice, which describes adoption "in their paid apps"; no separate primary statement of the rule was found. Apple's January 2014 FTC settlement over children's in-app purchases was not confirmed this session (the FTC press-release URL tried returned 404) and is therefore not cited. Google's equivalent billing API is left undated for the same reason.
