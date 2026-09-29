# The Tags Nobody Checks

**Niche:** [[niches/streaming-video-platforms/metadata-and-localisation/profile|Metadata & Localisation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The recommendation system runs on tags that were entered years ago by a vendor and have never been verified against anything.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #data-integration #transformers #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to produce descriptions, tags, artwork, subtitles, dubs and audio description for every title in dozens of languages without the cost scaling with the catalogue — and whoever breaks that relationship can carry a catalogue everyone else cannot afford.

## The Problem
Genre, mood, theme and attribute tags drive a large part of discovery. They were entered by different vendors under different guidelines across years, are inconsistent between catalogue segments, contain errors that route titles to the wrong audiences, and have never been validated against whether the resulting recommendations worked. A title tagged wrongly is invisible to the people who want it and surfaced to people who do not, and the effect is attributed to the title.

## Why It's Still Broken
Tags are treated as a delivery requirement rather than as a functional input, so they are checked for presence rather than for correctness — a field that must be filled gets filled, and nothing tests whether what was entered is right. The downstream effect is diffuse and is attributed to the recommender or the content. Different vendors applied different standards over years. And nobody owns tag quality.

## What a Fix Looks Like
Validate tags against the thing they are for. Measure tag quality by its effect on discovery — do titles with a given tag actually satisfy viewers who engage with that tag, which is the fix and is the only meaningful definition of correct here. Detect inconsistency across the catalogue, since the same attribute applied differently in different eras is a large and mechanical error class. Cross-check tags against the content itself using automated analysis, which will surface obvious errors quickly. Compare against viewer behaviour, as a title consistently abandoned by viewers who came through a tag is probably mistagged. Report tag coverage and consistency by catalogue segment, so the worst areas are identified. Re-tag the high-traffic catalogue first, since that is where the error costs most. Set and enforce one guideline rather than accumulating vendor conventions. Let viewers correct implicitly through their behaviour rather than requiring explicit feedback. Assign ownership of tag quality, because the absence of an owner is why this persists. And connect tag quality to the content valuation work, since a mistagged title's underperformance is currently blamed on the title.

## Who Feels the Pain
Viewers shown titles that do not match what they wanted; content teams whose titles underperform for a metadata reason; recommendation teams whose inputs are wrong; and a business attributing a tagging failure to its content.

## Impact If Fixed
A field that must be filled gets filled, and nothing tests whether what was entered is right. Measuring tag quality by its effect on discovery is the only meaningful definition, and viewer behaviour already reports where the tags are wrong.
