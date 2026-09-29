# Fix: Writing Time Is Not on the Calendar

**Niche:** The Tester
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A third of the work in every engagement is unbilled, unscheduled and therefore done in the evenings, and no system the firm runs records that it happened.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #revenue-impact #workflow-orchestration #hypothesis-testing
**Contested on:** Whether the write-up is work the schedule makes room for, or unpaid evening labour squeezed between back-to-back engagements.

## The Problem

The engagement is ten days of testing. The report is three to five days of work. The client is billed for ten days. The scheduler books the tester for ten days and assigns the next engagement immediately after.

The three to five days still happen. They happen at 9pm, at weekends, and in stolen hours during the following engagement. The tester is doing two jobs for a fortnight, one of which is invisible to every system the firm operates and to the client paying for both.

Nobody planned this. It is the arithmetic consequence of billing by the day and scheduling by the booking. And because the extra time appears nowhere — not in utilisation, not in project accounting, not in capacity planning — the firm's view of its own economics is systematically wrong by a third of delivery effort. Margin per engagement looks better than it is. Capacity looks larger than it is. The cost of a firm's reporting inefficiency is real and literally uncountable in its own books.

The people absorbing it are the firm's scarcest and most expensive resource, and the reason they leave is rarely the testing.

## Why It's Still Broken

**Utilisation is the metric the whole model runs on.** A firm that schedules write-up time drops its utilisation percentage immediately and visibly. Every firm that has tried it has watched the practice erode as soon as the quarter got tight, because the number is what leadership looks at.

**Clients will not pay for a line item called reporting.** Buyers compare proposals on total days for the testing. A firm quoting thirteen days where a competitor quotes ten loses, regardless of what the thirteen include — so the writing gets absorbed into an unstated portion of the ten.

**Nobody has counted it.** Write-up hours are not logged anywhere. The cost is therefore an anecdote rather than a number, and anecdotes do not change resourcing models.

**Testers absorb it without complaint, until they leave.** The professional culture treats evening write-up as normal, so it generates no escalation. It generates resignations instead, and exit interviews attribute those to burnout generically rather than to a specific structural cause.

**The problem is worst for the best testers.** The people who find the most findings have the most to write. The firm's strongest performers carry the heaviest unpaid load, which is precisely backwards.

## What a Fix Looks Like

**Measure it for one quarter.** Ask testers to log write-up hours, honestly, with an explicit assurance that the data will not be used against them. The resulting number — very likely twenty-five to thirty-five per cent of delivery effort, entirely unbilled and unscheduled — is what makes every subsequent change possible. This costs nothing and is the prerequisite.

**Put it in the schedule as a booked task.** Write-up days booked into the resourcing tool as delivery work, not as availability. The scheduler stops assigning into the gap, and the tester stops working two engagements at once.

**Price the engagement as delivery, not as testing days.** Quote the complete deliverable rather than a count of test days, so the write-up is inside the price rather than outside the schedule. This requires the firm to hold its nerve on price comparison, which is easier if the proposal states coverage and depth rather than days — which is what [[niches/penetration-testing-firms/assessment-assurance/profile|🔵 Assessment Assurance]] would enable.

**Change the headline metric to delivery completion.** Engagements delivered complete and on time, rather than utilisation. This single change removes the structural pressure that erodes every other fix, and it measures something closer to what the business actually sells.

**Cut the write-up burden directly.** Capture during testing, a firm finding library, and a single report format across clients. Every hour removed from the write-up is an hour that stops being taken from someone's evening, and this is where the technology in this niche pays.

**Schedule review capacity separately.** Peer review currently lands on senior testers who are mid-engagement, creating a second invisible queue on the same people.

**Protect the gap in the calendar.** A minimum interval between engagements, defended as a delivery requirement rather than offered as a courtesy, because anything framed as a courtesy disappears under pressure.

## Who Feels the Pain

The tester, working evenings and weekends on the unglamorous half of a job they took for the interesting half, and eventually leaving the profession over it.

The client, receiving a report written by someone tired, a fortnight late, describing a system that has since changed.

The firm, whose margin and capacity figures are wrong by a third of delivery effort, and which loses its most productive people for reasons its own reporting cannot see.

And the profession, which trains operators over years and loses them to a scheduling model nobody has examined.

## Impact If Fixed

Counting the hours once would reframe the entire subject. The number is large, it is currently unknown, and every firm could produce it in a quarter.

Booking write-up time is the whole fix, and it is blocked by a metric rather than by economics — the work is already being done, it is simply being done invisibly by people who are not paid for it.

And reducing the write-up burden through capture and reuse is the one intervention that helps regardless of whether the commercial model changes, which makes it the right place to start.
