# Renderings Where Every Object Is Orderable

**Niche:** [[niches/interior-design-firms/rendering-and-presentation/profile|Rendering & Client Presentation]]
**Industry:** [[industries/interior-design-firms|Interior Design Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Generative tools render a beautiful room in seconds and every chair in it is fictional; traditional renders use real products but take days.
**Tags:** #diffusion-models #contrastive-learning #cnns #k-nearest-neighbors #transfer-learning #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce a photoreal view of the proposed room with real, orderable trade products fast enough to show in the first meeting, and whoever ties the rendering to the SKUs takes the presentation.

## The Problem
A designer wants to show a client the proposed living room on a site photograph in the first meeting. A generative image looks right but cannot be bought; a modelled render uses real products but needs 3D models that most trade manufacturers do not supply and takes days.

## Why Nobody Has Built This
Image generation and product identity have developed separately; trade manufacturers rarely publish 3D models; and conditioning generation on exact products has only recently become workable.

## What to Build
Generate the room from the site photograph and the designer's selected products, conditioning on each product's images so the rendered item matches it, and keep a link from every object to its SKU, price and lead time. Where the designer edits the image, retrieve the nearest real products for the new object.

## Target Customer
Residential studios presenting to clients, and studio-software vendors adding it as a feature.

## Impact If Built
Photoreal concepts in the first meeting, with a shopping list that matches, compress the first presentation cycle and the outsourcing bill.
