# The Same Track Uploaded Forty Times

**Niche:** [[niches/digital-audio-platforms/catalogue-intake-at-scale/profile|Catalogue Intake at Scale]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same recording exists in the catalogue dozens of times under different names and nothing merges them.
**Tags:** #quick-win #contrastive-learning #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #graph-theory #compliance
**Contested on:** Every serious competitor in this niche is fighting to ingest well over a hundred thousand tracks a day without letting the bad ones through or losing the good ones — and whoever does it well controls what the catalogue actually is.

## The Problem
A recording is delivered several times — by different distributors, on different releases, in different territories, sometimes deliberately to spread streams across multiple identifiers. The catalogue holds duplicates, the listener sees several versions and does not know which to play, the streams split across identifiers, and royalty matching has several candidates for the same audio. The duplicates are detectable with fingerprinting the platform already runs.

## Why It's Still Broken
Fingerprinting is used to identify a recording rather than to deduplicate the catalogue, so the matches exist and produce no action — a capability deployed for one purpose is rarely pointed at an adjacent one without someone deciding to. Merging affects rights records and is therefore delicate. Duplicates are individually harmless. And nobody reports how many there are.

## What a Fix Looks Like
Use the fingerprints you already compute. Report the catalogue's duplicate rate, which is the fix's starting point and is computable from matching already performed. Link duplicates into a single logical recording rather than merging destructively, since linking gets most of the benefit with none of the rights risk. Consolidate the listener-facing presentation so one recording appears once. Aggregate streams across linked duplicates for reporting, as the split is currently invisible and misleads everyone including the artist. Flag deliberate duplication used to spread streams, since that is a distinct and adversarial behaviour. Detect duplicates at intake rather than in the catalogue, which prevents rather than repairs. Tell the distributor when they deliver a duplicate, because the cause is usually upstream and correctable. Handle legitimate versions — remasters, live, edits — distinctly, as collapsing them would be a real harm. Report duplicates by distributor, which will concentrate and point at the fix. And measure the effect of consolidation on discovery, since a cleaner catalogue should surface better.

## Who Feels the Pain
Listeners choosing between identical versions; artists whose streams are split across identifiers; rights operations matching against several candidates; and a catalogue whose size overstates its content.

## Impact If Fixed
A capability deployed for one purpose is rarely pointed at an adjacent one without someone deciding to, so fingerprint matches produce no deduplication. Linking rather than merging captures most of the benefit without touching rights records.
