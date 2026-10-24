# A Protocol Ledger and Suggester That Abstains on Contrast

**Niche:** [[niches/diagnostic-imaging-centers/exam-protocolling/profile|Exam Protocolling]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Radiologists protocol hundreds of orders a day with no record of why, so the decision can neither be learned nor handed to a junior.
**Tags:** #tacit-knowledge-ml #transformers #bert #large-language-models #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to attach the right protocol to every order before the patient arrives, and whoever cuts radiologist protocolling minutes per order most, with no rise in protocol-attributable repeats or recalls, takes the account.

## The Problem
A radiologist clears 80 protocol requests between reads, at 20–40 seconds each (estimate). Most are routine, and a few need judgement: prior surgery, renal function, an odd indication. The routine ones still take the same clicks, and the judgement ones get the same rushed glance.

## Why Nobody Has Built This
Protocol outcomes are scattered across reports, addenda and later orders, and protocol libraries differ by group and scanner. Contrast decisions carry patient-safety risk that makes vendors avoid automation claims.

## What to Build
A ledger that joins each order to its protocol, in-scan changes, report and any recall, repeat or "limited study" addendum. A suggester proposes the top protocol with confidence and evidence, and is calibrated to auto-propose only above a precision threshold. It always abstains on contrast in reduced renal function, prior reactions, implants and paediatric sedation. Every acceptance or edit becomes training data.

## Target Customer
Radiology groups reading for multi-site centres, and operators that employ their own radiologists.

## Impact If Built
Auto-proposing 60% of orders for one-keystroke sign-off would return 3–5 radiologist-hours a day to a five-radiologist group (estimate). That is time for 40–80 more reads.
