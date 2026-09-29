# Fix: Back-to-Back Difficult Contacts With No Recovery

**Niche:** [[niches/digital-bpo-operations/the-support-agent/profile|The Support Agent]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Fix (Pain Point)
**One-liner:** An agent finishes an abusive call and the next contact is connected before they have put the headset down.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #change-point-detection #worker-facing #quick-win #hypothesis-testing
**Contested on:** Whether an agent gets a moment after a contact that required one.

## The Problem

A customer has been abusive for eleven minutes. The agent ends the contact, and the routing engine — which knows nothing about what just happened — connects the next one immediately because the agent's status returned to available.

There is usually a mechanism for this. An agent can put themselves into an after-call or unavailable state. Doing so reduces their occupancy and adherence, which are measured and reported, and in many operations using it more than sparingly prompts a conversation with a team leader. So agents largely do not, and take the next contact.

The composition shift has made this constant. The easy contacts that used to arrive between the hard ones have been deflected, so the difficult ones now come consecutively, and the recovery that used to happen incidentally does not.

## Why It's Still Broken

Occupancy is a headline efficiency metric and often a contractual one. Any mechanism that reliably creates recovery time reduces it, and nobody has costed the alternative — the escalations, the errors, the absence and the attrition that follow an agent taking a fifth difficult contact in a row.

The automatic version has never been built because contact difficulty is not measured, so there is nothing to trigger on.

And the manual version is deterred by design: a status the agent can use but is measured on using is a status they will not use.

## What a Fix Looks Like

Make recovery automatic, triggered by the work, and exempt from the efficiency metrics.

Detect the contacts that warrant it. Abuse, extreme customer distress, bereavement or crisis disclosures, long escalations, and safety-related contacts are all detectable from the transcript in real time or immediately after. A flag on the contact is the trigger.

Insert recovery automatically. Ninety seconds to two minutes of unavailable status after a flagged contact, applied by the system rather than requested by the agent, and excluded from occupancy and adherence. No request, no approval, no conversation with a team leader.

Track cumulative exposure across the shift. Three flagged contacts in an hour should produce a longer break or a routing switch, not another ninety seconds. This is the state variable that makes the difference between a gesture and a system.

Cost the change honestly and against the right comparison. The occupancy effect is a small percentage; the comparison is attrition, absence, escalation rates and the quality of the contacts that would have been taken in that state. Measuring the second set is the argument, and it has never been made because the second set is not measured.

Let team leaders see it. An agent's flagged contact count for the day is exactly the information a team leader needs to check in on someone, and it is far better than waiting for the person to say something.

And handle abuse as a policy question too. Clear rules on ending abusive contacts, with the agent's judgement supported rather than second-guessed, is a change that costs nothing and that many operations still do not have.

## Who Feels the Pain

Agents, absorbing consecutive hostile and distressing contacts with no recovery, and penalised on their metrics for taking any. Customers reaching an agent who has just been shouted at for eleven minutes. Team leaders, managing people they can see are depleted with no lever to help. And the BPO, funding an attrition rate that is among the highest of any industry out of a metric it has never traded against anything.

## Impact If Fixed

Recovery happens automatically after the contacts that warrant it, triggered by the work rather than requested by the person. Cumulative exposure gets tracked across a shift. And the occupancy metric gets weighed, for the first time, against the attrition it is quietly buying.
