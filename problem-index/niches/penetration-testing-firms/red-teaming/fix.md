# Fix: The Adversary Is the One the Team Knows How to Be

**Niche:** Red Teaming & Adversary Simulation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every red team has a house style, the client's detection is measured against that style, and the result is generalised to adversaries who do not share it.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #compliance #tacit-knowledge-ml
**Contested on:** Whether the exercise reflects how a real adversary would behave against this organisation, or how this particular red team habitually operates.

## The Problem

A red team is a small number of people with particular skills, particular tooling they have built and refined, and particular paths they have found effective. That accumulated preference is expertise, and it is also a signature. The team reaches for the loader they trust, the lateral movement technique they are fluent in, the persistence mechanism they have used for three years.

The client's environment is then measured against that signature. If the team's favourite initial access vector is detected, the client hears they have good coverage. If it is not, they hear they do not. Either way the conclusion is drawn about detection in general, from a sample of one team's habits.

The distortion compounds. A client who engages the same firm annually is progressively measuring their detection against a fixed tradecraft — and if the blue team learns to detect that particular red team, which happens, the improvement is real for one signature and possibly nothing else. Meanwhile the techniques that team never uses have never been tested, in any year, and appear in no report as untested.

The engagement debrief usually acknowledges some of this, honestly. The board slide does not, because the board slide says the red team achieved its objective in nine days and the organisation needs to invest in detection.

## Why It's Still Broken

**House style is indistinguishable from expertise.** A team's preferred techniques are preferred because they work and because the operators are good at them. Asking a team to use tradecraft they are less fluent in produces a worse-executed exercise, which is a genuine trade rather than a simple improvement.

**Nothing records what was not attempted.** Because attempts are unlogged, the space of untried techniques is invisible. The client cannot ask about it because they cannot see it, and the team is not prompted to volunteer it.

**Operator scarcity constrains diversity.** Skilled red team operators are rare and expensive. A firm cannot easily rotate in operators with complementary tradecraft, and small firms have one team.

**The objective-achieved narrative dominates.** Exercises are judged on whether the objective was reached, so operators optimise for reaching it — which means using what works for them, quickly, rather than exercising breadth.

**Threat intelligence is decorative.** Reports often cite an adversary group whose behaviours the exercise supposedly emulated. The actual technique selection is usually driven by what the operators do, with the intelligence framing applied afterwards. Nobody checks the correspondence.

**Clients cannot evaluate it.** A client has no basis to judge whether the tradecraft used was representative, and the firms know more about this than the buyers by a wide margin.

## What a Fix Looks Like

**State the tradecraft profile in the plan, before the exercise.** Which techniques this exercise intends to exercise, selected from intelligence about actors targeting this sector, agreed with the client in advance. This converts an implicit house style into an explicit, reviewable choice, and it is the single most effective change available.

**Report what was not attempted.** A section listing the techniques in the selected profile that the exercise did not exercise, and why — not needed, not feasible, not within the team's current capability. The last reason is uncomfortable and is the most useful thing a client could learn.

**Rotate operators and teams deliberately.** Clients running annual exercises should be advised to vary the team, and firms should rotate operators across repeat clients. This is straightforward, costs little, and directly addresses the fixed-signature problem.

**Check the intelligence correspondence.** Where a report claims to emulate a particular adversary, compare the techniques actually used against that adversary's documented behaviours and report the overlap. If the overlap is thin, the claim should be dropped rather than stated.

**Separate the two deliverables.** The narrative of how the objective was achieved, which is genuinely valuable and belongs in the board conversation, and the coverage statement of what was and was not exercised, which belongs with the detection engineering team. Conflating them is why the board hears a conclusion the exercise does not support.

**Encourage clients to use multiple firms.** Uncomfortable advice for any individual firm, and correct. A client whose detection has been tested by three teams with different tradecraft knows something a client tested three times by one team does not, and honest firms should say so.

## Who Feels the Pain

The client, who draws a general conclusion about their detection posture from a sample of one team's habits, and reports it upward as a general conclusion.

The detection engineering team, who receive findings shaped by what one red team happens to do and build coverage against that, believing it to be broader.

The operators, who know their exercise has a signature and that the result is being generalised beyond what it supports, with no field in which to say so.

And the firms with genuinely broad capability, who cannot demonstrate it against a competitor whose single well-practised path also reaches the objective in nine days.

## Impact If Fixed

Declaring the tradecraft profile in advance costs nothing and converts an invisible bias into a reviewable engagement parameter. Everything else in this section follows from it.

The not-attempted section gives the client the denominator the exercise otherwise lacks, and it is the same fix that works throughout this industry — the value is in naming what was not done.

And separating the narrative from the coverage statement would let the board hear a compelling story and the security team receive an accurate measurement, which are different needs currently served badly by one document.
