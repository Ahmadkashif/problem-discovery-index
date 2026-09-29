# Consent That Travels With the Lead

**Niche:** [[niches/lending-marketplaces/consent-and-lead-compliance/profile|Consent & Lead Compliance]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A lead is resold twice and called by a party the consumer never saw named, and the record of what they agreed to is a screenshot.
**Tags:** #compliance #graph-theory #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to prove that every contact made to every consumer was covered by a consent that survives a courtroom — and whoever makes that provable at lead level removes the largest litigation exposure in the business.

## The Problem
A consumer fills in a form. They consent to contact from named parties, or from a list behind a link, or from partners generally. The lead is sold, possibly resold, and eventually someone calls. Whether that call was lawful depends on what the consumer actually saw on a page that may have changed since, on whether the caller was within the scope of the named parties, and on the timing. The proof required is specific and durable; the record kept is usually neither.

## Why Nobody Has Built This
Consent was implemented as a checkbox to satisfy a requirement, so what was built was a field rather than an evidence chain — and nobody re-architected it because the exposure is litigated rather than examined and only surfaces years later. Resale makes the chain cross company boundaries where no standard exists. Third-party certification covers the capture moment and not the downstream contacts. And nobody measures what proportion of contacts can actually be evidenced.

## What to Build
Build the evidence chain, not the checkbox. Capture the complete consent artefact — the rendered page, the named parties, the disclosure text, the interaction, the timestamp, the device — which is the core and is what a dispute actually turns on. Preserve the page version immutably, since the page changes and the version the consumer saw is the only one that matters. Link every downstream contact back to the consent that authorises it, because the failure is almost never at capture and almost always in the chain afterwards. Check automatically that the calling party is within the consent's named scope before the contact is made, which is the single most valuable control and is currently a matter of trust. Track the resale chain so a lead's provenance and permissions are known at every hop, as the industry's structure makes this unavoidable and nobody has built it. Expire consent according to the applicable rules, since staleness is a common failure and is mechanical to enforce. Measure the proportion of contacts with complete evidence, which nobody knows and which is the number that defines the exposure. Detect suspicious lead sources, because fabricated consent enters through the supply chain and is detectable by its patterns. Make the evidence retrievable per consumer in seconds, as litigation and complaints both demand it. Handle revocation across the chain, since a consumer who opts out must stop being called by everyone. And treat state rules as first-class, because they differ and are tightening.

## Target Customer
Compliance and legal leadership, lead buyers inheriting the exposure, regulators and plaintiffs' counsel examining the practice, and consent certification vendors covering only the capture moment.

## Impact If Built
Consent was implemented as a field to satisfy a requirement rather than as an evidence chain, and the exposure surfaces years later in litigation. Linking every contact to a preserved artefact and checking scope before the call is the control the category operates without.
