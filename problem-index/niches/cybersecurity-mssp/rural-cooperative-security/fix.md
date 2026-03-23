# SCADA Remote Access Security for Field Technicians

**Niche:** [[niches/cybersecurity-mssp/rural-cooperative-security/profile|Rural Cooperative & Utility Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Fix (Pain Point)
**One-liner:** Cooperative field technicians access SCADA systems remotely using shared credentials and consumer VPNs because secure remote access solutions are too expensive and complex for cooperatives with no IT staff — creating the single largest attack vector for critical infrastructure compromise.
**Tags:** #automation #compliance #worker-facing #quick-win

## The Problem
A cooperative lineman needs to check substation SCADA readings from the field during a storm. The cooperative has one SCADA administrator login shared among 8 field technicians. They connect via a consumer-grade VPN (or sometimes directly over the internet) using a shared password that has not changed in 3 years. This practice is a NERC CIP violation (CIP-005 requires individual credentials for electronic access to BES Cyber Systems) and a massive security risk — a compromised shared credential grants full access to the cooperative's power distribution SCADA system. But the cooperative has no budget for enterprise remote access solutions (CyberArk, BeyondTrust start at $25K/year) and no IT staff to configure and manage them.

## Why It's Still Broken
Cooperative field technicians work in harsh, remote environments where technology must be simple and reliable. Enterprise PAM (Privileged Access Management) solutions require agent installation, MFA token management, and session recording infrastructure that a 12-person cooperative cannot deploy or maintain. The field technicians are lineworkers and substation operators, not IT professionals — they need one-click secure access, not a security product. Previous attempts to implement secure remote access failed because the technology was too complex for non-technical field staff, and the cooperative lacked IT support to troubleshoot access issues.

## What a Fix Looks Like
A lightweight, cooperative-priced remote access solution for SCADA systems that: (1) provides individual credentials for each field technician (satisfying NERC CIP-005), (2) enforces MFA using the technician's personal phone (SMS or authenticator app — no tokens to lose in the field), (3) requires no agent installation on the SCADA system (connects via network-level gateway), (4) logs all access sessions with user identity, duration, and actions for compliance evidence, (5) allows the cooperative manager to grant/revoke access without IT expertise, and (6) costs under $200/month for the cooperative. Designed for non-technical users who access SCADA 2-5 times per week.

## Who Feels the Pain
Cooperative general managers who know their SCADA remote access is insecure but have no affordable alternative, field technicians who use workarounds because the "right way" is too complicated, and MSSP analysts who see shared-credential SCADA access and cannot remediate it due to cooperative budget constraints.

## Impact If Fixed
Eliminates the shared-credential SCADA access vulnerability — the single highest-risk finding in cooperative security assessments. Achieves NERC CIP-005 compliance for remote access at $2,400/year instead of $25K+/year for enterprise solutions. Provides audit-ready access logs for NERC compliance evidence.
