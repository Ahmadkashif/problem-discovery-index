# Fix: The Sector Tag Contains Everybody

**Niche:** Relevance & Customer Targeting
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Financial services covers a global bank and a three-person payments startup, and it is the primary signal by which intelligence is matched to customers.
**Tags:** #evaluation-metrics #confidence-intervals #k-means-clustering #worker-facing #descriptive-statistics #data-integration
**Contested on:** Whether relevance is assessed against what the customer actually runs and faces, or approximated by a sector label.

## The Problem

A customer is tagged financial services. So is every other organisation that handles money — retail banks, insurers, payment processors, trading firms, credit unions, fintech startups, asset managers. They run different technology, face different adversaries, operate at different scales and have entirely different exposure.

The tag is the primary relevance signal. Reporting and indicators are matched to customers by it, subscription tiers are organised around it, and adversary profiles describe targeting by it.

It carries almost no information. A tag that applies to organisations with nothing operationally in common does not distinguish anything, and the customer's analysts know this within a week of subscribing. They stop using sector as a filter and go back to reading everything or ignoring most of it.

The deeper problem is that the tag creates an impression of targeting. Because content is sector-tagged, both vendor and customer believe relevance is being handled. So the actual work — determining whether this threat applies to this organisation — remains undone and unacknowledged, and the noise the customer experiences is attributed to the volume of the threat landscape rather than to a targeting mechanism that does nothing.

## Why It's Still Broken

**Sector is what gets captured.** It is on the contract, it is a field in the customer record, and it requires no effort. Anything better requires collecting information nobody has asked for.

**It matches how vendors organise.** Sales teams, analyst specialisms and reporting series are frequently organised by sector, so the tag reflects an internal structure as much as a customer attribute.

**Adversary targeting is genuinely described by sector, partly.** Some adversaries do target sectors, so the tag is not meaningless — it is just far too coarse to act on, which is harder to notice than being wrong.

**Nobody measures whether it works.** Relevance accuracy is unmeasured, so there is no evidence that the tag fails and no pressure to improve it.

**Better attributes require customer effort.** A technology profile means asking the customer for something, and customers under-fill forms, so the data would be incomplete — which is used as a reason not to start.

**The customer compensates silently.** Analysts filter by hand, conclude that this is what the job involves, and never report that the tagging is useless.

## What a Fix Looks Like

**Add sub-sector and scale at minimum.** Retail banking versus payment processing versus asset management, with an organisation size band. This is two additional fields, captured at onboarding, and it immediately makes the tag carry information.

**Capture the technology profile, even partially.** Cloud provider, identity provider, major platforms, remote access products, the handful of technologies that most adversary reporting concerns. Ten fields, filled in once, would improve matching more than any amount of sector refinement.

**Ask what they actually care about.** A short statement of the customer's own concerns — which adversaries, which threat types, which assets — is a better relevance signal than any inferred attribute and takes a conversation.

**Let the customer filter on attributes, not tags.** Expose the structured characteristics of threats — affected software, geographies, techniques — so a customer can build their own filters against their own knowledge of their estate. This works even where the vendor knows nothing about the customer.

**Measure relevance feedback.** A one-click relevant-or-not on delivered content, tracked. Without any feedback, targeting cannot improve, and this is the cheapest possible loop.

**Stop implying that sector tagging is targeting.** A vendor honest that relevance filtering is coarse invites the conversation about doing it properly. The current presentation suggests the problem is handled, which is why it is not addressed.

## Who Feels the Pain

The customer's analysts, filtering by hand because the tag does not filter, using capacity the subscription was supposed to free.

Small and mid-sized organisations, who receive the same volume as a global enterprise in the same sector bucket and have no analysts to spare.

The vendor, whose genuinely relevant reporting arrives mixed into a stream the customer has learned to skim.

And the customer whose actual exposure sits outside their sector's typical profile, who receives content matched to organisations they do not resemble.

## Impact If Fixed

Sub-sector and scale are two fields that would immediately make the primary relevance signal carry information, at essentially no cost.

A ten-field technology profile, captured once, would improve matching more than any refinement of sector taxonomy, because adversary reporting concerns software far more specifically than it concerns industries.

And exposing threat attributes so customers can filter for themselves works regardless of what the vendor knows about them, which makes it the fix available to every vendor immediately.
