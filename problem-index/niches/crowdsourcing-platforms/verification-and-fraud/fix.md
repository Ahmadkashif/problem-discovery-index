# Fix: Excluded for Sharing a Household Computer

**Niche:** [[niches/crowdsourcing-platforms/verification-and-fraud/profile|Worker Verification & Fraud Control]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Two people in the same house both do crowdwork, the system reads it as duplicate accounts, and both lose access with no explanation and no appeal.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #worker-facing #quick-win
**Contested on:** Whether the ordinary circumstances that resemble fraud will be distinguished from fraud.

## The Problem

Duplicate-account detection flags accounts sharing a device, a network or behavioural patterns. In a household where two or three people do crowdwork — which is common, because the work spreads by word of mouth within families and communities — every one of those signals fires.

The accounts are suspended. The message, if there is one, refers to a terms of service violation. There is no route to explain that these are two different people, and no obvious way to prove it even if there were.

The same happens with university and workplace networks, shared computers in internet cafés, and carrier-grade NAT, which in several of the countries where this workforce is concentrated puts thousands of users behind one address. The pattern is that the circumstances most likely to trigger exclusion are the circumstances of the lowest-income workers.

## Why It's Still Broken

Because the error is invisible. An excluded worker with no appeal route stops appearing in the data, and the absence reads as the control working.

The signals are also genuinely correlated with real fraud — account farming does use shared infrastructure — so a control tuned on requester complaints will keep tightening.

And nobody has established the base rates. What proportion of honest workers share a device with another worker? Nobody knows, because nobody asked, and without that number every shared device looks equally suspicious.

## What a Fix Looks Like

Weight the evidence properly, look for the benign explanation, and provide a route.

Establish the base rates for each signal in this population. Shared IP, shared device, shared network by country and carrier type. Once you know that a shared IP in a particular market is unremarkable, the signal can be weighted accordingly, and this is a straightforward analysis over the existing population.

Distinguish strong from weak evidence. Shared payment instrument, identical browser fingerprint with identical timing, and answers copied verbatim are strong. Shared IP, shared device model, and similar working hours are weak. Treating them as one score is the direct cause of most of these exclusions.

Look for the exculpatory pattern. Two accounts on one device that are never active simultaneously, with different working hours, different task preferences and different writing styles, are two people. That analysis is available and is not run because the system is looking for guilt rather than at the case.

Offer a verification path instead of an exclusion. A flagged account should be able to verify identity and continue, rather than disappear. For genuine distinct individuals this resolves in minutes; for account farms it is a real barrier.

Explain the reason. A specific, plain-language statement of what triggered the flag, without giving away the detection detail, so a person knows whether they can contest it.

And sample the exclusions for review, deliberately, to find out what the false positive rate actually is. It is the only way to see an error class that by construction produces no complaints.

## Who Feels the Pain

Households where more than one person works, which is common precisely in the communities where this income matters most. Workers on shared or institutional networks. Workers in countries with heavy carrier NAT. All of them excluded without explanation from an income source, with no route back. And requesters, who lose access to an honest and frequently experienced pool.

## Impact If Fixed

The evidence gets weighted by what it is actually worth, which eliminates most of these exclusions immediately. Benign patterns get looked for rather than only guilty ones. A flagged worker gets a reason and a verification path instead of silence. And the platform finds out, for the first time, how often it is wrong.
