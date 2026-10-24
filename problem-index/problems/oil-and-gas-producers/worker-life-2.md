# The Leak-Survey Technician and the Paper Trail

**Industry:** [[oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Worker Life Changing
**One-liner:** An optical-gas-imaging technician films every component at site after site, then spends evenings filing clips, tagging leaks and chasing repairs against deadlines; a tool that did the filing and tracking would give back evenings and the fear of being the name on a missed repair.
**Tags:** #cnns #object-detection #semantic-segmentation #large-language-models #worker-facing #compliance #workflow-orchestration

## The Problem
Leak detection and repair (LDAR) at well sites and compressor stations is done by technicians with optical gas imaging (OGI) cameras, which show hydrocarbon plumes as moving smoke on an infrared screen. Under EPA's methane rules for new and modified sources (OOOOb) and the state plans that will apply them to existing sites (OOOOc), well sites and central production facilities with major production and processing equipment get an optical gas imaging survey at least quarterly and an audio-visual-olfactory check at least bimonthly. A leak found with OGI needs a first repair attempt within 30 calendar days and a final repair within 30 days after that (40 CFR 60.5397b). Several of the 2024 rule's compliance dates were moved to 22 January 2027 by an interim final rule published 31 July 2025 and finalised in November 2025 (EPA), but state rules in Colorado, New Mexico and elsewhere already require surveys (recalled), and operators' own programmes run regardless.

A technician may survey a dozen sites a day. At each one they walk every tank hatch, thief hatch, valve, connector, controller and compressor seal, filming at the distance and conditions the method requires. When they see a leak they tag it, photograph it, record the component and notify maintenance. At night they upload video, match clips to sites and components, fill the survey log, and check which repairs from earlier visits are still open.

## Why It Matters to the Worker
The fieldwork is hard but familiar: heat, cold, climbing on tanks with hydrogen sulfide risk, and driving between sites. The paperwork is what keeps technicians up. A survey that cannot be proved, because a clip was not saved, the wind speed was not logged or the component list was incomplete, counts as not done, and the technician's name is on it. Repairs depend on other people, but the technician is the one asked why a leak found in March was still on the list in May.

The skill is also hard to pass on. Experienced technicians read a faint plume against a hot background, know which thief hatches leak when a tank is filling and which ones are just venting through a working control, and spot an unlit flare from the road. New technicians miss faint leaks or flag heat shimmer.

## What a Solution Looks Like
Clips uploaded from the camera are matched automatically to site, date, conditions and component from the site's equipment list and GPS. A vision model flags likely plumes in each clip for the technician to confirm, and drafts the survey log and the leak record. A repair tracker sends each leak to maintenance with the clip attached and escalates before the deadline, and the annual report is assembled from the records. The technician reviews and signs instead of typing.

## Impact If Solved
If filing and logging take one to two hours a night today (estimate), automating them returns roughly 5–10 hours a week per technician. Catching faint leaks a junior would miss raises the skill floor of the whole crew, and a programme with no undocumented surveys removes the most common way a technician ends up named in a violation.
