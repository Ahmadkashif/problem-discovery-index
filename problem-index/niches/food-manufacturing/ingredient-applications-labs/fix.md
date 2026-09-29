# Seven Years to Make a Flavourist and Nothing Written Down

**Niche:** [[niches/food-manufacturing/ingredient-applications-labs/profile|Ingredient Applications Laboratories]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** The house's product is the judgment of a few hundred people trained by apprenticeship, and the reasoning behind every formulation they build is unrecorded.
**Tags:** #tacit-knowledge-ml #large-language-models #evaluation-metrics #worker-facing #workflow-orchestration

## The Problem
Flavour creation is one of the last genuine apprenticeship professions. A flavourist trains for years under a senior, learning a palette of hundreds of materials, what each does in combination, how each behaves under heat and acid and time, and how to move a profile from where it is to where the brief wants it.

What that training produces is judgment: this brief needs a top-note lift rather than more of the character material; this off-note is coming from the oxidation of that one, not from the base; this will fall apart in a UHT process regardless of what the accelerated stability says.

The formulation records the ratios. It does not record why the flavourist went that way, what they tried first, what the off-note was diagnosed as, or what they would change if the customer pushed on cost. That reasoning is transmitted by standing next to someone for years and by nothing else.

The exposure is acute and widely acknowledged in the industry. The senior bench is ageing, training pipelines are long and narrow, and demand for reformulation work — sugar reduction, sodium reduction, clean label, ingredient replacement — is rising faster than the profession can grow. Every retirement removes a palette that took decades to build.

The nearer-term cost is that juniors solve problems seniors solved twenty times, and nobody can find the twenty.

## Why It's Still Broken
The output format was fixed by the craft. A formulation is a list of materials and quantities because that is what gets made, and every downstream system is satisfied by it.

Bench time is the scarcest resource in the building, and documenting reasoning competes directly with working the brief queue.

There is also a genuine professional scepticism that the judgment is articulable at all — a belief that flavour creation is intuition that cannot be written. It is partly true at the top of the range, and it has been allowed to excuse recording nothing anywhere else, including for the routine matching and reformulation work that is most of the volume.

And the material is commercially explosive. A structured record of how the house builds its most successful profiles is the crown jewels in a form that could walk out on a laptop.

## What a Fix Looks Like
**Capture the move, not the essay.** At each significant iteration: what was wrong, what change was made, what it was intended to fix, and whether it worked. Three fields at the bench, on iterations that already take hours.

**Record diagnoses of off-notes as a controlled vocabulary.** Off-note diagnosis is the most repeated and most teachable judgment in the lab, and it is currently free text or verbal.

**Build retrieval over prior briefs by problem, not by customer.** "Show me how we have solved a bitterness masking problem in a dairy base" is the question a junior actually has, and it is unanswerable today.

**Pair capture with mentorship, not compliance.** Seniors will record reasoning if the artefact is visibly a teaching tool for their own team, and will not if it reads as an extraction exercise. This determines whether the programme survives contact with the bench.

**Treat security as a first-order design problem.** Access controls, no bulk export, audit trails. The reason this has not been built is partly that nobody wanted to create the file, and that concern deserves an engineering answer rather than avoidance.

**Feed it upward.** The reasoning record is the supervision for any retrieval or suggestion layer over the formulation library, and no such layer is possible without labelled examples of how ambiguous briefs were actually resolved.

## Who Feels the Pain
Senior flavourists, who are the product, are ageing, and cannot be in two briefs at once; juniors, learning by proximity in a profession with a seven-year runway; customers, who wait through iterations that repeat work the house has done before; and the house, whose competitive asset is a set of careers.

## Impact If Fixed
This is the largest tacit-knowledge concentration found anywhere in the vault outside medicine and law, in an industry where reformulation demand is rising and the trained population is not. Structuring the reasoning shortens apprenticeship, makes the routine two-thirds of the queue faster, and preserves a palette that currently retires one person at a time.
