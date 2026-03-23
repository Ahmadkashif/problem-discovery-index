# Design-to-Production Platform for Ornamental Metal

**Niche:** [[niches/metal-fabrication/ornamental-and-architectural-metal/profile|Ornamental & Architectural Metal]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform connects the ornamental metalwork design process (client presentations, design revisions, finish selection) to the shop floor production process (cut lists, weld sequences, finish schedules) — forcing the fabricator to manually translate an approved design into production documents every time.
**Tags:** #automation #workflow-orchestration #data-integration #revenue-impact

## The Problem
An ornamental metalwork project follows a unique workflow: design consultation with the client (material samples, finish options, design sketches), design revision cycle (2-5 rounds of design changes before approval), shop drawing creation (translating the approved design into fabricatable detail drawings), production (cutting, forming, welding, finishing), and installation. The handoff between design approval and shop floor production is entirely manual — the fabricator re-draws the approved design as shop drawings, creates a cut list from the shop drawings, specifies the finish for each element, and generates a production schedule. This design-to-production translation takes 4-16 hours per project and introduces errors when design intent is lost in translation (the client approved a specific patina application that the finisher wasn't told about).

## Why Nobody Has Built This
Ornamental metalwork is a niche within a niche — the market is too small and too varied for traditional manufacturing software vendors. The workflow combines creative design (where tools like Rhino and SketchUp live) with production management (where tools like JobBOSS live), and no single vendor spans both domains. The fabricators themselves are craft-oriented and often resistant to software-heavy workflows, preferring hand-drawn shop sketches over digital systems.

## What to Build
A project management platform designed for ornamental metal workflow: design presentation (shareable design boards with material/finish samples for client review and approval tracking), automatic shop drawing generation from the approved design (extracting component dimensions, weld joints, and finish specifications), cut list and BOM generation, production scheduling with finish-sequence logic (certain finishes must be applied before assembly, others after), and installation coordination. The platform bridges the creative front-end with the production back-end, ensuring design intent flows through to the finished product.

## Target Customer
Owner-operators of ornamental and architectural metalwork shops with $500K-$10M annual revenue, producing 20-100 custom projects per year. Approximately 5,000-8,000 shops in the US.

## Impact If Built
Reduces design-to-production handoff from 4-16 hours to 1-2 hours per project through automated shop drawing and BOM generation. Eliminates finish specification errors that require rework at $1,000-$5,000 per incident. Improves client experience through professional design presentations that increase project win rate. For a shop doing $2M annually, reducing rework by 3% saves $60,000/year.
