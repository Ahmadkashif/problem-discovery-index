# Fix: Nobody Compares the Rate to Anything

**Niche:** [[niches/telehealth-platforms/prescribing-accountability/profile|Prescribing Pattern Accountability]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The platform knows exactly how many prescriptions it wrote and for what, and has never placed that number next to a published benchmark.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #data-integration #worker-facing
**Contested on:** Whether the platform will compute a comparison that takes an afternoon and might be uncomfortable.

## The Problem

A telehealth platform can produce, from its own database, the share of encounters for any presentation that resulted in a prescription of any class. It is a group-by.

Guideline-concordant rates for many common presentations are published by professional bodies. Ambulatory benchmarks from in-person practice exist in the health services literature. Putting the two numbers side by side is the most basic form of clinical self-assessment available and takes an analyst an afternoon.

Most platforms have never done it. Not a rigorous case-mix-adjusted version — the simple descriptive comparison. So the organisation's belief about whether its prescribing is appropriate rests on the absence of complaints.

## Why It's Still Broken

Because the comparison might be unflattering and nobody is required to produce it. Complaint-driven regulation means that a platform with no complaints has no forcing function, and internal quality review in this industry is generally case-based — reviewing individual encounters flagged by something — rather than distributional.

The methodological objection is also deployed more heavily than it deserves. "Our population is different" is true and is a reason to interpret the comparison carefully, not a reason to refuse to look at it. A platform whose rate is four times the benchmark has learned something regardless of case mix; one whose rate is 20% above has learned that it needs the adjusted analysis.

And the number belongs to nobody. Clinical operations measures throughput, compliance handles complaints, and the distributional picture is not on anyone's dashboard.

## What a Fix Looks Like

Compute the descriptive comparison, look at it, and decide what to do next.

Pick the five or six highest-volume presentations. For each, compute the share of encounters resulting in a prescription, by class, over the last year. Break it down by clinician, by month, by time of day, by synchronous versus asynchronous, and by any relevant product or subscription segment.

Put the published benchmark next to each one. State clearly that it is unadjusted. Where the platform's rate is close, that is reassuring and cheap. Where it is far, the adjusted analysis becomes urgent and justified.

Look at the internal variation, which needs no external benchmark at all. If clinicians on the same platform seeing similar case mixes prescribe at rates differing by a factor of three, that is a finding about the platform's own consistency, it is entirely internal, and it is the most defensible starting point.

Watch the temporal patterns, which are equally internal. Does the rate rise when the queue is long, late in a shift, on asynchronous encounters, or after a compensation change? Any of these is a structural finding that points at the operating model rather than at a person, which makes it both more important and easier to act on.

Give each clinician their own numbers privately, against the platform distribution, framed as professional feedback. Most will want it, most will be near the middle, and the few who are not will usually adjust without any formal process.

And write down what threshold would prompt what action, before looking. This is what separates a quality programme from a discovery nobody knows what to do with.

## Who Feels the Pain

Patients receiving prescriptions the evidence does not support, and patients denied ones it does — the comparison detects both directions. Clinicians, who have no idea whether their own practice is typical and would mostly like to. The platform, whose exposure grows with every encounter it has not characterised. And the regulator or payer who asks the question and receives an assurance.

## Impact If Fixed

The industry's most-asked question about itself gets a number instead of an assurance, for the cost of an afternoon's analysis. Internal variation and temporal patterns — both needing no external benchmark and no case-mix debate — surface the structural drivers immediately. And clinicians find out where they sit, which for most of them is the only professional feedback on prescribing they will ever receive.
