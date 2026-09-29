# Rights Clearance and Release Verification

**Industry:** [[stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Whether an asset can be licensed commercially depends on releases, trademarks and property rights that are verified by a person looking at the image and the paperwork.
**Tags:** #object-detection #cnns #semantic-segmentation #bert #large-language-models #evaluation-metrics #compliance #automation

## The Problem
Commercial licensing requires that recognisable people have signed model releases, that private property and recognisable buildings have property releases where required, and that trademarks, logos, artworks and designs appearing in the frame do not create an infringement risk. Editorial-only assets avoid some of this and carry restrictions of their own.

Verification happens at review. A person examines the asset for recognisable faces, identifiable locations, visible logos and protected designs, checks the submitted releases against what is depicted, and assigns a licensing classification.

The judgements are genuinely hard. Recognisability is a spectrum. A logo partly obscured on a coffee cup may or may not matter. Buildings differ in protection by jurisdiction. Artwork in the background of an office shot carries its own copyright. Tattoos have been the subject of litigation.

The consequences are asymmetric and both real. An asset wrongly cleared for commercial use exposes the buyer, the contributor and the marketplace to a claim. An asset wrongly restricted to editorial loses most of its earning potential, invisibly, and the contributor is not told why.

Volume is very large and continuous, and the review is a small part of the assessment of each submission.

And release documents themselves are unstructured — photographs of signed forms, in many languages, with varying completeness, matched to assets by the contributor.

## What Already Exists
Face detection is mature. Logo and trademark detection exists commercially. Landmark recognition is capable. Release management is built into contributor submission workflows. Editorial and commercial classification is standard. Some platforms run automated pre-checks before human review.

## The Customisation Gap
Detection is deployed unevenly relative to what is available. Faces, logos, landmarks, artworks and screens displaying protected content are all detectable, and the systematic application of that detection at submission — with the specific region flagged — is inconsistent across the industry.

Release matching is manual. Verifying that the releases submitted actually correspond to the people visible in the asset, and that they are complete and signed, is document understanding plus a correspondence check, and it is done by eye.

Recognisability is not scored. It is a judgement made consistently by no two reviewers, and a model producing a recognisability estimate with the reasoning shown would improve consistency even where it does not decide.

Jurisdictional rules are not encoded. Property release requirements, editorial restrictions and trademark treatment vary by territory, and reviewers hold this as knowledge rather than referencing it as rules.

And contributors are not told. An asset restricted to editorial should carry an explanation and a remedy — obtain this release, reframe to exclude that logo — which converts a loss into a correction.

## Impact If Solved
Rights classification determines an asset's earning potential and the marketplace's legal exposure, and it is decided by eye at very large volume. Systematic detection with region flagging, automated release matching and encoded jurisdictional rules improve both accuracy and consistency, and telling contributors specifically why an asset was restricted turns an invisible penalty into a fixable defect.
