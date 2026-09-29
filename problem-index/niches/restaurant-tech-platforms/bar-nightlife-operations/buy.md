# Computer Vision Applied to the Weekly Bottle Count

**Niche:** [[niches/restaurant-tech-platforms/bar-nightlife-operations/profile|Bar & Nightlife Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Object detection and fill-level estimation from photographs are commodity capabilities, and the beverage industry's inventory count is a person tilting bottles and estimating tenths at two in the morning.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in beverage operations software is fighting to reconcile what was poured against what was sold, at a granularity and a cost that a bar will actually sustain — and whoever closes that variance takes the account.

## The Problem
Counting a bar means handling every bottle: identify the product, estimate what fraction remains, record it. A well-stocked bar has several hundred bottles across the back bar, the well, the service station and the store room. The count takes two to four hours, is performed after close by exhausted staff, and its accuracy is whatever tired estimation produces. Because it is expensive and unpleasant, it is done weekly at best and frequently monthly, which is the root cause of the attribution problem in this niche.

## What Already Exists
Object detection, label recognition and fill-level estimation from images are all mature computer vision tasks with strong off-the-shelf models and straightforward transfer learning. Several inventory vendors already use photography — Partender's interface is built on tapping a fill level on a photograph, and others photograph shelves. Barcode and label databases for spirits are commercially available. Phone cameras are universal. The technology needed is unremarkable; what varies is how much human work remains after the photograph.

## The Customization Gap
The adaptation is toward a count that is a walk-through rather than a handling exercise. It requires: (1) shelf-level rather than bottle-level capture — photographing a section and detecting every bottle, its product and its fill in one pass, which is the difference between four hours and twenty minutes; (2) robustness to the actual conditions, which are dark, cluttered, backlit by bar lighting, with bottles occluding each other and labels turned away, and which is where generic models degrade and domain-specific training earns its cost; (3) honest uncertainty per bottle, so the ambiguous minority is flagged for a human glance rather than silently estimated, since a confidently wrong fill level corrupts the variance calculation that is the whole point; (4) product identification against a spirits catalogue with the long tail handled, because a bar's back bar contains obscure bottles that no general catalogue covers and the system must learn a given bar's inventory; and (5) supporting a mid-week partial count of the high-velocity products only, which is what actually raises the cadence enough to enable attribution.

## Target Customer
Bars, nightclubs and beverage-led restaurant groups, and the beverage inventory vendors whose current interfaces still require per-bottle interaction.

## Impact If Solved
Cutting the count from hours to minutes changes its cadence, and cadence is what unlocks everything else in this niche — attribution is impossible at weekly resolution and becomes tractable at daily or per-shift. It also removes one of the most disliked tasks in hospitality from the end of a closing shift.
