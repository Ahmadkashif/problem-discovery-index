# Document Extraction on Records Written by Hand in 1890

**Niche:** [[niches/land-surveyors/title-plant-search-operations/profile|Title Plant & Search Operations]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The chain of title runs back through typescript, carbon copies, and handwritten grantor books, and the plant has to index all of it.
**Tags:** #ocr #computer-vision #named-entity-recognition #large-language-models #data-integration

## The Problem
A title plant is only as good as its index, and building and maintaining one means reading every recorded instrument in a county. Modern records arrive as reasonable digital images. Older ones are microfilm scans of typescript, carbon copies, and handwriting, in books that used varying conventions across decades and clerks.

The content that matters is specific: the parties, the instrument type, the legal description, the recording reference, and any conditions. Legal descriptions are the hardest part — metes and bounds written as bearings and distances referencing monuments that may no longer exist, or lot-and-block references to plats recorded elsewhere. Getting a legal description wrong misindexes the instrument, and a misindexed instrument is one a search will not find, which is a claim.

The work is done by indexers reading documents. It is the plant's largest operating cost and the constraint on extending coverage to new counties.

## What Already Exists
Document processing platforms and OCR are mature. Handwriting recognition has improved substantially. Named entity extraction from legal documents is offered commercially and works well on modern text.

## The Customization Gap
The generic tools were built for modern printed documents in known formats.

**Historical document conditions are the norm, not the exception.** Faded microfilm, bleed-through, skewed scans, and mixed handwritten and typed content across a century of clerk conventions. Recognition accuracy on this material is far below what modern-document benchmarks suggest, and the accuracy that matters is per-field on the fields that determine indexing.

**Legal descriptions need parsing, not extraction.** A metes-and-bounds description is a structured traverse expressed in prose, and it can be parsed into geometry, checked for closure, and matched against neighbouring parcels. That is a domain capability no document platform has, and it is exactly what would catch the errors that produce claims.

**Party name normalization across a century.** The same person appears as different spellings, with and without middle initials, as a trust, as an estate, as a corporation that later merged. Grantor-grantee chains only link if the names resolve, and the resolution problem spans generations.

**Errors have to be findable later.** A misindexed instrument is invisible — nobody knows it was missed until a claim. Confidence scoring per field, with systematic audit of low-confidence indexing against the source, is the only control, and generic pipelines report accuracy in aggregate.

**Cross-instrument consistency as a check.** A deed conveying a parcel that a prior instrument shows as already conveyed is an inconsistency the plant can detect. That kind of chain-level validation is where the real errors surface and no extraction product frames it.

## Target Customer
VP of Plant Operations or Chief Technology Officer at a title underwriter or plant operator, where indexing cost governs coverage and indexing error governs claims.

## Impact If Solved
Plant maintenance and extension is the cost that limits coverage, and indexing error is a direct claim cause that is invisible until it fires. Parsing legal descriptions into checkable geometry and validating chains for consistency attacks both — and the same capability makes the plant queryable in ways a name index never can be.
