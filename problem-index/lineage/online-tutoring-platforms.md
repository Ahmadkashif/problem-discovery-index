# Lineage: Online Tutoring Platforms

**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Wave:** [[series/eras/wave-11-covid-dislocation|11 — The COVID Dislocation]]
**The tool:** the Preply tutor commission schedule — the platform keeps 100% of a tutor's trial lesson with each new student, then a commission that starts at 33% and falls to 18% as the tutor's hours taught on the platform accumulate
**Builder:** Preply
**Builder in vault:** **ABSENT**
**Verification:** partial — schedule and founding verified; date the schedule was introduced not established

## The Problem That Came First

A one-to-one tutoring marketplace sells exactly one thing the tutor cannot get elsewhere: the introduction.

Once a student has found a tutor they like, everything else the platform offers — a video room, a calendar, a card on file — is available free or nearly free from general-purpose tools. So the platform's revenue sits on a relationship that both sides have a standing incentive to take private, and every lesson after the first is a lesson the platform has to keep earning the right to charge for.

That is the constraint the commission schedule is shaped around — a marketplace problem, not a teaching one.

## What Got Built

A two-part fee, published on Preply's own tutor recruitment page:

- **The trial lesson with a new student: 100% commission.** The tutor teaches the first hour and is paid nothing for it.
- **Every lesson after that: a commission starting at 33%, decreasing to 18%** "based on how many hours you've taught on the platform."

Read as a mechanism rather than a price list, it does two things. It charges for the introduction at the moment the introduction happens, in full, before any off-platform leakage is possible. And it pays the tutor a falling rate for staying — each hour taught on Preply lowers the price of the next, so the cost of leaving rises with tenure.

## Who Built It, And Why Them

Preply was founded in November 2012 by three Ukrainians — Serge Lukianov, Kirill Bigai and Dmytro Voloshyn — and launched as preply.com that month. Wikipedia attributes the idea to Bigai's own experience studying English online with a tutor, which he found more flexible and cheaper than the alternatives.

That origin is why the fee looks the way it does. Preply began as a language-tutoring marketplace for adults, and one-to-one conversation practice is the purest case of the leakage problem: no curriculum the platform owns, no materials, no assessment — only a match between a learner and a speaker. A business built on that match has to monetise the match. In June 2016 Preply added a machine-learning system for classifying and recommending tutors, so the platform increasingly controls *which* introductions happen as well as what they cost.

**The rationale above is this note's reading of the schedule, not Preply's stated one.** No Preply statement explaining why the trial lesson is priced at 100% was found this session.

COVID did not create any of this. The schedule's inputs — independent-contractor tutors who "set their own rates and schedules," ranked profiles, video lessons — predate 2020. What the school-closure demand shock did was pour volume through it: Preply reported more than 10 million lessons facilitated by March 2021.

## What It Cost

The tutor carries the acquisition cost. A tutor whose trial lessons convert poorly — or who is shown to many one-off browsers — teaches unpaid hours in proportion to the platform's traffic, not their own skill.

The tenure discount compounds the vault's worker-life problem. The commission is levied on the paid hour only; preparation, marking and parent messages are the tutor's, unpaid, at every rate tier. And because the falling rate is keyed to *hours taught on the platform*, it rewards volume and retention, which are the same signals the ranking already optimises. Nothing in the schedule is keyed to whether a student improved.

## What You Still Touch

Any tutor on a marketplace today who accepts a free or near-free first session is working inside this shape: the platform is paid for the match, and the tutor absorbs the risk that the match fails.

- [[problems/online-tutoring-platforms/high-impact|🔴 Matching and Ranking Decide the Income, and Learning Is Never Measured]] — the commission and the ranking reward the same thing
- [[problems/online-tutoring-platforms/worker-life-1|🟢 The Tutor Working Unpaid Hours Around Paid Ones]] — the trial lesson is the first of them
- [[problems/online-tutoring-platforms/low-impact-1|🟡 Scheduling, No-Shows and Cancellation Policy]]
- [[niches/online-tutoring-platforms/matching-and-ranking/profile|Matching & Tutor Ranking]]
- [[niches/online-tutoring-platforms/the-tutor/profile|The Tutor]]
- [[niches/online-tutoring-platforms/learning-gain-attribution/profile|Learning Gain Attribution]] — the variable no fee is keyed to

**Sources:** Preply, "Teach" recruitment page, preply.com/en/teach (fetched 2026-09-25: "The commission for a trial lesson with a new student is 100%"; "For all subsequent lessons, the commission starts at 33% and decreases to 18% based on how many hours you've taught on the platform"); Wikipedia, *Preply* (founding November 2012, three founders, Bigai's online-English origin, June 2016 ML recommendation system, tutors as independent contractors setting own rates, 10M+ lessons by March 2021); this vault's `history/online-tutoring-platforms.md` and `problems/online-tutoring-platforms/` (cited as vault material, not independent corroboration). ⚠️ **Not established:** when Preply introduced this schedule or whether its tiers have changed — Preply's help-centre commission article returned 404, the Wayback Machine could not be fetched, and WebSearch was unavailable (session cap reached), so the schedule is verified only as of September 2026. Also not established: whether Preply originated the free-trial-to-platform model or inherited it from an earlier marketplace; Wyzant (Chicago, 2005) and Tutor.com (New York, 1998) predate it, but their Wikipedia pages give no fee structure.
