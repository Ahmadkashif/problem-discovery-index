# The Revision Nobody Versioned

**Niche:** [[niches/data-labeling-services/guideline-and-taxonomy/profile|Guideline & Taxonomy Iteration]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** The guideline is revised in week three, the items annotated before and after are governed by different rules, and nothing records which items fall on which side.
**Tags:** #descriptive-statistics #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to find the ambiguity in a guideline before it produces a batch of inconsistent data — and whoever does that takes project delivery, because guideline ambiguity is the single most common cause of the disagreement everyone attributes to annotators.

## The Problem
A boundary is clarified in week three, sensibly, in response to accumulated questions. Items annotated in weeks one and two follow the old rule and items after follow the new one. The delivered dataset therefore contains two inconsistent definitions of a category, which nothing marks. The customer's model trains on both and learns a blurred boundary. When the inconsistency surfaces, the vendor cannot identify which items were annotated under which rule, cannot re-annotate selectively, and cannot even establish that the revision was the cause — because the guideline lives in a document with no version history linked to the production data.

## Why It's Still Broken
The guideline is a document, frequently in a shared editor, and its revisions are edits rather than versions. Linking a version to the items annotated under it requires the platform to record a guideline reference per item, which is a small schema field nobody added. Revisions feel like clarifications rather than specification changes, which understates their consequence. And the inconsistency is invisible in the delivered data, since a label does not carry the rule that produced it.

## What a Fix Looks Like
Version the guideline and record it against every item. Treat the guideline as a versioned artefact with an identifier, which is a small change and is the precondition for everything else. Record the version against each annotated item, which is one field and makes the whole problem tractable. Classify each revision as a clarification or a change, since a clarification of something already implied is compatible with earlier work and a genuine change is not, and the two require different responses. On a change, identify the affected earlier items and decide deliberately whether to re-annotate, adjust or disclose — which is a choice the vendor can currently not even make. Measure the revision's effect on agreement, which is the evaluation that establishes whether guideline work helps and is the argument for doing more of it. Disclose version boundaries in the delivered data, so the customer knows the dataset is not homogeneous, which is honest and is what a model team needs. And keep the revision history with its reasoning, since the guideline's evolution is the accumulated knowledge of the project and is currently lost when the document is edited.

## Who Feels the Pain
Customers training on datasets containing two definitions of a category; delivery managers who cannot prove or fix an inconsistency they suspect; and annotators marked down for following the rule that was in force when they worked.

## Impact If Fixed
A guideline version identifier recorded against each item is one schema field and makes an otherwise intractable inconsistency identifiable and fixable. Measuring each revision's effect on agreement is the evaluation that would make guideline work a discipline rather than a reaction.
