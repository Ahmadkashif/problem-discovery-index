# Read-Confidence Gating at the Exit

**Niche:** [[niches/parking-operators/frictionless-entry-capture/profile|Frictionless Entry & Paid-at-Exit Capture]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A camera platform treats a low-confidence plate read the same as a clean one, so members get billed wrongly or paying drivers become unpaid sessions.
**Tags:** #cnns #object-detection #transformers #logistic-regression #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to have every car pay before it leaves, and whoever collects the highest share of parking sessions as payment at or before exit, with no notice needed, takes the account.

## The Problem
Dirty plates, temporary tags, bike racks and glare produce misreads at ~1–3% of plates in poor light (estimate). Misread entries fail to match exits, and the session is lost or charged to the wrong account.

## Why Nobody Has Built This
Recognition vendors report average accuracy, not calibrated per-read confidence, and the cost of a misread lands later, on the notice processor or the support desk.

## What to Build
A calibrated confidence score for every read and every entry–exit match, computed from the detector and OCR outputs, image quality and match ambiguity within the facility. High-confidence matches charge automatically. Low-confidence ones trigger a prompt at the exit (screen, text or QR) before the car leaves, and anything still unresolved is held back from notices. Reads are matched only within one facility, and images are deleted on the state and contract retention schedule.

## Target Customer
Camera-platform operators and PARCS vendors adding recognition.

## Impact If Built
Resolving half of misread sessions at the exit (estimate) on a facility with 1,000 exits a day and a 2% misread rate saves ~10 sessions a day, worth ~$40–70K a year at typical tickets.
