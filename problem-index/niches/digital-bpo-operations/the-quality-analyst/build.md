# Build: Diagnosis and Coaching Material From Full Coverage

**Niche:** [[niches/digital-bpo-operations/the-quality-analyst/profile|The Quality Analyst & Team Leader]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Turn full-coverage scoring into a per-agent diagnosis and a set of specific contacts to review, so coaching is about something real.
**Tags:** #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #worker-facing #tacit-knowledge-ml
**Contested on:** Whether an agent's specific weakness can be identified well enough to coach on.

## The Problem

A team leader sits down with an agent for a coaching session. They have four quality scores, an adherence percentage and a handle time average. From this they are expected to identify what the agent should do differently.

They cannot, so the coaching is generic — work on your greeting, watch your handle time, remember to confirm understanding — delivered to fifteen people with different actual weaknesses, none of which anyone has identified. Agents experience it as a ritual and largely ignore it, which everyone knows.

The material for real coaching exists. Across several hundred contacts a month, an agent's pattern is visible: they are strong on billing and weak on technical escalations; they handle upset customers well but rush the diagnosis; they do not confirm understanding before closing, specifically on complex contacts. That is coachable. Four sampled scores cannot show it.

## Why Nobody Has Built This

The diagnosis requires full-coverage scoring, which is the build in the effectiveness niche and is only now feasible. Before it, the material genuinely did not exist.

The roles have also been organised around the sampling constraint for so long that the constraint is invisible. The analyst's job is defined as scoring a quota; the team leader's coaching cadence is defined by how many scores exist. Nobody has re-asked what these roles should do if coverage were not the limit.

And team leaders are given more agents than they can coach properly, which makes better material only part of the answer.

## What to Build

A per-agent diagnosis and a coaching queue built from it.

**Aggregate the full-coverage scores into a pattern.** Performance by contact type, by rubric item, by customer sentiment, by time of shift, by contact complexity, with intervals. The useful output is where this agent differs from their peers on comparable contacts — which requires controlling for the contact mix they receive, since agents do not get the same work.

**Name the specific weakness.** Not a score but a statement: this agent resolves billing contacts well and loses technical contacts at the diagnosis stage, specifically by accepting the customer's framing without checking. Generated from the pattern plus the transcripts, anchored in examples.

**Pull the examples.** Three contacts that illustrate it, timestamped to the moment, plus two where the agent handled it well. A coaching session built on five specific contacts is a completely different conversation from one built on a number, and assembling them is a query once scoring is universal.

**Track whether coaching worked.** The rubric item coached, measured before and after across full volume. This is the loop that has never existed in this industry — nobody knows whether coaching changes anything — and full coverage makes it a straightforward comparison.

**Give the team leader their time back.** Most of what consumes a team leader's day is mechanical: adherence exception chasing, schedule swaps, absence logging, escalation routing. Automating the routine portion is what makes coaching time actually exist, and it is a workflow project rather than a modelling one.

**Redefine the analyst role.** From scoring a quota to maintaining the rubric, adjudicating disputes, calibrating the model and doing deep reviews of the contacts that matter. Better work, and it is the role the function needs once coverage is solved.

## Target Customer

BPO quality and operations leadership, where the case is coaching effectiveness against attrition and quality outcomes — and where the analyst headcount currently spent on listening is a visible cost that can be redeployed rather than removed.

## Impact If Built

Coaching becomes specific, evidence-based and about something the agent recognises, which is the difference between a ritual and a conversation. Team leaders get the time to hold it. Analysts move from listening to adjudicating. And for the first time anyone can measure whether coaching changes performance.
