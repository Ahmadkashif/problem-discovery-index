# Release Delivery and DSP Specification Compliance

**Industry:** [[music-distribution-platforms|Music Distribution Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every streaming service has its own ingestion rules on top of a shared standard, and a release rejected on a specification detail misses its date.
**Tags:** #bert #large-language-models #object-detection #cnns #k-nearest-neighbors #evaluation-metrics #data-integration #automation

## The Problem
Delivering a release means producing a package that satisfies each destination service. DDEX provides the common message standard, and each service layers its own requirements: audio format and loudness, artwork dimensions and content restrictions, title formatting conventions for versions and features, contributor role vocabularies, explicit content flagging, territory and release date handling, pre-save and pitch windows.

The rules differ in small ways and change without much notice. A title formatted as acceptable at one service is rejected at another. Artwork containing a logo, a social handle or a price is rejected by some and not others.

Rejections arrive asynchronously, sometimes days later, sometimes as a status without a clear reason. The distributor's operations team interprets, corrects and redelivers.

Release dates are hard deadlines with marketing attached. An artist who has promoted a Friday release and whose track is rejected on Wednesday has a problem the distributor must solve in hours.

And the volume is extreme. The major distributors ingest a very large number of tracks daily, most from self-serve users who have never read a specification.

## What Already Exists
DDEX standardises the message format. Distributors maintain validation at upload for the obvious cases: file format, duration, artwork dimensions. Services publish specifications and provide rejection feedback of variable clarity. Some distributors offer pre-delivery checks.

## The Customisation Gap
Validation is shallow relative to what the specifications actually require. Title formatting conventions, contributor role correctness, explicit flagging consistency and artwork content restrictions are all checkable before delivery and are frequently discovered at rejection.

Artwork content checking is a vision problem treated as a manual review. Logos, text overlays, social handles, prices and prohibited imagery are detectable, and are currently caught either by a reviewer or by the service's own rejection.

Rejection reasons are not learned from. Every distributor has a large history of rejections with their eventual corrections, which is a directly supervised mapping from defect to fix, and it is used to write help articles rather than to prevent the defect.

Specification changes are absorbed reactively. A rise in rejections of a particular type is the signal that a service changed something, and it is visible in the distributor's own telemetry before any notice arrives.

And the guidance given to artists at upload is generic. Correcting a defect at upload, in language a non-specialist understands, is worth more than any downstream process.

## Impact If Solved
Delivery failures hit at the moment an artist has least tolerance for them, and they are almost all preventable by checking against rules that are written down. Deeper pre-delivery validation, vision-based artwork checking and learning from the rejection history convert a reactive operations queue into an upload-time correction.
