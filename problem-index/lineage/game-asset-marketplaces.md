# Lineage: Game Asset Marketplaces

**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the Unity Asset Store — a third-party marketplace built into the Unity editor, which delivers each purchase as a Unity package imported straight into the buyer's project; launched with Unity 3.1 on 10 November 2010
**Builder:** Unity Technologies
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A small game team needed more art, code and sound than it could make.

A game is built from many parts: models, textures, animations, shaders, audio, and scripts for cameras, inventories and pathfinding. Large studios make them in-house. A two-person team cannot, and often need not — somebody has already built a working inventory system.

Buying one was possible. TurboSquid, founded in New Orleans in 2000 by Matt Wisdom, brokered 3D models for a share of each sale, to game developers but also to architects, broadcasters and visual-effects houses. What it sold was a file. Turning that file into something working inside a particular game engine — import settings, materials, scale, scripts — was the buyer's job, and a script could not be sold that way at all without an engine to run it in.

## What Got Built

**The Unity Asset Store**, announced at Unite 2010 on 10 November and shipped the same day inside the Unity 3.1 update.

The store is inside the editor. A developer browses it from the same application they build in, buys, and the package imports into the open project with its folders, prefabs, materials and scripts already arranged the way Unity expects. Because every seller and every buyer works in the same engine, a store could now sell things no general 3D marketplace could: editor extensions, gameplay systems, shaders — code, not just geometry. The launch release promised "free tutorials and open-source libraries, individual assets for just a few dollars, to art packs, advanced script libraries."

Sellers could be anyone; publishers keep 70% of each sale and Unity takes 30%.

## Who Built It, And Why Them

**Unity Technologies**, founded in Copenhagen on 2 August 2004 by David Helgason, Nicholas Francis and Joachim Ante. The company began as a game studio; its first game, GooBall, failed commercially in 2005, and the founders turned the tools they had built into an engine for other developers, sold by licence.

That history explains the store's shape. Unity's business was selling the engine to small teams, and its pitch was making game development accessible to people without a studio's resources. A marketplace served that pitch in two directions. It filled the gap that made a small team slower than a studio, and it gave Unity users a way to earn from the engine — Helgason's launch statement said it let "individual developers … monetize their skills in an entirely new way" and would let developers "easily combine their work with that of others."

Only the engine maker could build this version: delivery into the editor, in a format every buyer shared, depended on owning both. A standalone marketplace sold files; Unity could sell working parts of a Unity project.

## What It Cost

The package works because it belongs to one engine, and it is tied to that engine's versions. Each package is uploaded from a specific Unity release, and the store will not deliver a package built in a newer editor than the buyer's. Publishers who want to support a range of versions upload from the oldest one they support, or upload separately from several. Unity's current submission guidelines set minimum editor versions for new and updated packages.

So the store sells a listing — title, screenshots, category, a stated Unity version — for a package whose real compatibility depends on the buyer's render pipeline, platform and other packages. None of that is checked before purchase. And because the store took 30% and left support to the seller, keeping a package working through each engine release became the creator's permanent, unpaid job.

## What You Still Touch

Every post-purchase "import package" dialog is the 2010 design; every "broken in this Unity version" review is its cost.

- [[problems/game-asset-marketplaces/high-impact|🔴 You Cannot Tell If It Will Work Until You Have Bought It]]
- [[problems/game-asset-marketplaces/worker-life-1|🟢 The Creator Supporting Six Engine Versions Forever]] — the support burden the 70/30 split left with sellers
- [[problems/game-asset-marketplaces/worker-life-2|🟢 The Technical Artist Making Other People's Assets Fit]]
- [[niches/game-asset-marketplaces/integration-fit/profile|Integration Fit & Compatibility]]
- [[niches/game-asset-marketplaces/automated-asset-validation/profile|Automated Asset Validation]]
- [[niches/game-asset-marketplaces/the-supported-creator/profile|The Supported Creator]]

**Sources:** Unity Technologies press release, "Unity Technologies Launches 3rd Party Marketplace 'Unity Asset Store'," 10 November 2010 (Helgason quotes; launch inventory description); MCV/Develop, "Unity launches Unity Asset Store" (Unite 2010 announcement, Unity 3.1 same day; ~70 products at launch — search summary); Wikipedia, *Unity Technologies* (founded 2 August 2004 in Copenhagen by Helgason, Francis and Ante; GooBall 2005; Asset Store November 2010); Unity Asset Store, *Start publishing* and *Submission Guidelines* (70% to publishers; current minimum editor versions); Unity Discussions thread "Publishing an asset for multiple Unity versions," 2017–2018 (per-version uploads; store will not deliver a package from a later Unity version than the buyer's — publisher-reported, not confirmed by Unity staff in that thread); Wikipedia, *TurboSquid*, and Biz New Orleans (founded 2000 in New Orleans by Matt Wisdom; share-of-sale brokerage). ⚠️ **Not established:** whether the 70/30 split applied from the 2010 launch — a Unity forum thread titled "Earn 70% each sale" surfaced in search but its date was not confirmed. Unity's 2014 "Asset Store turns four" blog post (reportedly with early user numbers) now returns 404. The origin of the `.unitypackage` format itself was not researched.
