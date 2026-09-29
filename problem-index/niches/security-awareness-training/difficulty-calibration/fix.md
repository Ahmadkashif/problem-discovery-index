# Fix: The Benchmark Compares Different Tests

**Niche:** Difficulty Calibration
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** An organisation compares its click rate against an industry benchmark, and the benchmark is an average of numbers produced by tests nobody has made comparable.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #compliance #revenue-impact
**Contested on:** Whether a simulation's difficulty is a measured property, so that click rates can be compared.

## The Problem

A security leader reports that the organisation's click rate is four per cent against an industry benchmark of six, and concludes the programme is performing above average.

The benchmark is an average across the vendor's customers. Those customers ran different campaigns, with different templates, at different difficulties, with different notification practices, on different schedules. Some pre-announce. Some whitelist the sender infrastructure. Some have retired their harder templates after complaints. Some use the same three templates repeatedly.

So the comparison is between a number produced by one set of tests and an average of numbers produced by many different sets of tests. It supports no conclusion, and it is presented and consumed as though it did — in board reports, in insurance applications, in vendor marketing and in internal programme justifications.

The same applies within an organisation. Comparing this quarter to last quarter compares two campaigns whose relative difficulty nobody measured. Comparing departments compares populations who received different templates.

Everyone in the chain treats these comparisons as meaningful because the numbers are on the same scale and nobody has said that the scale is not one.

## Why It's Still Broken

**The benchmark is a sales asset.** Published industry click rates help vendors demonstrate value and help customers feel calibrated. Qualifying them undermines both.

**Comparability was never claimed and is always assumed.** No vendor asserts that their benchmark is a calibrated comparison; every consumer of it reads it as one.

**Difficulty is not measured, so the qualification cannot even be stated.** Without a difficulty parameter, a vendor could not say how much of the difference is the test even if they wanted to.

**Nobody asks.** Security leaders, auditors and insurers consume these numbers without asking what makes them comparable.

**Comparison feels necessary.** A programme owner needs some external reference, and an imperfect benchmark is more comforting than none.

**Sector benchmarks compound it.** Breaking benchmarks down by industry adds apparent precision to a comparison that was not valid to begin with.

## What a Fix Looks Like

**State what the benchmark is.** An average of click rates from campaigns of unstated and varying difficulty. One sentence, attached to every published benchmark, and it would change how the number is used immediately.

**Publish the campaign composition behind it.** Difficulty distribution, notification practice, whitelisting and repetition. Consumers could then judge comparability for themselves.

**Use an anchor set for external comparison.** A small standard template set, run identically across organisations, whose click rate is genuinely comparable. This is what testing does for cross-form comparison and it would give the category its first real benchmark.

**Compare internally against a fixed anchor, not against last quarter.** An organisation's own trend is only meaningful against constant difficulty, and a fixed anchor set supplies it cheaply.

**Report the reporting rate too.** Reporting rate is harder to inflate through easier tests and is a better cross-organisation comparison than click rate.

**Stop using benchmarks in assurance contexts until they mean something.** Insurance applications and board reports should not cite a comparison that does not support one, and saying so is the honest position for a programme owner who knows.

**Ask the vendor how comparability is established.** A customer asking this question would get an informative answer either way, and nobody asks.

## Who Feels the Pain

The organisation, drawing conclusions about its own security posture from a comparison that supports none.

The security leader, presenting a benchmark comparison to a board as evidence, in good faith, on a foundation nobody has examined.

Insurers and auditors accepting click rates as evidence of a functioning control, with no basis for comparing one applicant to another.

And programmes that are genuinely rigorous, whose harder campaigns produce worse numbers than easier ones elsewhere, with no way to show the difference.

## Impact If Fixed

A one-sentence qualification on every published benchmark would change how the number is used, and it costs a vendor nothing but candour.

A shared anchor set run identically across organisations would give the category its first genuinely comparable measure, and it is a small standard template set rather than a new technology.

And reporting the reporting rate alongside the click rate would provide a cross-organisation comparison that is considerably harder to inflate — which is what a benchmark is supposed to be for.
