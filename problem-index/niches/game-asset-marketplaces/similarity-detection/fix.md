# Rescaled, Recoloured and Relisted

**Niche:** [[niches/game-asset-marketplaces/similarity-detection/profile|Similarity & Derivation Detection]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The reseller changed the scale, swapped the texture colours and exported to a different format, and the platform's hash check saw a new asset.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #k-nearest-neighbors #confidence-intervals #automation #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell whether an uploaded asset matches something already in the catalogue after retopology, rescaling, recolouring and format conversion — and whoever builds that detector takes the account.

## The Problem
Where a platform checks anything at all, it checks file hashes, and resellers defeat that with a trivial edit. Scaling the mesh, shifting the texture hue, re-exporting through a different tool — any of these produces different bytes and the same asset. The check that exists provides false assurance: the platform believes it is screening uploads and is screening only the least effortful cases.

## Why It's Still Broken
The check operates on bytes rather than on content — a detector defeated by any edit whatsoever gives the appearance of screening while catching only what would have been caught anyway. Content-level matching was assumed to need a research project. Nobody measured the detector's actual catch rate. And the false assurance is comfortable.

## What a Fix Looks Like
Add cheap content-level signals before building anything sophisticated. Compare normalised geometry statistics — vertex and face counts, bounding proportions, topology signatures — which is the fix and catches rescaling and re-export immediately at almost no cost. Compare texture perceptual hashes rather than file hashes, since those survive recolouring and recompression. Match on internal structure, naming and directory layout, as resellers rarely rebuild the package. Check against recently listed assets first, because resale usually follows the original quickly. Measure the current hash check's catch rate honestly, which will show it is near zero and justify everything else. Flag rather than block on these weaker signals, keeping the false positive cost manageable. Cluster by seller account, since these signals are far stronger in aggregate than individually. Run the checks retrospectively across the catalogue, which surfaces the existing backlog. Give creators a self-service search using the same signals, which turns them into the detection network. And report what the improved checks caught, so the next step is funded.

## Who Feels the Pain
Creators whose work is trivially relisted; platforms with a screen that screens nothing; buyers unable to identify the original; and honest sellers undercut by copies.

## Impact If Fixed
A detector defeated by any edit whatsoever gives the appearance of screening while catching only what would have been caught anyway. Normalised geometry statistics and perceptual texture hashes are cheap signals that catch the common cases.
