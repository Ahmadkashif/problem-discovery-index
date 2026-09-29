# Nobody Measures Time to First Build

**Niche:** [[niches/developer-tools-vendors/developer-environment-setup/profile|Developer Environment Setup]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every engineering organisation knows onboarding is slow and none of them can say how slow, which is why nobody has ever been asked to improve it.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to make a project build on a new machine in minutes and stay building when something upstream changes — and whoever does that takes platform engineering, because the lost week is the most reliably wasted time in software.

## The Problem
An engineering leader is asked how long it takes a new developer to become productive. They say a few weeks, because that is the received figure. Nobody has measured time from first day to first successful local build, first commit, or first merged change. Nobody has measured how many colleague-hours each onboarding consumes. So the setup experience — which every engineer describes as bad — has no number attached, competes with nothing on the platform roadmap, and stays bad indefinitely.

## Why It's Still Broken
The measurement spans systems: the joiner's start date is in the HR system, their first build is on their laptop, their first commit is in the repository. Nobody has joined them because nobody owns onboarding time. It is also politically awkward in a small way, since a bad number reflects on the platform team who would have to produce it. And the cost is borne by individuals in their first fortnight, when they are least likely to complain.

## What a Fix Looks Like
Measure the interval and its causes. Time from start date to first successful local build, to first commit and to first merged change, per joiner — a join across three systems that most organisations can do in a day. Colleague-hours consumed, approximated from help requests in the onboarding channel, which is a lower bound and is usually startling. Failure points in the setup sequence, instrumented by having the setup process report which step failed, which is a small change to a script and produces a ranked list of what to fix. Drift incidents: how often an existing developer's environment breaks, how long it takes to recover, and how many people the same break hit — which is the recurring half of the cost and is never counted at all. Track the trend after each improvement, since that is what turns this into an owned metric rather than a one-off audit. And publish it, because an engineering organisation that can see a fortnight of lost time per joiner will fund the fix, and one that cannot will not.

## Who Feels the Pain
New joiners spending their first week on something unrelated to their job; colleagues losing hours to other people's setup; and platform teams who know the experience is bad and have no evidence with which to prioritise it.

## Impact If Fixed
The measurement is a join across three systems and takes about a day, and it converts a universally acknowledged frustration into a number that can compete for roadmap attention. The per-step failure instrumentation produces the specific fix list immediately.
