# Deal Modelling Libraries as the Trustee's Book of Record

**Niche:** [[niches/trust-companies/structured-finance-trustee-reporting/profile|Structured Finance Trustee Reporting]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Investor-side vendors already code the waterfalls of thousands of deals; the trustee needs the same logic run on actual cash, with rounding, amendments and an audit trail.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to compute every payment-date waterfall, coverage test and investor report correctly from the deal documents and the servicer's or manager's data before the distribution date, and whoever does it with the fewest restatements takes the account.

## The Problem
Trustees and investors code the same deal separately, and discrepancies between the trustee's distribution and the investor's model become disputes.

## What Already Exists
Coded deal libraries from structured finance modelling vendors such as Intex and Moody's Analytics, used by investors and underwriters to project cash flows (profiled as [[niches/sales-finance-companies/auto-abs-deal-analytics/profile|🔍 Auto ABS Deal Modelling & Surveillance Analytics]]).

## The Customization Gap
A book-of-record version needs: actual collections and account balances rather than projected cash flows; exact rounding and day-count conventions as the documents specify; version control tied to each amendment's effective date; the trustee's own tests and report formats; and controls an auditor and the trustee's risk function will accept, including reproducible runs for every past distribution date.

## Target Customer
Structured finance trust operations at trustees seeking to stop maintaining their own deal-by-deal code.

## Impact If Solved
One shared logic for trustee and investors reduces disputes and halves duplicated coding effort (estimate), while the trustee keeps control of the calculation it signs.
