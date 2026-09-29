# Hypothesis Generation From Behavioural Data

**Industry:** [[conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Session recordings and heatmaps generate an endless supply of observations and no way to tell which of them describe a mechanism worth testing.
**Tags:** #k-means-clustering #gradient-boosting #dbscan #bert #graph-neural-networks #evaluation-metrics #dimensionality-reduction #feature-engineering

## The Problem
Hypothesis generation in conversion optimisation draws on session recordings, heatmaps, funnel analytics, form analytics, survey responses and support contacts. The supply of observations is effectively unlimited: watch enough sessions and you will see people hesitate, scroll past things, abandon forms and misread labels.

What is missing is a filter. An observation becomes a worthwhile test only if it identifies a mechanism that plausibly affects enough users to produce a detectable effect, and the tooling provides no basis for that judgement. So test backlogs fill with ideas drawn from a handful of watched sessions, ranked by frameworks that score ideas on subjective impact, confidence and effort estimates supplied by the person who proposed them.

The result is a capacity problem. Test slots are scarce and are spent on hypotheses selected by vividness — the session recording where someone visibly struggled — rather than by prevalence. A behaviour that affects two percent of users cannot produce a detectable result no matter how compelling the recording was.

## What Already Exists
Session replay and heatmapping from Hotjar, FullStory, Contentsquare, Clarity and Quantum Metric are mature and widely deployed, with automated friction detection — rage clicks, dead clicks, error encounters, form abandonment — increasingly built in. Funnel analytics from Amplitude and Mixpanel quantify drop-off by step. Voice of customer tooling supplies survey and feedback input. Prioritisation frameworks such as ICE and PIE are standard practice and are entirely subjective.

## The Customisation Gap
The tools surface individual sessions and aggregate heatmaps; the missing quantity is prevalence attached to mechanism. How many users exhibit this specific behaviour, at what point, and what is their subsequent conversion rate compared with those who do not — that is computable from the same event data and is not how any of these tools present their findings.

With prevalence, prioritisation becomes arithmetic rather than opinion: the maximum possible effect of fixing a behaviour is bounded by how many people it affects, and comparing that bound against the test's minimum detectable effect tells you immediately whether the test is worth a slot. Most proposed tests fail that comparison, which is precisely the discipline the backlog needs.

Clustering behaviour into recurring patterns is the second gap. Sessions that share a friction signature — the same hesitation at the same step, the same repeated interaction — form groups, and identifying the group rather than the individual session converts an anecdote into a quantified population.

And the customisation is that friction signatures are site-specific. A rage click on one interface is frustration and on another is a known interaction quirk, so the detection has to be calibrated against a site's own conversion outcomes rather than against generic definitions.

## Impact If Solved
Test capacity is the binding constraint on an experimentation programme and is currently allocated by how compelling a session recording felt. Prevalence-weighted hypothesis generation, with the possible effect bounded and compared against detectability before a slot is spent, would eliminate most of the backlog and redirect the programme toward the small number of changes capable of producing a measurable result.
