# Field Ticket and Service Report Documentation

**Industry:** [[oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Field techs spend 45-90 minutes per day transcribing handwritten notes into service tickets — a solved problem in other industries, but oilfield terminology and multi-party billing make generic dictation tools useless.
**Tags:** #llm #speech-recognition #text-generation #nlp #automation

## The Problem
After every wellsite visit, field technicians must document what they found, what they did, parts consumed, and hours worked. This information flows into billing (operator pays service company), maintenance history, and regulatory records. Most techs scribble notes on paper tickets in the field, then transcribe them into FieldFX or a similar system hours later — often at the end of a 12-hour shift. Details get lost, part numbers are wrong, and billable hours are under-reported because techs cannot remember exact arrival/departure times.

## What Already Exists
General-purpose voice-to-text tools (Otter.ai, Google Dictation, Apple Dictation) can transcribe speech, and field service platforms like ServiceMax offer mobile entry. However, none of these understand oilfield-specific terminology — "stuffing box," "polished rod," "tubing hanger," "ESP intake," "chemical batch treat" — or the multi-party billing structure where a single visit may be split across an operator, a working interest partner, and a rental equipment provider. Generic NLP also cannot distinguish between a tech describing what they observed versus what they did, which maps to different fields in the service ticket.

## The Customisation Gap
The solution needs an oilfield-specific speech recognition vocabulary trained on field tech language (including regional dialect variations between Permian Basin, Bakken, and Eagle Ford crews). It must auto-populate structured fields: well name/API number, equipment serviced, failure mode, parts used (mapped to vendor catalogs), labor hours (auto-captured via GPS arrival/departure), and the correct billing split. It must also flag when a described activity triggers a regulatory reporting requirement (e.g., a fluid spill above the reportable threshold).

## Impact If Solved
Reclaims 30-60 minutes per tech per day in documentation time, reduces billing disputes by 25-40%, and creates a complete, searchable maintenance history for every well — which in turn feeds the predictive maintenance models that depend on accurate historical records.
