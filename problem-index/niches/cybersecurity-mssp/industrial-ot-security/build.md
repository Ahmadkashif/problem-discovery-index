# IT/OT Attack Chain Correlation Engine

**Niche:** [[niches/cybersecurity-mssp/industrial-ot-security/profile|Industrial OT/ICS Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product correlates IT security events (phishing, credential theft, lateral movement) with OT security events (PLC configuration changes, HMI anomalies) into a unified attack chain visualization — the gap that allows IT-to-OT attacks to succeed undetected.
**Tags:** #graph-ml #anomaly-detection #tabular-ml #tacit-knowledge-ml

## The Problem
The most dangerous industrial cyberattacks begin in IT (a phishing email to an engineer) and pivot to OT (accessing the engineering workstation to modify PLC logic). The IT SOC sees the phishing alert. The OT monitoring platform sees a PLC configuration change. Neither system connects the two events. The IT analyst clears the phishing alert as "user reported, credential reset." The OT analyst notes the PLC change as "authorized engineering activity." The attack succeeds because no one correlated the IT compromise with the OT modification. Experienced OT security analysts can mentally bridge this gap, recognizing temporal and contextual patterns between IT and OT events — but this expertise is scarce (fewer than 5,000 qualified OT security analysts globally).

## Why Nobody Has Built This
IT and OT monitoring produce fundamentally different data types. IT SIEM data uses IP addresses, user accounts, and process names. OT data uses device tags, register addresses, and protocol-specific messages (Modbus function codes, DNP3 object types). Correlating these requires a translation layer that maps IT identities to OT access paths (which IT users can reach which OT engineering workstations) and temporal correlation (did the IT event precede the OT event within a plausible attack window?). Building this translation layer requires understanding both IT and OT architectures at each client site — there is no universal mapping.

## What to Build
A correlation engine that sits between the IT SIEM and OT monitoring platform, consuming alerts from both and building a unified event timeline. The engine: (1) maps IT user accounts to OT system access paths through network topology and jump-host logs, (2) identifies temporal sequences matching known IT-to-OT attack patterns (Triton, Colonial Pipeline, Oldsmar), (3) correlates IT compromise indicators with subsequent OT anomalies, and (4) generates unified attack chain visualizations showing the full path from initial IT access to OT impact. Each correlated event chain is scored for severity based on the OT asset's safety criticality.

## Target Customer
MSSPs with 5+ industrial clients running both IT SIEM and OT monitoring platforms, where IT and OT alerts are reviewed by separate analyst teams with no systematic correlation.

## Impact If Built
Detects IT-to-OT attack chains 10-50x faster than manual correlation, reducing mean time to detect from days to minutes. Prevents the most damaging industrial cyberattack pattern — the one that has caused every major industrial cyber incident in the past decade. Enables MSSPs to charge premium rates for converged IT/OT monitoring.
