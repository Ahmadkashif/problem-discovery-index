# A Manual Craft in an Automated Pipeline

**Niche:** [[niches/print-on-demand-platforms/embroidery-and-stitch-decoration/profile|Embroidery & Stitch Decoration]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every embroidered order depends on a stitch file produced by a skilled person from an arbitrary image, which is the one manual step in an automated pipeline and the one that determines whether the result is any good.
**Tags:** #convex-optimization #graph-theory #cnns #evaluation-metrics #confidence-intervals #optimization-fundamentals #automation #dynamic-programming
**Contested on:** Every serious competitor in this sub-niche is fighting to turn an arbitrary uploaded image into a stitch file that runs cleanly on a given fabric — and whoever does that takes the category, because digitising is a manual craft standing between a platform's automated pipeline and a physical result.

## The Problem
A merchant uploads a logo with fine lettering and a gradient. Automatic digitising produces a file with excessive density in the gradient area, an underlay that will not support the lettering, and stitch directions that pull the fabric. A digitiser rebuilds it, taking twenty minutes, which is longer than every other step in the order combined. On the next order for the same design, at a different facility on a different fabric, the compensation is wrong and it puckers. The craft knowledge that would have got both right exists in individual digitisers and has never been captured, because nobody records what they decided or what happened afterwards.

## Why Nobody Has Built This
Digitising is genuinely skilled and the automatic tools have been poor for long enough that the assumption of manual necessity is fixed. The knowledge is tacit and held by practitioners who were never asked to structure it. There has never been a dataset connecting digitising decisions to stitched outcomes at scale, because no single embroidery shop produced enough variety — which is exactly what a platform now does. And the volume share is small enough that it does not command engineering attention.

## What to Build
Learn the conversion from the outcomes. Capture the digitising decisions and the stitched result together — the source artwork, the stitch parameters chosen, the fabric, the machine and whether it ran clean — which is the dataset nobody has ever had and is the precondition for everything here. Generate stitch files automatically from the artwork and the fabric, learning from that corpus, with the digitiser reviewing rather than building, which is the build and converts twenty minutes into two. Model fabric behaviour explicitly — stretch, pile, stability — into the underlay and compensation, since the same file on two fabrics needs two different compensations and the current practice is one file reused. Assess embroiderability before listing, which the fix note develops. Simulate the result and show it, since a stitch simulation is achievable and gives both the digitiser and the merchant something to react to before any thread is used. Optimise stitch count against appearance, since stitch count is the cost driver and is routinely higher than it needs to be. Match thread colours to the artwork against a measured palette rather than by eye, which is a small, mechanical and currently approximate step. Maintain the stitch file per fabric rather than per design, so a design ordered on a cap and a fleece gets the right file each time. And treat digitiser expertise as something to capture rather than to employ indefinitely, since it is scarce and ageing.

## Target Customer
Embroidery production operations, platform production engineering, the digitisers, and merchants offering embroidered products.

## Impact If Built
No single embroidery shop ever had enough variety to learn the conversion and a platform generates it daily. Capturing digitising decisions alongside stitched outcomes is the dataset that has never existed, and per-fabric stitch files fix a failure the current one-file-per-design practice guarantees.
