# OT-Safe Incident Response Playbooks

**Niche:** [[niches/cybersecurity-mssp/industrial-ot-security/profile|Industrial OT/ICS Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SOAR platforms like Cortex XSOAR and Swimlane automate IT incident response playbooks, but their "isolate and remediate" actions would cause safety incidents if applied to OT systems — a compromised PLC controlling a chemical reactor cannot simply be taken offline.
**Tags:** #workflow-orchestration #automation #compliance

## The Problem
When a SOC analyst detects a compromised device on the IT network, the standard playbook is: isolate the device (cut network access), contain the threat (disable accounts, block IPs), and remediate (reimage, patch). Applying this playbook to an OT device would be catastrophic — isolating a PLC controlling a boiler could cause an explosion, disconnecting an HMI could blind operators to a running process. OT incident response requires coordinating with plant operations: can this device be safely isolated? What is the production impact? Is there a manual fallback? Is the process in a safe state to allow changes? MSSP analysts trained in IT security do not know how to make these judgments for industrial processes.

## What Already Exists
Cortex XSOAR, Swimlane, and Tines provide SOAR (Security Orchestration, Automation, and Response) platforms with customizable playbooks. These platforms can model complex decision trees and automate response actions. Dragos provides OT-specific threat intelligence and response guidance. But no SOAR platform ships with OT-safe playbooks that enforce safety checks before response actions, require plant operations approval before isolation, and include process-state validation steps.

## The Customization Gap
OT-safe playbooks must: (1) classify each OT asset by safety criticality level (safety-instrumented system, process control, monitoring only), (2) enforce mandatory human approval from plant operations before any containment action on safety-critical systems, (3) include process-state checks ("is the boiler in shutdown mode?") before allowing isolation, (4) provide alternative containment strategies (monitoring without isolation, traffic filtering instead of disconnection), and (5) integrate with the plant's change management process (OT changes require MOC — Management of Change — documentation). These playbooks must be customized per client site based on their specific process safety requirements.

## Target Customer
MSSPs managing OT security monitoring for manufacturing, chemical, utility, and oil & gas clients where incorrect incident response could cause safety hazards.

## Impact If Solved
Enables MSSP SOC analysts to respond to OT incidents safely without deep industrial process knowledge. Reduces OT incident response time by 60% while maintaining safety constraints. Prevents the most feared MSSP liability scenario — an automated response action causing a safety incident at a client's plant.
