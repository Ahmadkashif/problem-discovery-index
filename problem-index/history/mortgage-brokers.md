# History: Mortgage Brokers

**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** [[origins/credit-bureaus/profile|Credit Bureaus]]
**Episode Tier:** 1
**Transferable Pattern:** A computation can be compressed to seconds and the business built on it can still run at the speed of the slowest mandatory clock in the room — because the clock is the law, not the software.

> **Wave-assignment note.** Mortgage brokers never got an SAP. The client-server-era system this industry actually built was the **LOS — the Loan Origination System**: Byte, Calyx Point, and what became Ellie Mae's Encompass. Read "Wave 4" as "the LOS generation." The computation that matters most here — automated underwriting — wasn't client-server software at all. It was a decision service two GSEs stood up on their own wires, closer in spirit to Wave 5.

## Before

A broker's entire asset was a private map: which of a few dozen wholesale lenders would say yes to a specific borrower, on what terms, this week. Before the mid-1990s that map was tested by hand — a paper file, assembled by a loan officer, read by a salaried human underwriter against a lender's written overlays. Turnaround ran **days to weeks**, and the judgement inside it was exactly the one this vault's credit-bureaus origin describes: *should a lender's decision rest on what a person believes about a borrower's character, or on a statistic computed from their record?* Through the 1980s that question was still mostly settled by asking a person.

## The Origin Event

There is a real one, and it's not a founding but a **launch of a decision service**: Fannie Mae's **Desktop Underwriter (DU)** and Freddie Mac's **Loan Prospector (LP)**, both brought to market in the mid-1990s as automated underwriting systems (AUS) — software that takes a loan file and returns a recommendation in minutes rather than the days a human file review took.

> **Flagged, honestly.** This session's search-engine access was exhausted mid-task and most GSE/vendor history pages returned 403s or 404s to direct fetches, so an exact launch year for DU or LP could not be pinned to a primary source. **1995 is the year overwhelmingly cited in trade literature for both**, and it is corroborated circumstantially by one fact this session did confirm live: Freddie Mac required lenders to use FICO scoring on **all** new mortgage applications starting in **1995** — same company, same year, same underwriting-automation push. Treat 1995 as likely, not confirmed.

What both systems did, confirmed by general industry description: took a file — credit, income, assets, the loan — and returned a decision "in minutes rather than days," progressively **reducing the documentation required** as the model's confidence in the file substituted for manual line-by-line verification. Freddie Mac's product was later renamed **Loan Product Advisor (LPA)**; the renaming date is unverified.

This is the credit-bureaus argument re-fought one layer up. FICO (Fair, Isaac 1956, first scorecards 1958, bureau-wide FICO with Equifax 1989, all three bureaus by 1991, FCRA 1970/71) settled *whether a number could stand in for a person's payment character*. DU and LP settled the next question: *whether a number could stand in for an underwriter's judgement of a whole file.* Loan officers didn't disappear, but the default first opinion on a loan stopped being a human read of a paper stack and became a service call to a GSE's own computers.

## What Became Cheap

**The underwriting decision itself** — not the loan, the *decision*. A recommendation that used to occupy a trained underwriter for a day or more became a same-session query answer: judgement compressed into a service.

What did **not** become cheap is the whole shape of this episode: *closing* the loan. Income and asset verification, appraisal, title, insurance, and — from the 2010s — a federally mandated disclosure and waiting sequence, none of which cares how fast the underwriting engine answered. The broker's old edge — knowing which of 30–50 wholesale lenders would clear a file, and clearing it fast — had its slowest step automated. The other steps didn't move, and a new one got added by statute.

## How It Was Actually Solved — the LOS and the plumbing under it

**The LOS.** Byte Software and Calyx Point (Calyx Software) served the broker channel by the 1990s; founding years for both are unverified this session. **Ellie Mae**, founded **1997** by Limin Hu and Sigmund Anderman as "Electronic Mortgage Affiliates," built **Encompass** into the dominant cloud LOS. It went private under Thoma Bravo in **April 2019** (~$3.7B); **Intercontinental Exchange announced its acquisition in August 2020** (~$11B), **closing September 2020** — combined with ICE's earlier MERS (2016/2018) and Simplifile (2019) deals into today's **ICE Mortgage Technology**. Wave 4's thesis holds exactly: the LOS became the system of record, and owning the record became worth more than any feature in it — enough that a stock exchange operator bought it.

