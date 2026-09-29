# The Book That Was Customised Once in 2021

**Niche:** [[niches/field-service-software/flat-rate-price-book-content/profile|Flat-Rate Price Book Content]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** Contractors spend weeks customising a price book at implementation and then never touch it again, so a business's entire pricing rests on a set of decisions made in one exhausting month years ago by someone who may have left.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #change-point-detection #confidence-intervals #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in price book content is fighting to make a task's price right for this trade in this market with this contractor's cost structure — and whoever needs the least customisation on arrival takes the account.

## The Problem
Implementation includes price book customisation: thousands of tasks reviewed, times adjusted, materials costs entered, prices set. It takes weeks, it is done under deadline pressure alongside everything else in a platform migration, and it is completed. Then it ossifies. Three years later the book contains tasks the contractor no longer performs, omits ones they perform daily, carries materials costs from a different economy, and reflects a labour rate two raises ago. The contractor knows the book is stale and the prospect of reviewing thousands of tasks again is enough to prevent anyone starting.

## Why It's Still Broken
Price book maintenance is an all-or-nothing task in every product — there is no mechanism that surfaces the twenty tasks worth reviewing this quarter, so the choice is between reviewing everything and reviewing nothing, and nothing wins. Nobody owns it either: it was the implementation consultant's job during onboarding and became nobody's afterwards. And the staleness is invisible, because a stale price still produces an invoice.

## What a Fix Looks Like
Make maintenance continuous and tiny. Rank tasks by how much a pricing error would cost — volume times margin exposure — and surface the top few each month for review with the evidence attached: your cost basis for this task has moved eleven percent, your close rate on it has fallen, your realised labour time is consistently above the book's. Flag tasks quoted frequently that are not in the book, which the technicians are currently handling with a custom line item, and tasks in the book that have not been quoted in two years. Show a staleness date per task so the contractor can see the shape of the problem rather than feeling it. Reviewing five tasks a month with evidence is a habit a business can keep; reviewing four thousand tasks once is a project it will not repeat.

## Who Feels the Pain
Owners whose pricing was set by a departed manager in an implementation sprint; technicians quoting custom line items for work the book does not cover; and the vendors, for whom price book dissatisfaction is the most-cited switching reason in the category.

## Impact If Fixed
Ranking tasks by pricing-error exposure concentrates attention on the small number that actually matter, which is what makes maintenance feasible at all. Contractors who adopt a monthly review habit keep a book that reflects the business, and the vendor removes the single largest source of the churn it currently absorbs.
