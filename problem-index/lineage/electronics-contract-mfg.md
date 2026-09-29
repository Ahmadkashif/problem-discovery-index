# Lineage: Electronics Contract Manufacturing

**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**The tool:** IPC-A-610, *Acceptability of Electronic Assemblies* — the pictorial solder-joint standard with three product classes, first issued August 1983
**Builder:** IPC
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An electronics assembler builds a board it did not design, for a customer who will inspect it and can refuse to pay for it. The unit of that dispute is the solder joint — thousands to a board — and whether a joint is good enough is, at the point of inspection, a visual judgement.

There was no shortage of definitions. The US military alone specified soldering through **MIL-STD-454, MIL-S-45743, DOD-STD-2000 and MIL-STD-2000** at various times, and commercial buyers wrote assembly drawings that could carry, in IPC's own later wording, "customer's own preferences or internal standard requirements."

A captive factory with one customer can live with that. **An assembler with many customers inspects the same joint against many definitions of acceptable** — and every disagreement is a rejected lot, a rework bill and an argument about who pays.

## What Got Built

**IPC-A-610, first issued in August 1983** — a picture book that contracts could cite. Illustrations of joints, leads and components, each labelled against a product class and an acceptance condition.

The classes let one document serve very different buyers: **Class 1, General Electronic Products; Class 2, Dedicated Service; Class 3, High Performance**, where "equipment downtime cannot be tolerated." Each criterion sits at one of four levels — **Target, Acceptable, Process Indicator, Defect** — and the standard is explicit that Target is "close to perfect/preferred" but "not always achievable and may not be necessary to ensure reliability."

**That sentence is the commercial heart of the document.** It separates the ideal joint from the joint a customer must accept, which is precisely the line an assembler gets paid on.

Revisions followed in **1990, 1994, 2000, 2005 and 2010**. Its process twin, **J-STD-001, appeared in January 1992**, written to complement and eventually replace MIL-STD-2000; Defense Secretary William Perry's **1994** memorandum then pushed the Pentagon toward commercial standards.

## Who Built It, And Why Them

**IPC — founded in 1957 as the Institute of Printed Circuits, a trade association of board makers — because it had done this once already.** In its first decade it published **IPC-A-600, *Acceptability of Printed Wiring Boards***: the same answer to the same buyer–supplier argument, one layer down, for bare boards.

The second reason is membership. **In the decade the standard appeared, IPC opened its membership to contract assembly companies**, and it later coined the term "Electronics Manufacturing Services." One OEM's workmanship spec binds only its own suppliers; a military spec binds only defence work. An assembler needed one standard all its customers would name, from an association opening its doors to assemblers in the same decade.

The standard also settles who decides. **"The customer (user) has the ultimate responsibility for identifying the class"; if the two sides do not document one, "the manufacturer may do so."** Contractual precedence runs agreement first, customer drawing second, IPC-A-610 third. The shape is a supplier's: a default both sides can fall back on.

## What It Cost

**It judges what an eye can see.** IPC describes the document as a "pictorial interpretive" standard, and concedes that some process considerations related to performance are "not commonly distinguishable through visual assessment." A joint hidden under a component package, or one that looks right and cracks under thermal cycling, falls outside what a picture can settle.

It also kept inspection human: a trained person comparing a joint to a picture, with every Defect call becoming a technician with an iron.

## What You Still Touch

Many through-hole shops still inspect every joint by eye against IPC-A-610, and automated optical inspection machines are, in effect, trying to learn the same picture book.

- [[problems/electronics-contract-mfg/high-impact|🔴 NPI First-Pass Yield Ramp Optimization]] — yield is counted against the Defect line this standard draws
- [[problems/electronics-contract-mfg/worker-life-2|🟢 Rework Technician Micro-Soldering Strain]] — where every Defect call lands
- [[niches/electronics-contract-mfg/legacy-through-hole-assemblers/fix|IPC-A-610 Inspection Bottleneck on Through-Hole Joints]] — the picture book as a queue
- [[niches/electronics-contract-mfg/smt-inspection-data-vendors/profile|SMT Inspection Data & Process Analytics]] — machines encoding the photographs
- [[niches/electronics-contract-mfg/defense-itar-ems/profile|Defense & ITAR-Compliant EMS]] — the customers who once wrote their own soldering specs

The firm-level twin of this artefact — one certificate instead of one audit per customer — is in [[lineage/contract-manufacturing|Lineage: Contract Manufacturing]].

**Sources:** IPC, *IPC-A-610E-2010* table of contents and opening chapter (electronics.org PDF, read directly) for the supersession list (August 1983; A March 1990; B December 1994; C January 2000; D February 2005), the scope and "pictorial interpretive document" wording, the "customer's own preferences or internal standard requirements" line, the three class names and Class 3 wording, the four acceptance conditions and the Target definition, the class-responsibility sentence, the order of precedence, and the "not commonly distinguishable through visual assessment" concession. Global Electronics Association (formerly IPC), *History* timeline, for the 1957 founding, IPC-A-600 in its first decade, the 1977–1986 opening of membership to contract assembly companies, the first IPC-A-610 in that decade, and coining "Electronics Manufacturing Services Industry" in 1987–1996. Wikipedia, *IPC (electronics)*, for the Institute of Printed Circuits name and the 2024/2025 rename. Search summaries (militaryaerospace.com, PCBSync, Sierra Circuits) for J-STD-001 (January 1992) as a parallel to MIL-STD-2000, the older MIL-STD-454 / MIL-S-45743 / DOD-STD-2000 lineage, and the 1994 Perry memorandum — not read at primary source. This vault's through-hole niche profile for 100% visual IPC-A-610 inspection (vault material, not independent corroboration). ⚠️ **Not established:** the founders of IPC — secondary sources say six board manufacturers, which IPC's own timeline does not confirm; the first edition's exact title (IPC's timeline says *Printed Circuit Assemblies*, later editions say *Electronic Assemblies*); and which committee members, OEM or assembler, drafted the 1983 edition. The later F–J revisions were not checked.
