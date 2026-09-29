# One Evidence Set, Many Programmes

**Niche:** [[niches/agtech-platforms/sustainability-carbon-reporting/profile|Sustainability & Carbon Reporting]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every carbon programme, grain buyer and conservation scheme wants different evidence in a different format from the same farm records, so growers enrol in one, decline the rest, and re-enter data for each.
**Tags:** #data-integration #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in agricultural sustainability reporting is fighting to let one set of farm records satisfy every programme that wants evidence — and whoever makes a grower's data reusable across programmes takes the enrolment.

## The Problem
A grower could participate in a carbon programme paying for reduced tillage and cover cropping, a grain buyer's supply chain programme wanting the same practices documented differently, and a conservation scheme with its own forms. Each requires field-level practice history, input records, and attestations, through its own portal, with its own field identifiers and its own vocabulary. Doing all three means entering substantially the same information three times and maintaining three enrolments. The grower does one, which is the rational choice, and the other two programmes record a farm that declined to participate rather than a farm that could not face the paperwork.

## Why Nobody Has Built This
Each programme built its own collection infrastructure because each launched independently with its own methodology and its own verification requirements, and none had an incentive to make a grower's data portable to a competitor for the same acres. The verification requirements genuinely differ in ways that matter, so the programmes' position is not merely obstructive. But the underlying farm records — what was planted, what was applied, what tillage was performed, what cover was grown, on which acres, in which years — are identical, and nobody has built the layer that holds them once and projects them into each programme's requirements.

## What to Build
A canonical practice and field record held by the grower, with programme-specific projections generated from it. The record captures practices at the field-season level with the evidence attached — machine data showing the tillage pass that did not happen, seed invoices for the cover crop, application records — which is the same reconciled record the interoperability niche produces and is the reason the two belong together. Each programme's requirements are encoded as a projection: which fields qualify, which evidence is needed, in which format, through which channel. Enrolment in a second programme becomes a review rather than a re-entry. Conflicts between programmes — additionality rules, exclusivity terms, differing baselines — are surfaced explicitly, since a grower enrolling the same acres in overlapping programmes is a real risk that nobody currently warns them about. The record stays the grower's, which matters: a farm's practice history is its own asset and should not be captured inside a programme operator's platform.

## Target Customer
Growers considering multiple programmes, farm management platform vendors, the programme operators who want higher enrolment, and the food companies and grain buyers whose supply chain reporting depends on supplier participation.

## Impact If Built
Participation is limited by the administrative burden rather than by grower willingness, so making evidence reusable raises enrolment across every programme at once — which is the rare case where the interests of the grower and all the programme operators align. Grower ownership of the record is the design decision that makes it a durable asset rather than another enrolment portal.
