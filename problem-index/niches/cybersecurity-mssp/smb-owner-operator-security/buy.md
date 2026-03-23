# BEC Detection Tuned for SMB Email Patterns

**Niche:** [[niches/cybersecurity-mssp/smb-owner-operator-security/profile|SMB Owner-Operator Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Proofpoint and Abnormal Security detect business email compromise (BEC) using behavioral baselines trained on enterprise email patterns, but SMB email looks fundamentally different — the CEO emails the bookkeeper directly about wire transfers, and this is normal behavior, not an attack indicator.
**Tags:** #bert #text-classification #nlp #anomaly-detection #revenue-impact

## The Problem
Business email compromise (BEC) is the single largest financial cybercrime category, causing $2.7B in reported losses annually. SMBs are disproportionately targeted because they have fewer controls (no dual authorization on wire transfers, no email security beyond Microsoft 365 defaults). But BEC detection tools trained on enterprise email patterns generate massive false positive rates in SMB environments. In an enterprise, the CEO emailing the CFO saying "please wire $50K to this account today, time-sensitive" is suspicious. In a 15-person business, the owner emailing the office manager about a wire transfer is Tuesday. The same behavioral pattern that flags an attack in enterprise is normal business in SMB.

## What Already Exists
Abnormal Security, Proofpoint TAP, and Microsoft Defender for Office 365 provide BEC detection using email behavioral analytics and NLP. These tools build sender profiles and flag anomalies (unusual request, unfamiliar recipient, urgency language). But their models are trained on enterprise email volumes (thousands of messages per user per month) and organizational structures (clear hierarchy, documented approval processes). SMB email volumes are lower, organizational structures are flat, and communication patterns are informal — breaking the behavioral models.

## The Customization Gap
SMB BEC detection must account for: (1) flat organizational structures where any employee may legitimately request financial actions, (2) low email volumes that make statistical baselines unreliable (a user sending 5 emails/day instead of 50 means less data for behavioral profiling), (3) informal communication patterns (owner emails from personal device, uses shortened names, drops greetings), (4) vendor impersonation (SMBs receive legitimate invoices from vendors via email, making fake invoice BEC harder to distinguish), and (5) absence of formal approval workflows (the "unusual request" signal is meaningless when all requests are informal).

## Target Customer
MSSPs and MSPs serving SMB clients where BEC protection is the highest-value security service they can offer — directly preventing financial losses rather than defending against abstract threats.

## Impact If Solved
Reduces BEC false positive rate in SMB environments from 30-40% (enterprise-trained models) to 5-10% (SMB-tuned models). Detects 80-90% of BEC attempts before financial loss. Average BEC loss is $125K per incident for SMBs — preventing even one per year per 50 clients justifies the entire service cost.
