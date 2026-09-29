# Process Manufacturing

**Layer:** Origin — a parent industry, not a prospect
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Founding event:** Honeywell TDC 2000 — internal proposal 1969, patent filed Feb 3 1975, announced Nov 11 1975 — the first commercial Distributed Control System; Charlie Cutler's Dynamic Matrix Control, demonstrated on a Shell FCC unit ~1973
**Children in this vault:** food manufacturing, contract manufacturing, medical device manufacturing, metal fabrication, electronics contract manufacturing

## Profile

**What it is:** Manufacturing built around continuous or batch **processes** — chemical reactions, thermal treatment, mixing, formulation — rather than discrete assembly. The product is a formula executed under controlled physical conditions: temperature, pressure, flow, concentration. Get the recipe right and the conditions wrong, and the batch is still off-spec.

**Who pays:** OEMs and downstream customers buying a formulated, specified product — a chemical intermediate, a food product, a pharmaceutical batch — who care about consistency and documentation as much as the product itself.

**The economics:** A process plant's profitability is set by how tightly it can run against its true physical and safety limits without crossing them. Every degree of unnecessary conservatism between the operating point and the true constraint is money left on the table; every excursion past it is a safety incident or a scrapped batch. That single trade-off — **how close to the edge do you run, continuously, and how much do you trust the model that tells you where the edge is** — is the whole operating problem.

## Why This Is an Origin

Process manufacturing is where control theory actually shipped as a commercial product, twice: first as **the Distributed Control System**, decentralising plant control off a single panelboard and onto microprocessor-based modules; then as **model predictive control**, using a model of the process to compute, continuously, the tightest safe operating point rather than a conservative fixed one.

It is also the origin with the clearest case in this vault of a cyberattack causing deliberate physical damage — **Stuxnet** — which permanently reframed the security of process-control systems (operational technology, OT) as a discipline distinct from conventional IT security.

## The Contested Decision

> **Given a process with a real physical limit — a temperature, a pressure, a concentration, a speed — how close to that limit do you actually run it, continuously, and how much do you trust the model telling you where the limit is?**

Run too conservatively and a competitor undercuts you on cost. Run too close and a bad model, a stale assumption, or an attacker who has changed what the model believes becomes a safety incident.

## The Files

- [[origins/process-manufacturing/origin-story|Origin Story]] — the Data Hiway and the fluid catalytic cracker
- [[origins/process-manufacturing/the-fight|The Fight]] — Stuxnet, and the discovery of OT as its own security discipline
- [[origins/process-manufacturing/the-mechanism|The Mechanism]] — what Dynamic Matrix Control actually computed
- [[origins/process-manufacturing/legacy|Legacy]] — what process manufacturing bequeathed downstream

**Sources:** Honeywell corporate/patent history, TDC 2000 (patent filed Feb 3 1975, granted Jan 1977); AspenTech/DMC Corporation corporate history, Charlie Cutler and Dynamic Matrix Control; Symantec/ICS-CERT technical analyses of Stuxnet (2010–2011); ISA/OT-security literature on the IT/OT security divide.
