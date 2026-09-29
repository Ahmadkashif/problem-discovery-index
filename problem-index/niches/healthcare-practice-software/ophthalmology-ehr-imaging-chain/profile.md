# Ophthalmology EHR — the Imaging-to-Code Chain

**Parent Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in ophthalmology EHR is fighting to make diagnostic images from every device in the lane arrive in the chart already bound to eye, date and the interpretation that justifies the code — and whoever closes that chain best takes the account.

## Profile
**Market Size:** $650M US ophthalmology and optometry practice software
**Share of Parent Industry:** ~16% of the specialty EHR block
**Digital Adoption:** High — ophthalmology is among the most device-dense specialties in ambulatory medicine and has been digital for two decades
**Target Buyer:** Physician-owners and practice administrators at 3-30 provider ophthalmology and multi-site optometry groups
**Automation Potential:** Very High — the chain from device output to billed code is almost entirely mechanical and is almost entirely manual

## What Makes This a Distinct Niche
Ophthalmology runs on imaging in a way no other ambulatory specialty does. A single glaucoma follow-up may generate an OCT, a visual field, fundus photography and pachymetry, from four devices made by three manufacturers, each producing its own report. Every one of those tests is separately billable, several are billed per eye, and the modifier structure — RT, LT, -50, and the interpretation requirement attached to each code — is where the money is won or lost. The specialty is therefore uniquely exposed to a failure that is invisible elsewhere: an image that lands in the chart without laterality is both a billing defect and a clinical one. Practices carry staff whose job is substantially to reconcile images to eyes and encounters, and the volume is high enough that it is a real line of cost rather than a nuisance.

## Current Tools & Gaps
Nextech, Compulink, Eyefinity/OfficeMate, MDoffice and Modernizing Medicine's ophthalmology product all ship device interfaces and image viewers, and most support DICOM. DICOM is exactly the hinge: where a device emits proper DICOM with populated laterality and study description, binding is solvable; where it emits a vendor-proprietary report or a rendered PDF — which remains common across visual field and older imaging estates — the binding is a person reading a screen. No vendor reports how much of a given practice's inbound imaging binds automatically, which means practices cannot tell in advance which of their devices will work and which will produce daily reconciliation work. Image management vendors sit alongside the EHR rather than inside the coding path, so the interpretation-to-code link is left to the physician's memory.

## Problems
- [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/build|🔨 Build: Laterality-Bound Image Ingestion Across Mixed Device Estates]]
- [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/buy|🛒 Buy: DICOM Worklist Adapted to the Ophthalmic Lane]]
- [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/fix|🔧 Fix: The Unbilled Interpretation]]
