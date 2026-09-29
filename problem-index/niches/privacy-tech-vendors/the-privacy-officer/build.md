# Build: Assurance for the Person Who Signs

**Niche:** The Privacy Officer
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An assurance layer that tells the privacy officer how accurate their record is, what it does not cover, and what changed in the organisation that should concern them.
**Tags:** #evaluation-metrics #confidence-intervals #change-point-detection #hypothesis-testing #compliance #worker-facing #data-integration #automation
**Contested on:** Whether the person who signs the processing record has any means of establishing that it is accurate.

## The Problem

A privacy officer signs a record of processing. In doing so they are stating that the organisation's processing activities are as described. They have no way to check.

The record came from a survey. They did not see the systems. They do not have access to the cloud accounts, the databases, the tag manager or the identity provider. They cannot tell whether a declared retention period is implemented, whether a system described as holding no special category data actually holds some, or whether a flow described as staying in one region actually does.

What they have is the assurance of the people who answered the questionnaire, filtered through whoever assembled it, about an estate that has changed since. And the regulator's correspondence will be addressed to them.

They are also the last to know when something changes. A new analytics vendor is added on a Tuesday. A team starts sending customer records to a new destination. An application is granted broad access to the customer database. Each is materially relevant to their position and none reaches them, because there is no channel from the organisation's systems to the person accountable for how those systems process data.

## Why Nobody Has Built This

**The product was built to produce the artefact.** Privacy platforms generate records, assessments and audit trails. Assurance that the artefact is true is a different product, and nobody has asked for it because the artefact is what the regulation appears to require.

**The officer cannot obtain the access.** Verification needs technical access to systems that a legal function does not command, which means any assurance product has to be sold jointly with engineering or security.

**Accuracy measurement produces uncomfortable numbers.** An officer who learns their record covers sixty per cent of the estate now knows something they must act on, and their organisation may not fund the action.

**Independence is formally required and practically constrained.** The role is meant to be independent and is typically employed by the organisation it oversees, reporting to a leadership that sets its budget. Tooling that strengthens the officer's position relative to the organisation is an awkward product to sell to that organisation.

**The market is small per organisation.** One person, sometimes part-time, with no budget of their own.

**Nobody has framed it as assurance.** The category thinks of itself as compliance workflow. Framing it as providing assurance to an accountable individual is a different product concept that nobody has taken up.

## What to Build

**Report the record's accuracy and coverage.** What fraction of the estate is covered, when each entry was last verified, and which entries rest on assertion rather than observation. A record that carries its own confidence is a fundamentally different artefact to sign.

**Verify a sample continuously.** Rotate through the record checking entries against the systems — declared retention against actual, declared flows against observed, declared data categories against classification. A rolling verification programme gives the officer a live accuracy estimate rather than an annual leap of faith.

**Alert on what should concern them.** A new third-party recipient, a new cross-border flow, a system processing beyond its declared purpose, an application granted broad data access, a consent enforcement failure. These are the events that change the officer's position and today none reaches them.

**Assemble the escalation case.** When something needs leadership attention, produce the evidence, the exposure, the options and the recommendation as an artefact. The officer's independence is exercised through escalation and constructing each one currently takes hours they do not have.

**Track their own advice.** What they advised, when, to whom, and what was decided. In a role with personal exposure, a record of advice given and decisions taken by others is protection, and no platform provides it.

**Support the regulator relationship.** Correspondence, responses, commitments made and their status. This is currently email and a folder, for the interactions with the highest consequence in the job.

**Capture institutional memory for the successor.** Why this exception exists, what the regulator accepted last time, which team needs handling carefully. Turnover in this role is high and the handover is currently a conversation.

## Target Customer

Data protection officers and privacy leadership at organisations large enough to have a dedicated role, particularly where the officer is formally designated and personally identified to a regulator.

General counsel as the sponsor, since the organisation's exposure and the officer's personal exposure are related and both are currently unmanaged.

The privacy platforms, for whom assurance is a differentiated position in a category competing on workflow features.

## Impact If Built

The person accountable for the record gains a means of knowing whether it is true, which is a remarkable thing for them not to have.

Change alerting would turn the officer from someone who learns about new processing at the annual survey into someone who learns about it when it happens, which is the difference between an advisory role and a control.

And a record of advice given is genuine personal protection in a role where an individual is named to a regulator for decisions the organisation makes.
