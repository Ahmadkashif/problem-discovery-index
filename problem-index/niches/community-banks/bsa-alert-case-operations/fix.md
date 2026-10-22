# The Disposition That Says "Activity Consistent With Profile"

**Niche:** [[niches/community-banks/bsa-alert-case-operations/profile|BSA/AML Alert & Case Operations]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Fix (Pain Point)
**One-liner:** Most alerts close with a one-line rationale that tells an examiner nothing, so sampled dispositions become findings even when the decision was right.
**Tags:** #large-language-models #transformers #compliance #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to close the alerts that are noise without missing the one that becomes a SAR, and whoever can prove to an examiner that its deprioritised alerts were safe takes the account.

## The Problem
An analyst clears a cash alert on a landscaping company because she knows the business. She writes "activity consistent with customer profile" and moves on. Eighteen months later an examiner samples the alert and asks what was reviewed and why it was consistent. The analyst may have left.

## Why It's Still Broken
Writing a full rationale for every routine alert takes time the team does not have, and the case management system accepts any text.

## What a Fix Looks Like
Draft each disposition from the facts the analyst reviewed: the customer's stated business and expected activity, the comparison with prior months and seasons, prior alerts and how they closed, related accounts checked. The analyst confirms or edits in seconds, and every closed alert carries a rationale an examiner can follow.

## Who Feels the Pain
BSA analysts; BSA officers defending sampled dispositions; examiners reading thin files.

## Impact If Fixed
Better documentation at no extra analyst time, fewer disposition-quality findings, and a corpus of reasoned decisions that later tuning and models can learn from.
