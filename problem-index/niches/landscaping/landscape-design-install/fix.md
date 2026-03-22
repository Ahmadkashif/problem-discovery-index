# Plant Availability and Substitution Tracking

**Niche:** [[niches/landscaping/landscape-design-install/profile|Landscape Design & Install]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Fix (Pain Point)
**One-liner:** Landscape designers specify plants that nurseries may not have in the right size, quantity, or cultivar — discovering this after the client has approved the design forces last-minute substitutions that change pricing, spacing, and the aesthetic intent of the plan.
**Tags:** #data-integration #worker-facing #gradient-boosting

## The Problem
A landscape designer creates a planting plan specifying 12 'Bloodgood' Japanese Maples in 3-inch caliper, 50 'Knock Out' roses in 3-gallon, and 200 Liriope 'Big Blue' in 1-gallon. The client approves the design. The purchaser then calls 3-5 regional nurseries to source the material and discovers: the 'Bloodgood' Japanese Maples are only available in 2-inch caliper (too small for the design intent) or 4-inch caliper ($200 more per tree), the nursery has 'Knock Out' roses but only in 5-gallon ($8 more per plant x 50 = $400), and Liriope 'Big Blue' is backordered until next season. The purchaser now calls the designer to discuss substitutions: "Can we use 'Emperor One' instead of 'Bloodgood'? Can we use 'Aztec Grass' instead of Liriope?" Each substitution potentially changes spacing (different mature width), visual effect (different foliage color or texture), maintenance requirements, and pricing. This back-and-forth cycle takes 2-5 days per project and sometimes requires redesigning sections of the plan after client approval.

## Why It's Still Broken
Nursery inventory is not digitized in any standardized, queryable format. Most wholesale nurseries publish availability lists as weekly PDF or Excel files emailed to established accounts — and these lists are updated weekly at best, with actual availability changing daily as other contractors buy stock. There is no API for nursery inventory. Plant naming is inconsistent: one nursery lists "Acer palmatum 'Bloodgood'" while another lists "Bloodgood Japanese Maple" and a third lists "A. palmatum Bloodgood" — making automated matching unreliable without a botanical name normalization layer. Substitution logic is entirely in the designer's head: which cultivars have similar growth habits, colors, and site requirements is tacit knowledge built over years of plant experience.

## What a Fix Looks Like
A plant sourcing platform that aggregates weekly availability lists from regional wholesale nurseries (ingested via email parsing or portal scraping), normalizes plant names to a canonical botanical taxonomy, and provides real-time searchable inventory by species, cultivar, size, quantity, and location. When a designer creates a planting plan, the system checks material availability across regional nurseries before the design is presented to the client, flagging items with low availability or long lead times. For unavailable plants, the system recommends substitutions based on a recommendation model trained on botanical similarity (growth habit, hardiness zone, sun requirements, mature size, foliage characteristics) and designer acceptance history — learning that designers in this firm prefer 'Crimson Queen' over 'Tamukeyama' as a 'Bloodgood' substitute. Substitutions include pricing impact and spacing adjustments so the designer can make informed decisions without calling nurseries.

## Who Feels the Pain
Designers who have to rework approved plans due to availability issues, purchasers who spend 4-8 hours per project calling nurseries and negotiating substitutions, and clients who experience project delays because plants they approved aren't available.

## Impact If Fixed
Eliminates the 2-5 day post-approval sourcing delay on 60-70% of projects, reducing average project start-to-install timeline by a week. Reduces purchaser phone time by 50-70% (3-5 hours per project) and prevents the 10-15% of projects where unavailable plants force design revisions that erode client confidence.
