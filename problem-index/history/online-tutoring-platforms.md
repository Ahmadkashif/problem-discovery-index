# History: Online Tutoring Platforms

**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Primary Wave:** [[series/eras/wave-11-covid-dislocation|11 — The COVID Dislocation]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** None on file. `grep -l online-tutoring-platforms origins/*/legacy.md origins/*/profile.md` returns nothing — none of the eighteen origins names this industry as a child, and none fits: it is not a hospital-systems-style statutory unlock, not an airlines-style yield-management inheritance, and its marketplace mechanics (search, rating, commission) are generic Wave 6 plumbing rather than a transplant from a specific origin story. Recorded as a genuine absence.
**Episode Tier:** 1
**Transferable Pattern:** A dislocation can produce a demand spike for an industry and, separately and later, gut a whole segment of it — and the two events can come from entirely different waves. Attributing both to the same cause is the error to avoid.

## Before

The marketplace infrastructure for online tutoring is not a COVID product. **Wyzant was founded in 2005** by Andrew Geant and Mike Weishuhn in Chicago; by 2013 it had roughly 500,000 registered tutors and outside investment from Accel Partners. **Preply was founded on 1 November 2012** by Serge Lukianov, Kirill Bigai and Dmytro Voloshyn in Ukraine, matching students to language tutors with a machine-learning ranking model from early on. Video classrooms, scheduling, per-session billing with a platform commission — the entire mechanical shape of this industry existed for the better part of a decade before the pandemic reached it.

## The Origin Event — two dislocations, three years and one wave apart

**This industry does not have a single origin event, and forcing one would misdescribe what actually happened to it.** What it has instead is two separate shocks from two different waves, and keeping them apart is the discipline this file exists to enforce.

**The first, in 2020, was a demand shock: mass school closure.** UNESCO's monitoring recorded, at the pandemic's educational peak, **"more than 1.6 billion students and youth" affected globally** by full or partial school closures — a figure this session could confirm directly from UNESCO's own COVID-19 education response page. *(This vault's earlier Wave 11 research cites a comparable figure of over 1.5 billion learners across roughly 190–200 countries; the two are consistent within the kind of rounding this scale of disruption produces, and neither should be quoted as more precise than it is.)* Existing marketplaces absorbed a wave of parents and students suddenly needing remote instruction that a closed classroom no longer provided.

**The second, starting in 2023, was a supply-side collapse inside one segment of the same industry, caused by generative AI — a Wave-9-adjacent event with nothing to do with COVID.** Chegg, founded in 2005 as a textbook-rental business that had grown a large "homework help" answer-lookup product, told investors in May 2023 that ChatGPT was displacing that product; **its stock fell 38% in a single day.** The decline did not reverse: 2024 revenue was $618M against an operating loss of $737M and a net loss of $873M, CEO Dan Rosensweig stepped down in June 2024 after fourteen years, and despite launching its own AI product ("Cheggmate") the company cut roughly **two-thirds of its workforce across two 2025 layoff rounds.**

Treating either event as explaining the other would be a genuine error. **COVID did not create the marketplaces, and generative AI is not a COVID aftershock** — it is an unrelated dislocation that happened to land on the same industry three years later and destroy the specific sub-segment (paid answer-lookup) that competed most directly with what a free chatbot now does for nothing.

## What Became Cheap

**Getting an answer.** First, in the 2010s, a subscription to a homework-help service made getting a worked solution to a specific problem cheap relative to hiring a private tutor by the hour. Then, from 2023, a free conversational AI made getting an answer cheaper still — cheap enough that the paid product built to do exactly that stopped being worth paying for. Two waves, the same falling cost, applied to the same task twice.

## The Graveyard, and What Survived Next to It

**Chegg is the closest thing this file has to a corpse, and it is instructive precisely because a directly adjacent business did not die.** Preply — the human, one-to-one, conversation-based tutoring model — raised a **$150M Series D in January 2026 at a $1.2B valuation**, becoming a unicorn nearly fourteen years after founding. The distinction is exactly the one this vault's own hub note for the industry already draws without reference to either company: a marketplace optimised around **matching and rebooking** survives a generative-AI shock, because a chatbot is a poor substitute for live conversational practice with another person; a product built around **retrieving an answer to a specific question** does not survive it, because that is precisely the task a large language model performs better and for free. The same wave that gutted one segment of online tutoring left the adjacent segment, built on a different value proposition, largely untouched.

