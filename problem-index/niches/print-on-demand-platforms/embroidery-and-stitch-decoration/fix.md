# A Design That Was Never Embroiderable

**Niche:** [[niches/print-on-demand-platforms/embroidery-and-stitch-decoration/profile|Embroidery & Stitch Decoration]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Designs with gradients, photographic detail, hairline strokes or forty colours are offered on embroidered products because the catalogue lists every product for every design, and none of them can be stitched.
**Tags:** #cnns #evaluation-metrics #confidence-intervals #automation #descriptive-statistics #worker-facing #quick-win #object-detection
**Contested on:** Every serious competitor in this sub-niche is fighting to turn an arbitrary uploaded image into a stitch file that runs cleanly on a given fabric — and whoever does that takes the category, because digitising is a manual craft standing between a platform's automated pipeline and a physical result.

## The Problem
A merchant uploads a detailed illustration with a photographic gradient and a dozen subtle colour transitions. The platform lists it across every product including an embroidered cap, because listing everywhere is the default and nothing checks. A customer orders the cap. The digitiser opens the file and can see immediately that it cannot be stitched acceptably — the detail is below minimum stitch size, the colour count exceeds the machine's needles, and the gradient has no embroidery equivalent. They do their best, it looks poor, it is refunded. Everything about that outcome was determinable from the image at upload.

## Why It's Still Broken
The catalogue lists all products for all designs because that maximises the merchant's apparent range and the platform's listing count. Embroiderability is a judgement that only a digitiser has made, at order time, one order too late. There is no check because nobody wrote down what makes a design embroiderable in terms a system could apply. And the loss is small per order and spread across merchants.

## What a Fix Looks Like
Check embroiderability at upload and list accordingly. Score every design against the properties that matter — minimum feature size, stroke width, colour count, gradient content, detail density, aspect against the available embroidery area — which are all measurable from the image and together capture most of what a digitiser judges in a glance, and this scoring is the fix. Restrict product availability automatically, so an unembroiderable design is simply not offered on embroidered products rather than being sold and refunded. Tell the merchant why and what to change, since many designs become embroiderable with a simplified variant and merchants will make one. Offer an automatically simplified embroidery variant for approval, which turns a restriction into a product. Set the threshold from outcomes rather than from rules of thumb, using the digitisers' own accept and reject history. Show a stitch simulation at upload so the merchant sees the difference between their illustration and its embroidered form. Report how many listings are currently offering unembroiderable combinations, which is likely a large number and is a retrospective sweep. And give digitisers a route to reject an order as unembroiderable rather than producing a poor result, which the operator niche develops.

## Who Feels the Pain
Digitisers producing work they know will be refunded; merchants whose ratings suffer from products that could never have worked; and customers receiving an illustration rendered as a stiff patch.

## Impact If Fixed
Everything about the failure is determinable from the image at upload and the catalogue lists every product by default. Scoring the measurable properties captures most of what a digitiser judges instantly, and an automatically simplified variant turns a restriction into a product.
