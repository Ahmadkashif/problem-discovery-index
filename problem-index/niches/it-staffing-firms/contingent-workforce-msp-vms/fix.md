# Programme Managers Know Which Suppliers Deliver and Score Them on Speed

**Niche:** [[niches/it-staffing-firms/contingent-workforce-msp-vms/profile|Contingent Workforce MSP & VMS Programmes]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The scorecard measures submission speed and fill rate, and the programme manager's actual knowledge of who to trust with a hard requisition is nowhere in it.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #causal-inference #worker-facing #data-integration

## The Problem
Supplier scorecards rank staffing firms on submission speed, submittal-to-interview ratio, fill rate, and time to fill. Those metrics drive distribution — which suppliers see which requisitions first — and therefore drive the suppliers' revenue.

They also measure the wrong thing in a predictable way. A supplier who submits fast on easy requisitions scores well. A supplier who is the only one who can find a rare skill and takes three weeks to do it scores badly. A supplier whose consultants stay for the full engagement and one whose consultants leave at month four look identical on fill rate.

Programme managers know all of this. They know which suppliers to call when a requisition is genuinely hard, which ones submit padded profiles, which ones handle a specific client's environment well, which ones will quietly decline rather than waste everyone's time. That knowledge routes real work every day, informally, and it is nowhere in the system that produces the scorecard.

## Why It's Still Broken
The scorecard was built from what the workflow already timestamps. Submission times, interview flags, and fill dates are recorded because the process records them, and the metrics are whatever could be computed from that without additional capture.

Quality outcomes are not timestamped. Whether a placed consultant performed, stayed, and was extended is known to the hiring manager and rarely returns to the programme as structured data. So the scorecard measures the process and not the result.

And the manager's judgment is deliberately kept informal. Supplier relationships are commercial and sometimes contentious, and a written record of "this supplier pads profiles" is uncomfortable — which leaves the knowledge unaccumulable and the scorecard uncorrected.

## What a Fix Looks Like
Capture the outcome and the judgment, and adjust the metrics for what was actually asked.

**Close the loop on placement outcomes.** Extension, early termination, conversion to permanent, and a brief hiring manager assessment. This is the missing measurement and it is a short form at two points in an engagement.

**Adjust for requisition difficulty.** Fill rate and time to fill mean nothing without controlling for the skill scarcity, rate ceiling, location, and clearance requirements of what the supplier was shown — and the programme controls distribution, so it knows exactly what each supplier saw.

**Structured programme manager observations.** Typed, dated notes on suppliers — profile accuracy, responsiveness on hard requisitions, environment fit, declination honesty — held internally as programme knowledge rather than as commercial commentary.

**Test the judgments.** With outcomes captured, the manager's view of a supplier can be checked against how that supplier's placements actually performed. Some will hold and become evidence; some will turn out to be reputation, which is equally worth knowing.

**Feed it into distribution.** The point of knowing which supplier can fill a hard requisition is to send it to them. Today that happens through a phone call from a manager who happens to know, which does not survive their departure.

## Who Feels the Pain
Programme managers, whose real expertise routes work and appears in no system. Suppliers, ranked on metrics that reward easy submissions and punish difficult successes. Hiring managers, who receive candidates from whoever scored well rather than whoever was right. And the client, paying for a supplier management function whose central judgment is undocumented.

## Impact If Fixed
Supplier distribution is the programme's main lever on outcomes, and it is currently driven by process metrics that are systematically biased against the suppliers who do the hard work. Adjusting for what was asked and measuring what actually happened afterward makes the scorecard defensible to suppliers, useful to the client, and independent of which programme manager is on the account.
