# Electronics Contract Manufacturing

## Profile
**Category:** Manufacturing & Industrial
**Market Size:** ~$500B globally, ~$80B in North America; EMS (Electronics Manufacturing Services) providers assemble PCBAs and complete electronic products for OEMs across consumer electronics, industrial, automotive, medical, aerospace, and telecommunications
**Tech Maturity:** High — SMT lines are heavily automated with placement machines, reflow ovens, and AOI systems, but NPI yield optimization, BOM management, and test engineering remain deeply dependent on experienced process engineers
**Workforce:** SMT operators, reflow technicians, AOI operators, ICT/FCT test technicians, rework/repair technicians, process engineers, NPI engineers, materials/procurement specialists, quality engineers — a typical EMS facility runs 200-2,000 production workers with 10-15% engineering and quality headcount

## Key Pain Themes
NPI (New Product Introduction) yield ramp is the defining economic challenge — every new customer program requires establishing SMT process parameters (reflow profile, stencil design, placement program, solder paste volume) for a unique BOM with its own component mix, thermal mass characteristics, and quality requirements, and the first 3-6 months of production typically see 5-15% yield loss while process engineers empirically tune these parameters. BOM management and component availability consume enormous procurement effort — a single PCBA may have 200-2,000 unique component line items, each subject to allocation, obsolescence, and counterfeit risk, and the ECM's AVL (Approved Vendor List) must reconcile customer-specified components against available supply with form-fit-function equivalent alternatives. Test engineering is chronically under-resourced — developing ICT (In-Circuit Test) and FCT (Functional Test) fixtures and programs for each new product is a 4-8 week effort that compresses NPI timelines, and test coverage gaps that escape to the field generate warranty costs. Rework is the hidden cost center — hand rework of BGA, QFN, and fine-pitch components requires skilled technicians working under microscopes, and rework rates of 2-5% on complex assemblies represent significant labor cost and yield risk.

## Current Tech Landscape
Aegis FactoryLogix, Cogiscan, and Valor (Siemens) dominate MES for electronics assembly. AOI systems from Koh Young (3D SPI and AOI), Mirtec, and Viscom perform automated solder joint and placement inspection. Component management platforms (SiliconExpert, Octopart, IHS Markit) provide lifecycle and cross-reference data. ERP is typically SAP, Oracle, or Epicor. Test management is often custom or semi-custom per facility. No platform provides ML-assisted NPI yield optimization, predictive BOM risk scoring, or intelligent test coverage analysis — process engineers rely on experience and empirical iteration.

## Problems
- [[problems/electronics-contract-mfg/high-impact|🔴 High Impact: NPI First-Pass Yield Ramp Optimization]]
- [[problems/electronics-contract-mfg/low-impact-1|🟡 Low Impact: BOM Scrubbing and AVL Cross-Reference]]
- [[problems/electronics-contract-mfg/low-impact-2|🟡 Low Impact: Test Coverage Gap Analysis]]
- [[problems/electronics-contract-mfg/worker-life-1|🟢 Worker Life: SMT Operator Changeover Time]]
- [[problems/electronics-contract-mfg/worker-life-2|🟢 Worker Life: Rework Technician Micro-Soldering Strain]]

## Analysis
- [[problems/electronics-contract-mfg/ml-opportunity|🧠 Machine Learning Opportunities]]
- [[problems/electronics-contract-mfg/ai-agents-platforms|🤖 AI Agents & Platforms]]
