# Breaking the Linear Cost

**Niche:** [[niches/streaming-video-platforms/metadata-and-localisation/profile|Metadata & Localisation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every additional title and every additional territory multiplies a cost that is almost entirely production work.
**Tags:** #transformers #seq2seq #large-language-models #cnns #evaluation-metrics #automation #confidence-intervals #transfer-learning
**Contested on:** Every serious competitor in this niche is fighting to produce descriptions, tags, artwork, subtitles, dubs and audio description for every title in dozens of languages without the cost scaling with the catalogue — and whoever breaks that relationship can carry a catalogue everyone else cannot afford.

## The Problem
A title arriving on a platform in thirty territories needs subtitles in thirty languages, dubs in several, artwork in multiple aspect ratios for each surface, descriptions and marketing copy per territory, genre and mood tags, content warnings, and audio description. Multiply by a catalogue of thousands and a constant arrival rate. The work is skilled but largely mechanical, the quality bar is real, and the cost grows with every dimension the business wants to expand along.

## Why Nobody Has Built This
Quality failures are highly visible and reputationally costly, so the industry reviews everything fully and captures little of the automation benefit — a process where a single bad subtitle is a public embarrassment defaults to full human review regardless of how good the generation is. Localisation is bought from vendors priced per unit. Tagging quality is not measured, so its effect is invisible. And accessibility work is treated as compliance rather than as product.

## What to Build
Generate widely and review selectively. Generate the first pass across subtitles, descriptions, tags and artwork variants, which is the core and is where the volume is. Route review by predicted risk rather than reviewing everything, since the difference between full review and targeted review is the entire economic benefit. Detect the errors that matter — mistranslation that changes meaning, timing failures, culturally wrong copy — rather than treating all errors alike. Measure tagging quality against its downstream effect on discovery, because tags exist to serve recommendation and their quality is currently unmeasured against the only thing they are for. Generate artwork variants from a small number of approved assets, as producing dozens of crops and compositions by hand is pure production work. Treat audio description and accessibility as product features with quality measurement, since they serve real audiences and compliance framing produces minimum-effort output. Preserve human judgement for creative copy and culturally sensitive material, which is where automation fails and the failures are worst. Build a feedback loop from viewer signals — subtitle toggles, abandonment at a dub, artwork click-through — as the audience is reporting quality continuously and nobody listens. Measure cost per title per territory, which is the number that decides expansion. And keep provenance of what was generated and what was reviewed, because a quality incident requires it.

## Target Customer
Content operations leadership, localisation vendors, accessibility advocates and audiences, and media supply chain vendors.

## Impact If Built
A process where one bad subtitle is a public embarrassment defaults to full human review regardless of generation quality. Routing review by predicted risk is where the entire economic benefit sits, and viewer signals already report where quality failed.
