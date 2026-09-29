# Counted by Eye off a Yellow Card, Written on a Clipboard

**Niche:** [[niches/greenhouse-horticulture/biological-control-advisory-teams/profile|Biological Control Field Advisory Teams]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The primary measurement in the entire discipline is a human squinting at a glue trap and estimating a number.
**Tags:** #cnns #object-detection #evaluation-metrics #transfer-learning #data-integration

## The Problem
Pest pressure is measured with sticky cards. Yellow or blue rectangles hung in the crop, collected weekly, and counted — by an advisor or a grower's scout, by eye, often in poor light, on a card holding hundreds of insects of several species at several life stages.

Counting a card properly takes real time, so in practice it is estimated. Species are confused, particularly small thrips against small flies. Two people counting the same card produce materially different numbers. Counts drift with fatigue across a long day of houses.

Everything rests on this measurement. The release rate is calculated from it. The decision to intervene chemically is triggered by it. And the surveillance and forecasting value described above is bounded entirely by it, because a forecast built on estimated counts inherits the estimation error.

The card itself is discarded after counting. The evidence is destroyed at the moment of measurement.

## What Already Exists
Insect counting from sticky trap images is an active applied research area with strong published results, and several commercial products offer camera traps or phone-based card counting for greenhouse use. Object detection on small dense targets is a well-served problem class. Some greenhouse climate platforms integrate trap imagery.

The gap is that existing products are built for growers monitoring their own houses, and they target the easy part — total insect count, or one or two headline species. The advisory workflow needs something harder: species-and-stage resolution across the specific complex that matters for biological control decisions, comparable across thousands of houses and dozens of advisors, with confidence attached.

## The Customization Gap
**Species and life stage, not insect count.** The release decision depends on whether the thrips are adults or larvae and whether the whitefly are greenhouse or silverleaf. A general insect counter answers none of the questions that change the programme.

**The taxonomy is regional and crop-specific.** The pest complex in an Ontario pepper house is not the complex in a Dutch tomato house or a Californian cut-flower operation. Models need regional adaptation and a controlled vocabulary the supplier defines.

**Capture must survive a greenhouse.** Hot, humid, high-glare, gloved hands, a phone camera at arm's length, and a card that is curled and partially full. Field conditions defeat products validated on flat, well-lit imagery.

**Confidence has to reach the decision.** An uncertain count should widen the release recommendation, not silently produce a precise-looking number. This is the difference between a counting tool and a decision input.

**Beneficials must be counted too.** The cards catch the released predators as well as the pests, and the ratio is what tells the advisor whether the programme is establishing. Products built for pest monitoring ignore exactly the half that matters here.

**The advisor stays in the loop and their correction is the label.** Advisors will not accept a black box over their own professional judgment, and every correction they make is a training example the supplier alone can collect.

## Target Customer
Technical Director or Head of Digital at a beneficial-insect supplier, owning the advisory workforce and the visit workflow.

## Impact If Solved
Every downstream claim in this business — release rates, establishment, forecasting, regional pressure — rests on a count made by eye off a card that is then thrown away. Making the count consistent, species-resolved and confidence-scored is the precondition for all of it, and it converts the weekly advisory visit from an observation into a measurement.
