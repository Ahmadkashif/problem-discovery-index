# The Toll-Fraud Weekend

**Niche:** [[niches/telecom-resellers/smb-hosted-voice-ucaas/profile|SMB Hosted Voice & UCaaS]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** A small business's SIP credentials are guessed on Friday night, the account dials international premium numbers until Monday, and the provider faces a wholesale bill it can't pass on without losing the customer.
**Tags:** #change-point-detection #gaussian-mixture-models #feature-engineering #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to move a small business's numbers, call flows and handsets onto its platform with no missed calls on cut-over day, and whoever makes the switch invisible wins the seats.

## The Problem
International revenue share fraud and PBX hacking are among the most common telecom fraud types, and the CFCA put global telecom fraud losses at $38.95B in 2023. At a hosted-voice provider the usual pattern is a compromised SIP account or voicemail box on a new customer's system, found by automated scanning and used outside business hours to pump calls to high-cost destinations. The provider owes its wholesale carrier for the minutes, and the customer refuses to pay for calls it didn't make. A single incident can cost tens of thousands of dollars (estimate).

## Why It's Still Broken
Security settings are left at defaults during a rushed cut-over: weak device passwords, international calling enabled for every user, no per-account spend limit. Fraud monitoring, where it exists, is a static threshold on daily spend that triggers after the money is gone, and nobody is watching on Saturday night.

## What a Fix Looks Like
Make safe defaults part of cut-over: international calling off unless requested, strong generated credentials, registration only from expected networks. Then watch each account's calling pattern continuously, flag a change in volume, cost or destination mix within minutes, block high-risk destinations automatically, and notify the customer and the on-call engineer with the evidence.

## Who Feels the Pain
Provider finance teams writing off fraud; small-business customers billed for calls they never made; and on-call engineers woken after the damage is done.

## Impact If Fixed
Most incidents are stopped within minutes instead of running all weekend, and providers stop choosing between eating the loss and losing the customer.
