# Lineage: IT Staffing Firms

**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** DICE — the Data Processing Independent Consultants Exchange, a dial-up bulletin board opened in 1990 where staffing and consulting firms posted contract IT requisitions for technical contractors, later dice.com
**Builder:** Dice
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A contract programmer's next job was a phone call away, and nobody had the list of phone numbers.

IT contracting runs on short engagements. A COBOL or Unix contractor finishes a six-month project and needs the next one within weeks; a staffing firm holds a client requisition that must be filled before a competitor fills it. Both sides were matching through recruiter phone networks, newspaper classifieds and word of mouth — slow, local and invisible to anyone outside the circle.

Federal tax law had tightened that circle. **Section 1706 of the Tax Reform Act of 1986** removed the Section 530 safe harbour for firms placing "technical service workers" — engineers, drafters, computer programmers, systems analysts — with client companies. In these three-party arrangements only the common-law employment test applied, which pushed independent IT contractors toward working through a broker or staffing firm rather than billing clients directly. The intermediary was now structural, and intermediaries need inventory.

## What Got Built

A bulletin board system — a computer you dialled into with a modem — carrying open contract positions.

DICE was not a public job board. Access was restricted to **technical contractors on one side and recruiting, staffing and consulting firms on the other.** The recruiters posted requisitions; contractors dialled in and read them. There were no hiring companies on it at first, which is the point: it was a marketplace for the intermediated contract trade specifically.

The service moved headquarters to Des Moines, Iowa, in the mid-1990s, went onto the web as dice.com, and only then opened to companies hiring directly. EarthWeb, a New York public company, acquired it in 1999; EarthWeb later renamed itself Dice Inc.

## Who Built It, And Why Them

Lloyd Linn and Diane Rickert, who founded DICE in the San Francisco Bay Area in 1990 — and who were, by every account found, **former contractors themselves.**

That is the reason it looked the way it did. A general employment site would have courted employers, because employers were the obvious payers. People who had lived the contract cycle knew the requisitions that mattered sat with the agencies, and that the contractor's problem was the gap between engagements, not a career search. So they built for the two parties actually in the transaction after 1986: the staffing firm with an open req, and the contractor about to roll off.

The dial-up form was a consequence of timing, not of choice. In 1990 there was no commercial web to build on. A BBS was the cheapest way to put a shared, continuously updated list in front of a technically literate audience — and IT contractors were an audience that already dialled into systems for a living.

## What It Cost

**A requisition board matches on words.** A posting names technologies; a contractor's profile names technologies back. The match is a string match between two self-declared lists, and neither side has to prove anything.

That was an acceptable trade when the users were a small community who often knew each other's reputations. It scaled badly. Once every contractor learned which keywords surfaced them, skill lists grew to match the searches, and the staffing firm's screening burden shifted from *finding* candidates to *disbelieving* them.

The second cost was commercial. Opening the board to direct employers put the service in competition with its founding customers — every requisition a client posted directly was one it did not route through a staffing firm.

## What You Still Touch

Keyword search over self-reported skills is still the front door of technical recruiting, and the thing a recruiter spends their day compensating for. That line runs from DICE's design to today's fraud-detection problem — on this note's reading, not by any documented design intent.

- [[problems/it-staffing-firms/high-impact|🔴 Technical Candidate Skill Authenticity Detection]] — the bill for matching on declared keywords
- [[problems/it-staffing-firms/worker-life-1|🟢 Recruiter Tech-Stack Learning Curve]]
- [[problems/it-staffing-firms/low-impact-1|🟡 Rate Card Management by Technology & Market]]
- [[niches/it-staffing-firms/technical-assessment-platforms/profile|Technical Assessment Platforms]]
- [[niches/it-staffing-firms/worker-classification-advisory/profile|Worker Classification Advisory]] — Section 1706's still-live residue

**Sources:** Wikipedia, *Dice.com* (founders Lloyd Linn and Diane Rickert, "two former contractors", 1990, Bay Area BBS; Iowa move; EarthWeb 1999; Dice Inc. 2001); Silicon Prairie News, *Dice Holdings' Paul Melde talks about history of Dice.com & its Iowa base* (2010) (founders, 1990, San Francisco, EarthWeb 1999); search-result summaries of HandWiki / Wikipedia text for the full name "Data Processing Independent Consultants Exchange" and the contractor-and-staffing-firm-only access rule; Congressional Research Service report 98-481, *Independent Contractors: Repeal of Section 1706 of the Tax Reform Act of 1986 for Technical Service Workers*, and IRS, *Worker reclassification – Section 530 relief* (Section 1706 scope and effect). ⚠️ **Sources disagree** on the Iowa move (1994 vs 1995), the web launch (1996 vs purchase of the dice.com domain in 1997) and when direct employers were admitted (1998 vs 1999) — hence "mid-1990s" and undated wording above. ⚠️ **Not established:** DICE's original pricing and who paid (posting fees vs subscriptions); and any documented statement by the founders that Section 1706 motivated the business — the 1986 statute is offered as context, not as their stated reason.
