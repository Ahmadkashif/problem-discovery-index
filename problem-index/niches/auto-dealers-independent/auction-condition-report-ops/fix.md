# Two Inspectors, One Vehicle, Different Grades, Thousands of Dollars

**Niche:** [[niches/auto-dealers-independent/auction-condition-report-ops/profile|Wholesale Auction Condition Report Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** The composite grade moves the sale price materially and the auction has never measured how much of it is the vehicle and how much is the inspector.
**Tags:** #evaluation-metrics #hypothesis-testing #tacit-knowledge-ml #worker-facing #automation

## The Problem
The condition grade is a number attached to a vehicle by a person. It is built from a walkaround under time pressure, applying a written standard to cosmetic wear, mechanical impressions and disclosure judgments, and it moves the realised price by an amount that dealers track closely.

Inspectors are trained and certified against the standard. What is not established is whether two certified inspectors grading the same vehicle produce the same result — and the structure of the work makes it likely they do not. Cosmetic severity thresholds are inherently judgmental, lighting and lane conditions vary, and the workforce turns over quickly enough that experience distribution is wide.

Because vehicles are graded once, the variance is invisible. A seller whose cars are consistently graded by one inspector and a seller whose cars go to another are receiving different treatment, and neither can detect it. A dealer who believes a particular auction grades harshly may be right, and has no evidence.

The variance also contaminates everything downstream. Grade-based price analytics, the arbitration risk modelling above, and the market reports the auction publishes all rest on grades carrying inspector noise as if it were vehicle condition.

The inspectors' own knowledge is equally unrecorded. Experienced inspectors know which damage types are routinely under-called, which models hide structural repair, and where the written standard is ambiguous. None of it is captured.

## Why It's Still Broken
Throughput governs. Vehicles must be inspected before the lane runs, and duplicate grading consumes capacity in a workforce that is already the bottleneck.

Measurement is also uncomfortable for a high-turnover, frequently contracted workforce. Individual accuracy scores in that setting are a labour relations question before they are an analytics question, which is a real constraint on design rather than a reason to avoid the measurement.

And the auction is caught between customers again: demonstrating grading variance invites disputes from sellers who were graded harshly and buyers who were graded generously, on transactions already settled.

## What a Fix Looks Like
**Duplicate-grade a rolling sample.** A small share of vehicles graded independently by a second inspector, continuously. That single practice converts grading consistency from an assumption into a measurement.

**Report agreement by damage category and by site, before by individual.** Where the standard is ambiguous, the fix is the standard. Starting with categories and locations rather than named inspectors makes the programme survivable and is where most of the improvement is.

**Use the imagery as a standing referee.** Where a second observer from photographs disagrees with the human record, that is a calibration event that costs nothing to generate.

**Flag borderline grades explicitly.** A vehicle sitting at a grade boundary carries more risk for both parties than one well inside it, and the report says only the grade.

**Capture where the standard is unclear.** A one-tap note recording an ambiguous call, with the reason, builds the record of which parts of the condition standard need rewriting — which is the highest-leverage fix available and currently invisible.

**Weight the historical corpus accordingly.** Grades from periods or sites with measured drift should be discounted when fitting the price and arbitration models, not treated as truth.

## Who Feels the Pain
Dealers buying sight-unseen on a grade whose reproducibility is unknown; sellers whose consignments are worth more or less depending on who inspected them; inspectors carrying a price-moving judgment with no calibration feedback; and the auction, whose product in a digital market is the trustworthiness of a number it has never tested.

## Impact If Fixed
Wholesale has moved to buying on description, which makes grading consistency the platform's core product attribute. Measuring it makes the grade defensible in dispute, identifies the parts of the condition standard that actually need rewriting, and cleans the corpus that every analytical use of condition data depends on.