**The standard.** **MISMO**, the Mortgage Industry Standards Maintenance Organization, is a wholly owned nonprofit subsidiary of the Mortgage Bankers Association (175+ member organisations today) whose purpose is this vault's EDI/UPC pattern exactly: an agreed data format nobody individually owns, so a file means the same thing to every LOS, AUS, and investor. MISMO's founding year is unverified this session, though its stated role — "reduces processing costs, increases transparency, boosts investor confidence" — is the mortgage industry's own format war, settled because everyone needed it settled.

**The AUS.** DU and LP/LPA, above — the layer that actually moved a turnaround time, not just a file format.

## The Contest — the broker's edge was never really about speed

The obvious reach is broker-versus-retail-lender competition, or wholesale lenders bidding for broker volume. Sharper: **once underwriting was equally fast for everyone with DU or LP access, what was a broker still selling?**

The subprime-era answer: **access and pricing, not judgement.** Wholesale lenders paid brokers **yield spread premiums** — a rebate for placing a borrower at a higher rate than they qualified for, documented compensation architecture of the period. The Mortgage Bankers Association's own chairman is on record during the crisis saying brokers "did not do enough to examine whether borrowers could repay." The fight wasn't broker-versus-lender; it was the broker's compensation structure versus the borrower's interest, and regulators eventually adjudicated it.

## The Binding Constraint — this is the episode

DU and LP did their job: underwriting that took days now takes minutes. The broker channel's bottleneck since 2008 hasn't been computational — it's been **regulatory**, arriving in three layers stacked on the channel automation had just made fast:

**1. The SAFE Act (2008).** Title V of the Housing and Economic Recovery Act of 2008 required every state to license and register mortgage loan originators through a single national system — the **NMLS**, which had actually started **January 2008** as a *voluntary* registry from the Conference of State Bank Supervisors and the American Association of Residential Mortgage Regulators, covering seven states. SAFE made it mandatory nationwide, attaching pre-licensing education and a permanent, portable originator ID to every loan officer — the same "identifier follows the person" logic as FCRA-era credit files, now applied to the person originating rather than the person borrowing. This raised the cost of *becoming* a broker. It did nothing to underwriting speed.

**2. Dodd-Frank's loan-officer compensation rule (2010, implemented 2013–2014).** Dodd-Frank statutorily banned originator compensation that varies with a loan's terms — killing the yield-spread-premium mechanic at its root. The CFPB, formally stood up **July 21, 2010** and empowered to enforce from **July 21, 2011**, issued the implementing final rule **January 20, 2013** (published February 15, 2013), effective **January 10, 2014**. This is the direct regulatory answer to the contest above: it didn't change broker speed, it removed the lever — steering a borrower into a worse rate for a bigger rebate — that had made speed-plus-access profitable in the wrong direction.

**3. TRID (2015).** The TILA-RESPA Integrated Disclosure rule, required by Dodd-Frank, took effect **October 2015**, replacing the Good Faith Estimate/HUD-1/Truth-in-Lending forms with the integrated Loan Estimate and Closing Disclosure. *(October 2015 is confirmed live; the specific day, widely cited elsewhere as October 3, is not re-verified this session.)* TRID attaches **mandatory waiting periods** around the Closing Disclosure before a loan can fund — a fixed regulatory clock, indifferent to how many seconds DU or LP took weeks earlier.

**This is dental practices' annual maximum wearing different clothes.** DU and LP moved the constraint computation could actually move. SAFE Act, the compensation rule, and TRID are three un-erasable clocks and floors that computation cannot touch, because they measure statutory compliance, not a computation. An FDE selling a broker "faster underwriting" in 2026 is automating a step that was already automated thirty years ago, while the three steps that were never computational sit untouched.

## The Graveyard — a lender, not a brokerage, and the distinction matters

**New Century Financial** filed Chapter 11 on **April 2, 2007**, after more than half its eleven warehouse lenders pulled funding within weeks — one of the first visible failures of the subprime era. Precision matters here, the way freight-brokerage's episode insists Convoy's death not become "digital freight brokerage failed": **New Century was a wholesale *lender* depending on the broker channel for volume, not a brokerage itself.** The failure is real and dated. What is *not* confirmed this session is any count of independent brokerages that closed after 2007–2010, or a verified market-share time series for the channel.

