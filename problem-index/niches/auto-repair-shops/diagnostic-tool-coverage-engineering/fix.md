# Coverage Is Sold as a Checkbox and Experienced as a Function That Does Not Run

**Niche:** [[niches/auto-repair-shops/diagnostic-tool-coverage-engineering/profile|Diagnostic Tool Coverage Engineering]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Fix (Pain Point)
**One-liner:** A shop buys a tool against a make-model-year coverage list, then discovers on a customer's car that the specific function it needed is partial, unreliable or absent — and neither the shop nor the vendor can say in advance which it will be.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #worker-facing

## The Problem
Coverage is marketed at the resolution of vehicle: this tool covers Ford, 1996 to present. Coverage is experienced at the resolution of function: can I run the steering angle sensor relearn on this specific 2019 trim, right now, with the customer waiting.

Between those two resolutions sits everything that goes wrong. A tool may read codes on a vehicle but not stream the live data that would localise the fault. It may support a bidirectional test on most trims of a model and not the one on the lift. It may have a code definition that is generic where the manufacturer's is specific. It may connect to four modules out of nine. Every one of those is "covered" on the list.

The technician finds out by trying. A diagnostic that fails halfway is worse than one that never started, because the labour is already spent and the customer is already waiting. In independent shops running thin margins on diagnostic time, this is a direct and frequent loss, and it drives the expensive defensive behaviour the segment is known for: buying two or three tools and learning by experience which one works on which car.

The vendor's coverage engineers are not being dishonest. Coverage genuinely is partial, protocol behaviour genuinely varies by trim and software revision, and the marketing resolution is the resolution the sales channel understands. But the gap between claimed and realised coverage is not measured by anyone — not the vendor, not the shop, not the trade press.

## Why It's Still Broken
Coverage lists are a competitive artefact. They are compared side by side in buying decisions, and no vendor will be the first to publish coverage at function level with honest reliability rates while competitors publish checkboxes. Being more truthful loses the comparison.

The measurement is genuinely hard to define. What counts as a function working? Completing on the bench car, on most trims, on a car in poor condition, in the hands of a technician who has done it before? Without an agreed definition, nobody has to produce a number.

The failure is attributed to the vehicle. When a function does not complete, the diagnosis inside the vendor is usually that the vehicle was faulty, the connection was bad, or the technician erred — and each of those is sometimes true, which is enough to keep the question closed.

Support tickets are the only feedback channel and they systematically undercount. Technicians in a hurry do not file tickets; they switch tools and move on. The vendor's view of field reliability is therefore built on the small, unrepresentative fraction of failures that someone had time to report.

And the shop has no way to aggregate its own experience. A technician knows this tool is unreliable on that platform. Nobody in the shop has that written down, and nobody across shops has it pooled.

## What a Fix Looks Like
**Define function-level success and measure it.** A single agreed criterion — did the requested function complete and return a usable result — applied per vehicle, per trim, per function, from field telemetry rather than tickets. Everything else follows from having the number.

**Report coverage with an interval, not a tick.** "Bidirectional ABS bleed, 2018-2022 platform: completes in 94% of attempts, n=3,100 shops" is a usable statement. A checkmark is not. The uncertainty matters most exactly where coverage is thin and the sample is small, which is where buyers are currently most misled.

**Test whether reported failures differ from the rest.** The claim that failures are vehicle or user problems rather than coverage problems is testable against the telemetry population, and it should be tested rather than assumed. Where it holds, the vendor can say so with evidence; where it does not, it is a coverage defect that support has been absorbing.

**Warn before the attempt, not after.** The tool knows the vehicle, the trim and the function requested before it starts. Where the historical completion rate is poor, saying so up front costs a technician thirty seconds instead of forty minutes.

**Give the shop its own record.** Which functions on which platforms have worked in this shop, on this tool, is a small dataset that already exists in the tool's own logs and would settle arguments that currently run on memory.

## Who Feels the Pain
The technician, whose diagnostic time is billable and whose failed attempt is not. The shop owner, paying for two or three overlapping tool subscriptions as insurance against coverage claims nobody can verify. The vehicle owner, paying for diagnostic labour that produced no diagnosis. And the coverage engineer, whose good work is invisible because nobody measures what actually works in the field.

## Impact If Fixed
Diagnostic capability at the independent shop is the gate on whether most vehicles in the country can be repaired outside a dealership. That capability is bought against claims measured in checkboxes, and the difference between the checkbox and the reality is paid for in unbillable labour, one failed diagnosis at a time.
