# Lineage: Crowdsourcing Platforms

**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Amazon Mechanical Turk and its Human Intelligence Task (HIT) — a unit of work posted through an API at a price the requester sets, and approved or rejected by that requester
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Amazon's catalogue had duplicates, and no program could find them.

Around the turn of the millennium the Amazon marketplace accumulated tens of thousands of duplicate product pages — the same can opener listed twice under slightly different titles and photographs. Engineers tried automated matching and, by IEEE Spectrum's account, gave up and called the problem insurmountable. Telling whether two pictures and two blurbs describe the same object is trivial for a person and was intractable for software.

Hiring staff to walk the catalogue was the alternative. The work was enormous in total, tiny in each unit, and not worth a full-time employee at any single moment.

## What Got Built

A marketplace in which a program can call a person.

A requester breaks a job into small pieces — "are these two product pages the same item?" — and posts each piece as a **HIT**, with a price attached. Anonymous workers, identified by number rather than name, pick HITs off a list, complete them and submit. The requester reviews the result and **approves or rejects** it; approval triggers payment and rejection feeds the worker's reputation. Everything is callable through an API, so a program can post work, wait and read the answer as if it were a slow function call.

It ran internally first and opened to the public on **2 November 2005**, named after the eighteenth-century chess "automaton" that concealed a human player. Jeff Bezos's phrase for it was "artificial artificial intelligence".

## Who Built It, And Why Them

**Amazon**, from a patent by **Venky Harinarayan, Anand Rajaraman and Anand Ranganathan**: "Hybrid machine/human computing arrangement", priority date **19 March 2001**, granted 2007 as US 7,197,459. It describes a central server that decomposes a task into subtasks, dispatches them over the internet to human-operated nodes, verifies answers by majority vote or accuracy weighting, and pays according to quality.

Harinarayan and Rajaraman had arrived through Amazon's August 1998 acquisition of Junglee, their comparison-shopping company. Comparison shopping lives or dies on recognising the same product across different listings, so the likeliest answer to **why them** is that they already knew where machine matching failed — and they worked for the one retailer whose catalogue made the problem large enough to need a thousand strangers.

**Why Amazon rather than a staffing firm:** Amazon was already the requester. The duplicate problem was its own, and it had the payments system and customer accounts to pay millions of tiny amounts. Selling the tool outside was the second step, not the first.

## What It Cost

**The design put every judgment in the requester's hands.**

A system built for Amazon to clean its own catalogue assumed the requester was competent and honest: it knew what the task should pay and could tell good work from bad. So the requester sets the price per HIT without knowing how long it takes, and the requester decides whether to pay after seeing the work. The worker, anonymous by design, has no field in which to be told why. IEEE Spectrum cites a 2017 study putting median worker earnings around $2 an hour, with 4% above the US federal minimum wage — the realised rate of a price set per piece by someone who never timed the piece.

Rejection was also the quality mechanism. Paying only for approved work made quality the worker's cost, not the platform's, which is why gold-standard questions and approval-rate thresholds became the industry's default instruments.

## What You Still Touch

Every annotation job, survey panel and labelling queue that prices work per item and lets the buyer reject after delivery runs the 2001 patent's bargain.

- [[problems/crowdsourcing-platforms/high-impact|🔴 Pay Is Set Per Task by Someone Who Does Not Know How Long It Takes]] — the requester-set HIT price
- [[problems/crowdsourcing-platforms/worker-life-1|🟢 The Worker Whose Submission Was Rejected Without a Reason]] — approve/reject with no reason field
- [[problems/crowdsourcing-platforms/low-impact-1|🟡 Quality Control Beyond Gold Standards]]
- [[niches/crowdsourcing-platforms/pay-setting-and-rate/profile|Pay Setting & the Realised Rate]]
- [[niches/crowdsourcing-platforms/requester-reputation/profile|Requester Reputation & Trust]]
- [[niches/crowdsourcing-platforms/error-cost-allocation/profile|Error Cost Allocation]]

**Sources:** Google Patents, US7197459B1, "Hybrid machine/human computing arrangement" (inventors, Amazon Technologies assignee, priority 19 March 2001, filed 12 October 2001, granted 27 March 2007, subtask/consensus/quality-pay description); IEEE Spectrum, "Untold History of AI: How Amazon's Mechanical Turkers Got Squeezed Inside the Machine" (duplicate-products problem, "insurmountable", Bezos's "artificial artificial intelligence", numbered worker IDs, 2017 wage study figures — cited second-hand, study not read); Wikipedia, *Amazon Mechanical Turk* (HIT terminology, chess-automaton name, approve/reject affecting reputation, 20% minimum commission as of 2019); Wikipedia, *Venky Harinarayan* (Junglee founded 1996, acquired by Amazon August 1998, credited as an inventor of the MTurk concept); Slashdot, 4 November 2005, and secondary accounts for the 2 November 2005 launch. ⚠️ **Not established:** the Junglee-to-entity-matching link is my inference from Junglee's comparison-shopping business, not a statement by the inventors. Whether rejection without a stated reason was a deliberate design decision or an omission was not found. The history of MTurk's commission rate before 2019 was not verified and is not asserted.
