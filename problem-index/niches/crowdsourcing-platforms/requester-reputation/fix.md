# Fix: The Community Built the Rating System the Platform Did Not

**Niche:** [[niches/crowdsourcing-platforms/requester-reputation/profile|Requester Reputation & Trust]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Workers maintain review sites, forum threads and browser extensions to approximate requester reputation, badly, from outside, because the platform publishes nothing.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will publish, or keep relying on volunteers to approximate.

## The Problem

Experienced crowdworkers do not evaluate requesters from the platform. They check a community review site, search a forum thread, or run an extension that overlays community ratings onto the listing page.

That infrastructure is impressive and it is a poor substitute. Coverage is partial, weighted toward requesters somebody complained about. The data is self-reported and unverifiable. The sites go down, get abandoned, or break when the platform changes its markup. Extensions violate terms of service on some platforms and can get a worker's account suspended. And none of it is available to a new worker who has not yet learned it exists — which is exactly the person most likely to work for a bad requester.

Meanwhile the platform holds the verified version of every number these sites attempt to estimate.

## Why It's Still Broken

Publishing exposes paying customers. That is the whole of it.

The existence of the community infrastructure also reduces the pressure, and is occasionally cited as evidence that the need is being met — which mistakes a volunteer workaround for a solution.

And some platforms have actively discouraged the extensions, through terms of service enforcement or markup changes, which is the least defensible position available: preventing workers from assembling the information while declining to provide it.

## What a Fix Looks Like

Publish the verified version, and stop fighting the volunteers in the meantime.

Start with the least contentious numbers. Median time to approval and payment reliability are hygiene facts that no reasonable requester objects to publishing, and they are among the most useful to a worker deciding whether to spend an evening on a batch. Publishing these first establishes the surface with minimal resistance.

Add rejection rate normalised by task type, with uncertainty, after a private period in which requesters see their own figure. Most will not be outliers and the outliers will mostly correct.

Provide an API or a data export so the community tooling can use verified data instead of scraping. This turns an adversarial relationship into a cooperative one, improves the extensions immediately, and costs almost nothing.

Stop enforcing terms of service against reputation extensions. Whatever the general position on automation, tools that help workers evaluate requesters are doing something the platform declines to do, and penalising their users is indefensible.

Credit and incorporate the community data where it covers things the platform cannot measure — requester communication quality, task clarity, whether the requester was helpful. These are genuine subjective judgements and the community collects them better than any platform survey would.

And measure what happens. Batch fill rates and worker retention for requesters above and below the median on the published figures. If good requesters fill faster once the numbers are public, that is the argument that makes the whole thing commercially sensible.

## Who Feels the Pain

New workers, who do not know the community infrastructure exists and are the most likely to work for a requester everyone else avoids. All workers, relying on partial volunteer data that breaks without warning. Volunteers, maintaining public infrastructure for a commercial platform for free. And good requesters, whose conduct is invisible.

## Impact If Fixed

The verified numbers replace the approximations, immediately and for everyone including the newest worker. The community tooling gets better data and stops being adversarial. And the information asymmetry that defines this market — one side fully scored, the other anonymous — starts closing with facts the platform already computes.
