# Impairment Localization Trained on the Senior Tech's Fixes

**Niche:** [[niches/wired-broadband-providers/hfc-plant-maintenance/profile|HFC Plant Maintenance & Proactive Network Maintenance]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** PNM tools show that an impairment exists and roughly where; nothing learns from the repairs that cleared past impairments which plant element a new signature points to.
**Tags:** #tacit-knowledge-ml #cnns #graph-neural-networks #gradient-boosting #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to locate an outside-plant impairment from modem telemetry before customers call, and whoever sends the right crew to the right span first, without a premises visit, takes the account.

## The Problem
An operator's PNM dashboard lights up a node with micro-reflections on a dozen modems. The tool estimates echo distances, but turning that into "replace the tap at pole 14" still takes a senior maintenance technician who knows the plant and has read hundreds of these plots. Juniors drive the leg checking taps one by one, or the impairment waits until customers call and installers are sent to houses.

## Why Nobody Has Built This
The label doesn't exist. Repairs are logged as resolution codes without a map location or the telemetry around them, so no vendor has the paired history of signature and confirmed fix. Plant maps are unreliable, which undermines any topology-based model. And the largest MSOs, who have the data, build internally and don't sell.

## What to Build
A repair log that pins each fix to a plant element in under a minute and automatically attaches downstream telemetry from before and after; the signature change becomes the label. On it, convolutional models classify impairment type from pre-equalization and spectrum data, a graph model over topology ranks the shared elements most likely at fault, and the system learns span-length and tap-assignment corrections to the plant map from where fixes actually cleared signatures. Senior technicians review ranked suggestions during calibration, so their read becomes training data.

## Target Customer
Directors of field maintenance at mid-sized cable operators and at telcos running legacy coax, and PNM vendors who want localisation accuracy they can sell.

## Impact If Built
Maintenance crews go to the right element first, premises dispatches for shared faults fall, and the senior technician's judgement is retained after retirement. For an operator with hundreds of thousands of subscribers, avoided wrong-location dispatches are worth millions a year (estimate).
