# The Installed Base Reports Every Diagnosis It Cannot Complete, and Coverage Is Still Planned by Instinct

**Niche:** [[niches/auto-repair-shops/diagnostic-tool-coverage-engineering/profile|Diagnostic Tool Coverage Engineering]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of engineers decide which vehicles and functions to reverse-engineer next from sales anecdote and the model-year calendar, while millions of tools in the field record precisely which diagnoses technicians attempt and fail to complete.
**Tags:** #gradient-boosting #large-language-models #k-means-clustering #evaluation-metrics #feature-engineering

## The Problem
A scan tool is worth what it covers. The coverage groups at the major tool makers acquire vehicles, put them on a bench, reverse-engineer the manufacturer's module communication, and build out what the tool can do on that vehicle: read and define fault codes, stream live data, actuate components bidirectionally, run calibration and relearn procedures. Coverage breadth is the entire basis of competition, and building it is slow, physical, expensive engineering work performed one vehicle and one system at a time.

The permanent question is therefore what to build next. The space is enormous — every make, every model year, every module, every function — and engineering capacity is fixed. Getting the allocation right is the most consequential decision the organisation makes.

It is made from sales requests, dealer relationships, the model-year introduction calendar, competitor coverage lists, and the accumulated judgment of people who have done this for twenty years. That judgment is real and mostly good.

Meanwhile the answer is arriving continuously and being discarded. Millions of connected tools are in shops, and each one records what happened: which vehicle, which module, which function was attempted, whether the connection succeeded, whether the code returned had a definition, whether the bidirectional test ran, whether the technician tried the same thing four more times and then gave up. A failed diagnostic attempt is the sharpest possible demand signal — a technician with a paying customer's car on a lift, unable to finish the job with this tool.

The vendors collect telemetry and mostly use it for support and licensing. The joint record of attempted-and-failed diagnostics, by vehicle and function, has never been the input to the coverage roadmap.

There is a second discarded dataset alongside it. Coverage is validated in a garage against a small number of acquired vehicles. The field tells you whether it actually works — across every trim, region, software revision and wear state that the bench never sees — and that signal is treated as support tickets rather than as validation.

## Why Nobody Has Built This
The invoice is hardware and a subscription. Coverage engineering is the cost of goods sold, and its budget is defended by output volume — vehicles covered, functions added — not by evidence that the right ones were chosen. Nobody in the structure is accountable for allocation quality, because allocation quality has never been measurable.

Telemetry sits with product and support, coverage sits with engineering, and they answer to different people. The data is not withheld; it simply has no path to the roadmap meeting.

Failure telemetry is also uncomfortable. A dataset that ranks the vehicles the tool cannot handle is a list of the product's shortcomings, and it would be visible to sales and to executives who are told coverage is the strength of the line.

And there is a genuine analytical difficulty. A failed attempt may mean missing coverage, or a broken vehicle, or a technician using the tool wrong, or a bad cable. Separating those requires work, and the absence of that work is the stated reason the signal is treated as noise.

## What to Build
**Rank coverage gaps by observed demand.** Attempted-and-failed diagnostics, grouped by vehicle and function and weighted by how many distinct shops hit them, is a demand estimate with no survey error. It is the roadmap input the organisation has always wanted and has never had.

**Separate the failure modes.** Missing coverage, vehicle fault, user error and hardware fault have different signatures across repeated attempts, across shops and across vehicles. Distinguishing them is a tractable classification problem and it is what turns raw failure counts into a usable ranking.

**Validate coverage in the field, quantitatively.** Every release should be measured on whether its functions actually complete in the wild, by vehicle and trim, against a defined success criterion. Bench validation on three acquired cars is not a substitute and everyone involved knows it.

**Mine the repair narrative.** Where the tool records or is adjacent to the technician's own notes, the chain from symptom to code to tested component to actual fix is present in free text and is the highest-value asset in the whole segment. Structuring it turns a code definition into guided diagnosis — which is the product the segment has been promising for a decade.

**Cluster vehicles by protocol behaviour rather than by badge.** Coverage is planned by make, model and year because that is how vehicles are sold. Modules and protocols are shared across platforms and across brands, and grouping by actual communication behaviour would show where one engineering effort covers far more of the fleet than the badge-based plan implies.

## Target Customer
VP of Engineering or Director of Vehicle Coverage at a diagnostic tool maker. The argument is direct: coverage engineering is the largest discretionary spend in the business, it is allocated on judgment, and the evidence for a better allocation is already being transmitted from the installed base every day.

## Impact If Built
Independent shops handle most of the vehicles on American roads and their diagnostic capability is bounded by what their tools cover. Coverage capacity is finite and is currently pointed by instinct, while the complete record of what technicians actually cannot diagnose accumulates unread.
