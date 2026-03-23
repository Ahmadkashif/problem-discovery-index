# OT Asset Inventory Staleness

**Niche:** [[niches/cybersecurity-mssp/industrial-ot-security/profile|Industrial OT/ICS Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Fix (Pain Point)
**One-liner:** MSSPs cannot protect OT assets they do not know exist — and OT asset inventories go stale within months because plant engineers add devices, change configurations, and swap hardware without notifying the MSSP.
**Tags:** #data-integration #automation #compliance #quick-win

## The Problem
An MSSP onboards an industrial client and performs an initial OT asset discovery using Claroty or Nozomi Networks, identifying 500 devices (PLCs, HMIs, engineering workstations, network switches). Six months later, plant engineers have added 30 new devices, replaced 15 devices, and changed firmware versions on 40 devices — none of which were communicated to the MSSP. The MSSP's monitoring rules are based on the original inventory. New devices are unmonitored. Replaced devices trigger false alarms ("unknown device on network"). Changed firmware versions may introduce new vulnerabilities that the MSSP does not know to scan for. The asset inventory, which is the foundation of OT security monitoring, degrades continuously.

## Why It's Still Broken
OT environments are managed by plant engineers and maintenance staff who operate independently from IT and security teams. Adding a PLC to a production line is a plant engineering decision, not an IT project — it goes through the plant's maintenance work order system, not the MSSP's change management process. Passive OT monitoring tools detect new devices on the network but generate alerts that are indistinguishable from false positives (a contractor's laptop temporarily on the OT network looks the same as a permanently installed PLC). There is no feedback loop between plant engineering changes and MSSP security monitoring.

## What a Fix Looks Like
An automated asset inventory reconciliation workflow that: (1) runs continuous passive discovery to detect network changes (new devices, removed devices, firmware version changes), (2) correlates detected changes with the plant's maintenance work order system (was this new device part of a planned engineering change?), (3) flags unplanned changes for MSSP analyst review, (4) automatically updates monitoring rules when planned changes are confirmed, and (5) generates a monthly asset drift report showing inventory changes with security impact assessment. Integrates with CMMS (Computerized Maintenance Management Systems) like Maximo and SAP PM to bridge the plant engineering and security monitoring gap.

## Who Feels the Pain
MSSP OT security analysts who cannot maintain accurate asset inventories, and plant managers who receive compliance audit findings for undocumented OT assets.

## Impact If Fixed
Maintains 95%+ asset inventory accuracy (vs. 70-80% after 6 months without reconciliation). Eliminates 40-60% of false positive alerts caused by inventory drift. Ensures new OT assets are monitored within days of installation, not discovered months later.
