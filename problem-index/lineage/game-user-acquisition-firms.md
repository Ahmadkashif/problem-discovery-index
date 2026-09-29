# Lineage: Game User Acquisition Firms

**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** SKAdNetwork — Apple's StoreKit class that "validates advertisement-driven app installations": a cryptographically signed install-validation postback sent to the ad network, with no user or device data, carrying from iOS 14 a single 6-bit conversion value
**Builder:** Apple
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A game UA team buys installs and is judged on what those installs later spend. To do that it has to join two events that happen in different companies' systems: an ad tapped inside someone else's app, and a purchase made days later inside its own game.

For most of the smartphone era that join ran through a device identifier, seen by the ad network at impression and the game at launch, and matched by a mobile measurement partner. Every cohort and payback curve was built on that match.

**The binding fact was that the match did not need the platform's permission — only the identifier.** When the platform decided to withdraw the identifier, the industry needed something else to tell it which ad produced which player, and the only party positioned to know that without a shared ID was the store where the install happened.

## What Got Built

A class in StoreKit, first available in **iOS 11.3, released 29 March 2018**, with a method called `registerAppForAdNetworkAttribution()`.

Its shape is set out in Apple's documentation. Ad networks register with Apple for an ad network ID. They sign each ad they serve. When a user taps and installs, the advertised app calls the method on first launch, which starts a 24-hour timer; when it expires the device sends the ad network an **install-validation postback** — "cryptographically signed data that confirms that a user installed and launched this app as a result of an ad." Apple states the signed information "doesn't include user- or device-specific data."

From **iOS 14.0** Apple added `updateConversionValue(_:)`: the app may report "a 6-bit value that the ad network or the app defines" — 64 possible values — raising it as often as it likes before a rolling 24-hour timer runs out, after which the postback arrives within a further 0–24 hours, and includes the value only if Apple's privacy threshold is met.

The date that made it mandatory was the other half. Apple announced on **3 September 2020** that apps would need permission to read the advertising identifier, enforced from iOS 14.5; Flurry reported in May 2021 that 96% of US users opted out. SKAdNetwork became the default record of which ad drove which install.

## Who Built It, And Why Them

Apple, because Apple owns the only system that witnesses both ends of the join without sharing an identifier: the App Store download and the device on which the ad was tapped. A third party can only reconstruct that link by tracking the user; the platform can assert it.

That is also why its shape is so narrow. Apple was building a product that let it close the identifier path and still leave advertising measurable in aggregate — so the postback is delayed, signed, stripped of the user, and thresholded by Apple.

**What is not established is Apple's own stated reason in 2018.** The class shipped two and a half years before the tracking announcement, and I found no Apple statement explaining why it was introduced then, or naming the team that designed it.

## What It Cost

**Six bits, roughly a day in.** Game revenue sits in a heavy tail of players who have mostly not spent yet at 24 hours. A UA team whose whole job is to predict a cohort's lifetime value was handed 64 buckets and a timer, and had to decide in advance what those buckets would mean — usually a first-day proxy for spend.

Later versions loosened it — from iOS 16.1, up to three postbacks across three conversion windows — and Apple now points advertisers to AdAttributionKit too. The constraint has moved, not gone: the platform decides how much the advertiser may know.

## What You Still Touch

The conversion value schema a UA manager maintains, and the lag before iOS results can be trusted, descend from that postback.

- [[problems/game-user-acquisition-firms/high-impact|🔴 Predicting a Number Whose Mass Is in People Who Have Not Spent Yet]] — now predicted from 64 buckets
- [[niches/game-user-acquisition-firms/lifetime-value-prediction/profile|Lifetime Value Prediction]]
- [[niches/game-user-acquisition-firms/heavy-tail-estimation/profile|Heavy-Tail Estimation]]
- [[niches/game-user-acquisition-firms/incrementality-operations/profile|Incrementality Operations]] — the fallback when attribution goes dark

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch and direct retrieval of Apple's documentation JSON. Apple Developer Documentation, *SKAdNetwork* (class description, "introducedAt 11.3", registration, signed ads, postback content, up to five non-winning postbacks for version 3+, iOS 16.1 three conversion windows, AdAttributionKit); *registerAppForAdNetworkAttribution()* (iOS 11.3, 24-hour timer, install notification wording); *updateConversionValue(_:)* (iOS 14.0, 6-bit value, rolling 24-hour timer, 0–24-hour postback, privacy threshold); Wikipedia, *iOS 11* (11.3 released 29 March 2018), *App Tracking Transparency* (3 September 2020 announcement, iOS 14.5, Flurry 96% US opt-out May 2021). The device-ID matching narrative in the first section also appears in this vault's `lineage/app-marketing-firms.md` (vault material, not independent corroboration). ⚠️ **Not established:** why Apple introduced SKAdNetwork in 2018, and who designed it — no Apple statement or named engineer found; the release date of iOS 14.5 was not confirmed this session and is left undated. "Apple's reason was to close the identifier path while keeping ads measurable" is the note's inference from the design, not a quoted Apple rationale.
