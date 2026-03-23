# Zero Job Profitability Visibility

**Niche:** [[niches/metal-fabrication/small-custom-job-shops/profile|Small Custom Job Shops (<20 Employees)]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Fix (Pain Point)
**One-liner:** Small fab shop owners know whether the shop made money last month from checking the bank account — they have no idea which of their 30 active jobs made money and which lost money, because no system tracks actual time and material per job.
**Tags:** #automation #revenue-impact #worker-facing

## The Problem
A small fab shop produces 20-40 jobs per month. Each job was quoted at a specific price based on the owner's estimate. Actual production may differ: a job estimated at 8 hours of welding takes 12 because the fit-up was tighter than expected; a job estimated at $400 in material uses $600 because the first set of parts didn't fit. The owner doesn't know about these overruns at the job level — they see the aggregate result in the monthly bank balance. If the shop quoted $200,000 in work last month and the bank balance went up by $15,000, the owner knows they're roughly at 7.5% margin — but not that 5 of their 30 jobs lost money while 25 were profitable, and the 5 unprofitable jobs consumed the margin from the profitable ones.

## Why It's Still Broken
Per-job profitability tracking requires: (1) time tracking per job (operators logging hours against specific jobs), (2) material tracking per job (knowing which material was consumed on which job), and (3) overhead allocation (applying a fair share of shop overhead to each job). Steps 1 and 2 require a tracking system that operators will actually use — and in a small shop where the owner works alongside the crew, introducing a time-tracking system feels like bureaucracy. Step 3 requires a cost model that most small shop owners don't know how to build. The result: nobody tracks anything at the job level, and the owner discovers profitability problems months after they've accumulated.

## What a Fix Looks Like
A radically simple job-level cost tracker: at job start, the operator taps "start" on a tablet or phone (linked to the job number); at job end, they tap "stop." Material cost is estimated at job creation from the quote and adjusted at completion if additional material was used. Overhead is applied as a configurable hourly rate. At job completion, the system shows: quoted price, actual labor hours x shop rate, actual material cost, overhead applied, and job profit/loss. A monthly dashboard shows top 5 profitable and bottom 5 unprofitable jobs — giving the owner the data to adjust pricing, decline unprofitable work, or investigate why specific jobs consistently overrun.

## Who Feels the Pain
Shop owners who sense that certain job types or customers are unprofitable but lack data to confirm it or quantify it.

## Impact If Fixed
Surfaces the 15-25% of jobs losing money that the owner currently can't identify. Enables data-driven pricing adjustments that improve overall shop margin by 2-5 percentage points. For a $2M/year shop operating at 6% margin, improving margin by 3 points adds $60,000 in annual profit — often the difference between the owner taking a salary and not.
