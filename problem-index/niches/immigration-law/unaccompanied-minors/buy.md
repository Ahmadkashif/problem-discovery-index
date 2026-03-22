# State-Specific SIJS Requirements Database

**Niche:** [[niches/immigration-law/unaccompanied-minors/profile|Unaccompanied Minors]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SIJS state court finding requirements vary across all 50 states — which court has jurisdiction, what constitutes "abuse, neglect, or abandonment," what petition to file, what the order must contain — and attorneys research each state's requirements from scratch using scattered PDF practice advisories.
**Tags:** #data-integration #large-language-models #transfer-learning #compliance #quick-win

## The Problem
To obtain SIJS, a child must first get a state court finding that includes three specific determinations: (1) the child was abused, neglected, or abandoned by one or both parents, (2) it is not in the child's best interest to return to their home country, and (3) reunification with the abusive/neglectful parent is not viable. Each state defines these terms differently under its own child welfare statutes. In California, the finding comes from juvenile dependency court or probate guardianship court. In New York, it comes from family court. In Texas, the jurisdictional rules changed after a 2023 court ruling. Some states require the child to be in state custody; others allow any interested adult to petition. The order itself must contain specific language that USCIS recognizes as satisfying the statutory requirements — if the state court order uses slightly wrong phrasing, USCIS may deny the SIJS petition. Attorneys handling their first SIJS case in a new state spend 5-15 hours researching that state's requirements, reading practice advisories from NIWAP or the ABA, and finding sample court orders from colleagues. Even experienced SIJS attorneys must re-research when handling a case in an unfamiliar state.

## What Already Exists
NIWAP (National Immigrant Women's Advocacy Project at American University) publishes state-specific SIJS practice advisories — detailed PDF documents covering jurisdictional requirements, statutory definitions, and procedural steps for each state. The ABA's Commission on Immigration publishes practice guides. Individual state bar associations have CLE materials on SIJS. These resources are comprehensive but static (PDFs that may be outdated), scattered (no single searchable repository), and unstructured (a 40-page PDF must be read linearly to find the answer to a specific question like "does Texas require the child to be in state custody?").

## The Customization Gap
The missing tool is a structured, searchable database of SIJS requirements by state with four layers: (1) jurisdictional mapping — for each state, which court(s) have jurisdiction, what petition to file, filing fees, and whether pro se filing is permitted, (2) statutory definitions — how each state defines "abuse," "neglect," and "abandonment" under its child welfare code, with statutory citations, (3) order requirements — the specific findings and language that must appear in the state court order for USCIS to accept it, with sample orders that have been accepted, (4) case law updates — recent state and federal court decisions that affect SIJS practice in each state (e.g., jurisdictional rulings, BIA decisions on order language), auto-updated through case law monitoring. An LLM layer enables natural-language queries ("Can a probate court in Florida issue an SIJS finding?") with cited answers drawn from the structured database.

## Target Customer
Attorneys handling SIJS cases in states where they haven't previously practiced — including pro bono attorneys at large firms who take one or two SIJS cases and need to learn the state-specific requirements from scratch.

## Impact If Solved
Reduces state-specific SIJS research from 5-15 hours to 30-60 minutes per case. Prevents SIJS petition denials due to deficient state court orders that used incorrect language. Enables pro bono attorneys to confidently handle SIJS cases in any state, expanding the available representation capacity for unaccompanied minors who currently wait months for an attorney with state-specific expertise.
