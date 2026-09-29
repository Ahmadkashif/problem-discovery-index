# Field Capture Infrastructure That Already Works Offline

**Niche:** [[niches/agtech-platforms/independent-crop-consultants/profile|Independent Crop Consultants — Acres Per Consultant]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** On-device speech recognition, offline-first data sync and geotagged media capture are all commodity components, and a crop consultant standing in a field with no signal writes in a notebook and types it up that night.
**Tags:** #transformers #seq2seq #cnns #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor selling to independent consultants is fighting to raise the acres one person can cover at quality — and whoever cuts the hours between walking a field and delivering a report takes the firm.

## The Problem
The consultant is in the middle of a field, a mile from the truck, with no cellular coverage, holding a plant in one hand. The application requires typing into fields and does not work reliably offline, so they write in a notebook. That evening they transcribe the notebook into the application and then write reports from it — two transcriptions of the same observations, the first of which exists only because the capture tool did not work where the work happens.

## What Already Exists
On-device speech recognition runs offline on any modern phone with good accuracy. Offline-first synchronisation frameworks are mature. Geotagged photo capture is native. Bluetooth integration with field instruments — soil probes, moisture meters, weather stations — is standard. Rugged and weatherproof device options are established in every field trade. Every component required is available and inexpensive.

## The Customization Gap
The adaptation is to agronomy's vocabulary and physical conditions. It requires: (1) offline as the default operating mode with the full field record pre-staged before the drive, since the whole failure is assuming connectivity where there is none; (2) speech recognition adapted to agronomic vocabulary — crop stages, pest and disease names, chemical names, the local shorthand — which is exactly where a general model degrades and where a domain vocabulary is decisive; (3) structured extraction from free speech rather than a form, so the consultant says what they see and the structure is derived, which is the difference between a tool used in the field and one used in the truck; (4) location captured automatically with every observation, since where in the field matters enormously and is the detail most often lost in a notebook; and (5) photograph classification as an assist rather than an authority, because a pest identification from an image is a prompt for the consultant and not a conclusion, and products that have overstated this have damaged trust in the whole category.

## Target Customer
Independent consultants and scouting platform vendors, and the retail agronomy organisations whose staff face identical conditions.

## Impact If Solved
Eliminating the notebook removes an entire transcription pass and is the precondition for the automatic reporting in the build note, since a report cannot be generated from observations that were never captured digitally. The vocabulary adaptation is the specific work and is a fortnight of effort against a component that otherwise fails in daily use.
