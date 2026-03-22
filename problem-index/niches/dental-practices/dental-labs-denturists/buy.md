# Production Tracking with Dentist-Facing Portal

**Niche:** [[niches/dental-practices/dental-labs-denturists/profile|Dental Labs & Denturists]]
**Industry:** [[industries/dental-practices|Dental Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lab management software handles internal production tracking but doesn't expose case status to the dentist — the gap is a dentist-facing portal integrated with the lab's existing production system that eliminates "where's my case?" phone calls.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win #revenue-impact

## The Problem
Dental labs track case production internally using lab management software (LabStar, Evident/DDX, Maestro3D) — they know which cases are in design, waxing, casting, finishing, and shipping. But this information is invisible to the dentist who submitted the case. When a dentist's front desk calls to ask "when will the Johnson crown be ready?" a lab receptionist must look up the case, check its current stage, estimate remaining time, and relay that information by phone. Labs with 100+ active cases at any time field 15-25 of these status inquiry calls per day. The calls interrupt lab workflow, consume staff time on both sides, and often result in imprecise answers ("probably Thursday or Friday") that make it impossible for the dental office to schedule the patient's delivery appointment with confidence.

## What Already Exists
LabStar and Evident/DDX have production tracking dashboards for internal lab use. Some labs have built simple web portals on their own (usually a basic PHP page showing case status by ID), but these are custom builds maintained by the lab owner and don't integrate with the production tracking system — staff must manually update the portal in addition to their production system. Package tracking analogies exist (FedEx, UPS tracking pages), but dental case tracking requires production stage granularity, not just shipping status.

## The Customization Gap
The gap is an externally-facing portal layer connected to the lab's existing production tracking system. When a lab technician updates a case to "finishing" in LabStar, the dentist's portal should automatically reflect that status without any additional data entry. The portal needs: (1) case status by stage with estimated completion date (calculated from the lab's historical stage-duration data, not a manual estimate), (2) push notifications to the dental office when the case ships (with courier tracking link), (3) a revision request channel (the dentist can submit shade corrections or fit adjustments with photos before the case ships, reducing remakes), and (4) dentist-facing analytics (average turnaround time, remake rate, on-time delivery percentage) that help the dentist evaluate lab performance. This is a customization of existing production tracking — the data already exists inside the lab system, it just needs an external-facing window.

## Target Customer
Dental labs with 20+ active dentist accounts currently fielding 15-25 daily "where's my case?" calls, using LabStar, Evident, or similar production tracking software that can serve as the data source for a dentist-facing portal.

## Impact If Solved
Eliminates 15-25 status inquiry calls per day (saving 1.5-2.5 hours of lab staff time), enables dental offices to schedule delivery appointments with confidence (reducing patient rescheduling), and provides dentists with objective lab performance data that strengthens the lab's competitive position with high-value accounts.
