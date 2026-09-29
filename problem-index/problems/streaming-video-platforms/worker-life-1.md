# The Content Operations Specialist at Ingest

**Industry:** [[streaming-video-platforms|Streaming Video Platforms]]
**Type:** Worker Life Changing
**One-liner:** Someone checks every asset against a specification by watching it, and the catalogue never stops arriving.
**Tags:** #cnns #object-detection #semantic-segmentation #large-language-models #transfer-learning #evaluation-metrics #worker-facing #automation

## The Problem
Every title entering the catalogue passes through quality control. The video is checked for encoding artefacts, dropped frames, audio synchronisation, loudness compliance, aspect ratio and letterboxing errors, colour issues and black frames. Subtitles are checked for timing, reading speed, character limits, positioning and translation quality. Audio tracks are checked per language. Content advisories are verified against what is actually on screen.

Much of this is done by watching. A specialist plays the asset, sometimes at speed, sometimes in full, looking for problems that may occur once in ninety minutes.

Volume is relentless. A large platform ingests continuously, and every territory, language variant and re-delivery is another pass.

Specifications differ. The platform's own requirements, each territory's regulatory requirements, accessibility standards and distribution partner specifications all apply, and they are documented across many pages that change.

Errors found late are expensive. An asset that fails after publication generates a customer-visible defect, a takedown and a redelivery, so the pressure is to catch everything, at speed, on the first pass.

And the same suppliers make the same mistakes repeatedly, which is the most useful fact available and the least systematically used.

## Why It Matters to the Worker
The work is sustained attention for defects that are rare and consequential, which is the specific cognitive task humans perform worst over long periods and which is nonetheless scheduled as an eight-hour shift.

Volume pressure conflicts with the care the work requires, and the specialist absorbs that conflict personally.

The specifications are extensive, differ by context and change, so the job requires holding a large and unstable body of detail with a documentation set that is not built for the moment of use.

It is invisible when done well. A clean catalogue looks like nothing happened; a single visible defect is escalated.

And the career path is limited despite the expertise being real — knowing what a compression artefact looks like versus a source defect is genuine skill that does not transfer to an obvious next role.

## What a Solution Looks Like
Automated detection of the defects that are mechanically detectable, which is most of them. Encoding artefacts, dropped frames, audio sync drift, loudness deviation, black frames, aspect ratio errors, subtitle timing and reading speed violations, and character limit breaches are all measurable by machine, continuously, across the whole asset, without fatigue.

Human attention directed to what machines cannot judge: translation quality, cultural appropriateness, whether a content advisory matches what is actually depicted, and genuinely ambiguous artefacts.

Specification checking as code. Each platform, territory and partner specification expressed as executable rules, versioned, so that compliance is verified rather than remembered.

Supplier quality tracking. Which suppliers produce which defects, at what rate, across deliveries — this redirects effort to the deliveries that need it and gives the platform an argument with the supplier rather than a resigned re-check.

Risk-based sampling. Once defect rates by supplier, content type and pipeline are known, full review can be reserved for high-risk assets rather than applied uniformly, which is how every mature quality function outside this industry already works.

Content advisory verification from the video itself, which is a classification problem and is currently a person watching with a checklist.

## Impact If Solved
This function scales linearly with a catalogue that grows continuously, and it is built on a sustained-attention task that humans do poorly and machines do well. Automating mechanical defect detection, expressing specifications as executable rules and tracking supplier quality lets human attention go to the judgements that actually require it and makes the workload survivable.
