# Music Cue Sheets and the Delivery Schedule

**Industry:** [[postproduction-studios|Postproduction Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every finished programme must ship with a music cue sheet and dozens of paper deliverables, and the post team still builds them by scrubbing the final mix and retyping licences into spreadsheets.
**Tags:** #large-language-models #cnns #feature-engineering #evaluation-metrics #data-integration #automation #compliance

## The Problem
When a distributor or network acquires a programme, its delivery schedule lists everything the post house or producer owes with the picture: often ~80–200 items (estimate), from textless backgrounds and M&E tracks to the music cue sheet, final credits, chain-of-title documents, music licences, E&O insurance certificate and closed caption files. The cue sheet is the most laborious. It lists every piece of music in the final cut, with in and out timecodes, duration, usage type (background instrumental, visual vocal, main title), composer, publisher and performing rights organisation. Broadcasters and performing rights organisations use it to pay royalties, and a missing or wrong cue sheet holds up the composer's royalties and, often, the distributor's final payment. This note covers the delivering side; the distributor's later re-servicing of each of its own licensees is analysed under [[film-distributors|Film Distributors]].

The post coordinator or music editor builds it after picture lock, by scrubbing the final mix session or EDL, matching each cue to the music supervisor's licence log and the composer's cue list, and retyping it into the distributor's template. Every re-cut after lock changes the timings. On a series, it is done again for every episode and every version (broadcast cut, streaming cut, international).

## What Already Exists
Music fingerprinting and reporting services such as Soundmouse generate cue reports from audio, and performing rights organisations run their own cue sheet portals (BMI's RapidCue, for example). Rights management platforms such as Rightsline track licences. Editorial systems export EDLs and AAFs with clip names. Spreadsheets do the rest.

## The Customisation Gap
The generic tools solve parts of it: fingerprinting identifies commercial tracks, PRO portals accept submissions. The post-specific logic is: reading the locked cut's AAF or EDL to find every music event, including score cues that were edited and recut and that no fingerprint library holds; merging adjacent fragments of the same cue the way PRO rules require; classifying usage type from picture and audio context (is the vocal visible on screen?); reconciling every cue against the licence log so an unlicensed use is caught before delivery; and writing out each distributor's own template and each PRO's format. The rest of the delivery schedule needs the same treatment: a checklist parsed from the distributor's PDF, with each item linked to the file or document that satisfies it.

## Impact If Solved
Cue sheet assembly drops from one to three days per feature, or hours per episode, to a review of a generated draft (estimate), and a delivery schedule tracked item by item stops being the reason final payments slip by weeks.
