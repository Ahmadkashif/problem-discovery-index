# Package Theft and Damage Photo Evidence Capture

**Industry:** [[last-mile-delivery|Last-Mile Delivery]]
**Type:** Worker Life Changing
**One-liner:** Delivery drivers who photograph package placement at every door — a required step for proof-of-delivery documentation — but whose photos are inconsistent in quality and framing get guided photo capture that ensures every delivery photo is an adequate evidence record for claims and recipient disputes.
**Tags:** #computer-vision #automation #compliance #worker-facing

## The Problem

Proof-of-delivery (POD) photos are the primary evidence for resolving "package not received" claims — one of the top sources of carrier liability and customer dispute costs. A well-framed POD photo shows: the package at the delivery location, the address number visible, and the placement context (at door, in mailbox area, beside door). A poorly-framed photo (package barely visible, no address number, shot from too far) provides inadequate evidence, costing the carrier or DSP the disputed package value.

Drivers are required to take POD photos but not trained on what constitutes adequate evidence. The quality of their photos varies enormously — some drivers take careful, consistent evidence photos; others take quick, low-quality shots that provide no evidentiary value.

## Why It Matters to the Worker

Drivers who take inadequate POD photos face claim chargebacks from carriers or DSP contracts. A DSP that generates excessive insufficient-evidence claims from poor photo quality faces contract penalties and eventually contract loss. Drivers bear personal liability for claims tied to their route when evidence is inadequate. Improving POD photo quality protects drivers from disputed deliveries that were actually made correctly.

## What a Solution Looks Like

A real-time photo guidance overlay in the delivery app: after the driver takes a POD photo, a quick-check model evaluates the photo for: address number visibility, package visibility and clarity, adequate lighting, framing. If the photo fails a criterion, the driver sees a brief prompt: "Address number not visible — retake" before the app allows submission. The check takes < 1 second. Drivers quickly learn to take photos that pass on first attempt.

## Impact If Solved

Reduces insufficient-evidence claims by improving POD photo quality across all drivers. Protects drivers from disputed deliveries where the package was correctly delivered but the photo evidence is inadequate. Reduces DSP liability from customer claims on deliveries where the evidence exists but was poorly captured.
