# Engineers Know Which Submissions Look Wrong and Say So in Email

**Niche:** [[niches/hvac-contractors/equipment-performance-certification/profile|HVAC Equipment Performance Certification]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** A reviewing engineer's instinct that a claimed rating is optimistic is the most valuable signal in the programme and has nowhere to go.
**Tags:** #tacit-knowledge-ml #anomaly-detection #worker-facing #data-integration #compliance

## The Problem
A certification engineer reviewing submissions develops a feel for them. That this manufacturer's ratings tend to sit at the very top of what the configuration should physically achieve. That a claimed efficiency just above a rebate threshold is worth a second look. That a particular product family has been resubmitted three times with small upward revisions. That this combination's rating is inconsistent with the same outdoor unit's rating in a neighbouring combination.

Some of it triggers a question to the manufacturer, or a note to whoever selects challenge tests. Most of it is a passing observation in a review that has a queue behind it. It goes into an email, or a hallway conversation, or nowhere.

The programme's entire deterrent value depends on manufacturers believing that optimistic ratings get caught. The best available detector for that is the reviewing engineer's judgment, and the programme captures none of it.

## Why It's Still Broken
The review is a compliance gate, so the record it produces is binary: the submission is complete and conforming, or it is not. Suspicion is not a finding, and there is no field for something short of a finding.

The politics reinforce it. Members are the certified manufacturers, and a written record of staff suspicion about a member is uncomfortable, so the culture keeps that kind of observation verbal. Which means it is also unaccumulable, unauditable, and gone when the engineer leaves.

And the loop never closes. When a challenge test does find a misstated rating, nobody goes back to see whether an engineer had flagged the submission a year earlier — so the accuracy of engineering intuition in this programme has never been assessed, and there is no evidence base to argue it should be recorded.

## What a Fix Looks Like
Give the observation a structured, internal home and connect it to test outcomes.

**Typed review flags.** A short controlled set — rating near a threshold, inconsistent with related combinations, at the edge of physical plausibility, unusual resubmission pattern — recorded on the submission with a confidence and a note. Seconds to enter, and it turns a passing thought into a record.

**Kept internal, explicitly.** Nothing is communicated to the manufacturer and nothing constitutes a finding. This is the programme observing its own process, which resolves the governance concern entirely and is worth stating in policy so engineers actually use it.

**Joined to challenge outcomes.** When a model is retested, the result should be matched back to whether it was flagged and how. Within a couple of years the programme would know, for the first time, how predictive its engineers' judgment is — and if it is predictive, flags become a legitimate and defensible input to test selection.

**Cross-submission consistency checks, automated.** The specific thing engineers do best is notice that a rating does not sit right against related combinations. Much of that is computable from the catalogue itself and should be surfaced to the reviewer rather than depending on them remembering the neighbouring rating.

**Patterns visible above the individual review.** Three engineers independently flagging different products from the same manufacturer in one quarter is a signal the programme currently cannot see, because each flag exists only in one person's head.

## Who Feels the Pain
Reviewing engineers, whose most valuable contribution is invisible and unrecorded. The certification leadership, whose deterrent depends on detection they cannot measure. And the industry, where every efficiency rebate and code compliance decision assumes these ratings are true.

## Impact If Fixed
The programme's authority rests on manufacturers believing overstated ratings get caught, and the best detection available is human judgment that currently evaporates. Capturing it, validating it against retest outcomes, and feeding the validated part into test selection is the cheapest available increase in the integrity of every efficiency number in US HVAC.
