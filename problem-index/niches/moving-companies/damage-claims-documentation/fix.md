# Pre-Move Photo to Post-Move Claim Matching

**Niche:** [[niches/moving-companies/damage-claims-documentation/profile|Damage Claims Documentation & Resolution]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Movers take hundreds of pre-move photos but cannot reliably match a specific photo to a specific claimed item weeks later, making the documentation useless when it's needed most.
**Tags:** #cnn #multiclass-classification #computer-vision #data-integration #automation

## The Problem
Even movers who diligently photograph items before a move face a retrieval crisis when a claim arrives. A 4-bedroom house generates 80-150 pre-move photos. The claim says "antique mahogany end table, scratched during move." The claims handler must scroll through 150 unorganized photos looking for that specific table, hoping the crew photographed it, hoping they can identify which of several tables in the photos is the one being claimed, and hoping the photo is clear enough to show pre-existing condition. In practice, the match is found less than 40% of the time, and the claims handler spends 30-60 minutes searching. When the match isn't found, the mover pays the claim by default.

## Why It's Still Broken
Photos are captured without metadata linking them to specific inventory items. The crew takes photos in sequence as they walk through the house, but the inventory list is created separately (on a different form, often by a different person). No connection exists between "photo #47 in the camera roll" and "item #23 on the inventory sheet." Attempts to fix this with manual tagging (crew types item name for each photo) fail because crews are under time pressure and won't spend 10 seconds labeling each of 150 photos.

## What a Fix Looks Like
An automated photo-to-inventory linking system that uses object detection to identify the item type in each photo (end table, sofa, dresser, TV), matches it to the corresponding entry on the inventory list based on item type + room location + sequence, and creates a searchable catalog indexed by item. When a claim arrives, the handler searches "mahogany end table, living room" and immediately retrieves all pre-move photos of that item. The system must work passively — the crew takes photos as they normally would, and the matching happens automatically via the vision model, requiring zero additional crew effort.

## Who Feels the Pain
Claims handlers who spend 30-60 minutes per claim searching through unorganized photo folders, and moving company owners who pay claims they shouldn't because the evidence exists but can't be found.

## Impact If Fixed
Increases pre-move photo retrieval success rate from 40% to 85-90%, reduces claims research time by 70%, and prevents $1,000-3,000/month in claims paid due to inability to locate existing documentation.
