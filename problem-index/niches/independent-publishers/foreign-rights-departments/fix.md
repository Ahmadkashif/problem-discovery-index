# Automated Rights Reversion and Royalty Collection Tracking

**Niche:** [[niches/independent-publishers/foreign-rights-departments/profile|Foreign Rights Departments]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** Rights contracts include reversion clauses (rights return to the publisher if the licensee doesn't publish within 2 years or lets the translation go out of print), but nobody tracks these deadlines — so territories sit locked up with licensees who never publish or stopped paying royalties.
**Tags:** #automation #compliance #workflow-orchestration #revenue-impact

## The Problem
A rights manager has sold Korean rights to Title X with a contract requiring publication within 24 months and annual royalty reporting. The Korean publisher delays publication. The contract says rights revert after 24 months of non-publication, but the rights manager doesn't notice because the reversion date is buried in a Word document stored in a folder called "Korea Deals." Three years later, another Korean publisher wants to acquire the same title — but the rights are technically still sold to the non-performing licensee. The rights manager must now negotiate a reversion (a legal process), losing months and potentially the new deal. Meanwhile, 40% of active rights deals are delinquent on royalty payments, but nobody sends collection notices because the rights manager doesn't have time to audit 200 contracts for payment status.

## Why It's Still Broken
Rights contracts are stored as individual Word or PDF files in folders organized by territory or publisher. Extracting the contractual obligations (publication deadline, royalty reporting dates, reversion triggers) requires reading each contract — a task that nobody does proactively. Enterprise rights management platforms (Klopotek) have contract fields for these dates, but setting them up requires entering data from hundreds of existing contracts. The rights manager, typically a solo role at an indie press, doesn't have 80 hours to backfill contract data. So the system stays manual, and reverted territories go unrecognized until someone asks about them.

## What a Fix Looks Like
A contract obligation tracker that: (1) extracts key dates and obligations from rights contracts using document parsing (publication deadline, royalty reporting frequency, reversion triggers, advance payment schedule), (2) maintains a calendar of upcoming obligations by licensee, (3) auto-generates reminder emails to licensees when royalty reports or payments are overdue, (4) flags territories where reversion triggers have been met (publication deadline passed, royalties unpaid for 2+ reporting periods), (5) generates a reversion notice template that the rights manager can customize and send. The initial data entry challenge is solved by LLM-powered contract parsing — upload the PDF, the system extracts the relevant terms and asks for confirmation.

## Who Feels the Pain
Rights managers who discover years later that valuable territories were locked up with non-performing licensees, and publishers losing $10K–$50K annually in uncollected foreign royalties.

## Impact If Fixed
Identifies an estimated 10–15% of sold territories eligible for reversion and relicensing, recovering $20K–$100K in potential advance revenue for a mid-size indie catalog. Improves royalty collection rates from 60–70% to 90%+ through systematic follow-up. Reduces the rights manager's contract review overhead from 20+ hours per quarter to 2–3 hours.
