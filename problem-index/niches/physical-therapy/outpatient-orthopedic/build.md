# Referral Source ROI Dashboard

**Niche:** [[niches/physical-therapy/outpatient-orthopedic/profile|Outpatient Orthopedic PT Clinics]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clinic owners quantify each surgeon referral relationship — volume, conversion, outcomes, and revenue — instead of relying on gut feel to manage the pipeline that keeps their practice alive.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration #revenue-impact

## The Problem
Outpatient orthopedic PT clinics are referral-dependent businesses that have zero data infrastructure around their referral relationships. A clinic owner knows Dr. Smith sends patients, but cannot answer: How many patients did Dr. Smith refer this quarter vs. last? What percentage of Dr. Smith's referrals actually schedule an evaluation? What are the average outcomes for Dr. Smith's post-surgical patients compared to Dr. Jones's? Is Dr. Smith sending fewer patients because a competitor clinic opened nearby, or because a hospital system hired a new surgeon who captures those referrals internally? When a referral source goes quiet, the clinic finds out months later when revenue drops — too late to intervene.

## Why Nobody Has Built This
Referral data is fragmented across fax referrals (still dominant), EMR intake notes, and scheduling systems. No standard data format exists for PT referrals — some arrive as handwritten fax orders, others as electronic referrals through health system portals, others as patient self-referrals who mention their surgeon's name at intake. Linking a referral to downstream outcomes requires connecting the intake record to the treatment episode to the discharge outcome score — a join across multiple data tables that PT EMRs don't expose cleanly. The market is also fragmented: thousands of independent clinics, each with 1-5 locations, making it hard to build a venture-scale business on this problem alone.

## What to Build
A referral intelligence platform that ingests data from the clinic's EMR (WebPT, Prompt, TheraOffice) and scheduling system, identifies referral sources from intake data (physician name, NPI, practice affiliation), and builds a per-referrer dashboard: referral volume over time with trend detection, referral-to-evaluation conversion rate, average treatment duration and outcome scores by referral source, revenue per referral source, and alerts when referral volume from a source drops below its trailing average. Advanced features: compare outcomes by surgical procedure and surgeon to give the clinic data for conversations with referral sources ("Your ACL patients achieve full ROM 2 weeks faster than the regional average at our clinic").

## Target Customer
Owner-PTs and clinic directors at independent outpatient orthopedic PT practices (1-5 locations) who depend on surgeon referrals and currently have no quantitative visibility into referral relationship health.

## Impact If Built
Prevents revenue loss from undetected referral source attrition — a single orthopedic surgeon referral relationship is worth $50K-$200K annually to a PT clinic. Early detection of referral volume decline (4-6 weeks earlier than current manual awareness) gives the clinic time to re-engage the surgeon before patients are permanently redirected. Provides outcome data that strengthens referral relationships and differentiates the clinic from corporate chain competitors.
