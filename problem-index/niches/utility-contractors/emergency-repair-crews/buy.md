# Utility Dispatch Adapted for Emergency Triage

**Niche:** [[niches/utility-contractors/emergency-repair-crews/profile|Emergency Repair Crews]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Utility dispatch systems (Oracle WAM, IBM Maximo, ClickSoftware) handle routine work order scheduling but switch to radio and paper during emergencies because they lack real-time triage, priority-based re-routing, and the rapid decision cadence that emergency operations require.
**Tags:** #gradient-boosting #workflow-orchestration #automation #quick-win

## The Problem
Routine utility work order dispatch operates on a day-ahead or week-ahead schedule: maintenance work orders are assigned to crews by geography and skill, and the schedule rarely changes intra-day. Emergency operations are fundamentally different: incidents arrive in real-time, priorities shift as new information emerges (a "gas odor" report is reclassified as a "gas main rupture" when the crew arrives), and resource allocation must adjust continuously. Existing dispatch systems can't handle this cadence — they're batch schedulers, not real-time dispatchers. During emergencies, dispatchers bypass the system entirely, reverting to radio communication, paper tracking, and whiteboard status boards.

## What Already Exists
Oracle WAM, IBM Maximo, and ClickSoftware (now Salesforce Field Service) handle work order management, crew scheduling, and dispatch for routine utility operations. They support GPS crew tracking, mobile work order completion, and reporting. They do not support real-time priority re-ranking, dynamic re-routing, or the rapid incident classification that emergency operations require.

## The Customization Gap
An emergency operations mode for existing dispatch platforms that: (1) switches the interface from scheduled-work mode to real-time incident mode — incoming reports are displayed on a map with priority-coded icons; (2) auto-classifies incidents by probable type and severity from intake data, using a gradient-boosted classifier trained on historical emergency reports; (3) recommends crew assignments based on incident priority, crew location, and equipment match, updating recommendations as conditions change; (4) provides a real-time operations dashboard showing all active incidents, crew locations, estimated time to resolution, and resource utilization; and (5) generates a post-event report documenting response times, resource utilization, and incident outcomes for regulatory reporting and after-action review.

## Target Customer
Utilities using Oracle WAM, IBM Maximo, or Salesforce Field Service for routine dispatch who need emergency operations capability without replacing their primary dispatch system. These vendors as platforms seeking to add emergency management functionality.

## Impact If Solved
Eliminates the radio-and-paper emergency dispatch fallback by providing a digital real-time dispatch capability. Reduces emergency response time by 15-25% through optimized crew assignment. Creates a documented record of emergency operations (currently unrecorded when managed by radio) for regulatory reporting and liability protection. Reduces dispatcher stress during major events by providing decision support rather than requiring unaided judgment.
