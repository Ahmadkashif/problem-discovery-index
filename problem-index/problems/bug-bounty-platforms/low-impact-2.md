# Scope Ambiguity and Severity Disputes

**Industry:** [[bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Scope is prose, severity is judgement, and both are decided after the researcher has done the work.
**Tags:** #bert #large-language-models #gradient-boosting #confidence-intervals #bayesian-inference #evaluation-metrics #compliance #k-nearest-neighbors

## The Problem
A programme's scope is a policy document listing in-scope assets, out-of-scope assets, prohibited testing methods and excluded vulnerability classes. It is written in prose, it does not anticipate every case, and the ambiguities are resolved after a researcher has submitted — by the programme, whose interest is in paying less.

Severity is the larger dispute. Standard scoring frameworks provide a vocabulary and leave substantial judgement in the inputs, so the same finding can be rated differently by different programmes and by the same programme in different months. Payment brackets attach to severity, which means every judgement call is a money decision made unilaterally by one party.

Researchers experience this as arbitrariness, and the perception is not unfounded: there is no external calibration, no appeal to an independent standard, and the platform's position between the parties is commercially closer to the programme paying the fees.

The asymmetry is structural. The researcher does the work first and learns the terms afterwards, which is an unusual arrangement in any labour market and is accepted here because the alternative is not participating.

## What Already Exists
Platforms provide scope definition tooling and policy templates. Standard scoring frameworks are widely used. Mediation processes exist on the major platforms and are invoked in disputes. Researcher reputation and programme reputation are both visible, which creates some reciprocal pressure. Some programmes publish their severity rubrics with examples, which is the best current practice and is uncommon.

## The Customisation Gap
Scope should be checkable before the work, not after. A researcher able to submit a proposed target and receive a scope determination — in scope, out of scope, or genuinely ambiguous and therefore escalated for a human decision before testing — removes most scope disputes at their source. The determination is a classification over a policy document and a target description, and it is not built anywhere.

Severity calibration is the platform's natural role and its unique capability. It sees how comparable findings were rated across thousands of programmes, which supports a reference rating with a range — this class of finding in this context is typically rated here. A programme rating well outside the range is doing something unusual and both parties should be able to see that, which converts a unilateral judgement into a discussion with a reference point.

Ambiguity should be identified proactively. Where a policy is silent or unclear, and where researchers have repeatedly submitted things the programme rejects on scope, the platform can see the pattern across programmes and tell the programme its policy is producing disputes — which is useful to a programme manager who does not know their policy is unclear.

And the decisions should be recorded as precedent. A programme's own history of scope and severity determinations is the fairest available standard for future decisions and is currently not retained in usable form.

## Impact If Solved
Scope and severity disputes are the main source of grievance in the researcher community and a persistent drag on programme reputation, which determines the quality of attention a programme receives. Pre-work scope determination removes most of them; cross-programme severity calibration gives both sides a reference instead of an assertion; and precedent makes a programme consistent with itself, which is the minimum researchers are asking for.
