# Legacy: What Semiconductor Fabs Bequeathed

**Origin:** [[origins/semiconductor-fabs/profile|Semiconductor Fabs]]

## The Direct Inheritance

Every industry downstream that manufactures a physical product to a tolerance inherited some version of the fab's closed loop.

| Child | What it inherited |
|---|---|
| [[industries/electronics-contract-mfg\|Electronics Contract Manufacturing]] | The measure-detect-adjust loop one level up the supply chain — board-level test and rework processes run on the same statistical logic as wafer-level process control, on components the fab already qualified this way. |
| [[industries/medical-device-mfg\|Medical Device Manufacturing]] | Statistical process control as a **compliance requirement**, not just an efficiency choice — regulators expect documented control limits and deviation handling, turning the fab's voluntary discipline into an auditable obligation. |
| [[industries/contract-manufacturing\|Contract Manufacturing]] | The yield mindset generalised beyond chips: a defect caught at the step it occurred is cheap, and the same defect caught at final inspection or, worse, by the end customer, is not — the semiconductor industry's founding economic argument, applied to whatever is being made. |

## The Deeper Inheritance: monitoring as production discipline, not an afterthought

Semiconductor fabs did not bolt statistical monitoring onto an existing process late in the industry's life. They built it in from the start, because the arithmetic of yield left no other option, and by 1991 it was already codified doctrine rather than a new idea. Every industry that now takes for granted that a production process should be watched continuously, with a defined response when it drifts, is running a version of a discipline this industry was forced into decades before "MLOps," "drift monitoring" or "data quality checks" existed as vocabulary — a pattern that generalises past the three named children above into anywhere in this vault where a model or a process is deployed once and expected to keep working.

## The Second Inheritance: quality is a collective good, sometimes

[[origins/semiconductor-fabs/the-fight|The Fight]] recorded something unusual for an industry this competitive: American semiconductor manufacturers, having lost ground to Japanese yield discipline through the 1980s, chose to jointly fund shared process-control research through SEMATECH rather than each trying to solve the problem alone. That is a genuine exception to the pattern the rest of this vault documents, where the platform or the incumbent hoards its advantage. Here, the incumbents decided the underlying manufacturing discipline was not where they wanted to compete, and treated it as infrastructure worth building together — closer to the standards work in [[origins/ocean-shipping-ports/profile|Ocean Shipping & Ports]] than to the moat-building in [[origins/airlines/profile|Airlines]].

## What an Episode Should Take From This

1. **There is no clean founding moment here, and that is itself the finding.** Where most origins in this vault open on a named date, this one opens on a codified 1991 handbook describing practice that already existed — a reminder that not every important capability arrives as an event.
2. **A customer's quality measurement can be more damaging than a competitor's.** The Anderson Bombshell worked precisely because it came from HP, a buyer with no stake in embarrassing American suppliers, which made the finding impossible to dismiss as competitive noise.
3. **Sometimes the profitable move is to stop competing on the input everyone needs.** SEMATECH is evidence that even fierce rivals will jointly fund shared infrastructure when the alternative is each of them separately failing to keep up.

**Sources:** See [[origins/semiconductor-fabs/the-mechanism|The Mechanism]] and [[origins/semiconductor-fabs/the-fight|The Fight]] for full citations; this vault's `industries/electronics-contract-mfg.md`, `industries/medical-device-mfg.md` and `industries/contract-manufacturing.md`.
