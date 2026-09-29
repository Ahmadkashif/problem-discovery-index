# Fix: The Policy Page Is Out of Date

**Niche:** Scope Specification
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Infrastructure changes weekly and the scope page changes annually, so researchers work against a description of an estate that no longer exists.
**Tags:** #evaluation-metrics #change-point-detection #confidence-intervals #compliance #worker-facing #workflow-orchestration
**Contested on:** Whether what counts as in-bounds is machine-checkable before a researcher starts, or a paragraph of prose interpreted after they finish.

## The Problem

A programme's scope page was written when the programme launched and edited twice since. In the meantime the organisation has acquired a company, migrated two services to a different cloud, decommissioned a legacy platform, spun up a dozen new subdomains, and moved a customer-facing application behind a new domain entirely.

The researcher works from the page. They spend a week on a listed asset that was decommissioned in March and is now a parked domain. Or they find something on an asset the organisation acquired last year, which is unquestionably theirs and is not on the page, and the submission is closed as out of scope.

Both outcomes are the same failure: the document describing the programme does not describe the organisation. And both are entirely avoidable, because the security team almost certainly has a more current inventory in their own tooling — it is simply not the artefact the bounty programme publishes.

The programme staff know the page is stale. Updating it is a manual task with no deadline, owned by someone whose main job is triage, and there is no moment at which its staleness causes a visible problem to them. It causes problems to researchers, who are not in the room.

## Why It's Still Broken

**Nobody owns it.** Scope maintenance sits between the security team that knows the assets, the programme manager who runs the bounty, and the infrastructure teams who change things. It is nobody's named responsibility and has no trigger.

**Staleness is asymmetric in cost.** A stale page costs the researcher a week and costs the programme a triage ticket. The party who could fix it bears the smaller share, which is why it stays broken.

**Adding assets means paying for findings on them.** A programme that expands its scope is committing budget. There is a quiet incentive to leave new assets off the page, and it does not require anyone to intend that outcome — it simply means expansion is never urgent.

**Scope changes are not versioned.** When the page is updated, there is no record of what it said before and no rule about which version a submission is evaluated against. A researcher who started work under the old scope has no standing to invoke it.

**Acquisitions are the worst case and the most common.** An acquired company's infrastructure is the organisation's responsibility, is frequently the weakest part of the estate, and is almost never added to the bounty scope promptly.

## What a Fix Looks Like

**Generate the page from the asset inventory.** Whatever the security team already uses — ASM, cloud inventory, DNS records — as the source, with the programme applying an eligibility overlay. Scope stops being a document someone edits and becomes a view of something already maintained. This is the fix; everything else is refinement.

**Version every change with an effective date.** Submissions evaluated against the scope in force when the researcher began work, which they declare at submission. This resolves the mid-investigation change dispute entirely and costs nothing.

**State a default for unlisted assets.** A single sentence — assets demonstrably belonging to the organisation but not listed are eligible at this band, subject to ownership confirmation — removes the entire category of dispute about newly discovered infrastructure, and it is what programmes usually intend anyway.

**Put scope review on a schedule with a named owner.** Quarterly at minimum, and triggered by acquisitions and major migrations. A recurring calendar item with a person's name is the difference between a page that drifts and one that does not.

**Publish a changelog.** Researchers can see what was added and removed and when. This is trivial to produce from a versioned specification and it is the kind of transparency that builds the trust the researcher relationship runs on.

**Flag decommissioned assets rather than deleting them.** A researcher who spent a week on a parked domain should be told it was retired and when, not silently told they are out of scope. The distinction matters enormously to the person who lost the week.

## Who Feels the Pain

The researcher, who loses a week to a decommissioned target or finds something real on an unlisted asset and is paid nothing for it.

The triage analyst, handling submissions on assets that should never have been listed and disputes about assets that should have been.

The organisation, whose acquired and newly deployed infrastructure — statistically its weakest — is the part least likely to be in scope and therefore least likely to be looked at.

And the programme's reputation, which degrades in the researcher community through exactly this kind of avoidable friction, long before anyone at the organisation notices participation declining.

## Impact If Fixed

Generating scope from the inventory removes an entire class of dispute at a stroke, using data the organisation already maintains for other reasons.

Versioning with effective dates resolves the mid-work scope change grievance completely and costs a database column.

And a stated default for unlisted assets would mean the organisation's newly acquired and newly deployed infrastructure — the part most likely to be weak — stops being the part nobody is allowed to look at.
