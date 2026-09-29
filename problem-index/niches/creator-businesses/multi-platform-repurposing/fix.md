# Finding the Clip by Scrubbing

**Niche:** [[niches/creator-businesses/multi-platform-repurposing/profile|Multi-Platform Repurposing]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** The editor scrubs through a forty-minute video looking for the twenty seconds worth clipping, and does it again for every platform.
**Tags:** #worker-facing #quick-win #transformers #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #seq2seq
**Contested on:** Every serious competitor in this niche is fighting to make one piece of content become six without six times the work — and whoever breaks the linear relationship between platforms and production hours changes what a small team can cover.

## The Problem
The source is long, the moments worth extracting are brief, and finding them means watching or scrubbing through the whole thing. The editor did this during the original edit and is doing it again. They will do it again for the next platform, and again when the creator asks for a different cut for a sponsor. The knowledge of where the good moments are exists — the editor had it an hour ago — and nothing in the toolchain retained it.

## Why It's Still Broken
The edit and the derivatives are separate projects in separate timelines, so the knowledge from the first does not carry to the second — a workflow organised around output files discards everything learned in making them. Transcripts exist but are not searchable in the editing context. Nobody marks moments during the original edit because it is extra work for a later task. And derivative production is treated as a separate, lesser job.

## What a Fix Looks Like
Capture the moments once. Mark candidate clip points during the original edit, which is the fix and costs the editor seconds when the knowledge is fresh. Generate a transcript with timecodes and make it searchable, since scrubbing is being used as a substitute for search. Surface the moments the audience responded to — retention peaks, most-replayed segments, comment timestamps — as the audience has already identified them and the data is available. Keep clip candidates with the project rather than in a separate file, so every later request starts from the list. Auto-generate rough cuts from the marked points, leaving the editor to refine rather than to find. Track which derivatives performed and mark the source moments accordingly, which builds a sense of what travels. Let the creator mark moments while recording, because they know when something good happened. Reuse the transcript for captions, descriptions and written derivatives rather than regenerating each. Store derivatives with their source timecodes, so a later variant does not start from scratch. And measure time spent finding versus time spent editing, since the split will be surprising.

## Who Feels the Pain
Editors watching the same footage repeatedly; creators waiting for derivatives; teams whose platform coverage is limited by search time; and businesses paying editor hours for scrubbing.

## Impact If Fixed
A workflow organised around output files discards everything learned in making them, so the editor rediscovers the same moments each time. Marking candidates during the original edit and surfacing audience retention peaks removes the search entirely.
