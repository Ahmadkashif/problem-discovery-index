# Chasing Someone Who Cannot Pay

**Niche:** [[niches/bnpl-providers/the-collections-agent/profile|The Collections Agent]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The agent is measured on recovery, the person on the other end has six plans and no income, and the only behaviour the measurement rewards is continuing to contact them.
**Tags:** #compliance #evaluation-metrics #worker-facing #confidence-intervals #quick-win #descriptive-statistics #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell the agent who needs a payment plan and who needs to be left alone — and whoever does that changes both the recovery rate and what this job does to the people doing it.

## The Problem
The agent's target is recovery. The customer in front of them has lost their income, holds plans at several providers, and cannot pay any of them. The right action is forbearance — a plan, a pause, a write-off, a referral to debt advice — and every one of those reduces the agent's measured performance. The measurement rewards persistence with people who cannot pay, the agent knows this, and they either follow the measure and feel bad or ignore it and are marked down. The function's incentive structure is pointed at the wrong outcome for the population it is actually serving.

## Why It's Still Broken
Recovery rate is the collections metric everywhere and was imported without asking whether it fits a population holding small obligations across several providers — the measure came with the practice and nobody examined its fit. Forbearance outcomes are not recorded as successes. Hardship is hard to verify, which makes agents cautious about accepting it. And the cost of the wrong treatment falls on the customer and the agent rather than on the business.

## What a Fix Looks Like
Measure the right outcome. Count appropriate forbearance as a successful resolution in the agent's own metrics, which is the fix, is a measurement change rather than a system one, and immediately aligns the incentive with the correct action. Give the agent authority to offer a plan or a pause without escalation, since requiring approval for the humane action makes it the slow option. Identify hardship before contact so the agent arrives prepared, which is the build note's segmentation and changes the conversation entirely. Record forbearance outcomes and follow them, since a customer given a plan who then completes it is a recovery and is currently not counted as one. Set the write-off threshold explicitly, because pursuing a small balance through a full sequence can cost more than the balance and nobody has computed where that line sits. Refer to debt advice where appropriate, which is both the right action and increasingly an expectation. Measure complaint rate and vulnerable customer outcomes alongside recovery, so the function is judged on all of what it does. Protect agents from the queue's emotional load with rotation and support, since this is a documented occupational hazard in collections and this population is particularly distressed. Train on the treatment selection rather than on negotiation, because the skill this job needs is judging which situation this is. And report total resolution including forbearance, since a function measured only on money recovered will keep chasing people who have none.

## Who Feels the Pain
People in genuine difficulty pursued for small amounts; agents whose humane judgement costs them their target; and providers whose collections function is generating complaints and regulatory attention.

## Impact If Fixed
The recovery metric came with the transplanted practice and nobody examined its fit for a population holding small obligations across providers. Counting appropriate forbearance as a resolution is a measurement change that aligns the incentive with the correct action immediately.
