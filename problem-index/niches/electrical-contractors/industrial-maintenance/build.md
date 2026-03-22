# Arc Flash Hazard Analysis Automation

**Niche:** [[niches/electrical-contractors/industrial-maintenance/profile|Industrial Maintenance]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that calculates incident energy levels at every panel, MCC, and disconnect in a facility from electrical system data — delivering NFPA 70E-compliant arc flash labels without the $5-10K engineering study that most small and mid-size facilities can't afford.
**Tags:** #gradient-boosting #feature-engineering #compliance #automation #evaluation-metrics #cross-validation #data-integration #worker-facing

## The Problem
NFPA 70E requires employers to perform an arc flash hazard analysis to determine the arc flash boundary and incident energy at every point in the electrical distribution system where workers might interact with energized equipment. The results determine what PPE workers must wear (from safety glasses to full arc-rated suits) and appear on warning labels affixed to each panel and disconnect. A proper study requires modeling the entire electrical system — utility source impedance, transformer ratings, conductor lengths and sizes, protective device types and settings — and calculating available fault current and clearing times at each point. Engineering firms charge $5-10K for this analysis using SKM PowerTools or ETAP. Facilities must update the study every time they modify the electrical system (add a panel, change a transformer, modify protective device settings). Most facilities under 200,000 SF either never perform the study (OSHA violation risk) or perform it once and never update it (rendering labels inaccurate after the first electrical modification).

## Why Nobody Has Built This
The calculation methodology (IEEE 1584) is well-defined and deterministic — the challenge is data collection. To calculate incident energy at a panel, you need: available fault current at the source, conductor impedance (length, size, material) from source to panel, protective device type and trip characteristics, and gap distance between conductors. This data is scattered across single-line diagrams, panel schedules, equipment nameplates, and protective device coordination studies — none of which are digitized in most facilities. The existing tools (SKM, ETAP) assume an electrical engineer is building a system model from scratch, which is the expensive part. The calculation itself takes seconds; the data gathering and model building takes 40-80 hours.

## What to Build
A guided data collection + calculation platform: (1) mobile app for the electrician to photograph each piece of electrical equipment (panels, MCCs, disconnects, transformers) and enter nameplate data (voltage, amperage, interrupting rating); (2) OCR and CNN-based extraction of nameplate data from equipment photos; (3) guided system topology builder — the electrician traces the power flow ("this panel is fed from that transformer through this disconnect") to build the system single-line diagram; (4) automatic IEEE 1584 incident energy calculation at each point; (5) generated arc flash labels in NFPA 70E format, ready to print and affix. The system stores the model, so when the facility adds or modifies equipment, only the changed portion needs updating. A gradient-boosted model trained on historical studies estimates conductor impedance when exact length data isn't available, using building dimensions and typical routing patterns.

## Target Customer
Manufacturing facilities, warehouses, and commercial buildings with 480V electrical service that need NFPA 70E compliance but can't justify the $5-10K engineering study cost. Industrial electrical contractors who want to offer arc flash studies as a service line at lower cost than engineering firms.

## Impact If Built
Reduces arc flash study cost from $5-10K to $500-1,500 per facility by eliminating the electrical engineering labor for model building. Makes study updates affordable (currently $2-5K per update, reduced to $200-500), enabling facilities to maintain accurate arc flash labels as their systems evolve. Reduces OSHA citation risk (average arc flash OSHA fine: $15K-70K) and, most importantly, ensures workers are wearing the correct PPE at each equipment location.
