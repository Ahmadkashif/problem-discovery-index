# Build: A Practice Instrument for Tutors

**Niche:** [[niches/online-tutoring-platforms/the-tutor/profile|The Tutor]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute a tutor's realised hourly rate including preparation and admin, forecast their income from the booking calendar, and give them a portable record of their own practice.
**Tags:** #time-series-forecasting #descriptive-statistics #confidence-intervals #evaluation-metrics #exponential-smoothing #data-integration #worker-facing #quick-win
**Contested on:** Whether unpaid preparation and admin can be captured accurately enough to compute a real hourly rate.

## The Problem

A tutor quotes $50 an hour. After commission, preparation, marking, parent messages, progress notes and the sessions cancelled at short notice, the realised figure is frequently closer to $28. Almost no tutor has computed this, and the ones who have tend to raise their rates or leave.

The second gap is forecasting. Tutoring income is highly seasonal — it collapses in summer, surges before exams, and shifts with school terms — and it is visible weeks ahead in the booking calendar and in the tutor's own history. Tutors experience each summer as a surprise.

The third is portability. A tutor with four years of experience, several hundred students, strong feedback and demonstrable results has all of that inside one platform's database. They cannot take it anywhere, which is what makes a commission increase something they absorb rather than respond to.

## Why Nobody Has Built This

The platform has no incentive on any of the three. A tutor who computed their realised rate might raise prices or leave; one who could forecast might diversify; one with a portable record would be easier to lose.

Third parties have not built it because the market looks small and diffuse and the data access is awkward. It is neither as small nor as awkward as it looks: tutors are numerous, many work across two or three platforms, they already buy materials and tools, and the core inputs — bookings, payouts, and the tutor's own time — are available through exports and light self-tracking.

The unpaid time specifically has never been captured because nobody tracks work nobody pays for.

## What to Build

A tutor-side practice tool covering economics, forecast and record.

**Capture the unpaid time with minimal effort.** Preparation, marking and messaging, logged with one tap against a student, or inferred where possible — platform message timestamps, document edits, calendar entries. A tool that requires diligent logging will not be adopted; one that infers most of it and asks for confirmation will. Even a rough multiplier, established over two weeks of tracking and then applied, is enormously better than nothing.

**Compute the realised rate.** Earnings after commission, divided by total hours worked including the unpaid. Per student, per subject, per platform, ranked. The output people react to is the per-student ranking, because it invariably contains a surprise: the student who needs an hour of preparation for every session and is the most demanding to report on is frequently the least profitable, and is often the one the tutor most wants to keep.

**Forecast income.** From the booking calendar, recurring students' patterns, the tutor's own seasonality and the term calendar, project the next three months with an interval. The seasonal component is strong and regular, which makes this unusually tractable, and knowing in April that July will be thin is worth a great deal to someone who can act on it.

**Build the portable record.** Hours taught by subject and level, students taught, retention, feedback, qualifications and, where the tutor can obtain it, evidence of student outcomes. Exportable, presentable and owned by the tutor. This is the piece with the most leverage in it: a credential a tutor can carry between platforms is what makes the supply side mobile, and mobility is what makes commission rates contestable.

**Compare across platforms.** Realised rate per hour worked, by platform, for the same tutor. Commission is the visible difference; cancellation policy, unpaid admin burden and student quality frequently matter more, and no tutor can currently compare them.

## Target Customer

Tutors directly, particularly the substantial population who tutor as a primary income and work across multiple platforms. Also tutor organisations and, potentially, platforms competing on supply, for whom supporting the record's portability is a recruitment advantage against incumbents whose tutors are locked in.

## Impact If Built

A tutor learns what they actually earn per hour worked, which is the number that governs every pricing and client decision they make and which almost none of them has seen. The summer collapse becomes foreseeable. And a portable professional record makes switching possible, which is the only mechanism by which unilateral commission changes ever face resistance.
