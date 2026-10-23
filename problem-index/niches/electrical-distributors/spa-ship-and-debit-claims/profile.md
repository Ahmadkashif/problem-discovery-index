# Manufacturer SPAs & Ship-and-Debit Claims

**Parent Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to turn every job-specific SPA the distributor quoted into a paid ship-and-debit credit — the 844 claim accepted on the manufacturer's 849 — before the agreement or claim window closes, and whoever gets the most SPA dollars paid on first submission takes the account.

## Profile
**Market Size:** ~$8–12B a year of ship-and-debit credits owed by manufacturers to US electrical distributors (estimate: ~20–40% of project sales on SPA pricing, credits of ~15–30% of cost); the labour and software spent claiming it is ~$250M (estimate)
**Share of Parent Industry:** ~5–8% of EW's ~$151.2B distributor sales estimate (search summary) in claimable credit (estimate)
**Digital Adoption:** Low — claims move on EDI, but agreements are keyed from PDFs and portals and 849 rejections are worked in spreadsheets
**Target Buyer:** CFO or controller at the distributor; SPA or rebate analysts who run the desk
**Automation Potential:** High — agreement extraction, line matching and rejection handling are mechanical once terms are structured

## What Makes This a Distinct Niche
In electrical distribution the SPA is a project instrument. It is requested at quote time for a named contractor and job, granted by the manufacturer (often through its rep agency) with a product list, quantities and an expiry, and settled through ship-and-debit: the distributor buys at normal cost, sells at the SPA price and files an EDI 844 per line, and the manufacturer's 849 accepts, adjusts or rejects each line with a reason code. Industrial distributors claim SPAs too, mapped at [[niches/industrial-distributors/rebates-and-spa-claims/profile|Supplier Rebates & SPA Claims]], which left electrical to this build; the electrical difference is that the agreement is tied to a job, so jobs that slip, releases spread across branches and contractors who reuse SPA pricing on other jobs are the main leaks. Third-party claim administration and recovery services are logged once, at [[niches/industrial-distributors/rebate-spa-claim-administration/profile|Rebate & SPA Claim Administration Services]].

## Current Tools & Gaps
EDI translators and networks for 844/849, manufacturer portals, Epicor Eclipse contract-pricing tables, rebate platforms such as Enable and Vistex, and spreadsheets. The gaps: SPA numbers keyed by hand under the wrong job or ship-to, expiries missed when jobs slip, quantity caps consumed invisibly across branches, and 849 reason codes never analysed.

## Problems
- [[niches/electrical-distributors/spa-ship-and-debit-claims/build|🔨 Build: The 849 Rejection Worked Before the Window Closes]]
- [[niches/electrical-distributors/spa-ship-and-debit-claims/buy|🛒 Buy: EDI Platforms Taught to Read SPA Agreements]]
- [[niches/electrical-distributors/spa-ship-and-debit-claims/fix|🔧 Fix: The Job That Slipped Past Its SPA Expiry]]
