# Origin Story: Part 11

**Origin:** [[origins/pharma-rd-cros/profile|Pharma R&D and CROs]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]

## What Was True Before

A clinical trial ran on paper. Investigators at each site filled out **case report forms (CRFs)** by hand for every patient visit, and those paper forms were periodically collected, monitored on-site by a human comparing them against source medical records, and eventually transcribed into a database for statistical analysis. Corrections were made by striking through an entry, initialling and dating the change, and writing the new value beside it — a paper audit trail, legible and slow.

Database-driven capture of trial data existed through the 1980s and into the 1990s in various forms. But none of it had a settled legal answer to an unglamorous, load-bearing question: **if this record lives only as bits, and the FDA later needs to trust it enough to approve a drug, what makes those bits equivalent to a signed paper form?**

## The Trigger

The US FDA issued **21 CFR Part 11** in **March 1997**, effective **20 August 1997**. Its substance is narrower and more procedural than its consequences: it required systems handling regulated electronic records to maintain secure, computer-generated, time-stamped **audit trails**, enforce **access controls**, detect invalid or altered records, and bind an electronic signature to its record such that the signature could not be repudiated. Critically, it also required the sponsor to certify that electronic signatures were the **legally binding equivalent** of a handwritten one.

**This is the unlock, and it is the centre of this origin's story.** Not a faster computer, not a better database — a regulatory definition of what an electronic record has to be able to prove about itself before an inspector will accept it in place of paper.

## What Actually Happened Next — and What Did Not

Electronic Data Capture (EDC) and electronic case report form (eCRF) software became commercially viable at scale once Part 11 gave them a defined regulatory standing. That much is well supported.

**What is not well supported, and should not be asserted, is any single "flip date" at which EDC replaced paper CRFs.** No credible source names a year the industry crossed over. The transition stretched across roughly two decades and had not fully completed even a decade and a half after Part 11 took effect: the UK's ICR-CTSU (Institute of Cancer Research Clinical Trials and Statistics Unit), a real, still-operating academic trials unit, was documented converting trials from paper **as late as 2012**.

> **This is a negative finding, and it is reported here as one rather than papered over.** The commonly implied narrative — "Part 11 (1997) enabled EDC, and paper CRFs were phased out shortly after" — compresses a multi-decade, uneven, sponsor-by-sponsor and trial-by-trial transition into a clean before/after that the sources do not support. Say "EDC became viable" and stop there; do not attach a completion date, because none is defensible.

## Why the Slowness Itself Is the Lesson

The regulation existed by 1997. The technology to build EDC systems existed shortly after. And yet real trial groups were still converting from paper fifteen years later. **Regulatory permission is necessary for adoption at scale, but it is not sufficient, and the gap between "this is now allowed" and "everyone has actually switched" can run into decades** when the switching cost includes revalidating every process a trial site has run for years, retraining investigators, and re-earning an inspector's trust in a new system one trial at a time.

**Sources:** US FDA, 21 CFR Part 11, Final Rule, March 1997, effective 20 August 1997; FDA guidance on Part 11 scope and application; ICR-CTSU (Institute of Cancer Research Clinical Trials and Statistics Unit) public documentation of trial-level paper-to-electronic transitions through 2012; general EDC/eCRF industry retrospectives — treated cautiously given the absence of a single authoritative timeline.
