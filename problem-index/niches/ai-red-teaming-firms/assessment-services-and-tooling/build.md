# Buying Judgement and Buying Breadth

**Niche:** [[niches/ai-red-teaming-firms/assessment-services-and-tooling/profile|Assessment Services & Tooling]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An expert engagement is bought to find what nobody thought of and an automated platform is bought to cover known ground cheaply and continuously, and firms sell them as one offering to buyers with opposite requirements.
**Tags:** #evaluation-metrics #automation #compliance #descriptive-statistics #workflow-orchestration #confidence-intervals #data-integration #worker-facing
**Contested on:** Not terminal — the contest differs by whether the buyer is purchasing judgement or breadth, and the decomposition is recorded in the profile.

## The Problem
A firm pitches a lab and an enterprise engineering team. The lab has a capable internal red team and wants an outside view, a novel technique, a finding their own people would not have reached — and will pay a great deal for one of those. The engineering team has twenty deployed applications, no specialist staff and a compliance deadline, and wants broad, cheap, continuous testing that stays current. The firm's offering is an engagement with some automation in it, which is expensive breadth for the second buyer and shallow novelty for the first.

## Why Nobody Has Built This
The expertise that finds novel techniques is the same expertise that builds the automated probes, which makes one organisation look natural. Engagement revenue is large per client and platform revenue scales, and both are attractive. But an engagement business staffed for judgement prices badly against a product, and a product business cannot supply the novelty a lab is paying for, and firms attempting both tend to deliver a mediocre version of each.

## What to Build
Build the shared substrate and let the businesses diverge. The genuinely common asset is a maintained technique catalogue with an execution harness — every known attack class, expressed so it can be run automatically, versioned as the field moves — which both halves need and which is the industry's most underbuilt shared infrastructure. Feed novel findings from engagements into the catalogue, so expert work compounds into automated breadth rather than ending in a report, which is the one genuine synergy between the two businesses and is the reason to keep them under one roof at all. Maintain a harm taxonomy alongside it, since findings have to be classified against something to be comparable. Record every probe and outcome in a common schema across both halves, which the corpus niche depends on. Track the catalogue's currency explicitly, since techniques become ineffective as models are updated against them and a stale catalogue is a false assurance. Report which catalogue version an assessment used, so a reader knows what was in scope. Make the harness runnable in a client's environment, since many systems cannot be probed from outside. And be explicit about which business a firm is in, because a lab paying for novelty and receiving a catalogue run will not renew.

## Target Customer
Labs and regulated enterprises buying engagements, engineering teams buying continuous testing, and the firms deciding which of those they are.

## Impact If Built
A maintained, versioned technique catalogue with an execution harness is the industry's most underbuilt shared asset. Feeding engagement findings into it is the one real synergy between the two businesses and is what turns expert judgement into compounding breadth.
