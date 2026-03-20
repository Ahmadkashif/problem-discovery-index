# Regulatory Compliance and Physician Oversight

**Industry:** [[med-spas|Med Spas]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic compliance tools track training records and policy documents, but they don't know that Texas requires the medical director to review every treatment plan within 72 hours, that California prohibits RNs from injecting dermal filler without an NP or PA on-site, or that storing before/after photos in Dropbox violates HIPAA — and that a single violation can trigger a state medical board investigation that shutters the practice.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #evaluation-metrics #entropy-cross-entropy-kl-divergence #compliance

## The Problem
Med spas operate in a regulatory gray zone that varies dramatically by state. Core compliance requirements include: physician oversight (some states require on-site medical director presence during treatments, others allow remote supervision with chart review within 24-72 hours), scope of practice (which procedures RNs, NPs, PAs, and aestheticians can perform varies by state — some states allow RNs to inject neurotoxins but not fillers, others prohibit RN injection entirely), informed consent (must be procedure-specific, signed before each treatment, and include specific disclosures required by state law), HIPAA for photos (before/after photos are medical records — storing them in marketing platforms, texting them to patients, or posting on social media without proper consent violates HIPAA), and advertising regulations (some states prohibit "before and after" advertising for certain procedures).

A multi-state med spa chain faces different rules at every location. Even a single-location practice faces evolving regulations — state medical boards are actively tightening med spa oversight, with 15+ states enacting new med spa-specific regulations since 2020.

## What Already Exists
Aesthetic Record includes consent management. HIPAA compliance platforms (Compliancy Group, HIPAA Secure Now) handle general healthcare compliance. Medical board websites publish regulations. No platform aggregates state-specific med spa regulations into an actionable compliance framework that monitors regulatory changes, tracks medical director oversight requirements, enforces scope-of-practice rules in scheduling (preventing an RN from being scheduled for filler in a state where that's prohibited), and manages photo storage/usage with HIPAA-compliant workflows.

## The Customisation Gap
A med spa compliance system needs to: (1) maintain a state-specific regulatory database covering physician oversight requirements, scope of practice by credential type, consent requirements, advertising rules, and photo storage regulations, (2) enforce scope-of-practice rules in the scheduling system — preventing non-compliant provider-procedure combinations, (3) track medical director chart review SLAs and alert when reviews are overdue, (4) manage treatment photo lifecycle (capture → storage → patient consent for marketing use → HIPAA-compliant sharing), (5) monitor regulatory changes and alert the practice when new rules affect their operations, and (6) generate audit-ready compliance documentation on demand.

## Impact If Solved
Prevents regulatory violations that result in $10K-$100K fines and potential practice closure. Eliminates the 5-8 hours per month the practice manager spends manually tracking medical director chart reviews. Enables multi-state expansion with confidence in location-specific compliance. Reduces legal liability from HIPAA violations related to before/after photo management.
