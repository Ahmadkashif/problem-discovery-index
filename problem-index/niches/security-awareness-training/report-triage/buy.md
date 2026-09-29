# Buy: Triage Automation From Security Operations

**Niche:** Employee Report Triage
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security orchestration platforms automate phishing report triage as a flagship use case, and many organisations running awareness programmes handle the queue by hand.
**Tags:** #bert #gradient-boosting #evaluation-metrics #workflow-orchestration #automation #data-integration #confidence-intervals
**Contested on:** Whether the reporting stream the programme creates is handled as a detection source or dumped on a security team that never asked for it.

## The Problem

Phishing report triage is the textbook security orchestration use case. It is the first playbook most vendors demonstrate, the example in most of their documentation, and one of the most widely deployed automations in the category.

The playbook is standard: receive the report, extract the message, check the sender reputation, detonate the attachments and links in a sandbox, check the gateway verdict, look for other recipients, cluster against recent reports, and either resolve automatically or route to an analyst with everything attached.

It works, it is available, and many organisations running large awareness programmes have not deployed it — frequently because the awareness function created the reporting stream and the orchestration platform belongs to a different team who were not consulted.

There is also a piece the standard playbook does not cover, which is the reporter's experience. Security orchestration is built to resolve the alert. Whether the person who reported it hears anything is outside its frame, and it is the part the awareness programme depends on.

## What Already Exists

Security orchestration: Splunk SOAR, XSOAR, Tines, Torq and Swimlane, with phishing triage playbooks as a standard content pack.

Email security platforms: Proofpoint, Mimecast, Abnormal and the native capabilities in the major mail platforms, several with their own report-and-remediate workflow.

Sandboxing and reputation: link and attachment detonation, sender reputation and threat intelligence enrichment, all with APIs and standard integrations.

Awareness platforms: report buttons that submit into a mailbox or a ticket, with limited triage capability of their own.

Case management: the ticketing where the queue lands and where acknowledgement would be sent from.

## The Customization Gap

**The reporter's experience is outside the playbook.** Orchestration resolves the alert. Acknowledging the person, thanking them and telling them the outcome is the behavioural half and no playbook includes it.

**Simulation reports need filtering before anything else.** The organisation's own campaigns clogging its own queue is specific to this setting and is a trivial filter nobody has added to the standard playbook.

**Campaign clustering is more valuable here than the standard playbook allows.** Forty reports of one message is a campaign signal, and treating it as forty items rather than one loses both the efficiency and the signal.

**The awareness function does not own the orchestration platform.** The team that created the stream and the team that could automate it are different, which is the main reason this is not deployed.

**Email security vendors could resolve most of it upstream.** A report button integrated with the gateway can check its own verdict instantly, and several platforms do this partially.

**Yield measurement is absent everywhere.** Nobody reports how many real threats came from employee reports, which is the number that would justify resourcing the whole capability.

## Target Customer

Security operations teams already running an orchestration platform, for whom this is a content pack to deploy rather than a product to buy — and one of the highest-return automations available.

Email security vendors, for whom report triage integrated with their own gateway verdict is a natural extension several have built partially.

Awareness platform vendors, who create the stream and should not be handing their customers an unmanaged queue as a side effect of their product working.

## Impact If Solved

A mature, standard automation exists for exactly this queue and is not deployed in many of the organisations generating it, which makes this a distribution problem rather than a technical one.

Filtering the organisation's own simulations out of its own queue is a trivial addition to the standard playbook and removes a substantial share of the volume.

And adding the reporter acknowledgement step to the playbook is a small change that connects an operations automation to the behavioural objective of the programme that created the stream.
