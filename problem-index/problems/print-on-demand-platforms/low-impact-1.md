# Artwork Preflight and Colour Reproduction

**Industry:** [[print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Preflight tooling is a mature discipline in commercial printing and the version shipped here checks resolution and dimensions, which are not what causes customers to complain.
**Tags:** #cnns #semantic-segmentation #object-detection #evaluation-metrics #confidence-intervals #feature-engineering #hypothesis-testing

## The Problem
A creator uploads artwork. The platform checks that it meets a minimum resolution and fits the print area, and accepts it.

The problems that actually generate complaints are not checked. Colours that cannot be reproduced by this process on this substrate — saturated cyans and oranges are common casualties in direct-to-garment printing — are accepted and print dull. Fine detail below the effective resolution of the process is accepted and prints as a smudge. Gradients that will band are accepted. Transparency and soft edges that will render as a hard halo against a coloured garment are accepted. Designs positioned across a seam, a zip or a pocket are accepted.

Each of these is knowable at upload, when a creator could adjust the file at no cost. Instead it is discovered by the customer who received the item.

The creator has no way to know. They designed on a bright screen in a wide colour space, and no one told them that the process cannot get there.

## What Already Exists
Preflight is a well-established discipline in commercial printing with mature tooling — Enfocus and similar products check colour spaces, resolution, fonts, overprint and trapping comprehensively. ICC colour management is a decades-old standard. Soft proofing on calibrated displays is routine in professional print. Print-on-demand platforms provide print area templates and basic resolution checks. Mockup generators produce a visual preview.

## The Customisation Gap
Commercial preflight assumes a professional operator who understands colour management and a proof step to catch what preflight misses. The print-on-demand creator is not a print professional and there is no proof, so the checks must be both more comprehensive and expressed in terms someone without printing knowledge can act on.

Substrate-specific gamut is the specific missing check. Whether a colour is achievable depends on ink, process and fabric together, and the platform has the measurement data to characterise this and generally does not.

Mockups actively mislead. A generated mockup shows the artwork at full screen saturation on a rendered garment, which is a promise the process cannot keep, and it is the primary thing both the creator and the end customer see before ordering. An honest preview showing predicted output would reduce complaints substantially and is resisted because it looks worse.

Placement checking against the physical garment is the fourth gap — seams, pockets, zips and collars vary by garment model and are known, and designs are placed against a flat rectangle.

## Impact If Solved
Preflight is the last free moment to fix an artwork problem, and the checks currently performed catch the least consequential issues. Substrate-aware gamut checking, banding and detail prediction, and an honest preview replace a costly downstream discovery with a message at upload — and the honest preview alone would address a large share of expectation-driven complaints.
