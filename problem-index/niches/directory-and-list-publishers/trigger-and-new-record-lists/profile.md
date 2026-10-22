# Trigger & New-Record Lists

**Parent Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to deliver the new record first — the business that filed last week, the household that moved last weekend — with the fewest false triggers, and whoever delivers the freshest trigger at a measured false-trigger rate takes the account.

## Profile
**Market Size:** ~$350M US spend on new-business, new-mover, new-homeowner and similar trigger lists (estimate)
**Share of Parent Industry:** ~4% of the ~$8B US buyer spend on directories, lists and compiled business data, including directory advertising (estimate; see overview)
**Digital Adoption:** High — weekly or daily files and API feeds built from public records and other sources
**Target Buyer:** Marketing director at an insurer, bank, utility, home-services or B2B services firm; list resellers
**Automation Potential:** Very high — ingestion, filtering, matching and delivery are pipeline work once the inference rules are right

## What Makes This a Distinct Niche
A trigger list sells an event, not a universe: a business just formed, a family just moved in, a home just sold, a new licence just issued. Buyers — insurers, banks, payroll and merchant-services firms, home-services companies, local retailers — want to reach people at the moment of need, and value decays by the week. The inputs are mostly public records (state business filings, county deed recordings, licence boards) and indirect move signals, because USPS licence terms forbid building new-mover lists from NCOALink data. The hard part is inference: deciding which new filing is a real operating business rather than a holding company at a registered agent's address, and which address change is a real move.

## Current Tools & Gaps
Bulk downloads and scrapes of state registries, county recorder feeds from property-data aggregators, licence-board files, and rules to filter and match them. Gaps: false triggers (re-filings, shell entities, registered-agent addresses, refinances misread as sales) are filtered by hand-tuned rules with no measured error rate; latency is not reported per source; and the same event arrives from several sources days apart and is sold twice.

## Problems
- [[niches/directory-and-list-publishers/trigger-and-new-record-lists/build|🔨 Build: A False-Trigger Rate Measured, Not Guessed]]
- [[niches/directory-and-list-publishers/trigger-and-new-record-lists/buy|🛒 Buy: Public-Records Feeds Pointed at Trigger Lists]]
- [[niches/directory-and-list-publishers/trigger-and-new-record-lists/fix|🔧 Fix: The New Business That Is a Registered-Agent Filing]]
