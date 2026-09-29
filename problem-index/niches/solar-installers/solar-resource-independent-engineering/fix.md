# Loss Assumptions Are the Judgment and They Live in Spreadsheets

**Niche:** [[niches/solar-installers/solar-resource-independent-engineering/profile|Solar Resource Assessment & Independent Engineering]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Fix (Pain Point)
**One-liner:** The difference between two engineers' yield assessments of the same plant is a dozen loss percentages chosen from experience, recorded as numbers in a cell with no reason attached.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #workflow-orchestration #automation #worker-facing

## The Problem
An energy yield model is a chain of losses applied to an incident resource: soiling, shading, mismatch, wiring, inverter efficiency, transformer, availability, curtailment, degradation, and several more. The resource dataset and the simulation software are largely common across the industry. The loss assumptions are not, and they are where two competent engineers assessing the same plant produce materially different answers.

Each assumption is a judgment. Soiling depends on site dust, rainfall pattern, tilt and cleaning regime. Availability depends on the O&M contract and the operator's history. Curtailment depends on the grid node and a view of how congestion will develop. Degradation depends on module technology and climate.

Those judgments are entered as percentages into a model file. The reasoning — which comparable sites the engineer had in mind, what the developer said about the cleaning schedule, why they discounted the manufacturer's degradation warranty — is not recorded anywhere. The report states the assumption; it rarely states the basis, and never states what evidence would change it.

Three things follow. Consistency is unknown: the firm cannot say whether its engineers assume the same things for comparable sites, because there is no queryable record of assumptions. Defensibility is weak: when a lender's technical adviser challenges a soiling assumption, the answer is reconstructed from memory. And succession is a live risk: the senior engineers whose assumption-setting is the firm's actual product are the scarce resource in a growing market, and what they know leaves with them.

## Why It's Still Broken
Nobody bills for writing down reasoning. Assessments are fixed-fee and time-pressured — a condition precedent to a closing with a date — and every hour documenting rationale is an hour not on the next job.

The model file is the deliverable's substrate, and spreadsheets and simulation packages have a cell for a number and no field for why. The tooling shaped the practice.

And there is a quiet reluctance to be pinned down. An assessment is a professional opinion delivered into a transaction with adverse parties; an explicit record of the basis for each assumption is a document that can be argued with. That instinct also prevents the firm demonstrating that its assumptions are consistent and evidence-based, which is what would distinguish it.

## What a Fix Looks Like
**Make assumptions structured objects.** Each loss assumption stored with its value, the site attributes it was based on, the comparable projects referenced, the evidence source, and a one-line rationale. This is a template change to a workflow that already exists.

**Build the comparables library.** Engineers reason from similar sites constantly. A queryable record of what was assumed for what kind of site — and, once the validation record exists, how those assumptions performed — is useful from the first week, which is what determines whether anyone uses it.

**Report assumption distributions across the practice.** What soiling loss do our engineers assume for arid sites with no cleaning contract, and how wide is the spread. That single report tells a firm whether it has a house standard or a set of individual habits.

**Close the loop where operations data exists.** For plants the firm monitors, compare assumed soiling, availability and degradation to measured values. This is the same infrastructure the validation work needs and it makes each assumption individually testable.

**Give it to the junior engineers.** The system succeeds when someone with three years of experience can see what the practice has assumed for comparable sites and why, and bring the senior engineer a defensible draft rather than a blank model.

## Who Feels the Pain
Senior engineers, who are the bottleneck on every assessment and whose judgment is the firm's product; junior engineers, who learn assumption-setting by apprenticeship in a market growing faster than the profession; lenders, who receive a loss stack with no stated basis and cannot distinguish a well-founded assumption from a habitual one; and the firm, whose consistency is unmeasured and whose expertise walks out at retirement.

## Impact If Fixed
The loss stack is where an energy yield assessment is actually made, and it is the least documented part of a document that hundreds of millions of dollars of financing rests on. Structuring it makes consistency measurable, makes assumptions defensible in the technical negotiation that follows every assessment, and creates the record without which no validation of the firm's forecasts is possible.
