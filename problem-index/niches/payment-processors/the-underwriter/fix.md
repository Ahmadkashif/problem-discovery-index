# Never Learning Which Decision Was Right

**Niche:** [[niches/payment-processors/the-underwriter/profile|The Underwriter]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** The underwriter has approved thousands of merchants over four years and has never been told how any of those decisions turned out.
**Tags:** #evaluation-metrics #worker-facing #data-integration #confidence-intervals #quick-win #descriptive-statistics #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to give the underwriter evidence and feedback rather than a website and a clock — and whoever does that turns an unmeasured judgement into a skill that can improve.

## The Problem
Four years, thousands of decisions, each one a judgement about whether a business was safe to process for. The losses that followed are in a portfolio report. The merchants that thrived are in a revenue report. Neither is connected to who approved them or on what basis. The underwriter cannot say whether their instinct about a particular kind of applicant is good or bad, cannot improve deliberately, and cannot demonstrate their value beyond throughput. A new underwriter is trained by sitting with an experienced one, inheriting instincts nobody has validated.

## Why It's Still Broken
The outcome and the decision sit in different systems owned by different teams, and the join belongs to nobody — the same ownership gap that runs through every decisioning problem in this cluster, here landing on the person whose skill depends on it. Losses are managed as a portfolio number. Attribution would identify individual underwriters as better or worse, which is uncomfortable. And nobody has asked the underwriters whether they would like to know.

## What a Fix Looks Like
Tell them what happened. Join every decision to the merchant's subsequent outcomes and report it back to the person who decided, which is the fix, is feasible with a reference field, and is the difference between four years of experience and four years of repetition. Report both directions — losses from approvals and the performance of merchants who were nearly declined — since an underwriter who only sees their losses will tighten indefinitely. Show it by applicant type, so the feedback is about a pattern rather than about individual cases and is therefore learnable. Compare against peers on the same application mix, which reveals genuine differences in judgement that can be examined rather than assumed. Run calibration exercises on the same applications, which measures the variation directly and is the fastest way to see how much the outcome depends on who reviewed it. Build the training material from the record, so a new underwriter inherits evidence rather than instinct. Feed the confirmed outcomes into the models, since they are the labels. Balance the speed target with the accuracy measure once accuracy exists, which is the management change this enables. Publish portfolio quality by underwriter as a development tool rather than a ranking, since the purpose is improvement. And measure how long a new underwriter takes to match an experienced one's accuracy, because that interval is what feedback shortens and it is currently years.

## Who Feels the Pain
Underwriters repeating four years rather than accumulating them; acquirers whose loss rate depends on unvalidated instincts; and merchants declined by a judgement nobody has checked.

## Impact If Fixed
The ownership gap between decision and outcome lands here on the person whose skill depends on it, so four years of experience is four years of repetition. A reference field joining decisions to merchant outcomes, reported back by applicant type, turns instinct into something learnable.
