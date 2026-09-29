# The Provider Changed the Schema on Tuesday

**Niche:** [[niches/data-marketplace-brokers/in-ecosystem-data-sharing/profile|In-Ecosystem Data Sharing]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** A shared dataset is live, so the provider's schema change, backfill or withdrawal reaches every consumer immediately with no version to pin to and frequently no notice.
**Tags:** #data-integration #change-point-detection #compliance #automation #evaluation-metrics #workflow-orchestration #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to make external data appear inside the buyer's own platform with governance and lineage intact and nothing copied — and whoever does that takes the account, because the buyer has already chosen the platform and is choosing between its marketplace and friction.

## The Problem
The zero-copy proposition is that the consumer always sees current data, which is its main advantage and its main hazard. A provider renames a column, changes a categorical encoding, backfills a correction that shifts historical aggregates, or deprecates the share entirely. Every consumer's pipeline is affected at the moment of the change. There is no version to pin, frequently no notification, and no way for the consumer to test against the new state before it becomes the only state. A copy-based delivery, for all its inefficiency, at least gave the consumer control over when a change landed.

## Why It's Still Broken
Versioning a live share requires retaining historical state, which costs storage the platform would have to charge someone for and which undercuts the zero-copy story. Providers have no visibility into who depends on which fields, so they cannot assess impact even when willing. Notification requires a channel between parties who have a commercial relationship but no operational one. And the consumer's breakage is experienced as their own pipeline failing.

## What a Fix Looks Like
Give the consumer control over when a change arrives. Support pinnable versions or time-travel on shares, so a consumer can build against a stable state and adopt a new one deliberately — which is the fix, and the storage cost is a small price against production breakage across every consumer. Require change notification with a notice period for breaking changes, enforced by the platform rather than left to the provider's courtesy. Publish consumer dependency information to providers in aggregate, so a provider can see that forty consumers read a field before they drop it, which the lineage work in the build note enables. Classify changes by severity automatically — additive, breaking, semantic — since a new column and a changed encoding are different events and are currently the same notification if any. Offer a staging share carrying the upcoming state, so consumers can test before the change lands. Detect semantic changes that no schema diff would catch, such as a distribution shift after a backfill, which is the category consumers are least able to see. And let a consumer pause adoption of updates temporarily, which is the minimum control and is currently unavailable.

## Who Feels the Pain
Consumers whose pipelines break on another company's Tuesday deployment; providers who broke forty customers without knowing; and platforms whose zero-copy advantage becomes a reliability complaint.

## Impact If Fixed
Pinnable versions give the consumer control over when a change lands, which is the one thing copy-based delivery offered and sharing removed. Aggregate consumer dependency information lets a provider assess impact before dropping a field rather than after.
