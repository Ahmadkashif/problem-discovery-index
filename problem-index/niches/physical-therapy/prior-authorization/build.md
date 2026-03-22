# Universal PT Authorization Tracker

**Niche:** [[niches/physical-therapy/prior-authorization/profile|Prior Authorization & Concurrent Review]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** PT clinics see every patient's authorization status — remaining visits, expiration dates, extension status, and payer-specific requirements — in one dashboard instead of checking 4 different UM portals and a spreadsheet.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #automation #compliance #revenue-impact #data-integration

## The Problem
A mid-sized outpatient PT clinic manages 200+ active patients across 5-10 different payers, each with different authorization rules and UM vendors. Patient A has 8 visits remaining through EviCore, Patient B needs a Cohere Health extension submitted before Tuesday, Patient C's authorization expired yesterday and nobody noticed. Tracking this requires: checking multiple UM vendor portals daily, cross-referencing with the EMR's visit count, calculating remaining visits, identifying patients approaching their limit, and initiating extension requests 2-3 visits before expiration. No tool aggregates authorization data across payers into a single view. The front desk coordinator manages this on a spreadsheet that is perpetually out of date, creating a daily risk of delivering unauthorized visits.

## Why Nobody Has Built This
Authorization data lives in payer and UM vendor systems (EviCore, Cohere Health, Carelon, and payer-specific portals) that don't offer standard APIs for third-party access. Scraping these portals is technically possible but legally and operationally fragile. Each payer has different authorization structures — some authorize by visit count, others by date range, others by a combination. Some require physician-ordered authorization, others accept PT-initiated requests. The permutations across payers create a combinatorial complexity that makes a universal tracker difficult to build and maintain. Additionally, the PT EMR market is fragmented — building integrations across WebPT, Clinicient, TheraOffice, and Net Health multiplies the development effort.

## What to Build
A centralized authorization management platform that: (1) ingests authorization data from all sources — payer portals, UM vendor portals (with secure credential storage), and the clinic's EMR — into a unified dashboard showing every patient's authorization status, (2) calculates remaining visits and days by combining authorized quantities with visit history from the EMR, (3) generates proactive alerts at configurable thresholds ("Patient has 3 visits remaining — initiate extension") with sufficient lead time for the extension process, (4) pre-populates extension request forms with clinical data pulled from the EMR — latest outcome scores, functional improvement data, treatment goals, and remaining treatment plan items, (5) tracks extension request status through submission, review, approval/denial, and appeal, and (6) reports on authorization-related revenue risk across the practice — total patients within 2 visits of expiration, total pending extensions, total unauthorized visits delivered.

## Target Customer
Front desk coordinators, authorization specialists, and billing managers at outpatient PT clinics (5+ clinicians) who currently manage authorization tracking across multiple payer portals using spreadsheets, sticky notes, or EMR free-text fields.

## Impact If Built
Prevents $50K-$200K annually in unauthorized visit losses per mid-sized clinic by ensuring extension requests are submitted before authorization expires. Reduces front desk time spent on authorization tracking by 8-12 hours per week. Eliminates the catastrophic scenario where a patient receives 5-10 unauthorized visits before anyone notices the authorization lapsed.
