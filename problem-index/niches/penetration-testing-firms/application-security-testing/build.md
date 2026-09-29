# Build: Testing What the Pipeline Cannot See

**Niche:** Application Security Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A methodology and toolset for the authorisation and business logic flaws no scanner will ever find, so manual testing stops duplicating the pipeline and starts covering what only a human can.
**Tags:** #graph-theory #large-language-models #markov-decision-processes #evaluation-metrics #confidence-intervals #transfer-learning #automation #tacit-knowledge-ml
**Contested on:** Whether assessment can keep pace with a codebase that ships daily, or whether a point-in-time test is obsolete before the report is written.

## The Problem

The economics of application testing have shifted and the practice has not. A decade ago a manual tester finding injection flaws and misconfigurations was providing something the client's tooling could not. Today those classes are increasingly caught in the pipeline, continuously, for the cost of a CI job. A manual engagement that spends its first week rediscovering them is selling work the client already owned.

What is left is the part that has not been automated and mostly cannot be: authorisation flaws, where the question is whether this user should be able to reach this object and the answer depends entirely on what the application means. Business logic abuse, where every individual request is valid and the sequence is the attack. Workflow state manipulation. Chains of individually harmless weaknesses. Multi-tenancy boundary failures. These are consistently the highest-impact findings in any serious assessment and the ones no scanner will ever produce, because they require knowing what the software is for.

And they have no methodology. Injection testing has decades of technique, checklists and tooling. Business logic testing has "think like an attacker", which is not a method. Whether a given engagement finds the authorisation flaw depends on whether that tester happened to imagine that particular misuse in the time available — which makes the most valuable part of the work the least systematic and the least reproducible.

## Why Nobody Has Built This

**It is believed to be pure craft.** The prevailing view is that logic testing is irreducible intuition and cannot be systematised, which is partly true and is used to justify not trying. Much of what good testers do is in fact enumerable — they work through role-object matrices, state machines and workflow sequences — and nobody has written it down as a method.

**The enumeration explodes.** Authorisation testing across roles, objects, actions and states is combinatorially large, and testing all of it is impossible. Prioritising it requires knowing which combinations matter, which requires understanding the application's semantics — the hard part.

**Semantics have to come from somewhere.** A tool needs to know that this endpoint transfers money and that one changes a display preference. That understanding lives in code, documentation and the tester's head, and extracting it reliably has only recently become plausible.

**Firms are not incentivised to expose the duplication.** A methodology that separates what the pipeline already caught from what only a human found would show clients exactly how much of the engagement was redundant. That is the right thing to show and it shortens engagements.

**False positives are ruinous here.** A tool that reports a hundred candidate authorisation flaws of which three are real destroys the tester's time and trust. Precision matters far more than recall, which is the opposite of how scanner design usually optimises.

## What to Build

**Extract the application's semantic model.** Roles, objects, actions, state transitions and the workflows that connect them, derived from API specifications, code, existing tests and documentation, with the tester correcting and enriching it. This model is the foundation and is what every subsequent capability depends on.

**Generate and prioritise the authorisation matrix.** Every role against every object and action, with the combinations ranked by consequence — which requires understanding which objects are sensitive, inferable from naming, data flow and the tester's input. Present the tester with a ranked list of untested combinations rather than an exhaustive grid, and track which were exercised, which feeds directly into [[niches/penetration-testing-firms/coverage-measurement/profile|🎯 Coverage Measurement]].

**Model workflows as state machines and probe the transitions.** Business logic abuse is usually a legal transition taken out of order, repeated, or from an unexpected state. Deriving the intended state machine and systematically attempting invalid transitions is a method, and it is one the best testers approximate by hand.

**Diff against the last engagement.** What changed in the application since the previous assessment — new endpoints, changed roles, modified workflows — so a repeat engagement concentrates where the risk is new rather than re-walking stable code. This is straightforward given repository access and would substantially improve repeat-engagement value.

**Separate pipeline-findable from human-only, explicitly.** Run the client's own tooling classes first, mark everything they would have caught, and report the engagement's findings split into what the pipeline already reported, what the pipeline could have caught and did not, and what no tooling would ever find. The third category is what the client is actually paying for and no report currently isolates it.

**Emit regression tests.** Each logic finding rendered as a test the client can run in their pipeline forever. This is the mechanism that stops class recurrence and is a natural deliverable that almost nobody produces.

## Target Customer

Specialist application security firms, whose testers are strongest at exactly this work and who need a way to demonstrate that they are selling something the pipeline cannot supply.

Application security leadership at organisations with mature pipelines, who are the ones already asking why they are paying for a manual test that reports what their scanners reported last Tuesday.

## Impact If Built

Manual testing moves to where it is irreplaceable. Every year the automatable portion grows, and a profession that does not explicitly relocate to the non-automatable part is selling a shrinking product at a falling price.

The highest-impact finding class gets a method. Authorisation and business logic flaws currently depend on whether one person imagined one scenario in two weeks, which is an unacceptable amount of variance for the most consequential part of the work.

And the three-way split of findings would let clients see what they are actually buying, which is the honest basis for a market where deep testing costs more than shallow testing and currently cannot prove it.
