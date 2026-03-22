# Commercial New Construction

**Parent Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Category:** High Market Share

## Profile
**Market Size:** $70-80B
**Share of Parent Industry:** ~35%
**Digital Adoption:** Medium — Procore and PlanGrid/Autodesk Build are standard for general project management on commercial jobs, but electrical-specific workflows (conduit/wire sizing, NEC load calculations, panel schedule generation) remain manual or use legacy desktop tools like ConEst and Accubid
**Target Buyer:** Commercial EC owner or lead estimator bidding plan-and-spec projects
**Automation Potential:** High — electrical design involves deterministic NEC calculations that are currently performed manually, and trade coordination conflicts are a geometric problem solvable with spatial analysis

## What Makes This a Distinct Niche
Commercial electrical new construction is a plan-and-spec bidding business: an architect and electrical engineer produce construction documents, and electrical contractors bid to install the specified work. The estimator performs a "takeoff" — counting every outlet, switch, fixture, panel, and conduit run from the plans — then applies labor hours per unit (how long to install each item) and material pricing to produce a bid. The critical competitive advantage is in labor hour estimation: the same outlet installation takes 0.5 hours in open-wall new construction but 1.5 hours in a finished-wall retrofit, and conduit routing through a congested ceiling plenum takes 3x longer than an open run. These multipliers are experience-dependent and firm-specific — NECA published labor units are averages that don't match any particular firm's actual productivity. On the construction site, the dominant pain is trade coordination: electrical conduit routes conflict with HVAC ductwork, plumbing waste lines, and fire sprinkler piping. BIM clash detection (Navisworks, BIM 360) exists for large projects but the $50K+ setup cost puts it out of reach for mid-market commercial work ($500K-5M electrical scope).

## Current Tools & Gaps
ConEst and Accubid (now Trimble) handle electrical takeoff — counting devices and applying material costs from distributor databases. They are strong on material takeoff but weak on labor estimation, which is where the profit or loss is determined. Procore manages project documents, RFIs, submittals, and change orders across all trades but has no electrical-specific intelligence. BIM clash detection via Navisworks requires a full 3D model, which most mid-market commercial projects don't have. For conduit and wire sizing, electricians use manual NEC Chapter 9 table lookups or simple calculators — no tool reads a single-line diagram and auto-generates conduit fill calculations per NEC Article 310 and raceway sizing per Chapter 9.

## Problems
- [[niches/electrical-contractors/commercial-new-construction/build|🔨 Build: Automated Conduit & Wire Sizing from Single-Line Diagrams]]
- [[niches/electrical-contractors/commercial-new-construction/buy|🛒 Buy: Mid-Market BIM Clash Detection for Electrical]]
- [[niches/electrical-contractors/commercial-new-construction/fix|🔧 Fix: Trade Coordination Conflict Resolution]]