## The Binding Constraint — and an honest doubt about whether tutoring addressed the thing it was supposed to

The 2022 NAEP results recorded the largest math score decline since testing began in 1990 — 4th-grade math down 5 points and 8th-grade math down 8 points against 2019, with no US state showing improvement, per this vault's already-sourced Wave 11 account. *(One caveat worth carrying forward, found independently in this session: broader NAEP reporting also describes score declines occurring across 2015–2025 as "long-term, occurring not only during the COVID-19 pandemic" — the pandemic accelerated a slide that was, to some degree, already underway. Do not attribute the entire decline to school closures alone.)*

**Whether the online tutoring industry measurably helped close that gap is a question this vault cannot answer honestly in the affirmative, and the reason is structural, not incidental.** `industries/online-tutoring-platforms.md` states the mechanism plainly: these platforms match on price, subject and star rating, and measure success by rebooking — not by any assessment of whether the student learned anything. A tutor who is warm and ineffective rebooks as well as one who is effective and demanding, and the platforms' own data cannot currently tell the two apart. That is not a claim that tutoring failed to help; it is the more uncomfortable claim that **the marketplaces have never built the instrumentation that would let anyone — the platform, the parent, or a researcher — know either way.** Any vendor efficacy claim encountered elsewhere should be read against that absence.

## What's Still Open

- [[problems/online-tutoring-platforms/high-impact|🔴 Matching and Ranking Decide the Income, and Learning Is Never Measured]]
- [[problems/online-tutoring-platforms/low-impact-2|🟡 Diagnostic Assessment and Session Planning]]
- [[problems/online-tutoring-platforms/worker-life-1|🟢 The Tutor Working Unpaid Hours Around Paid Ones]]
- [[niches/online-tutoring-platforms/tutor-effectiveness/profile|🔵 Tutor Effectiveness & Learning Measurement]] — the absent foundation this file's whole argument rests on
- [[niches/online-tutoring-platforms/learning-gain-attribution/profile|🎯 Learning Gain Attribution]]
- [[niches/online-tutoring-platforms/matching-and-ranking/profile|🔵 Matching & Tutor Ranking]] — optimising on the signal that exists, not the one that matters

## The Transferable Pattern

**Keep dislocations separated by wave even when they hit the same industry.** Online tutoring took a demand shock from Wave 11 in 2020 and a supply-side shock from generative AI in 2023, and the two produced opposite effects on different segments of the same business for unrelated reasons — one grew a market, the other destroyed a product line inside it. An FDE assessing this industry's history should resist the pull toward a single tidy narrative arc. The more useful and more honest finding is the second one: an industry can survive a wave that kills its neighbour, and still never have built the one measurement — did the student actually learn — that would let anyone tell whether surviving was deserved.

**Sources:** UNESCO, COVID-19 education response page (global school closures, "more than 1.6 billion students and youth" affected); Wikipedia, *Chegg* (founding 2005, May 2023 ChatGPT disclosure and 38% single-day stock decline, 2024 financials, CEO departure, 2025 layoffs); Wikipedia, *Preply* (founding 1 Nov 2012, founders, funding history through Jan 2026 $150M Series D / $1.2B valuation); Wikipedia, *Wyzant* (founding 2005, founders, 2013 tutor count and Accel investment, 2021 acquisition by IXL Learning); Wikipedia, *National Assessment of Educational Progress* (long-term 2015–2025 decline framing); this vault's `series/eras/wave-11-covid-dislocation.md` (NAEP 2022 point figures, sourced to NAGB/NAEP; UNESCO learner-count figure) — note that this session's own attempts to re-fetch nationsreportcard.gov and nagb.gov directly failed on repeated connection errors, so the specific NAEP point figures here are carried from the vault's prior, already-sourced research rather than independently re-verified in this session; this vault's `industries/online-tutoring-platforms.md`.
