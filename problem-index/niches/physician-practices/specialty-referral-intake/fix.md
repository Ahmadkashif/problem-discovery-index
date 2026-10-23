# Referrals That Vanish Between Two Fax Machines

**Niche:** [[niches/physician-practices/specialty-referral-intake/profile|Referral Intake in Specialty Practices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** The primary care office faxes a referral and assumes it arrived; the specialist's office never matches it to a patient who calls; neither side knows the referral died until the patient gets worse.
**Tags:** #data-integration #survival-analysis #workflow-orchestration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn each inbound faxed referral into a scheduled, insurance-cleared first visit within a day, and whoever converts the most referrals into kept first visits takes the account.

## The Problem
Referral loops fail at every handoff: the fax fails, the packet is filed under the wrong patient, the specialist's office calls once and gives up, or the patient never schedules. Trade estimates put the share of referrals never completed at ~20%–30% (recalled). For an urgent referral that is a safety event, and for the specialist it is lost revenue.

## Why It's Still Broken
Each office tracks only its own side. The sender has an order with no status, and the receiver has a fax with no link back. No shared identifier joins the two, and no one is paid to close the loop unless the group is in a value-based contract.

## What a Fix Looks Like
Track each referral as one object across both offices: sent, received, matched, contacted, scheduled, seen, consult note returned. Lapses trigger outreach at set intervals, and urgent referrals escalate to a nurse. The receiving practice confirms receipt automatically, and the consult note files itself to the sender's chart.

## Who Feels the Pain
Referral coordinators on both sides; PCPs who carry the liability for a lapsed urgent referral; specialists who lose the patient.

## Impact If Fixed
Recovering even a third of lapsed referrals (estimate) adds ~5%–10% to a specialty group's new-patient volume. It also closes a documented diagnostic-delay risk for the referring practice.
