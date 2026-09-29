# Origin Story: Drowning in Cheques

**Origin:** [[origins/retail-banking/profile|Retail Banking]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]

## What Was True Before

Post-war America wrote cheques, and the number was growing faster than the population of people willing to process them.

Every cheque was handled by hand. A clerk read the account number, found the ledger card, verified the balance, posted the debit, and filed it. Bank of America — the largest bank in the world at the time — was processing so many that branches were closing their doors mid-afternoon to finish the day's posting. The bank projected that at the prevailing growth rate it would need to employ an implausible share of California's workforce.

**This is worth pausing on, because it is the cleanest example in the spine of a business hitting a wall made of arithmetic.** Nobody needed to invent a new product. The existing product simply could not be delivered at the volume customers were demanding it.

## What They Built

Bank of America contracted SRI in 1950. The resulting machine — **ERMA**, the Electronic Recording Machine, Accounting — was publicly unveiled in **September 1955** and went into production, built by General Electric, on **September 14 1959**, processing 50,000 accounts a day.

By 1966 there were 32 ERMA systems across 12 regional centres, covering all but 21 of the bank's roughly 900 branches.

## The Part That Actually Mattered

ERMA's decisive invention was not the computer. It was **MICR** — Magnetic Ink Character Recognition, the strip of oddly-shaped numerals along the bottom of a cheque.

A cheque is a piece of paper that a customer writes on. To automate it you must first make it machine-readable *without* constraining what the customer writes. MICR solved that by pre-printing the account and routing numbers in magnetic ink in a font a machine could read reliably even when the cheque was crumpled, stamped or written over.

The American Bankers Association adopted the **E-13B** MICR font as the national standard in **1956**, and this is the second time in two files that the real achievement is an industry agreeing on a format rather than a company inventing a device. (The first was [[origins/supermarket-chains/origin-story|the UPC]]. It will not be the last.)

## And Then the Money Moved

Cheque automation solved processing, not the underlying absurdity that money moved by physically transporting paper. In **1968** Californian clearinghouses formed the **SCOPE** committee to design a paperless alternative. The first Automated Clearing House went live in **1972**, run by the Federal Reserve Bank of San Francisco with a coalition of California banks. Regional associations merged into **NACHA** in **1974**.

**ACH was built as an electronic replacement for paper cheque clearing — and paper cheque clearing was already an overnight batch process.** It inherited the clock rather than choosing one.

> **Flagged honestly:** no source found states this as an explicit recorded design decision. It is a well-supported inference from what ACH was built to replace. Present it that way. The alternative — asserting that a committee deliberately chose slowness — is tidier and not evidenced.

**Sources:** SRI International, *Banking automation — ERMA*; historyofinformation.com; Wikipedia, *Electronic Recording Machine, Accounting*; ABA MICR E-13B adoption, 1956; Federal Reserve History, *Automated Clearing House*; NACHA history.
