# Build: A Map That Is Observed

**Niche:** Data Discovery & Mapping
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A continuously derived map of where personal data is and where it goes, built from what systems actually do rather than from what their owners reported.
**Tags:** #graph-neural-networks #graph-theory #bert #evaluation-metrics #confidence-intervals #change-point-detection #data-integration #compliance
**Contested on:** Whether the record of where personal data lives and flows is observed from the systems or compiled by asking people.

## The Problem

A record of processing activities is the foundational privacy artefact and is a survey result. Its accuracy depends on system owners knowing what their systems do with data, remembering to mention every integration, and being available when asked.

None of those hold reliably. An engineer maintaining a service knows what it stores and often not what the analytics pipeline downstream does with the events it emits. A team that added a third-party integration last quarter did not think to tell the privacy team. A system decommissioned eighteen months ago still appears because nobody removed it. And an entire class of data locations — application logs, caches, message queues, temporary exports, developer copies of production data — is absent from every survey-based map because nobody thinks of them as systems holding personal data, though they are.

The consequence is that every downstream obligation is executed against an incomplete picture. A deletion request is fulfilled across the systems on the map. A transfer assessment covers the flows someone described. An incident response scopes to the systems the record lists. In each case the answer is confidently produced and is as complete as the survey was.

The organisation's systems know the truth. Network egress, API calls, database access, SaaS OAuth grants, warehouse lineage and tag telemetry describe what actually happens, continuously, and none of it is used to build the map.

## Why Nobody Has Built This

**Observation requires deep access.** Deriving flows means instrumenting networks, reading access logs, querying warehouse lineage and enumerating cloud resources. That is a far heavier integration than a questionnaire, and privacy teams — the buyers — rarely have the standing to obtain it.

**The buyer is legal, not engineering.** Privacy platforms are bought by counsel and programme managers, who want an artefact they can defend. An observed map is an engineering product sold to a legal buyer, which is an awkward fit that has shaped the whole category.

**An observed map would be embarrassing.** It would show flows nobody registered, systems nobody knew about, and third parties nobody approved. That is the correct and valuable finding, and it is also a document an organisation would then have to act on and disclose.

**Observation cannot settle meaning.** Traffic shows that data moves; it does not establish that the data is personal, whose it is or on what basis it is processed. That is the classification half, and a flow map without it is an engineering diagram rather than a privacy record.

**Scale and noise.** A large organisation's flows are enormous, most of them uninteresting. Extracting the privacy-relevant subset without drowning the user is a real design problem.

**The regulator accepts the survey.** Records of processing are assessed on existence and plausibility rather than on verified accuracy, so there is no external pressure to do better.

## What to Build

**Derive flows from the systems that already record them.** Cloud network egress, API gateway logs, database access logs, warehouse and pipeline lineage, SaaS OAuth grants and their scopes, and browser-side tag telemetry. Each is a partial view; together they cover most of a modern estate.

**Resolve endpoints to systems and organisations.** A flow to an IP address is not useful; a flow to a named third-party processor is. Attribution — resolving destinations to known vendors, internal services and unknown parties — is where the practical value is created.

**Diff observation against the declared record.** The product's sharpest output: flows observed that the record does not contain, systems in the record with no observed activity, and third parties receiving data who are not on the processor register. This comparison is what converts a survey into an audited artefact, and no vendor produces it.

**Measure and report map completeness.** What proportion of the estate the observation actually covers, stated explicitly. A map presented as complete when it covers the connected sixty per cent is the same failure as a green compliance dashboard over a partial estate.

**Cover the forgotten locations.** Logs, caches, queues, object storage and non-production copies of production data. These are where a deletion request most often fails and where no survey-based map ever looks.

**Update continuously and alert on change.** A new destination appearing, a new third party receiving data, a flow crossing a border it did not cross before. The map should be a live system, and change is the most actionable thing it produces.

**Hand meaning to the classification layer.** Observation establishes structure and flow; whether what moves is personal data and under what basis belongs to [[niches/privacy-tech-vendors/personal-data-classification/profile|🎯 Personal Data Classification]]. Building flow observation as though it answered the whole question is the category's recurring mistake.

## Target Customer

Privacy engineering functions at organisations large enough to have one, where the buyer understands the systems argument and can obtain the access.

Data governance and platform teams as co-buyers, since an observed flow map serves data lineage, security and cost purposes as well as privacy — which is the argument that unlocks the access a privacy team alone cannot get.

Privacy counsel as the beneficiary, since a derived and diffed record is a materially stronger position in front of a regulator than a survey.

## Impact If Built

The foundational artefact becomes evidence rather than testimony. Every downstream obligation in this industry inherits the accuracy of the map, and today the map inherits the accuracy of a questionnaire.

The diff against the declared record is the highest-value single output: unregistered third parties receiving personal data is the finding most organisations would least like and most need.

And continuous change alerting turns a point-in-time compliance document into an operational control, which is what a record of data flows should have been from the start.
