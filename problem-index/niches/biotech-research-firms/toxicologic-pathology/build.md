# A Pre-Screen That Sends the Pathologist to the Tissues That Matter

**Niche:** [[niches/biotech-research-firms/toxicologic-pathology/profile|Toxicologic Pathology & Histopathology Reads]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most tissues in a toxicology study are normal, and a scarce pathologist reads every one of them with the same care as the few that carry the finding.
**Tags:** #cnns #semantic-segmentation #transfer-learning #contrastive-learning #evaluation-metrics #compliance #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to deliver a pathology read that survives peer review and FDA scrutiny on the study's timeline despite a thin bench of board-certified toxicologic pathologists, and whoever multiplies each pathologist's throughput without weakening the diagnosis takes the account.

## The Problem
A 28-day rat study with four dose groups, both sexes and recovery animals can mean thousands of tissue sections (estimate). Control and low-dose tissues are mostly normal. The pathologist's judgement — what is background, what is test-article-related, how severe — is concentrated in a small share of slides, but the time is spread across all of them.

## Why Nobody Has Built This
Training data is locked study by study under sponsor ownership; GLP use needs validation and there is no agreed standard; and pathologists rightly distrust tools that might suppress a rare lesion. Clinical digital pathology vendors target human diagnostics, where the volume and reimbursement are.

## What to Build
A screening aid validated per species and tissue: whole-slide models trained on control-group tissue, which CROs hold in volume, flag slides with probable findings, and order the read so the pathologist starts with the high-dose group's flagged tissues. Severity is proposed, never assigned. Every model output is logged for the study record, and the pathologist's confirmations feed retraining under the CRO's data rights.

## Target Customer
Heads of pathology at large CROs and specialist pathology groups.

## Impact If Built
More studies read per pathologist without fewer eyes on the slides that matter, which is the contest in a niche limited by people, not microscopes.
