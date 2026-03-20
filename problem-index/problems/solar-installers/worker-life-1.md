# Site Survey Automation and Structural Assessment from Photos

**Industry:** [[solar-installers|Solar Installers]]
**Type:** Worker Life Changing
**One-liner:** Solar site surveyors who photograph roof conditions, measure setbacks, document electrical panel specs, and assess structural suitability in a 45-60 minute site visit — then spend another 30-45 minutes writing up the survey report — get the survey report auto-generated from their photos and measurements, ready for the design team before the surveyor drives away.
**Tags:** #large-language-models #transformers #transfer-learning #attention-mechanisms #evaluation-metrics #automation #worker-facing

## The Problem

The solar site survey is a prerequisite for final system design: the surveyor documents roof condition and dimensions, verifies the electrical panel's capacity for solar interconnection (main breaker size, bus bar rating, available breaker slots), assesses attic access for conduit routing, documents utility meter location, and photographs all relevant installation access points. This information is then manually typed into a site survey form that the design team uses to finalize the system layout and permit package.

The data capture and the report writing are two separate tasks, both done by the surveyor. Photos are taken on-site but not immediately organized. The survey form is filled out from memory or photo review after the visit. The result: 30-45 minutes of administrative work per site visit that adds no new information — it's transcription of what was already captured.

## Why It Matters to the Worker

Surveyors do 3-5 site visits per day in a productive market. Post-visit administrative work takes 1.5-3 hours daily — time that reduces the number of sites they can cover. The best surveyors are limited not by their survey speed but by report writing time. Reducing this bottleneck directly increases survey throughput.

## What a Solution Looks Like

A mobile survey app where the surveyor: photographs the electrical panel (OCR extracts main breaker size, bus bar rating, manufacturer, and model from the panel label); photographs the roof from street level and from each elevation; completes a quick structured checklist (attic accessible: yes/no, utility meter location, roof material condition). The system generates the survey report: panel specs from photo OCR, roof geometry estimate from aerial imagery matched to the address, structural observations from checklist, photos organized by category. Surveyor reviews the auto-generated report in 5 minutes and submits.

## Impact If Solved

Reduces post-survey administrative time from 30-45 minutes to 5-10 minutes per site. Increases survey throughput by 30-40%. Improves report accuracy — OCR-extracted panel specs are more reliable than manually transcribed values from memory.
