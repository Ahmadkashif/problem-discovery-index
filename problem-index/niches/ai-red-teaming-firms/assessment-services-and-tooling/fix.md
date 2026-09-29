# Findings With No Path to a Fix

**Niche:** [[niches/ai-red-teaming-firms/assessment-services-and-tooling/profile|Assessment Services & Tooling]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A report describes a behaviour a model can be induced into and stops there, leaving an engineering team to work out what to change in a system they cannot retrain.
**Tags:** #worker-facing #evaluation-metrics #compliance #descriptive-statistics #automation #data-integration #quick-win #confidence-intervals
**Contested on:** Not terminal — the contest differs by whether the buyer is purchasing judgement or breadth, and the decomposition is recorded in the profile.

## The Problem
A finding states that under a particular sequence the assistant can be induced to reveal information it should not. The engineering team receiving it does not train the model, cannot change its weights, and is running a third-party API. Their available actions are input filtering, output filtering, prompt changes, retrieval restrictions, permission scoping and monitoring — and the report says none of which apply, in what combination, or at what cost. They implement something, cannot verify it worked, and the finding sits open in a tracker for two quarters. The assessment identified a real problem and delivered nothing the recipient could act on.

## Why It's Still Broken
Red team researchers are specialists in finding, not in the defensive engineering of a system they saw for four weeks. Recommending a specific mitigation means owning whether it works, which firms avoid. The available mitigations depend on the client's architecture, which the engagement may not have examined. And the report's audience is partly a compliance function who needs the finding documented rather than fixed, which lets the actionability gap persist.

## What a Fix Looks Like
Deliver findings that a recipient can act on. State the mitigation options available at this client's architecture — filtering, prompt structure, permission scope, retrieval limits, monitoring — with their expected effectiveness and their cost in latency, false positives and engineering effort, which is the content the recipient needs and is currently absent. Provide a reproduction the client can run themselves, so they can verify a mitigation rather than guessing, which is the single most useful artefact a finding can carry and is cheap to include. Report the finding's success rate rather than asserting it is possible, since a behaviour reachable one time in five hundred and one reachable one time in three are different problems with different responses. Rank findings by what the client can actually change, since a finding that requires retraining a third-party model is not actionable for most recipients and should be separated from those that are. Verify mitigations in a short follow-up rather than in a new engagement, which the revalidation niche develops. Write for the engineering audience separately from the compliance audience, since one needs a change and the other needs a record. And track finding closure rates, because a firm whose findings are never closed is producing documents rather than improvements.

## Who Feels the Pain
Engineering teams holding findings they cannot act on; compliance functions filing documented risks that stay open; and the firms whose real discoveries produce no change in the systems they assessed.

## Impact If Fixed
A reproduction the client can run themselves is the cheapest artefact to include and the one that lets them verify a fix at all. Reporting success rates rather than possibility, and separating findings by whether the client can act on them, is what makes a report a work item.
