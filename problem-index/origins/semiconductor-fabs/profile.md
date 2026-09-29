# Semiconductor Fabs

**Layer:** Origin — a parent industry, not a prospect
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Founding event:** No single founding case. Statistical process control doctrine established by 1991; SEMATECH founded Aug 1987; run-to-run CMP control demonstrated early 1990s, generalising into Advanced Process Control (APC) through the mid-1990s
**Children in this vault:** electronics-contract-mfg, medical-device-mfg, contract-manufacturing — and all compute downstream

## Profile

**What it is:** The manufacture of integrated circuits, a process of several hundred sequential steps — deposition, lithography, etching, doping, polishing — each of which can push a wafer's electrical characteristics out of the narrow window that makes the finished chip work at all.

**Who pays:** Every device that contains a chip, indirectly. Directly, whoever buys the finished die — and the price they pay is set as much by how many usable die came off the wafer as by the cost of running the fab.

**The economics:** A fab costs billions of dollars to build and runs continuously once it exists, so the difference between profit and ruin is not the machine — it is **yield**: the percentage of die on a wafer that work. A few percentage points of yield, compounded across a run of tens of thousands of wafers, is the entire margin of the business.

## Why This Is an Origin

Semiconductor fabs instrumented themselves more thoroughly, and for longer, than almost any other industry in this vault, because yield made it existential rather than optional. Long before "data science" was a phrase, fabs ran statistical process control on individual steps, and by the early 1990s were closing the loop: measuring a wafer, comparing it statistically to what a healthy process should look like, and automatically adjusting the next run's recipe before the deviation became a defect.

That closed loop — measure, detect, adjust, repeat — is the direct ancestor of production monitoring, drift detection and automated retraining pipelines everywhere else in this vault.

## The Contested Decision

> **How much of this wafer's deviation from normal is a real problem worth stopping the line for, and how much is noise you would be foolish to chase?**

Answer too conservatively and defects propagate through hundreds of remaining steps before anyone notices. Answer too aggressively and you shut down or re-tune a healthy process because of statistical noise, which is its own, quieter form of ruin.

## An Honest Note on This Origin's Shape

**This file does not open with a named inventor or a dated eureka moment.** Unlike SABRE or the Ideal-X, semiconductor process control has no single company or paper that started it — it is a gradual, multi-vendor, consortium-driven evolution, which is itself the lesson this origin exists to teach. See [[origins/semiconductor-fabs/origin-story|Origin Story]].

## The Files

- [[origins/semiconductor-fabs/origin-story|Origin Story]] — statistical process control, and why there is no founding case
- [[origins/semiconductor-fabs/the-fight|The Fight]] — American fabs against Japanese yield
- [[origins/semiconductor-fabs/the-mechanism|The Mechanism]] — control charts, run-to-run control, and APC
- [[origins/semiconductor-fabs/legacy|Legacy]] — the closed loop, everywhere

**Sources:** Wikipedia, *SEMATECH*; DARPA, *SEMATECH* innovation timeline; Semiconductor Digest, *APC: A factory-wide strategy for ultimate yield improvement* (2003); GAO, *SEMATECH's Technological Progress and Proposed R&D Activities* (1992).
