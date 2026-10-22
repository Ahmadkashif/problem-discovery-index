# Effect Mask Proposals Trained on the Separation Archive

**Niche:** [[niches/greeting-card-publishers/embellishment-prepress/profile|Embellishment & Production Art Prepress]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Card publishers hold years of approved art paired with the foil, emboss and glitter masks a production artist drew for it, which is exactly the supervision a segmentation model needs, and nobody has trained one.
**Tags:** #semantic-segmentation #cnns #transfer-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche (outsourced prepress houses, specialty printers' prepress departments and publishers' in-house production art teams) is fighting to turn approved card designs into foil, emboss, die-cut, glitter and spot-gloss separations that pass the printer's proof first time, and whoever delivers the most designs right first time inside the seasonal window takes the publisher's production art work.

## The Problem
When a seasonal line is approved, hundreds of designs need effect separations within weeks. Production artists trace masks by hand, and the peak load sets the size of the team.

## Why Nobody Has Built This
Prepress software vendors serve packaging and commercial print, where effects are fewer and copy is the hard part. Card-specific effect separation is a niche inside a niche. The training data exists only inside publishers' archives, in mixed file formats.

## What to Build
A plug-in for the artist's existing software that takes the flattened art and a rough indication of which elements get which effect, and proposes each effect layer as an editable vector mask, using a segmentation model fine-tuned on the publisher's own art-and-separation pairs. It applies learned rules (minimum foil line weight, emboss depth near folds, die-to-type clearance) before export and learns from every correction.

## Target Customer
Production art directors at card publishers, at the specialty printers who do prepress for them, and at outsourced prepress houses competing for the same seasonal work.

## Impact If Built
Separation time per design cut substantially (estimate: half or more on foil and emboss), seasonal peaks absorbed without temporary staff, and fewer proof rounds.
