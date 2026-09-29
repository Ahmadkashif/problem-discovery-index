# Buy: Knowledge Platforms Adapted to Evidence From Someone Else's Contacts

**Niche:** [[niches/digital-bpo-operations/client-knowledge-base/profile|Client Knowledge Base Quality]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Knowledge management platforms report views and searches inside their own walls; the evidence about whether the content works is in contacts handled by a different company.
**Tags:** #word-embeddings #large-language-models #evaluation-metrics #data-integration #confidence-intervals #descriptive-statistics #workflow-orchestration #automation
**Contested on:** Whether knowledge platforms can consume quality evidence generated outside them by another organisation.

## The Problem

Knowledge management for support is a real category. Authoring, versioning, approval workflow, publication to multiple surfaces, search, and analytics on views and search terms are all available and widely deployed on the client side.

The analytics answer whether content was found and read. They do not answer whether it was right, whether it resolved the issue, or what customers asked about that had no article — and they cannot, because that evidence is in the contact record, which lives in the BPO's platform, in a different company.

## What Already Exists

Zendesk Guide, Salesforce Knowledge, Confluence-based support bases and the dedicated knowledge platforms. Authoring and versioning workflow. Search analytics with no-result reporting, which is the closest existing thing to gap detection. Content review scheduling. Publishing to self-service and agent-facing surfaces simultaneously.

## The Customization Gap

**The quality evidence is external and has no ingest path.** Contact-derived signals — question clusters with no matching article, agent corrections, articles followed by repeat contacts — have to reach the knowledge platform from the BPO's systems. That integration does not exist in any product and is the prerequisite for everything else.

**Search no-results is a weak proxy for a coverage gap.** It captures only questions someone searched for in the right words. The real gap set is questions customers asked in contacts, which requires the contact corpus and semantic clustering rather than search log analysis.

**Review cadence is calendar-driven and should be evidence-driven.** These platforms schedule reviews by date. The articles that need review are the ones being corrected, contradicted or followed by repeat contacts, and prioritising by evidence rather than by age is a different scheduling logic.

**Two organisations author and review.** The BPO can draft from what agents actually say; the client must approve and publish. A cross-organisation authoring and approval workflow with attribution and an SLA is not a permission setting — it is a workflow these products do not have.

**Assist has raised the cost of every defect and no analytic reflects it.** An article that is wrong is now retrieved and presented across every related contact. Content quality metrics should weight by retrieval frequency in the assist layer, which is a signal from yet another external system.

## Target Customer

Client-side support content owners who cannot tell which of their articles is wrong. Also the knowledge platform vendors, for whom contact-derived quality evidence is the obvious next analytic and the outsourced-operations case is where the evidence is richest.

## Impact If Solved

The authoring, versioning, approval and publishing machinery gets kept, and the external evidence ingest, semantic gap detection, evidence-driven review prioritisation, cross-organisation authoring and assist-weighted quality metrics get built. Concretely: a content team that knows which article to fix first and why.
