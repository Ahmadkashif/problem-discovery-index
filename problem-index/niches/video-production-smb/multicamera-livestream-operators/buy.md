# Equipment Loadout and Venue Setup Documentation System

**Niche:** [[niches/video-production-smb/multicamera-livestream-operators/profile|Multicamera Livestream Operators]]
**Industry:** [[industries/video-production-smb|Video Production SMB]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sortly and Gear Inventory track equipment, but a livestream operator needs to build venue-specific equipment loadouts that document exactly which gear goes to which venue, with setup diagrams and cable routing — so that any crew member can set up the system without the owner present.
**Tags:** #workflow-orchestration #data-integration #automation #worker-facing

## The Problem
A multicamera livestream operator sets up at a church every Sunday, a corporate conference center monthly, and various event venues ad-hoc. Each venue requires a different equipment configuration: different camera positions, different cable runs, different audio inputs, different network connections, and different power sources. The owner knows how to set up each venue from memory — Camera 1 goes on the tripod by the stage-left column, Camera 2 on the balcony rail, the ATEM switcher goes on the table by the sound booth, the encoder needs the ethernet cable that's taped behind the projector screen. When the owner sends a crew member to set up instead, the setup takes twice as long, cables are routed incorrectly, and the stream starts 15 minutes late. The venue-specific knowledge exists nowhere except the owner's head.

## What Already Exists
Sortly, Asset Panda, and Gear Inventory track equipment (serial numbers, location, maintenance status). Event production tools (LASSO, Crew) handle crew scheduling. But none connect equipment inventory to venue-specific setup configurations. Paper checklists exist ("bring: 3 cameras, 1 switcher, 8 cables, 2 monitors") but don't show placement or connections. Photos of past setups live in the owner's phone camera roll. CAD-style venue diagrams (Vectorworks, AutoCAD) are overkill for a 3-person operation.

## The Customization Gap
A livestream-specific setup documentation tool needs to: (1) store venue profiles with floor plan photos, power outlet locations, internet access points, and client contact information, (2) build venue-specific equipment loadout lists from the company's inventory (Camera A goes to Camera Position 1, HDMI Cable #3 goes from Camera A to the switcher), (3) include annotated photos of the setup — taken during the previous event — showing exactly where each piece of equipment is placed, (4) provide a connection diagram showing what plugs into what (the visual equivalent of a network diagram but for live production), (5) generate a loadout checklist that the crew uses when packing the truck (with checkbox confirmation), and (6) track setup/teardown times per venue to improve efficiency. When a new crew member is assigned to a venue they've never been to, they follow the documented setup and replicate the owner's configuration.

## Target Customer
Livestream production companies with 2+ crew members who set up at recurring venues (churches, corporate offices, event spaces) 5+ times per month.

## Impact If Solved
Reduces setup time at recurring venues from 2 hours (new crew member without documentation) to 1 hour (following documented procedure). Enables the owner to delegate setup to crew members without being present — freeing 5–10 hours per week of owner time. Eliminates the 10–15% of events where incorrect setup causes technical issues (wrong cable, wrong camera position, wrong audio input) that degrade stream quality.
