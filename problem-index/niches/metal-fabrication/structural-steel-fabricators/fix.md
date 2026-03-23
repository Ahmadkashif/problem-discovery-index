# Disconnected Detailing and Shop Floor Tracking

**Niche:** [[niches/metal-fabrication/structural-steel-fabricators/profile|Structural Steel Fabricators]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Fix (Pain Point)
**One-liner:** Detailers work in Tekla, the shop floor tracks production on whiteboards or paper piece lists, and the project manager reconciles status by walking the shop and yard — because the detailed 3D model data and the shop floor production status live in completely disconnected systems.
**Tags:** #data-integration #automation #worker-facing

## The Problem
A structural steel project has hundreds to thousands of unique piece marks. The detailer creates every piece in Tekla or SDS2, generating complete geometry, weld details, and material specifications. The shop floor receives shop drawings (2D printouts from the model) and tracks production status on paper piece lists, whiteboards, or basic spreadsheets — checking off each piece as it moves through fit-up, welding, finishing, and shipping. The project manager, who needs to report status to the general contractor and coordinate deliveries, determines project status by walking the shop floor, checking the whiteboard, and calling the shipping coordinator. There is no digital connection between the model (which knows every piece that needs to be fabricated) and the shop floor (which knows which pieces are complete).

## Why It's Still Broken
Tekla and SDS2 were designed for steel detailing, not production management. FabSuite and FabTrol bridge some of the gap but require manual piece status updates by shop floor supervisors — data entry that competes with production priorities. The fundamental disconnect: the model creates a perfect digital representation of the project, but the shop floor operates on paper derivatives of that model, and status tracking reverts to manual methods because nobody has built a lightweight connection between model data and shop floor reality.

## What a Fix Looks Like
A shop floor status tracking system that imports the piece list directly from Tekla/SDS2 (using the model's piece marks, quantities, and weights as the master list), provides a simple interface for shop floor supervisors to update piece status (scan a barcode or tap a piece mark on a tablet as it completes each operation), and feeds real-time completion data back to the project manager and the shipping coordinator. The detailer creates the model; the production tracker automatically inherits the piece list; the project manager sees real-time status without walking the floor.

## Who Feels the Pain
Project managers who spend 30-60 minutes daily on shop floor walks to determine production status, and shop foremen who manually maintain piece tracking lists that are always slightly out of date.

## Impact If Fixed
Eliminates the daily status reconciliation walk — recovering 30-60 minutes of project manager time per project per day. Provides real-time piece completion data for delivery coordination, reducing missed delivery dates caused by status miscommunication. For a fabricator running 5 projects simultaneously, recovering 2.5-5 hours of project manager time daily enables better coordination that prevents the $5,000-$15,000 field delay claims that result from late steel deliveries.
