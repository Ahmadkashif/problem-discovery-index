# Red Teaming & Adversary Simulation

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Low Digitized
**Contested on:** Whether the exercise reflects how a real adversary would behave against this organisation, or how this particular red team habitually operates.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Very low — bespoke, unrecorded, narrated afterwards
**Target Buyer:** CISOs, detection engineering leadership, board-level security sponsors
**Automation Potential:** Moderate — instrumentation automates, the adversary judgement does not

## What Makes This a Distinct Niche

Red teaming is sold as an answer to a different question from penetration testing. A test asks what weaknesses exist; a red team asks whether this organisation would detect and stop a capable adversary pursuing a specific objective. The deliverable is a narrative of how the objective was achieved and what the defenders saw.

The contest is over whether the exercise is representative. A red team's approach is shaped by the operators' own tooling, tradecraft and habits — the loaders they have built, the techniques they are good at, the paths they have used successfully before. That is not a flaw in any individual team; it is what expertise looks like. But it means the exercise measures detection of *this team's* tradecraft, and the client generalises the result to adversaries in general.

The gap is invisible because nothing is measured. What techniques were attempted? Which produced telemetry? Which produced an alert nobody actioned? Which were never tried? The exercise is narrated rather than instrumented, so the client learns that the red team got in — which they almost always do — and very little about the shape of their detection coverage.

Every serious competitor is fighting over realism, and none can demonstrate it. A firm that could show which adversary behaviours it exercised, which the client detected, and which were never tested would be selling something the category currently cannot.

## Current Tools & Gaps

Command and control frameworks — Cobalt Strike, Mythic, Sliver and bespoke implants — plus the operator's own tooling. MITRE ATT&CK is used widely for after-the-fact labelling of what was done. Purple team exercises, where the red and blue teams work together and attempts are logged deliberately, are the most instrumented form of this work and are a minority of engagements. Breach and attack simulation platforms automate technique execution continuously and are sold as products rather than services.

The gaps are the same as elsewhere in this industry and sharper here. Attempts are not logged systematically, so the denominator is missing entirely — nobody knows which techniques were tried and failed versus never tried. Detection outcomes are reconstructed from the defenders' recollection rather than joined to the red team's own timeline. Threat intelligence about which adversaries actually target this sector rarely shapes the tradecraft, so the simulated adversary is generic. And no firm can report whether a client's detection coverage improved between one exercise and the next, because neither exercise produced a comparable measurement.

## Problems

- [[niches/penetration-testing-firms/red-teaming/build|🔨 Build: The Instrumented Exercise]]
- [[niches/penetration-testing-firms/red-teaming/buy|🛒 Buy: Breach Simulation Coverage for a Human Team]]
- [[niches/penetration-testing-firms/red-teaming/fix|🔧 Fix: The Adversary Is the One the Team Knows How to Be]]
