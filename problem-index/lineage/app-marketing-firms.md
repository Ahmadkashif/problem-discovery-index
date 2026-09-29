# Lineage: App Marketing Firms

**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** the Advertising Identifier (IDFA) — the resettable per-device ID Apple's AdSupport framework exposes to apps, introduced in iOS 6 with a "Limit Ad Tracking" switch beside it
**Builder:** Apple
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A mobile ad network gets paid when an ad produces an install. Proving that it did means joining two events that happen in different places: a tap inside one app, and a first launch of a different app, with an App Store download in between that neither party can see.

On the web a cookie bridges the gap. On a 2010 iPhone, apps shared no cookie jar. What there was, was the **UDID** — the device's permanent hardware serial, readable by any app through a single call. Ad networks, analytics SDKs and game networks used it, raw or hashed, as the join key for everything: this device tapped that ad, this device later launched that app, this device spent money on day three.

It was also permanent, unresettable and handed to every third party that asked. **The join key and the privacy problem were the same number.**

## What Got Built

In iOS 5 documentation, found by developers in **August 2011** rather than announced, Apple marked UDID access deprecated and told developers to "create a unique identifier specific to your app." That removed the join key without supplying a replacement — a per-app identifier cannot link an ad in one app to an install in another.

The replacement arrived with **iOS 6 on 19 September 2012**: the **Advertising Identifier**, exposed through a new AdSupport framework, which Apple described as "a non-permanent, non-personal, device identifier, that advertising networks will use to give you more control over advertisers' ability to use tracking methods." Alongside it came a **Limit Ad Tracking** toggle in Settings; **iOS 6.1** added a reset.

Then the stick. On **21 March 2013** Apple told developers that from **1 May** the App Store "will no longer accept new apps or app updates that access UDIDs," and to move to "the Vendor or Advertising identifiers introduced in iOS 6." **Two identifiers, two purposes:** one for an app maker's own analytics, one reserved specifically for cross-app advertising.

## Who Built It, And Why Them

**Only the platform owner could build it.** No ad network could mint an identifier shared across every app on the phone.

It was built rather than simply removed because Apple sat on both sides of the trade. It took a 30% cut of paid downloads and in-app purchases, so installs driven by advertising were Apple revenue. And it had become an ad seller itself: it acquired mobile ad firm **Quattro Wireless** in early 2010 and launched **iAd** on **1 July 2010**. When UDID was deprecated, an industry executive quoted by TechCrunch predicted Apple would keep UDIDs internally for iAd and Game Center while denying them to third parties.

The IDFA is what that tension looks like as an artefact: **attribution preserved for the app economy, with a user-controlled off switch Apple could tighten later.** A separate advertising-only ID is exactly the shape you build if you expect one day to gate it.

## What It Cost

The IDFA made cross-app tracking legitimate and therefore universal: the mobile measurement partner and the user-level lifetime-value model both assumed the key would be there.

Apple kept the switch. On **3 September 2020** Apple announced that apps would need explicit permission to read the IDFA, and from **iOS 14.5** they had to ask. Flurry reported in May 2021 that 96% of US users opted out. The industry's replacement is **SKAdNetwork** — Apple-built again, aggregated, delayed and privacy-thresholded.

**The cost was dependency.** An entire discipline was built on a key whose owner had designed in its own off switch.

## What You Still Touch

The "Allow to track across other companies' apps?" prompt is the IDFA's gate. A UA manager reconciles four sets of numbers every Monday because the key that once made them agree was withdrawn by the party that issued it.

- [[problems/app-marketing-firms/high-impact|🔴 Bidding a Six-Month Payback on Three Days of a Coarse, Delayed Signal]] — what bidding looks like once the key is gone
- [[problems/app-marketing-firms/worker-life-1|🟢 The UA Manager With Four Sets of Numbers]]
- [[niches/app-marketing-firms/conversion-value-schema/profile|Conversion Value Schema Design]] — the few bits SKAdNetwork leaves you
- [[niches/app-marketing-firms/attribution-reconciliation/profile|Attribution Reconciliation]]
- [[niches/app-marketing-firms/predictive-value-under-aggregation/profile|Predictive Value Under Aggregation]]

**Sources:** WebSearch was unavailable this session (session cap reached); all research was by WebFetch on known URLs. Apple Developer News, *Using Identifiers in Your Apps*, 21 March 2013 (primary — UDID rejection from 1 May, identifiers "introduced in iOS 6"); TechCrunch, *Apple Phasing Out UDID in iOS 5*, 19 August 2011 (deprecation text, ad-network dependence, the iAd/Game Center quote); Wikipedia, *iOS 6* (release 19 September 2012, Apple's description of the identifier, Limit Ad Tracking, 6.1 reset), *iAd* (announced 8 April 2010, launched 1 July 2010, Quattro Wireless March 2010), *App Tracking Transparency* (3 September 2020 announcement, iOS 14.5 prompt, Flurry May 2021). ⚠️ **Not established:** the names of the Apple engineers or product owners who designed the identifier — not found in any source checked; Apple's developer docs for AdSupport and SKAdNetwork returned no readable content, so SKAdNetwork's first iOS version (commonly given as 11.3, 2018) is left undated here. Wikipedia's *App Tracking Transparency* article dates Limit Ad Tracking to iOS 10 while its *iOS 6* article dates it to iOS 6; the iOS 6 date is used.
