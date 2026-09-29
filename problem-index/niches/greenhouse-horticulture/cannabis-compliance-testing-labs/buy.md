# LIMS Adapted to a Result That Destroys Inventory

**Niche:** [[niches/greenhouse-horticulture/cannabis-compliance-testing-labs/profile|Cannabis Compliance Testing Laboratories]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Laboratory information systems are built for clinical and environmental testing, where a result informs a decision rather than deciding whether the sample's source can be sold.
**Tags:** #data-integration #workflow-orchestration #anomaly-detection #compliance #automation

## The Problem
A cannabis lab runs a fixed panel against action limits set by a state, on a chain of custody the state tracks, reporting into a state seed-to-sale system, on a turnaround the customer's working capital depends on. Every sample is the same shape and the stakes are binary.

The LIMS platforms serving these labs were built for clinical or environmental laboratories and adapted. They handle sample accessioning, instrument integration, and reporting competently. What they do not handle is the thing specific to this sector: the result is a gate on someone else's inventory, and everything about how the lab should prioritize, investigate, and communicate follows from that.

## What Already Exists
Mature LIMS platforms — LabWare, STARLIMS, LabVantage — with instrument integration, chain of custody, quality control workflows, and audit trails. Statistical process control tooling for analytical quality. Both categories are decades old and technically strong.

## The Customization Gap
Four adaptations, none of which the generic platforms make.

**Turnaround as an economic variable.** In a clinical lab, priority is clinical urgency. Here, every day a batch sits untested is holding cost on inventory the cultivator cannot sell, and sample scheduling should reflect batch value and the client's position, not arrival order. Generic LIMS scheduling is first-in-first-out with a STAT flag.

**Re-test and remediation as first-class workflow.** A failing batch is not the end of the record. It may be remediated and re-tested, and the relationship between the original result, the remediation, and the re-test is exactly the sequence a regulator and a lawyer will later want. Generic systems model a re-test as an unrelated new sample.

**Quality control tied to the action limit.** A result near the limit needs different scrutiny than one far from it, because that is where a lab's methods get challenged and where the incentive to shade exists. Uncertainty handling in generic LIMS is method-wide, not limit-relative.

**Cross-client pattern surfacing.** The same pesticide appearing across unrelated cultivators in a month is a supply chain contamination event, visible only to the lab. No generic LIMS has a concept of a finding that spans clients, because in clinical testing that would be a privacy violation rather than a service.

## Target Customer
Laboratory director at a licensed cannabis testing lab, typically running one to five sites and dissatisfied with a LIMS deployment that was configured rather than designed for the work.

## Impact If Solved
Faster turnaround on the batches where days cost the most, a defensible record when a result is disputed, and quality control focused where the risk actually is. The lab's operating constraint is throughput against a fixed instrument base, and scheduling against value rather than arrival order improves the economics without adding a single instrument.
