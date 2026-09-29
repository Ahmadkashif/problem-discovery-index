# Equipment Asset History Capture

**Industry:** [[field-service-software|Field Service Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform has an equipment record and almost none of them are populated well enough to be useful, because filling one in properly costs a technician ten minutes they are not paid for.
**Tags:** #cnns #object-detection #large-language-models #bert #feature-engineering #evaluation-metrics #transfer-learning #worker-facing

## The Problem
The single most useful fact at the start of a service call is what equipment is there and what has been done to it. Field service platforms all support an equipment record: make, model, serial, install date, warranty status, service history.

In practice these records are thin. Make and model are often blank or wrong. Serial numbers are frequently absent. Install dates are guesses. The reason is simple: capturing them means a technician standing in a cramped mechanical room, in poor light, typing a seventeen-character model number off a faded data plate into a phone, for no immediate benefit to themselves.

So the next technician arrives without knowing what is there, orders the wrong part, and the fix rate suffers. The asset record that would have prevented it was a field nobody filled in.

## What Already Exists
Equipment and asset modules are standard in every platform. OCR from photographs is mature. Manufacturer serial number formats are documented and decodable for major brands. Warranty lookup APIs exist for some manufacturers. Barcode and QR asset tagging is available and used in commercial contexts. IoT connectivity exists on newer commercial equipment.

## The Customisation Gap
The gap is capture effort, and the fix is to remove the typing rather than to add another field. A photograph of a data plate contains the make, model, serial and manufacture date. Reading it reliably requires handling the specific conditions of the job — glare, dirt, angle, faded print, and manufacturer-specific plate layouts that vary by brand and era. Generic OCR gets most of a plate and fails on exactly the characters that matter, which is worse than useless when a model number differs by one digit.

Model-specific enrichment is the second half and is where the value compounds. Once a model is known confidently, the platform can attach the manufacturer's specifications, common failure modes, required parts, warranty status and the vendor's own cross-contractor service history for that model. The technician arrives knowing what typically fails on this unit at this age.

The vendor is the only party positioned to build the model-level failure corpus, because it observes the full service life of every brand across thousands of contractors — something no manufacturer sees beyond its own warranty window.

## Impact If Solved
Equipment identification is the input to parts, diagnosis and warranty recovery, and it is currently missing on a large fraction of records because it costs an unpaid ten minutes. Making it a photograph turns the most under-populated data in the platform into the foundation for everything predictive built on top of it.
