# Operator Attribution

**Parent Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Category:** Low Digitized
**Contested on:** Whether the hundreds of accounts behind a counterfeit operation are recognised as one entity, using signals the firm already collects.

## Profile

**Market Size:** ~$560M
**Share of Parent Industry:** ~14%
**Digital Adoption:** Very low — enforcement is per-listing
**Target Buyer:** Investigations teams, brand counsel, enforcement leadership
**Automation Potential:** Very high — it is entity resolution over existing data

## What Makes This a Distinct Niche

A single counterfeit operation runs hundreds of accounts across several platforms. Removing listings one at a time is the least effective intervention available, and it is the one the industry uses, because nothing in the pipeline knows the accounts are one operator.

The data to know sits in the firm's own detection records. Shared or near-duplicate images across accounts. Common shipping origins and fulfilment patterns. Coincident account creation timing. Pricing behaviour that moves together. Overlapping description text and template structure. Contact details, return addresses and business registration fragments. Accounts that appear immediately after others are removed.

None of it is assembled. Detection produces listings, enforcement consumes listings, and the operator exists nowhere in the system except in the analyst's growing private suspicion that these are all the same people.

The contest is entity resolution over adversarial data. The operators know that shared images and addresses connect them and take steps to separate their accounts. So the signals that survive are the ones that are expensive to vary — fulfilment logistics, product sourcing, operational cadence — and finding them is a modelling problem over data the firms already hold and have never joined.

## Current Tools & Gaps

Manual investigation for high-value cases, where an analyst connects accounts by hand and builds a case. Test purchases establishing shipping origins. Some image-similarity clustering. Platform-provided seller information, which is limited. Legal discovery where litigation is pursued.

The gaps are that the routine case gets none of it. Clustering is manual and reserved for the few operations that justify an investigation, so the great majority are enforced against per-listing. Cross-platform signals are unused because the systems are separate. Post-enforcement reappearance — the strongest available link, since a new account appearing immediately after a removal with matching characteristics is almost certainly the same operator — is not tracked. Test purchase data establishing physical origin is collected for evidence and not fed back into clustering. And no firm can state how many distinct operators it is actually fighting.

## Problems

- [[niches/brand-protection-firms/operator-attribution/build|🔨 Build: The Operator Graph]]
- [[niches/brand-protection-firms/operator-attribution/buy|🛒 Buy: Entity Resolution and Ring Detection]]
- [[niches/brand-protection-firms/operator-attribution/fix|🔧 Fix: The New Account That Appeared the Next Day]]
