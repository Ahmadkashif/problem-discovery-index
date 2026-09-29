# Matching Through the Transformations Sellers Use

**Niche:** [[niches/game-asset-marketplaces/similarity-detection/profile|Similarity & Derivation Detection]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Exact file matching catches nothing, because nobody reselling an asset ships the same bytes.
**Tags:** #contrastive-learning #autoencoders #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #confidence-intervals #manifold-learning #graph-neural-networks
**Contested on:** Every serious competitor in this niche is fighting to tell whether an uploaded asset matches something already in the catalogue after retopology, rescaling, recolouring and format conversion — and whoever builds that detector takes the account.

## The Problem
Detecting a resold or derived asset requires matching through transformation. A mesh can be remeshed, decimated, rescaled, rotated and exported to a different format while remaining the same asset. A texture can be resized, recoloured, recompressed and repacked. Exact hashing catches only the laziest cases. What is needed is a representation in which the transformed asset lands next to the original, and no platform has built one.

## Why Nobody Has Built This
Geometry similarity that survives remeshing is a harder problem than image similarity and has fewer off-the-shelf answers. The catalogue is large and multi-format. There is no labelled set of known derivations to train against. And the platforms have not funded it because the reactive regime was adequate.

## What to Build
Learn representations that are invariant to the transformations that actually occur. Build geometry embeddings invariant to remeshing, decimation, scale and rotation, which is the core and is the technically hard half of the whole provenance problem. Build texture and material embeddings robust to resampling, recolouring and compression, since textures are where much of the identity lives. Match across formats rather than within them, because format conversion is the commonest disguise. Combine the modalities, as an asset matching on geometry and texture is far stronger evidence than either alone. Index for retrieval at upload latency across a catalogue of hundreds of thousands, which is the engineering constraint that shapes the architecture. Calibrate the threshold against genuine cases rather than a similarity score nobody has interpreted, since assets in the same style are legitimately similar and the false positive cost is high. Distinguish legitimate derivation from resale where the transformation pattern allows, which is a real and useful signal. Generate training pairs by applying the transformations synthetically, which solves the labelled data problem cheaply. Return the matched region rather than only a score, as reviewers need to see what matched. And expose it as a service other platforms and rights holders can query.

## Target Customer
Asset marketplaces, rights holders and creators, content identification vendors, and 3D search and retrieval providers.

## Impact If Built
Nobody reselling an asset ships the same bytes, so exact hashing catches almost nothing. Geometry and texture embeddings invariant to the transformations sellers actually apply is the detector the category lacks.
