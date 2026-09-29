# Metadata, Artwork and Localisation

**Industry:** [[streaming-video-platforms|Streaming Video Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every title needs descriptions, genres, tags, artwork in many aspect ratios, subtitles, dubs and audio description across dozens of languages, and most of it is produced by hand at enormous volume.
**Tags:** #cnns #object-detection #large-language-models #bert #transfer-learning #semantic-segmentation #evaluation-metrics #automation

## The Problem
A title arriving on a platform needs a great deal that is not the video. Synopses at several lengths. Genre and subgenre assignment. Mood, theme, setting and content tags that feed search and recommendation. Cast and crew credits resolved against an identity database. Content advisories and age ratings that differ by territory. Artwork in every aspect ratio the platform's surfaces require, in every language, personalised by recommendation systems that select among variants.

Then localisation. Subtitles in dozens of languages with timing, reading speed and line break conventions. Dubbed audio for major markets. Audio description for accessibility. Forced narrative subtitles for on-screen text.

Volume is enormous and continuous. A large platform ingests thousands of titles a year and maintains a catalogue of tens of thousands, each needing its metadata refreshed as territories, ratings and rights change.

Quality varies and matters. Metadata drives discovery, and a title tagged poorly is invisible to the recommendation system regardless of its quality. Subtitle errors are user-visible and generate complaints. Artwork variants drive click-through measurably.

Much of it arrives from the content supplier in inconsistent formats and quality, and has to be normalised, verified and frequently redone.

## What Already Exists
Automatic speech recognition and machine translation handle a growing share of subtitle work with human post-editing. Artwork personalisation systems select among variants and measure click-through. Metadata standards exist in several competing forms. Content classification models tag scenes, objects and moods. Synthetic voice dubbing is emerging and contested. Vendors supply localisation at scale.

## The Customisation Gap
Tag generation from the content itself is shallow. What a title is actually about — its themes, its tone, its narrative shape — is visible in the video, the script and the subtitles, and is currently assigned by humans working from a synopsis and a controlled vocabulary that lags how audiences actually search.

Artwork generation stops at selection. Platforms test among supplied variants; generating candidate variants from the title's own footage, targeted at specific audience segments, is a straightforward extension that nobody's supplier workflow accommodates.

Subtitle quality assessment is manual. Timing, reading speed, line breaks, character limits and translation fidelity are all mechanically checkable, and are checked by people watching.

Metadata freshness is unmanaged. Ratings, advisories, rights windows and credits change, and the catalogue drifts out of date silently.

And supplier-delivered metadata is normalised by hand, title by title, at the ingest point where the entire volume concentrates.

## Impact If Solved
Metadata determines whether a title can be found at all, and it is produced manually at a volume that grows with the catalogue. Generating tags from content, producing artwork variants from footage and checking subtitle quality mechanically compress a large operational cost and directly improve the discovery that the platform's recommendation investment depends on.
