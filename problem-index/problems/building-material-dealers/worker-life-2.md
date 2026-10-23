# The Truss Designer's Revision Queue

**Industry:** [[building-material-dealers|Building Material Dealers]]
**Type:** Worker Life Changing
**One-liner:** The truss and wall-panel designer gets back the evenings spent redrawing the same house for the third plan revision, and the clarity of knowing which change actually affects the structure.
**Tags:** #worker-facing #tacit-knowledge-ml #object-detection #graph-neural-networks #large-language-models #automation #workflow-orchestration

## The Problem
Many dealers own component plants that build roof trusses, floor trusses and wall panels; Builders FirstSource reported $3.4B of manufactured products in 2025, 22.4% of its sales. Behind each plant sits a design desk. The designer takes the architect's or home designer's plans, models the roof and floor system in MiTek or Alpine software, sets bearing points, girder locations, overhangs and heel heights, runs the engineering, produces the placement plan the framer will use, and sends the layout for the builder's approval and the plate supplier's engineering seal. A designer turns out a few houses a week (~3–10, estimate), each with dozens of truss profiles.

Then the plan changes. The builder moves a wall, the buyer adds a tray ceiling, the window schedule changes a header height, or the design arrives without bearing walls marked. Each revision means finding what changed between two PDF sets by eye, deciding which trusses are affected, re-running the design, re-issuing the placement plan and resubmitting for approval — often on a deadline set by a production schedule that has already given the plant its slot. Designers report spending a large share of their week on revisions rather than new work (estimate), and a missed change becomes a truss that doesn't fit on site.

## Why It Matters to the Worker
Truss designers are skilled and slow to train: it takes a year or more to become independently productive (estimate), and the craft — where a girder must go, which bearing the designer of record forgot, how this framer wants the hip set laid out — is learned by apprenticeship. They carry the blame for field fixes, they work late when the plant's slot approaches, and much of their time goes to clerical comparison of drawing sets rather than design. The trade is short of them, so the remaining designers carry more.

## What a Solution Looks Like
A revision assistant that compares two plan sets sheet by sheet, highlights every change that touches bearing, spans, heights, openings or roof geometry, maps those changes to the affected trusses and panels in the existing design, and drafts the revised layout for the designer to accept. For new houses, it pre-populates bearing walls, girder candidates and layout choices from the plans and from the designer's own past decisions on similar plans. The designer stays the decision-maker and signs the layout; the assistant takes the search and the redraw.

## Impact If Solved
If revision handling falls from hours to under an hour per change (estimate), a designer can absorb the revision load without evening work and take on more new houses, and the plant sees fewer field fixes from missed changes. The designers' own decisions, captured as they accept or reject suggestions, become the first record of the craft for training the next one.
