# Buy: Enrichment and Suppression From Security Operations

**Niche:** The SOC Analyst Receiving the Alerts
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security orchestration platforms automate enrichment and triage for every other alert type, and threat intelligence matches arrive as bare indicator hits.
**Tags:** #gradient-boosting #evaluation-metrics #bert #workflow-orchestration #automation #data-integration #confidence-intervals
**Contested on:** Whether the alerts an intelligence subscription generates are worth the analyst's attention.

## The Problem

Automating the gathering that precedes a triage decision is what security orchestration platforms do. A playbook fires on an alert, queries a dozen sources, assembles the context, applies decision logic, and presents the analyst with an enriched case — or resolves it entirely where the logic is confident.

The capability is mature and widely deployed. It is applied to phishing reports, endpoint detections, vulnerability findings and cloud misconfigurations.

Threat intelligence matches are among the highest-volume, most repetitive and most enrichable alerts in any queue, and they are frequently the least automated. The alert arrives as an indicator hit and the analyst performs the gathering by hand, every time, for a class of alert whose triage path is almost entirely mechanical.

The reason is not capability. It is that intelligence alerts come from the intelligence platform rather than from the detection stack, are treated as informational rather than as detections, and fall between the teams who build playbooks and the teams who manage subscriptions.

## What Already Exists

Security orchestration: Splunk SOAR, Palo Alto XSOAR, Tines, Torq and Swimlane, with playbook automation, multi-source enrichment, decision logic and case management.

Enrichment sources: passive DNS, WHOIS and registration data, certificate transparency, ASN and geolocation, reputation services, sandboxing — all with APIs and all commonly integrated.

Threat intelligence platforms: Anomali, ThreatConnect, OpenCTI and MISP, holding the indicator context and the feed provenance.

Case management: the disposition history that would show prior investigations of the same indicator.

Alert triage automation: the general practice of automated enrichment and confidence-based routing, well established for other alert types.

## The Customization Gap

**Intelligence alerts are treated as informational.** They arrive from a different system and are often not routed through the orchestration layer at all, which is why the playbooks were never written.

**Enrichment is available and not assembled.** Every source needed is integrated somewhere in most organisations. Assembling them into a standard intelligence-match playbook is a day of work that nobody has been assigned.

**Infrastructure classification is the missing enrichment.** Determining that an address is shared hosting or a dynamic residential range is the single most decisive enrichment for this alert type, and it is not a standard enrichment source in the way reputation lookup is.

**Prior-disposition lookup is not a playbook step.** Querying the case management system for previous investigations of the same indicator is trivially automatable and is essentially never done.

**Auto-resolution is avoided here more than elsewhere.** Organisations comfortable auto-closing low-risk phishing reports are unwilling to auto-close intelligence matches, which is partly reasonable and partly habit.

**Feed provenance is lost.** Playbooks cannot route by feed quality if the alert does not carry which feed matched, which is the same provenance gap that blocks measurement.

## Target Customer

Security operations teams already running an orchestration platform, for whom this is a playbook to write rather than a product to buy — and one of the highest-return playbooks available given the alert volume.

Orchestration vendors, who could ship a standard threat intelligence triage playbook as a supported content pack and largely have not.

Threat intelligence platform vendors, who hold the indicator context and could perform the enrichment before the alert is raised rather than leaving it to the downstream stack.

## Impact If Solved

The most repetitive, most mechanical, highest-volume alert class in the queue gets the automation that has been applied to every other alert class.

Infrastructure classification as a standard enrichment would resolve a large share of these alerts automatically, and it is a missing enrichment source rather than a missing capability.

And a standard, supported triage playbook shipped by the orchestration vendors would put this in front of every organisation that already owns the platform, which is most of the ones with the problem.
