# Fitting Identification From a Photo and a Gauge Reading

**Niche:** [[niches/industrial-distributors/fluid-power-hose-counters/profile|Fluid Power & Hose Assembly Counters]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Identifying a hydraulic fitting's thread and seal family is a skill counter staff learn over years; a phone camera and a gauge reading could carry most of it.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #transfer-learning #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a failed hose or fitting carried to the counter into a working assembly on the first build — right thread, right pressure rating, right length — and whoever gets the machine back with zero refits takes the account.

## The Problem
A new counter person faces a dirty fitting with a worn hex and must decide among thread families that look alike: 37° flare versus 45°, tapered versus parallel threads, O-ring face seal versus flare, metric light versus heavy series. They reach for the thread gauge, the seat-angle gauge and the veteran. A wrong call means a refit, a second trip for the customer, or a leak at pressure.

## Why Nobody Has Built This
Fitting identification looks like a small problem to software companies and a solved one to veterans. Manufacturers' tools assume you already know the family. There is no labelled image set of worn, real-world fittings, and collecting one requires working counters.

## What to Build
A counter app that takes two or three photos of the fitting plus the gauge readings the person already takes (thread pitch, outside diameter, seat angle), proposes the family and size with confidence, and shows the visual cues that distinguish the close alternatives. Every confirmed identification at the counter becomes a labelled example. The app then suggests the matching hose and crimp spec.

## Target Customer
Fluid power distributors and broadline branches with hose shops, especially those losing veterans; mobile hose-repair fleets.

## Impact If Built
If photo-assisted identification halves refits from ~5–10% of counter builds to ~2–5% (estimate) and cuts a new counter hire's time to unsupervised builds from ~12–18 months to ~3–6 (estimate), the branch saves second trips and gets a safer first build on assemblies that run at high pressure.
