# The Universe Everyone Buys, Ranked the Same Way

**Niche:** [[niches/private-equity-firms/deal-sourcing/profile|Deal Sourcing & Origination]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every sponsor subscribes to the same private-company databases and filters them by the same size and sector screens, so the "proprietary" pipeline is a list every competitor also has.
**Tags:** #survival-analysis #gradient-boosting #graph-theory #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know that a founder-owned company is becoming sellable — and to be the trusted buyer in the room — before a banker is hired and the price is set by auction.

## The Problem
A business development professional at a mid-market sponsor is responsible for a target list of several thousand founder-owned companies in the firm's sectors. The list comes from PitchBook, Grata or SourceScrub, filtered by revenue, headcount, geography and keywords — the same filters a hundred other sponsors apply to the same database. Outreach is calls, emails and conference meetings, ranked by gut and by whoever responded last. The question that matters — which of these companies will run a sale process in the next eighteen months, and does the founder already know us — is not modelled anywhere.

## Why Nobody Has Built This
The vendors have built generic signals (headcount growth, hiring, web traffic) and sell them identically to all customers, because their business is breadth. The sponsor has the differentiating data — years of touchpoints, call notes, and which relationships turned into deals — but it sits in the CRM as activity history rather than as labelled training data. And outcomes are slow and rare: a firm converts a handful of sourced relationships a year, too few to learn from alone.

## What to Build
A sale-readiness model that fuses vendor signals with the firm's own relationship record. Label historical companies by whether and when they entered a sale process, using transaction databases. Model time-to-process with survival methods so companies with no event yet are handled honestly. Add the features only the sponsor has: number and recency of founder conversations, sentiment of notes, whether an advisor or banker has been mentioned, which partner knows whom. Rank the business development team's weekly call list by expected value — probability of process times probability the firm wins given relationship depth. Close the loop by recording why each touch did or did not progress, so the model learns from the firm's own conversion rather than the vendor's population. Offer a consortium variant for smaller sponsors without enough history.

## Target Customer
Heads of business development and managing partners at lower-middle and middle-market sponsors with a dedicated sourcing team of three or more.

## Impact If Built
Business development time is the scarcest sourcing input and is currently allocated by database filter. A readiness ranking built on the firm's own conversion record directs it toward the companies that will actually trade, earlier, and turns a commodity data subscription into something competitors cannot copy.
