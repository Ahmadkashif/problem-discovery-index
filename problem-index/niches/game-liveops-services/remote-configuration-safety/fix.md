# One Number, Every Player, Immediately

**Niche:** [[niches/game-liveops-services/remote-configuration-safety/profile|Remote Configuration Safety]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** A value was changed at four in the afternoon, applied to the entire player base at once, and the consequence was discovered on social media.
**Tags:** #quick-win #workflow-orchestration #automation #compliance #evaluation-metrics #change-point-detection #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to tell someone what a configuration value actually reaches before they change it in a live game — and whoever maps the blast radius takes the account.

## The Problem
The standard live ops incident: someone adjusts a configuration value, it applies globally and instantly, and it turns out to affect something nobody anticipated. There is no percentage rollout, no automatic monitoring, no rollback trigger. The first indication of a problem is players posting about it, and by then the change has reached everyone for hours.

## Why It's Still Broken
The console applies changes globally by default — a tool whose only mode is all-at-once guarantees that every mistake is a maximal one, and nobody chose that behaviour, it was simply never revisited. Staged rollout exists for code and not for config. Monitoring after a change is manual. And the speed is genuinely useful, which is why nobody wants to slow it down.

## What a Fix Looks Like
Add the percentage and the watch, and change nothing else. Make staged rollout the default path with a percentage selector, which is the fix and is a straightforward addition to any configuration service. Keep an immediate-global option for genuine emergencies rather than removing speed, since removing it is how the control gets bypassed. Watch a small set of key metrics automatically for a defined window after each change, as the detection gap is the whole cost. Offer a one-click revert to the previous value, which most consoles technically support and do not surface. Require a second pair of eyes only on values marked high blast radius, so the friction lands where it matters. Show recent changes to the same value and what happened, which is the cheapest institutional memory available. Timestamp changes against timezone coverage, because a change made at the end of one team's day lands in another region's peak. Notify the community team automatically when a player-visible value changes, since they currently find out with the players. Record intent alongside the change, which makes the log usable afterwards. And default new values to staged rather than global, as defaults determine behaviour far more than policy does.

## Who Feels the Pain
Live teams learning about their own change from social media; the on-call person handling it; community managers with no notice; and players in a game that changed under them.

## Impact If Fixed
A tool whose only mode is all-at-once guarantees that every mistake is a maximal one, and nobody chose that behaviour — it was simply never revisited. A percentage selector and an automatic metric watch turn a maximal mistake into a contained one.
