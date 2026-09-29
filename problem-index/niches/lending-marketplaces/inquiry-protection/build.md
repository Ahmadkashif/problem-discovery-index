# Inquiries as a Managed Cost

**Niche:** [[niches/lending-marketplaces/inquiry-protection/profile|Inquiry Protection]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The borrower's credit file is a finite resource the marketplace spends freely because the cost lands entirely on them.
**Tags:** #gradient-boosting #evaluation-metrics #optimization-fundamentals #confidence-intervals #compliance #automation #logistic-regression #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to stop spending the borrower's credit file on applications that will be declined — and whoever treats the inquiry as a cost rather than as free takes the trust the category has never had.

## The Problem
A borrower is routed to four lenders, applies to all four, and is declined by three. Three hard inquiries now sit on their file, visible to every future lender, slightly reducing their score at the moment they most need it. The marketplace was paid for all four handoffs. No system anywhere counts the inquiries generated, no target constrains them, and no model trades an inquiry against the probability of approval, because the cost is borne by someone with no seat at the table.

## Why Nobody Has Built This
The inquiry is free to the marketplace, so it never appeared in any model or metric — an externality that no accounting captures is one nobody manages. Soft-pull prequalification requires lender support that is uneven. More applications produce more funded loans in expectation, which is the revenue-maximising behaviour absent a constraint. And nobody has been made to answer for the aggregate.

## What to Build
Put the inquiry in the objective. Count inquiries generated per borrower and report inquiries per funded loan, which is the core and is a metric that does not exist anywhere in the industry today. Prefer soft-pull prequalification wherever a lender supports it, since it makes most of the problem disappear and is already partially available. Sequence applications rather than sending them in parallel, because a borrower approved by the first lender never needs the other three and parallel submission is chosen for speed rather than for them. Use approval prediction to suppress applications below a probability threshold, which links this directly to the routing work and is where most of the saving is. Explain the rate-shopping window to the borrower, as multiple inquiries for the same loan type within a period are usually treated as one and almost no consumer knows this. Show the borrower the cost of each application before they make it, which is both honest and likely to improve their decisions. Set an inquiry budget per borrower journey, since an explicit constraint is what makes an optimiser trade properly. Measure the score impact where it is observable, because quantifying the harm makes it manageable. Report the metric publicly, as being the marketplace that minimises inquiries is a genuine trust position in a category with very little. And design the incentives so that inquiry efficiency is rewarded internally rather than penalised.

## Target Customer
Product and compliance leadership, borrowers whose files are being spent, lenders who prefer pre-screened applicants, and regulators examining consumer harm in lead generation.

## Impact If Built
An externality that no accounting captures is one nobody manages, so the inquiry never entered a model or a metric. Counting inquiries per funded loan and suppressing applications below an approval threshold makes the borrower's cost a managed quantity for the first time.
