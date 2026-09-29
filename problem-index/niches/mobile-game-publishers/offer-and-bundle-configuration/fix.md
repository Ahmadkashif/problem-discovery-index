# Everyone Gets the Same Starter Pack

**Niche:** [[niches/mobile-game-publishers/offer-and-bundle-configuration/profile|Offer & Bundle Configuration]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The same bundle at the same price appears for every player at the same point, regardless of what they already own or need.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #k-nearest-neighbors #confidence-intervals #automation #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to choose which offer to put in front of which player at which moment, a decision made thousands of times a day by hand-written rules — and whoever automates it well takes the account.

## The Problem
The most common live ops configuration is a uniform offer: the same starter pack, at the same price, triggered at the same progression point, containing items many players already have and omitting what they are actually short of. It converts adequately, which is why it persists. The players who decline it mostly decline because it is irrelevant rather than because it is expensive, and nothing records that distinction.

## Why It's Still Broken
The offer is configured once and the player state is read never — a rule keyed to a progression point and nothing else cannot notice that the player already owns what it is selling. Declines are not analysed. The uniform version is easy to reason about. And conversion looks acceptable against no alternative.

## What a Fix Looks Like
Filter and swap before personalising anything. Suppress items the player already owns from the bundle, which is the fix and is a lookup rather than a model. Substitute for the resource the player is currently short of, since relevance is most of the conversion gap. Trigger at the point of need rather than at a fixed progression marker, as timing is worth more than contents. Offer two or three variants and record which is taken, which starts the learning loop cheaply. Analyse declines by reason where the state makes it inferable, because that is the data the current setup throws away. Cap repeated presentation of a declined offer, which currently annoys the exact players who are engaged. Report conversion by player state rather than only in aggregate, as the aggregate hides which states are being served badly. Keep a control group on the uniform offer so the gain is measurable. Review the price ladder against the current audience rather than the one it was set for. And start with the suppression rules, since they are a day's work and carry most of the immediate improvement.

## Who Feels the Pain
Players offered things they already own; product managers whose conversion is flat and unexplained; publishers leaving revenue in obvious places; and support teams handling complaints about it.

## Impact If Fixed
A rule keyed to a progression point and nothing else cannot notice that the player already owns what it is selling. Suppressing owned items and substituting the missing resource is a lookup against state the game already tracks.
