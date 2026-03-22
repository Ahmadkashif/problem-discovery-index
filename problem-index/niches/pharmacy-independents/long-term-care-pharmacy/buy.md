# FrameworkLTC with Facility Coordination Portal and Medication Pass Optimization

**Niche:** [[niches/pharmacy-independents/long-term-care-pharmacy/profile|Long-Term Care Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** FrameworkLTC handles dispensing and cycle fills but facility coordination — new orders, delivery confirmation, medication discrepancies, emergency requests — still runs on fax, phone, and email, creating a communication gap that causes medication errors and delivery delays.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win #compliance

## The Problem
LTC pharmacies interact with facility nursing staff 20-50 times per day: new medication orders faxed in, order clarifications called back, delivery confirmations phoned, medication discrepancy reports discussed, emergency "stat" orders communicated urgently. Each interaction is unstructured — a fax that may or may not be legible, a phone call to whoever answers at the nursing station, a voicemail that sits unheard for hours. The pharmacy has no unified view of pending facility requests, and the facility has no visibility into order status. When a new admission arrives at a nursing home on Friday evening, the facility faxes the admission orders to the pharmacy, then calls to confirm receipt, then calls again to ask when medications will arrive — each touchpoint consuming time on both ends.

## What Already Exists
FrameworkLTC and QS/1 LTC handle the dispensing workflow: medication profile management, cycle fill generation, label printing, and billing. Some facilities use PointClickCare or MatrixCare for their side of the workflow. eMAR (electronic medication administration record) systems track what the nurse gives, but don't communicate back to the pharmacy in real time. SurescriptsClinical messaging exists but adoption for LTC facility-pharmacy communication is low.

## The Customization Gap
The gap is a shared coordination portal between the LTC pharmacy and its client facilities that: (1) replaces fax-based order transmission with digital order entry showing the resident's current medication profile for context, (2) provides real-time order status tracking — received, verified, in production, packaged, out for delivery, delivered — visible to both pharmacy and facility staff, (3) manages emergency order requests with priority routing and estimated delivery time, (4) documents medication discrepancy reports with resolution tracking, and (5) supports narcotic reconciliation workflows with digital counts and sign-offs. This needs to integrate with both FrameworkLTC (pharmacy side) and PointClickCare (facility side) through their respective APIs, and must be simple enough for a CNA or LPN to use on a tablet at the nursing station. A coordination layer priced at $50-100/month per facility (paid by the pharmacy as a service differentiator) fills this gap.

## Target Customer
LTC pharmacy owners serving 5-20 facilities who lose 2-4 hours daily to phone/fax communication and risk facility contract loss when coordination failures cause medication delivery delays or errors.

## Impact If Solved
Eliminates 2-4 hours of daily phone/fax coordination time, reduces medication order errors caused by illegible faxes by 70-80%, and gives facility nursing staff real-time delivery visibility that eliminates "where are my meds?" callback cycles. Pharmacies offering this coordination portal gain a competitive advantage in facility contract retention — the average LTC pharmacy contract ($200,000-500,000/year per facility) is won or lost on service reliability.
