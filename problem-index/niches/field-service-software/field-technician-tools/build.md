# The Visit Record That Writes Itself in the Driveway

**Niche:** [[niches/field-service-software/field-technician-tools/profile|Field Technician Tools]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A technician finishes a repair and then spends fifteen minutes describing it to a form, when the photographs, parts scans and a thirty-second spoken summary contain everything the form is asking for.
**Tags:** #transformers #seq2seq #large-language-models #cnns #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor building for technicians is fighting to have the visit record complete before the truck pulls out of the driveway, without the technician typing — and whoever gets time-from-last-task-to-moving lowest takes the technician's loyalty and the owner's account.

## The Problem
The repair is done, the customer is satisfied, and the technician sits in the truck. Now: select the work performed from a picklist, type a description, add the parts used, photograph the equipment nameplate and type the model number, complete the maintenance checklist, add recommendations for the customer, build the invoice, collect payment, get a signature. Fifteen minutes on a good day, four to six times a day, at the end of a physically demanding job. The parts of it that require judgement take thirty seconds; the rest is transcription of things that are visible in photographs already taken or were said aloud to the customer ten minutes ago.

## Why Nobody Has Built This
The technician is not the buyer, so the requirements have come from the people who consume the output — owners wanting complete records, accountants wanting clean invoices, dispatchers wanting equipment data — and each of those requirements became a field. Nobody has been accountable for the total time cost, which is distributed across a workforce and invisible in any system. The enabling technologies have also only recently become good and cheap enough: reliable on-device speech, nameplate reading from a photograph, and structured extraction from a spoken summary are all recent enough that the previous generation of attempts reasonably failed.

## What to Build
A visit record assembled from what the visit produced. The technician speaks a summary — what was wrong, what they did, what the customer should know — for thirty seconds, offline. That plus the photographs taken during the job, the parts scanned as they came off the truck, and the work order's own context yields a completed record: work performed, diagnosis, parts consumed, equipment details read from the nameplate photograph, recommendations, and a draft invoice against the price book. The technician reviews and confirms. The measured objective is the time from the last physical task to the truck moving, reported to the vendor and the customer, because it is the only metric that tells anyone whether this works. Every correction the technician makes improves the extraction, and it should visibly need fewer corrections in month three than in month one.

## Target Customer
Field service platform vendors, and directly the contractors with ten or more technicians for whom an hour a day per technician is a quantifiable and large number.

## Impact If Built
An hour a day per technician, largely recovered, is either capacity for another call or an hour of a person's life returned — and in a trade with a persistent labour shortage, both matter. The second effect is on data quality: the optional fields that technicians currently skip are exactly the ones the diagnosis prediction, equipment history and price book niches all depend on, and they get populated only if populating them is free.
