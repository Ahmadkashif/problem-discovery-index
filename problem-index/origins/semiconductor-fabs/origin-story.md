# Origin Story: Statistical Process Control, and Why There Is No Founding Case

**Origin:** [[origins/semiconductor-fabs/profile|Semiconductor Fabs]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]

## What Was True Before

A chip is built from a bare silicon wafer through several hundred sequential steps, and every one of those steps has to land inside a narrow tolerance for the finished device to work. Diffusion, oxidation and thin-film deposition were being run at scale from the mid-twentieth century onward, as fabs grew from workshops into factories, and the industry had already learned — informally, at first — that a process left unmonitored would drift, and drifted processes ruined wafers.

**Statistical process control** — plotting a measured quantity against control limits derived from its own historical variation, and flagging a point outside them as a signal something has changed — was applied to fab steps for decades before it was written down as doctrine. By the time the *Handbook of Quality Integrated Circuit Manufacturing* codified it in **1991**, SPC on diffusion, oxidation and thin-film steps was already standard practice.

## Why There Is No Single Trigger Here

Every other origin in this vault opens with a datable event: a flight in 1953, a cheque-processing crisis in the 1950s, a ship sailing in 1956. This one does not, and forcing one onto it would misrepresent the history.

**Semiconductor process control developed the way most durable industrial practice actually develops: gradually, across many companies, refined by whichever fab found a technique that worked and was willing to share it.** The clearest datable *milestone* — not origin — is the **run-to-run (R2R) control** work funded through **SEMATECH** in the early 1990s, which demonstrated that chemical-mechanical planarisation (CMP, the step that polishes a wafer flat between layers) could be kept in tolerance by measuring each completed run and adjusting the next recipe, rather than relying on a fixed recipe and hoping it held.

> **Flagged honestly.** Do not let an episode built from this file invent a founding case. There is no single company, date or paper equivalent to SABRE or the Ideal-X here. The honest claim is: SPC doctrine was well established by 1991, SEMATECH's early-1990s R2R work is the clearest datable milestone in closing the loop, and the practice generalised from there. That is a real finding, and it is a negative one — the absence of a clean origin is itself worth stating plainly rather than smoothing over.

## What Got Built From There

R2R control did not stay a CMP-only technique. Combined with **fault detection and classification (FDC)** — automatically flagging a process excursion from sensor data in real time rather than waiting for a human to notice a bad wafer downstream — it generalised through the mid-1990s into **Advanced Process Control (APC)**: a factory-wide discipline of collecting process data, detecting drift, and adjusting the next run automatically, across as many of a fab's several hundred steps as could be instrumented.

Named developers and adopters through this period include **AMD, IBM, Intel, Motorola, Samsung, Texas Instruments**, and **SEMATECH** itself as the consortium coordinating much of the shared development — a genuinely collective effort, in an industry usually associated with fierce secrecy between competitors.

## Why It Mattered

This is the industry that built the closed loop — measure, detect, adjust, repeat — into its core manufacturing discipline decades before "monitoring" and "drift detection" became vocabulary anyone else used. It did so because the arithmetic left no alternative: a few points of yield is the entire difference between a fab that makes money and one that does not, and yield is decided hundreds of steps before the finished chip is tested.

**Sources:** *Handbook of Quality Integrated Circuit Manufacturing* (1991); Wikipedia, *SEMATECH*; DARPA, *SEMATECH* innovation timeline; Semiconductor Digest, *APC: A factory-wide strategy for ultimate yield improvement* (2003) and *APC: The next frontier in wafer-level contamination control* (2003); GAO, *SEMATECH's Technological Progress and Proposed R&D Activities* (1992).
