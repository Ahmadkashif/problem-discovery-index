# Triage Dispositions Followed to What Happened Next

**Niche:** [[niches/answering-services/rn-telephone-triage/profile|RN Telephone Triage Lines]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A triage nurse decides tens of thousands of times a year whether a caller can wait, and the triage provider never learns how many of the "home care" callers turned up in an emergency department the next day.
**Tags:** #tacit-knowledge-ml #gradient-boosting #logistic-regression #survival-analysis #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to put a nurse licensed in the caller's state on the line within minutes at 3 a.m. and reach a protocol-correct disposition that keeps safe callers out of the emergency department, and whoever covers every state a practice's patients call from with the shortest wait for a nurse takes the account.

## The Problem
Protocols map symptoms to dispositions (call 911, go to the ED now, be seen today, call the office in the morning, home care). Nurses override the protocol in both directions on judgement. Experienced triage nurses "just know" which reassured-sounding parents to send in. Whether a disposition was safe, or was overtriage that sent a family to the ED for nothing, is visible only in the practice's next-day records, which the triage provider does not see.

## Why Nobody Has Built This
Outcome data is the practice's protected health information, held under a business associate agreement, and practices have not been asked to return it. Protocol publishers update content from expert review and quality projects at a handful of call centres, not from outcomes at scale.

## What to Build
A next-day outcome loop under each practice's agreement. The triage encounter is matched to the practice's next-day visit, urgent-care or ED notification and admission flags, and each disposition is labelled safe, overtriaged or undertriaged. Override-versus-protocol accuracy is modelled by complaint and nurse, and each practice gets a quarterly safety and utilisation report.

## Target Customer
Medical directors at triage providers and at health-system nurse lines; pediatric and family-medicine groups buying triage.

## Impact If Built
Undertriage becomes measurable and coachable, overtriage costs become visible to the practices paying for them, and the experienced nurse's overrides are captured as evidence rather than lost when she leaves.
