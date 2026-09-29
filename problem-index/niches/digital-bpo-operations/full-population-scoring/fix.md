# Fix: The Repeat Contact Is Never Linked to the First One

**Niche:** [[niches/digital-bpo-operations/full-population-scoring/profile|Full-Population Resolution Scoring]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Fix (Pain Point)
**One-liner:** A customer calls back three days later about the same problem and the two contacts are recorded as two contacts, with nothing connecting them.
**Tags:** #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #data-integration #quick-win #worker-facing #automation
**Contested on:** Whether repeat contacts about the same issue will be linked and counted.

## The Problem

The single clearest evidence that a contact did not resolve a customer's problem is that the customer came back about it. Every contact centre generates this signal continuously and almost none uses it.

The obstacles are mundane. Contacts are recorded per interaction with no issue thread. The repeat may arrive on a different channel, or be handled by a different vendor, or fall under a different queue. Customer identity across channels is imperfect. And relating two contacts requires judging whether they concern the same issue, which until recently meant a human reading both.

So a customer who calls three times about one problem generates three contacts, three handle times, three quality-sample eligibilities and no signal that anything went wrong. In a business paid per contact, three contacts is also more revenue than one, which has not accelerated anyone's interest in linking them.

## Why It's Still Broken

Partly data structure: interaction-centric records with no issue object, inherited from telephony systems.

Partly ownership: the customer's full contact history spans channels and sometimes vendors, and lives in the client's systems. The BPO sees its own queue. Getting the full picture requires a client integration nobody has prioritised because nobody was reporting the metric.

And partly incentive, in a per-contact commercial model. Repeat contacts are volume.

## What a Fix Looks Like

Link the contacts and report the rate. Most of this is available within the BPO's own data before any client integration.

Create an issue thread. Contacts from the same customer within a window, judged as concerning the same issue from the transcripts, grouped into one thread with a first contact and subsequent ones. Relatedness judgement is now cheap and reliable enough, and the grouping is the whole fix.

Report repeat contact rate by contact type, by agent, by queue, by handle time band. The last of these is the interesting one — the relationship between how long the first contact took and whether the customer came back is the industry's core question and it falls straight out of this grouping.

Frame it as a survival measure. Time to repeat contact, with censoring for customers who have not come back yet, rather than a fixed-window rate. This handles the recency problem properly and gives a cleaner comparison across periods.

Route the threads back as coaching material. A thread of three contacts about one issue is the most instructive artefact the operation produces, far better than a randomly sampled single contact, and it shows exactly where the first attempt failed.

Get the cross-channel history from the client. Chat, email, self-service and any other vendor's contacts, so the thread is complete. This is an integration with an obvious business case once the internal version has shown what the metric reveals.

And handle the commercial implication honestly. In a per-contact model, reducing repeats reduces billed volume. Raising that with the client — trading volume for a demonstrated quality outcome — is the beginning of the contractual conversation that this industry has been avoiding, and it is better begun by the vendor with the data than by the client with a suspicion.

## Who Feels the Pain

Customers, repeating their problem to a third person. Agents, taking a repeat contact with no visibility that it is one, and being scored on handle time for an issue that was mishandled before they got it. Clients, paying three times for one problem. And the BPO, which cannot demonstrate resolution quality because it never counted the clearest evidence it generates.

## Impact If Fixed

The clearest outcome signal in the industry starts being counted, from data mostly already held. Coaching gets the failed threads rather than random samples. And the relationship between handle time and repeat contact becomes visible — which is the fact the whole commercial structure of the industry rests on not knowing.
