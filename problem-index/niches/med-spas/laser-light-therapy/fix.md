# Treatment Parameter Documentation Across Multiple Devices

**Niche:** [[niches/med-spas/laser-light-therapy/profile|Laser & Light Therapy Clinics]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Fix (Pain Point)
**One-liner:** Laser treatment parameters (fluence, pulse width, spot size, cooling) are documented inconsistently across devices and technicians, making it impossible to reproduce successful treatments or identify what went wrong when outcomes are poor.
**Tags:** #llm #text-generation #nlp #tacit-knowledge-ml #worker-facing

## The Problem
Each laser treatment involves 4-8 device-specific parameters that must be documented: fluence (energy), pulse width, spot size, repetition rate, cooling settings, pass count, and treatment area. A clinic operating 5 different laser devices has 5 different parameter sets, each with different terminology and ranges. Technicians document these inconsistently — some write "40J/cm2, 30ms, 12mm" in free text, others check boxes, some don't document parameters at all. When a patient returns for session 2 of a 6-session protocol, the treating technician (who may not be the original tech) cannot reliably reproduce the exact settings from session 1.

## Why It's Still Broken
Each device manufacturer uses different parameter terminology and measurement units. There is no standard parameter documentation format across laser types. EHR SOAP notes are free-text fields that don't enforce structured parameter entry. Technicians are trained on the device but not on documentation standards, and the time pressure of a 30-minute treatment slot leaves little room for careful charting. The result is a documentation crisis that only becomes visible when outcomes vary or adverse events occur.

## What a Fix Looks Like
Device-specific structured documentation templates within the EHR that prompt for each parameter by name, with valid ranges and defaults pre-populated. Technician selects the device being used, and the template adapts to show that device's parameter set. Historical parameters from previous sessions auto-display for returning patients. Deviation alerts when a technician enters parameters outside the protocol range. Outcome linkage to connect parameter sets with treatment results over time.

## Who Feels the Pain
Laser technicians who cannot confidently reproduce a previous session's settings, and clinic directors responsible for adverse event investigations where treatment parameters were poorly documented.

## Impact If Fixed
Ensures treatment reproducibility across technicians and sessions, reduces adverse event risk from parameter errors, and enables data-driven protocol optimization by connecting documented parameters to outcomes.
