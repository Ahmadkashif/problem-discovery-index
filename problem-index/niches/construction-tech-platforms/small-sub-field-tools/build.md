# The One-Minute Shift Record

**Niche:** [[niches/construction-tech-platforms/small-sub-field-tools/profile|Small Subcontractor Field Tools]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every field product for small subcontractors asks a foreman for five minutes at the end of a twelve-hour shift, which is why every field product for small subcontractors is abandoned in the second month.
**Tags:** #transformers #seq2seq #large-language-models #evaluation-metrics #confidence-intervals #automation #worker-facing #quick-win
**Contested on:** Every serious competitor selling to small subcontractors is fighting to let a foreman with dirty hands and a phone record what happened in under a minute, from a site with no signal — and whoever gets that interaction shortest takes the account.

## The Problem
A foreman finishes at five. He has a phone in a pocket, hands that are not clean, and a truck to load. The app wants crew names, hours, work performed, quantities, photos, safety observations and a weather note, across seven screens with dropdowns. He does the first two fields, which payroll requires, and skips the rest. The owner receives hours and nothing else, so the job costing that would tell him whether this week is profitable is impossible, and he finds out at closeout. Every vendor's answer to this has been a better-designed form, and the form is the problem.

## Why Nobody Has Built This
Products in this segment are built by people who design for a screen, and the design target — under sixty seconds, one-handed, possibly with gloves, possibly with no signal — is so constraining that it eliminates most of what a product manager wants to collect. Vendors also sell to the owner, who wants data, rather than to the foreman, who will decide whether the product lives; so the requirements come from the buyer and the usage comes from someone else. And the technical enablers that make a sixty-second record possible — good speech recognition, on-device processing, offline-first sync — have only recently become cheap enough to assume.

## What to Build
A shift record whose primary input is thirty seconds of speech. The foreman says what happened in his own words, offline, on the walk to the truck. On-device transcription and structured extraction turn it into crew, hours, location, work performed, quantities where mentioned, and any issue raised, and present it as a filled-in record to confirm with one tap. Photos taken during the day are attached automatically by time and location rather than being selected. What was not said is inferred from the crew's assignment and yesterday's record rather than asked. Anything genuinely required and genuinely absent is one question, not seven. The product's own success metric is the median time from opening to confirmed, and it should be visible to the vendor and to the customer, because it is the only number that predicts whether this segment keeps using anything.

## Target Customer
Subcontracting businesses of 5-50 people across every trade, and the field platform vendors who have repeatedly lost this segment to abandonment.

## Impact If Built
A foreman who actually records the shift gives the owner weekly job costing instead of closeout accounting, which is the difference between correcting a losing job and discovering one. For the segment as a whole it is the first credible answer to a decade of failed adoption, and the constraint it accepts — sixty seconds, spoken, offline — is the one every previous attempt refused.
