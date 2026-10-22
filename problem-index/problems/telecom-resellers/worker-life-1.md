# The Porting Desk's Rejection Loop

**Industry:** [[telecom-resellers|Telecom Resellers]]
**Type:** Worker Life Changing
**One-liner:** A porting specialist spends the day resubmitting orders the losing carrier rejected two weeks late for a missing suite number or an "Inc." that should have been "Incorporated", and gets back the hours and the customer's trust when the order is matched to the carrier's records before it is sent.
**Tags:** #large-language-models #transformers #logistic-regression #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
Every customer a VoIP provider wins arrives with numbers to bring over: the main line printed on the trucks, the toll-free number on the website, forty DIDs behind an old PBX. The porting specialist collects a letter of authorisation and a recent bill, asks the losing carrier for the customer service record (CSR), and submits the order. Then they wait. The order comes back rejected because the company name doesn't match the invoice exactly, the service address lacks a suite, the person who signed isn't the authorised contact, one number in the range was left off, the billing telephone number can't move in a partial port, or there's an old pending order on the account the losing carrier forgot to close. A trade write-up puts simple ports at two to three weeks and complex ones at six to eight, and says carriers often take two to three weeks just to reject.

A specialist at a mid-sized provider juggles dozens of open orders, each in a different carrier portal or email thread, each with its own rejection codes. They spend the day re-reading CSRs against LOAs, chasing customers for a corrected signature, and moving cut-over dates that installers and customers had already planned around.

## Why It Matters to the Worker
The work is repetitive and the blame is not theirs, yet it lands on them. The customer has already told staff the new number goes live Friday. When the port slips, the specialist takes the angry call and the sales rep's escalation, even though the losing carrier's records were wrong and its rejection arrived late. The skill they build, knowing that one carrier wants the address exactly as printed on the bill and another rejects any order with a pending feature change, is valued nowhere and lives in their notes.

The losing carrier has no reason to hurry. The specialist is negotiating with a counterpart whose company is losing the customer, through a portal that returns a code and nothing else.

## What a Solution Looks Like
An assistant that reads the CSR, the bill and the LOA and flags every mismatch before submission, using the carrier-specific rules the desk has learned. It flags exact name and address formatting, numbers missing from a range, a billing number that needs a separate order, and an authorised-contact mismatch. It predicts which orders are likely to be rejected and why. It tracks every order's state across portals, chases firm order commitment dates, drafts the customer update when a date moves, and keeps a record of each carrier's rejection reasons so the next order to that carrier goes out right.

## Impact If Solved
If most rejections are caught before submission, each avoided rejection saves two to three weeks of a customer's waiting and an hour or more of the specialist's rework (estimate). The specialist moves from re-keying and chasing to handling the genuinely hard ports: rural carriers, number blocks and disputed accounts.
