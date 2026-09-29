# The Mechanism: MICR, and Why Batch

**Origin:** [[origins/retail-banking/profile|Retail Banking]]
**Tags:** #data-integration #workflow-orchestration #automation #compliance

## Part One: Making Paper Machine-Readable

The constraint was unusual and worth stating precisely. **The input document is written by the customer, in their handwriting, in whatever pen they have, and it must remain legally valid.** You cannot standardise the cheque without standardising the customer.

MICR's design solves exactly this:

- **Pre-print the machine-readable part.** Account and routing numbers go on the cheque before the customer ever sees it. The customer's handwriting lives in a region the machine ignores.
- **Use magnetic ink, not optical.** A stamp, a coffee ring or a signature written across the numbers does not defeat a magnetic read. Optical would have failed on exactly the documents that matter.
- **Design the font for the reader, not the human.** The E-13B glyphs look strange because their shapes were chosen to produce distinguishable magnetic waveforms.

Three design choices, all of which sacrifice elegance for **robustness against an adversarial real world**. Any FDE building an ingestion pipeline for documents they do not control is solving this problem again.

## Part Two: The Batch, and Why It Never Left

The machine was extraordinarily expensive, so it ran continuously, and the work was organised to feed it: accumulate the day's transactions, process them in one overnight pass, produce the new balances by morning.

This was correct. Given 1959 economics there was no alternative — interactive per-transaction processing would have been absurd.

The **nightly cycle** then became the organising fact of the bank. Cut-off times, value dates, "it'll clear tomorrow," end-of-day reconciliation, the settlement file that arrives after the decision it should have informed. Not a side effect — the architecture.

**And it is still here.** Core banking systems, largely COBOL on mainframes, still post demand-deposit accounts, accrue interest and reconcile in nightly batch. Industry estimates put the share of bank IT budgets consumed by maintaining legacy cores at roughly **78%**. The machine that was a competitive weapon in 1959 is a tax in 2026.

> ### The correction this whole phase was built around
>
> **"T+2 settlement" does not describe this.** T+2 is a *securities* settlement convention — trade date plus two business days for stocks and bonds — and US equities moved to **T+1 in May 2024**.
>
> Retail banking and card/ACH timing is a different mechanism entirely: intraday cut-offs and overnight settlement windows between banks and the Fed, inherited from paper cheque clearing.
>
> This vault's `industries/payment-processors.md` observes that an authorisation result *"lands in a settlement file two days later in a different system"* — a true and important observation whose cause is the batch inheritance described here, **not** securities settlement. Getting this wrong is easy, and it was got wrong in this project before research caught it. See `series/_plan.md` §5.

## The Trade-Offs Taken

**Speed was traded for throughput, permanently.** Batch maximises transactions per unit of expensive compute and minimises latency not at all. When compute stopped being expensive, the trade stopped making sense — and by then it was structural.

**Correctness was traded for reversibility.** Batch systems are exceptionally good at being auditable and re-runnable. They are poor at being interrupted. That is why banking software is conservative in a way that reads as backwardness and is actually a different objective function.

**Integration was traded away entirely.** Each overnight cycle produced files, and the files went to other systems on other schedules. The gap between a decision and the record of its outcome — the vault's **missing join** — is manufactured here, in the first wave, structurally.

## The Transferable Pattern

> **An architecture chosen under a binding constraint outlives the constraint, becomes the definition of how the industry works, and is then mistaken for a law of nature. Ask what the constraint was and whether it still binds.**

**Sources:** SRI International (ERMA/MICR); ABA E-13B standard, 1956; Federal Reserve History, *Automated Clearing House*; SIFMA and DTCC on the US equities move to T+1, May 2024; industry estimates of legacy core maintenance share of bank IT spend.