> **A genuine gap, recorded as one.** No accessible source this session gave the broker channel's market-share trajectory over time. The vault's hub note gives today's snapshot (~25% / ~$500B of ~$2T in annual originations, ~15,000 firms) but no verified before-and-after curve across the SAFE Act, the crisis, and Dodd-Frank. Trade press widely asserts a large contraction after 2007 and a partial recovery since roughly the mid-2010s — but this session cannot cite that shape with a verified number, and shouldn't be trusted with one until re-researched with working search access.

## What's Still Open

- [[problems/mortgage-brokers/high-impact|🔴 Lender matching as a system instead of tribal knowledge]] — the underwriting decision got fast; knowing *which* of 30–50 lenders to send it to first never did
- [[problems/mortgage-brokers/low-impact-1|🟡 Document extraction for self-employed borrowers]] — DU/LP's appetite for less documentation stops at K-1s and depreciation schedules
- [[problems/mortgage-brokers/worker-life-1|🟢 Condition clearing]] — the manual chase TRID's fixed clock makes expensive to delay
- [[problems/mortgage-brokers/low-impact-2|🟡 Compliance review]] — reading every disclosure line for exceptions nobody can compute away
- [[niches/mortgage-brokers/self-employed-borrower-specialists/profile|Self-Employed Borrower Specialists]]
- [[niches/mortgage-brokers/condition-clearing-automation/profile|Condition Clearing Automation]]
- [[niches/mortgage-brokers/mortgage-qc-compliance-audit/profile|Mortgage QC & Compliance Audit]]
- [[niches/mortgage-brokers/lender-submission-routing/profile|Lender Submission Routing]] — the tribal-knowledge map, as a system
- [[niches/mortgage-brokers/non-qm-specialty-brokers/profile|Non-QM Specialty Brokers]] — the segment that exists precisely because DU/LP's automated box has edges
- [[niches/mortgage-brokers/los-vendor-data-teams/profile|LOS Vendor Data Teams]] — where Encompass's owner sits now

## The Transferable Pattern

> **Find the fastest computation in the business, then ask what clock still runs after it finishes. If that clock is set by statute, no model retrains it away — and the software worth building serves the clock, not the computation.**

DU and LP are a clean instance of a pattern this vault keeps finding: a professional judgement — "will this file clear" — collapsed into a service call. That's the FDE's most legible opportunity, and it's real: lender-matching, document extraction, and condition-clearing in this industry are still-open versions of the same compression, one layer further out than DU/LP reached.

But the harder lesson, one dental practices taught first and this industry confirms independently: **a fast computation embedded in a slow, mandatory, legally-set process does not make the process fast.** The SAFE Act's licensing bar, Dodd-Frank's compensation ban, and TRID's waiting period aren't inefficiencies waiting for a model — they're the floor. An FDE who ships "underwriting in seconds" to a broker in 2026 has automated a step that was already automated thirty years ago, and left untouched the steps that were never computational to begin with.

**Sources:** Wikipedia — *Ellie Mae* (founding 1997; Thoma Bravo 2019; ICE announcement/close 2020); *Intercontinental Exchange* (Ellie Mae close Sept 2020; MERS 2016/2018; Simplifile 2019; "ICE Mortgage Technology"); *MISMO* (MBA subsidiary, 175+ members, purpose); *Mortgage underwriting in the United States* and *Mortgage industry of the United States* (DU/LP existence, LPA naming, minutes-not-days framing, reduced documentation); *Credit score in the United States* (Freddie Mac mandatory FICO use, 1995); *Nationwide Multi-State Licensing System and Registry* (NMLS founded Jan 2008 by CSBS/AARMR, 7 states, SAFE Act mandate, unique identifier); *Provisions of the Dodd–Frank Wall Street Reform and Consumer Protection Act* (originator compensation ban, unique-identifier requirement, CFPB established July 21 2010 / enforcement July 21 2011); *Mortgage origination* (TRID effective Oct 2015, Loan Estimate/Closing Disclosure); *New Century Financial* (Chapter 11, April 2 2007; warehouse-lender pullback); *Subprime mortgage crisis* (MBA chairman quote; broker incentive structure). Consumerfinance.gov, loan originator compensation final rule page (issued Jan 20 2013, effective Jan 10 2014). This vault's `industries/mortgage-brokers.md` and `origins/credit-bureaus/legacy.md`.

**Not independently verified this session — flag before script use:** exact launch years for DU and LP (1995 widely cited, unconfirmed here); MISMO's founding year; founding dates for Byte Software and Calyx Point; the exact TRID effective day ("October 3" not re-confirmed); any broker-channel market-share time series across the crisis and Dodd-Frank.
