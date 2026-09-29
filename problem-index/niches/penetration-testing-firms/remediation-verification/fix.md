# Fix: The Same Finding Every Year

**Niche:** Remediation Verification
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The annual test finds the same class of weakness it found last year in a different place, everyone notices, and nothing in the engagement is structured to say so.
**Tags:** #evaluation-metrics #survival-analysis #confidence-intervals #hypothesis-testing #worker-facing #compliance
**Contested on:** Whether a firm can demonstrate that its findings get fixed, that the fixes hold, and that the same weakness class stops recurring.

## The Problem

A tester returns to a client they tested last year. They find access control flaws in three new endpoints. Last year they found access control flaws in four different endpoints, which were fixed. The year before, five.

Every instance was remediated. The remediation rate looks excellent. And the organisation has learned nothing, because it fixed instances rather than the pattern that produces them — no framework-level authorisation control, no test in the pipeline, no change in how new endpoints get built. Next year there will be more.

The tester sees this immediately. It is one of the clearest and most useful observations available from repeat engagement, and there is nowhere to put it. The report format is a list of findings for this engagement. The engagement was scoped as an assessment of the current state. There is no section for "this is the third consecutive year of the same class", no metric that captures it, and raising it in the debrief depends on whether this particular tester worked the previous engagements and remembers.

So the client receives an annual list, closes it diligently, reports a strong remediation rate to their board, and pays for the same discovery indefinitely. The thing they most need to hear is the thing the engagement structure cannot say.

## Why It's Still Broken

**Engagements are scoped as snapshots.** Each test is independently commissioned and independently reported. Longitudinal analysis is not in scope, not in the fee, and not in the template, even when the same firm has done all five.

**Findings are prose, not classified data.** Without a consistent taxonomy applied at authoring time, comparing this year's findings to previous years means reading old reports. Nobody does, so the comparison never happens.

**Tester continuity is accidental.** Whether anyone notices the pattern depends on staffing. Firms rotate testers deliberately for fresh perspective, which is a real benefit and has the side effect of destroying the institutional memory that would catch recurrence.

**Remediation rate is the metric everyone likes.** Instance closure looks good for the client's security team, good for the firm, and good in a board pack. Class recurrence looks bad for everyone, which is why nobody computes it.

**The diagnosis points away from the firm's product.** The fix for recurrence is engineering process change — secure defaults, framework controls, pipeline tests — not more penetration testing. A firm surfacing it is recommending something it does not sell, which is admirable and commercially awkward.

**Naming it sounds like criticism.** Telling a security team their organisation has not learned in three years is a difficult message to deliver to the person who commissioned you and will decide on next year's engagement.

## What a Fix Looks Like

**Classify findings at authoring.** CWE or an equivalent taxonomy, applied by the tester as they write, taking seconds. This is the enabling step: without it no longitudinal analysis is possible, and with it the analysis is almost free.

**Add a recurrence section to every repeat engagement.** Classes seen in prior engagements with this client, whether they recurred, in new locations or old, and the trend. Three lines and a table. It is the most valuable page in the report for any client who has been tested more than once.

**Report two metrics, not one.** Instance remediation rate, which the client already has and likes, alongside class recurrence, which they do not have and need. Presenting both together makes the point without requiring anyone to deliver an accusation — the numbers say it.

**Distinguish regression from recurrence explicitly.** A fix that did not hold is a different problem from a class appearing somewhere new. The first is a remediation quality issue; the second is a development process issue. They need different recommendations and are currently conflated.

**Recommend the systemic fix and price it.** Where a class recurs, the finding is the pattern, and the recommendation should be the framework control, the secure default or the pipeline test that prevents the whole category. Firms are well placed to advise on this and consistently under-sell it because it is not a testing engagement.

**Carry the memory in the system, not the person.** Tester rotation is good practice and the institutional memory should not depend on it. A classified finding history per client, surfaced to whoever is assigned this year, gives the fresh tester the longitudinal view without compromising the fresh perspective.

## Who Feels the Pain

The client, paying annually to rediscover a category of weakness their process keeps producing, while their metrics tell them they are doing well.

The security engineer, who often suspects the pattern, lacks the evidence to make the case for a framework-level change, and would be handed exactly that evidence by a recurrence section.

The tester, who sees it clearly, has nowhere to record it, and watches the same engagement repeat.

And the firm, which is leaving its most differentiated advice unsaid and its most valuable analysis undone, because the report template has no room for it.

## Impact If Fixed

Classifying findings at authoring is nearly free and unlocks every longitudinal analysis in this niche. It is the smallest change with the largest downstream consequence in the whole industry.

A recurrence section converts a repeat engagement from a rediscovery exercise into something that tells the client what their organisation is actually doing wrong — which is a genuinely different product and one worth considerably more.

And reporting recurrence alongside remediation rate makes an uncomfortable truth visible without anyone having to say it out loud, which is usually the only way an uncomfortable truth gets acted on.
