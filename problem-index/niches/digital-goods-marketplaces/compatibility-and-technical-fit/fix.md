# Compatible With the Version From Two Years Ago

**Niche:** [[niches/digital-goods-marketplaces/compatibility-and-technical-fit/profile|Compatibility & Technical Fit]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The compatibility field was accurate when the creator typed it, the software has had six releases since, and nothing in the catalogue has been rechecked.
**Tags:** #change-point-detection #automation #evaluation-metrics #workflow-orchestration #compliance #quick-win #descriptive-statistics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer whether an asset will actually work in their project before they pay for it — and whoever answers that reliably removes the largest cause of refunds and abandoned purchases in the category.

## The Problem
An asset listed three years ago says it supports the then-current release. Six releases later the listing says exactly the same thing. Some of those assets still work perfectly and some break entirely, and the listing gives the buyer no way to tell which. The creator has moved on, or has four hundred listings and cannot retest them all, or does not know the software changed. Buyers purchase, fail, refund, and leave a review saying it does not work, which the creator disputes because it worked when they made it. Both are right and the catalogue is rotting silently.

## Why It's Still Broken
Compatibility is stored as a static claim with no expiry, which is the root of it — a fact with a shelf life recorded as if it were permanent. Retesting is manual and falls on creators who have no capacity for it. Nobody monitors software release calendars against the catalogue. And the decay is invisible until a buyer hits it, at which point it looks like one bad listing rather than a catalogue-wide condition.

## What a Fix Looks Like
Treat compatibility as a perishable fact and refresh it. Attach a last-verified date to every compatibility claim and display it, which is a one-field change that immediately tells buyers how much to trust it — this is the fix and it costs nothing. Re-verify automatically when a new software version releases, by opening the asset in that version where automation permits, which is entirely feasible for the major formats and is where most of the catalogue's value sits. Use buyer outcomes as verification: refunds, support messages and reviews mentioning a version are a strong and free signal that a claim has gone stale. Notify creators which of their listings need retesting after a release, prioritised by sales, which turns an impossible task into a short list. Mark unverified claims visibly rather than presenting them as current, since an honest unknown serves the buyer better than a stale certainty. Warn buyers who already own an affected asset, which converts a future frustration into a supported update. Track compatibility decay per category as a catalogue health metric, because it is currently invisible and is a direct measure of how much of the catalogue is quietly dead. Support a version matrix rather than a single claim, as assets frequently work across a range with caveats and a single field cannot express it. Protect creators from reviews caused by decay rather than by their work, which is a fairness issue and affects whether they keep listing. And retire or flag listings whose creator is inactive and whose claims can no longer be maintained.

## Who Feels the Pain
Buyers purchasing assets that no longer work; creators blamed for software changes they did not make; and platforms whose catalogues contain a growing share of listings that are quietly false.

## Impact If Fixed
A fact with a shelf life is recorded as if permanent, and the decay is invisible until a buyer hits it. A last-verified date is a one-field change, and buyer refunds and version-mentioning reviews are a free staleness signal already sitting in the platform.
