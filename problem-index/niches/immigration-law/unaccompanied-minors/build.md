# Dual-Court Case Coordination Platform

**Niche:** [[niches/immigration-law/unaccompanied-minors/profile|Unaccompanied Minors]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Unaccompanied minor cases require simultaneous proceedings in immigration court and state juvenile/family court with interdependent deadlines — no platform tracks both court tracks together, forcing attorneys to manage two parallel legal proceedings with incompatible calendaring systems.
**Tags:** #workflow-orchestration #data-integration #automation #compliance #worker-facing

## The Problem
An attorney representing an unaccompanied minor typically pursues SIJS (Special Immigrant Juvenile Status) as the primary relief. This requires: (1) filing a petition in state juvenile or family court to obtain a finding of abuse, neglect, or abandonment, (2) using that state court order to file a SIJS petition (I-360) with USCIS, and (3) defending the child in immigration court proceedings that are running in parallel. These three tracks have interdependent deadlines that must be coordinated. The state court hearing must happen before the USCIS petition can be filed. The USCIS petition should be approved before the immigration court hearing to enable adjustment of status. If the immigration court sets a merits hearing before the state court finding is obtained, the attorney must file a continuance motion in immigration court — and these continuances are increasingly denied by judges under pressure to reduce backlogs. The attorney manages these tracks using separate calendars (state court dates in one system, immigration court dates via paper notices, USCIS processing times as estimates), with no tool that visualizes the interdependencies or alerts when one track's timeline threatens the other.

## Why Nobody Has Built This
The user base is extremely narrow — perhaps 2,000-3,000 attorneys nationally handle SIJS cases regularly, mostly at legal aid organizations and pro bono programs. These organizations have near-zero software budgets. The dual-court workflow varies by state (different court systems, different filing procedures, different jurisdictional rules for SIJS), making it difficult to build a one-size-fits-all platform. Immigration court data (EOIR) is not programmatically accessible, and state court data varies by county. The commercial incentive is weak because the clients are children who cannot pay for legal services, and the attorneys are mostly funded by grants.

## What to Build
A case management overlay (not a replacement for LegalServer) that adds dual-court coordination for SIJS cases: (1) a visual timeline showing three parallel tracks (state court, USCIS, immigration court) with their respective milestones and deadlines plotted on a single view, (2) dependency mapping — if the state court hearing is delayed past a certain date, automatically flag that a continuance motion must be filed in immigration court by a calculated deadline, (3) state-specific workflow templates — for each state, pre-built milestone sequences reflecting that state's SIJS procedural requirements (which court to file in, what petition to use, what findings must be included in the order), (4) document routing — state court orders automatically flagged as ready to attach to the I-360 SIJS petition, (5) stakeholder tracking — guardian ad litem assignment, ORR (Office of Refugee Resettlement) case manager contact, sponsor information, and pro bono attorney assignment with contact details and role clarity.

## Target Customer
Legal aid organizations with children's immigration programs handling 20+ active SIJS cases, and pro bono coordinators at large law firms placing SIJS cases with volunteer attorneys who need guided workflow support.

## Impact If Built
Prevents the most catastrophic workflow failure in children's immigration: a state court finding that arrives too late to support the SIJS petition before the immigration court hearing, resulting in a removal order for a child. Reduces case management overhead for attorneys handling 30+ dual-court cases. Enables pro bono attorneys (who lack immigration expertise) to handle SIJS cases effectively by following the platform's state-specific workflow templates — expanding the pool of available representation for unaccompanied minors.
