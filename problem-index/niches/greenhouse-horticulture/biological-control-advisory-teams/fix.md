# The Programme Is the Advisor's Judgment and It Is Recorded as a Release Rate

**Niche:** [[niches/greenhouse-horticulture/biological-control-advisory-teams/profile|Biological Control Field Advisory Teams]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** An experienced advisor reads a house and adjusts a programme; what they read and why is not written down, and the industry is short of advisors.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #workflow-orchestration #worker-facing #automation

## The Problem
The release programme that leaves a greenhouse visit is a set of numbers — species, quantity, interval. Behind it is a judgment: this house has a ventilation pattern that concentrates pressure at the south end, this grower sprayed something three weeks ago that will suppress the predators, this crop is two weeks behind and the pest curve will overtake it, this operation will not follow a programme requiring three interventions a week.

None of that survives the visit. The order records what was released. The visit note may record a sentence. The reasoning stays with the advisor.

The industry cannot afford this. Skilled biological control advisors take years to develop — the work sits between entomology, crop production and customer management — and demand is growing faster than supply as protected cropping expands and chemical options narrow. Advisors are recruited aggressively between suppliers, and accounts move with them for exactly the reason the knowledge is undocumented.

Day to day it shows up as fragility. A house covered by a stand-in gets a programme built from records that hold rates but not context. A grower whose advisor leaves receives worse advice for a season. And a new advisor cannot learn from the most instructive two hundred decisions the practice made last year, because those decisions exist only as orders.

## Why It's Still Broken
Advisors are field staff whose day is full of houses, and documentation competes with visits during the weeks when pest pressure is actually moving.

The systems were built to move product. An order line has a species and a quantity; there is no field for why this rate rather than half of it.

And the same quiet leverage problem appears here as in agricultural retail: an advisor whose house knowledge is captured in the employer's system is easier to replace, and every advisor understands that without saying it.

## What a Fix Looks Like
**Make the house the record.** A greenhouse page accumulating structure, ventilation and climate quirks, spray history, grower constraints, past programmes and how they performed — across seasons and across advisors.

**Capture the adjustment reason, not an essay.** When a programme deviates from the standard for the crop and pressure level, one structured line: what drove it, and what would change it. Seconds, at the point the programme is already being written.

**Record the pesticide history explicitly.** Residual chemistry is the single most common cause of biological programme failure and it lives in the grower's memory and the advisor's. Making it a first-class field on the house record fixes the most diagnosable failure in the business.

**Give the advisor better recall than their own.** Searchable house history on a phone, between visits, is what makes the habit stick. Every attempt at documentation that serves head office first has failed in this industry and will again.

**Use it to onboard.** A new advisor inheriting structured house histories reaches competence in a season rather than three, which is the industry's binding constraint on growth.

**Feed it into establishment scoring.** Programme reasoning plus outcome is what turns thousands of commercial releases into evidence, which is the analytical work the company cannot start without it.

## Who Feels the Pain
Advisors covering unfamiliar houses from order records; growers whose programme quality resets when their advisor changes employer; new hires rebuilding context the supplier already paid for; and the supplier, whose entire differentiation against a competitor selling near-identical insects is advice it cannot institutionalise.

## Impact If Fixed
The supplier's moat is advisory quality in a workforce that is scarce, mobile and undocumented. Making the greenhouse the unit of record turns individual expertise into an institutional asset, shortens the onboarding that constrains growth, and supplies the context layer without which release outcomes cannot be interpreted at all.
