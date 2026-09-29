# Buy: Breach Simulation Coverage for a Human Team

**Niche:** Red Teaming & Adversary Simulation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Breach and attack simulation platforms already execute technique libraries and report detection coverage automatically, and human red teams — who go far deeper — report a story.
**Tags:** #evaluation-metrics #confidence-intervals #graph-theory #change-point-detection #data-integration #automation #workflow-orchestration
**Contested on:** Whether the exercise reflects how a real adversary would behave against this organisation, or how this particular red team habitually operates.

## The Problem

An entire product category already solves the measurement half of this problem. Breach and attack simulation platforms run libraries of adversary techniques against a live environment, continuously, and report which were detected, which were blocked, and which passed unnoticed — mapped to ATT&CK, trended over time, with coverage gaps identified.

Their limitation is well understood: they execute a catalogue. They do not improvise, do not chain novel paths, do not reason about this specific organisation's architecture, and do not do the creative work that makes a human red team valuable.

Human red teams have the opposite profile. They do all of the creative work and produce none of the measurement. The two capabilities are complementary to an unusual degree and are sold as substitutes, with the simulation vendors positioning against consultancies and the consultancies dismissing simulation as checkbox automation.

What nobody offers is the human exercise with the platform's instrumentation — the depth of a real operator with the coverage reporting of an automated one.

## What Already Exists

Breach and attack simulation: SafeBreach, AttackIQ, Cymulate, Picus Security, Pentera and Mandiant Security Validation. Technique libraries mapped to ATT&CK, automated execution, detection outcome measurement joined to the client's security stack, coverage trending and gap reporting.

Adversary emulation: MITRE's own emulation plans, Atomic Red Team's open technique library, Caldera for automated adversary emulation — all providing structured technique definitions with execution and detection guidance.

Command and control: Cobalt Strike, Mythic, Sliver and Brute Ratel, which produce detailed operational logs already.

Purple team tooling: VECTR and similar, built specifically to track attempted techniques against detection outcomes — the closest existing fit and used by a small minority of teams.

Detection engineering: Sigma rules, detection-as-code practices and the SIEM platforms holding the telemetry the join requires.

## The Customization Gap

**The instrumentation assumes the platform is executing.** BAS products measure what they themselves ran. Measuring what a human operator improvised requires parsing the operator's tooling output and inferring technique from behaviour, which no BAS vendor has built because it is not how their product works.

**VECTR is the right shape and the wrong scale.** Purple team tracking tools capture attempts and outcomes properly and require manual entry, which is exactly the adoption barrier that kills them in a covert engagement. Automating the capture from C2 logs is the missing piece.

**Detection joining is done manually and should not be.** BAS platforms integrate with the SIEM and correlate automatically. A human exercise correlates by asking the blue team afterwards. The integration pattern exists and has never been pointed at a human timeline.

**Coverage denominators differ.** BAS reports against its own library. A human exercise needs coverage against an intelligence-derived adversary profile, which is a smaller, more defensible and more meaningful denominator that no product currently constructs.

**The commercial positioning is adversarial.** BAS vendors sell against consultancies and vice versa, which has prevented the obvious combination. A firm using BAS instrumentation to measure its own human exercises is admitting the platform does something it cannot, which is a positioning problem rather than a technical one.

**Covert exercises resist telemetry access.** Joining to the client's SIEM during a covert engagement risks revealing the exercise. The join has to happen after the fact, which is workable and requires the red team's timeline to have been captured precisely enough to correlate.

## Target Customer

AttackIQ, Picus or SafeBreach could offer an instrumentation layer for human engagements, extending their platform into the services market and giving their measurement capability a depth argument it currently lacks.

The C2 framework vendors are the more interesting adapter, because they already hold the operational log and adding technique classification and export is a natural feature for the tooling operators already run.

Buyers are red team practices, and detection engineering leadership on the client side who want the coverage view and currently have to choose between depth and measurement.

## Impact If Solved

The two halves of adversary simulation stop being sold as alternatives. Depth and measurement are complementary, and a combined offering is strictly better than either.

Automated capture from C2 logs removes the adoption barrier that has kept purple team tracking a minority practice, since the objection has always been the manual bookkeeping rather than the value.

And an intelligence-derived coverage denominator would give the category a realism claim it can actually support, replacing the assertion that the exercise simulated a capable adversary with a statement of which adversary's behaviours were exercised and which were not.
