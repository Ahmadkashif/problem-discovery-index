# The Star Lost to Eleven Members

**Niche:** [[niches/health-insurance-carriers/regional-provider-sponsored-plans/profile|Regional & Provider-Sponsored Health Plans]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** In a small contract, a handful of members can move a measure across a cut point, and the plan finds out when the ratings are published.
**Tags:** #confidence-intervals #monte-carlo-methods #descriptive-statistics #evaluation-metrics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to give a 30,000-to-300,000-member plan the Stars, risk adjustment and interoperability capability a national carrier staffs internally, and whoever keeps a small plan's Star rating and risk scores level with its national competitors' without new analyst headcount takes the account.

## The Problem
A regional MA contract may have a few hundred members in a measure's denominator. A national contract has hundreds of thousands. When cut points sit close together, a dozen members' open care gaps decide whether the measure earns three stars or four, and a summary rating crossing 4.0 decides quality bonus payments (recalled).

## Why It's Still Broken
Small plans track measures as point rates against last year's cut points, without the uncertainty that comes from small samples or the fact that cut points move every year. Nobody tells them which members are pivotal.

## What a Fix Looks Like
Simulate each measure's year-end rate and its probability of each star level, using the open gaps, likely closure rates and a forecast range for cut points. Rank the specific members whose gap closure most changes the probability of crossing the next cut point, and give that list to the care team every week.

## Who Feels the Pain
Quality directors at small plans; finance teams budgeting bonus revenue; members whose care gaps would have been closed if anyone had known they mattered.

## Impact If Fixed
Outreach goes where it moves ratings, and the plan sees its Star risk months before CMS publishes it.
