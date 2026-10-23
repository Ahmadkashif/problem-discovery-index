# A Service History That Follows the Door

**Niche:** [[niches/locksmiths/commercial-door-hardware-service/profile|Commercial Door Hardware Service & Code Compliance]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A school district's locksmith has repaired the same exit device four times in two years and neither side can see it, because jobs are recorded by building and ticket, never by door.
**Tags:** #cnns #object-detection #large-language-models #survival-analysis #data-integration #tacit-knowledge-ml #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to be the vendor a facility calls for its openings. But a fire-rated or egress door is won by inspecting it and closing deficiencies before the fire marshal or accreditation surveyor arrives, while an access-controlled door is won by delivering electrified hardware that works with the client's access system and still releases for egress on commissioning day. The buyers, data and clocks differ. Decomposed into contested sub-niches below.

## The Problem
A multi-site client sends tickets by building and room: "Gym east doors won't latch." The locksmith fixes what it finds and invoices against the ticket. Six weeks later a different technician gets "gym doors not closing" and starts again, unaware that the closer was adjusted last time or that the hinge on the active leaf has been replaced twice. The client cannot answer basic capital questions: which doors cost the most to keep running, which hardware models fail first, and when repair stops making sense against replacement.

## Why Nobody Has Built This
Locksmith firms are small and their software is generic field-service tooling built around customers and jobs. Facility platforms treat HVAC units and elevators as tagged assets, but doors are rarely tagged. Hardware identification is genuinely hard, with thousands of models across brands, many painted or decades old. Nobody owns the data model for an opening.

## What to Build
An opening registry built as a by-product of service. Technicians scan or place a small tag on the hinge side of the frame, take three photos and record a voice note. A vision model identifies the hardware set, and the visit's invoice lines attach to that opening. Over time each door carries its own failure history. Survival curves by hardware model and use level give replace-or-repair advice. Portfolio reports show the client which openings consume the budget and which repairs did not hold. The same record feeds pre-dispatch parts lists and the senior technician's diagnostic suggestions described in [[problems/locksmiths/high-impact|The Technician's Read of a Failing Opening]].

## Target Customer
Owners and service managers of commercial locksmith and door-hardware firms with 5–50 technicians serving school districts, hospitals, universities, retail chains and property managers.

## Impact If Built
Repeat visits to the same door become visible and preventable. Clients get capital-planning evidence they currently lack, and the firm holding the record becomes very hard to replace at contract renewal. On a portfolio of thousands of openings that plausibly removes an estimated ~10–20% of service calls through earlier replacement and better first fixes (estimate).
