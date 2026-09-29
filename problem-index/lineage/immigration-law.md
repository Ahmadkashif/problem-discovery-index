# Lineage: Immigration Law Firms

**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Visa Bulletin — the State Department's monthly table of priority-date cut-offs, by preference category and country of chargeability, that says whose green-card case may move this month
**Builder:** US Department of State
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An immigration lawyer's client almost never asks "will I be approved?" first. They ask **"when?"**

For most family and employment green cards the honest answer is: when a number is free. Since the Hart-Celler Act, signed on October 3 1965, immigrant visas have been rationed by preference category, with a ceiling on any one country — 20,000 a year in the Eastern Hemisphere under the 1965 scheme. The Immigration Act of 1990, signed November 29 1990, rebuilt the categories as today's family preferences and EB-1 to EB-5, but kept the rationing.

Rationing means a queue, and a queue needs a position. That position is the **priority date** — in practice, the date the petition or labour certification was filed. The expensive part is not filing. It is knowing, for thousands of clients in dozens of category-and-country combinations, which of them the queue has reached, and telling each one before a window opens or closes.

## What Got Built

A monthly document with a fixed grid.

Rows are preference categories — F1 to F4 on the family side, EB-1 to EB-5 on the employment side. Columns are chargeability areas — all countries, then the most oversubscribed countries separately (China, India, Mexico and the Philippines, in the issues commonly cited). Each cell holds either a cut-off date, **"C"** for current, or **"U"** for unavailable. A case whose priority date falls before the cut-off may proceed to a final decision.

The Bulletin now prints two such grids. **Final Action Dates** says who can actually be issued a visa or have status adjusted. **Dates for Filing** says who may submit paperwork early. Each month USCIS separately announces which chart adjustment-of-status applicants must use — the Filing chart only when it judges more visas are available than known applicants.

Priority-date movement in the Bulletin has been tracked and archived since 1995, and the archive is how practitioners reason about **retrogression**: the moment a cut-off moves *backwards*, most visibly for India- and China-born applicants in EB-2 and EB-3.

## Who Built It, And Why Them

The Department of State, because it holds the counter.

Under the preference system the Department allocates the annual numbers worldwide — to its own consulates abroad and, for applicants already in the US, to the domestic adjudicating agency. Only the party issuing the numbers can see demand against supply across every category and country at once, and only that party can say where the line currently stands. Publishing the cut-off was the cheapest way to tell every consulate, every adjudicator and every applicant the same thing on the same day.

**The commercial consequence is that the lawyers did not build it and cannot improve it.** Their entire docketing layer is a consumer of a government table they have no input into. The Bulletin's shape — a grid of dates, not a list of cases — is dictated by how the State Department counts, not by what a law firm needs to track.

## What It Cost

**The Bulletin speaks in categories, not cases.** It tells a firm that EB-2 India moved; it does not tell the firm which of its clients that affects. Every firm rebuilds the join itself — priority date against category against chargeability — every month, usually by hand.

It is also a forecast, not a promise. Cut-offs advance, stall and retrogress, so a client told "current next month" can be told "not current" the month after. The two-chart system added a second decision — which chart applies — made by a different agency on a different page.

## What You Still Touch

Every "your date is current" email an immigration paralegal sends is a hand-computed lookup against this grid, and every missed window is a failure of that join. The case-status portals the vault's problem notes describe are the same pattern repeated: government artefacts published for the government's own counting, which firms must poll and reconcile.

- [[problems/immigration-law/low-impact-2|🟡 Multi-Portal Case Status Monitoring and Intelligent Alerts]]
- [[problems/immigration-law/worker-life-1|🟢 Automated Client Status Updates and Communication Management]]
- [[niches/immigration-law/family-based-petitions/profile|Family-Based Petitions]]
- [[niches/immigration-law/employment-based-visas/profile|Employment-Based Visas]]
- [[niches/immigration-law/case-status-tracking/profile|Case Status Tracking]]

**Sources:** Wikipedia, *Visa Bulletin* (published monthly by the US Department of State; C/U notation; INA 203(a), (b), (c) categories; priority-date movements archived since 1995; EB-2/EB-3 India and China retrogression); Wikipedia, *Immigration and Nationality Act of 1965* (signed October 3 1965; 20,000 per-country Eastern Hemisphere cap); Wikipedia, *Immigration Act of 1990* (signed November 29 1990; EB-1 to EB-5); USCIS, *Adjustment of Status Filing Charts from the Visa Bulletin* (Final Action Dates vs Dates for Filing and USCIS's monthly choice between them). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. travel.state.gov returned 403, and the Cornell LII text of 8 USC 1153 was truncated before subsection (e). ⚠️ **Not established:** the date of the first Visa Bulletin or its predecessor, and the office or official who began it — so the Bulletin's origin is not dated here at all; the year the Dates for Filing chart was introduced (commonly given as 2015, not confirmed this session); and the statutory text requiring numbers to be issued in priority-date order (8 USC 1153(e)), described here from general knowledge of the preference system rather than a fetched quotation. The chargeability columns named are those the Bulletin is commonly shown with; their exact current set was not confirmed against a live issue.
