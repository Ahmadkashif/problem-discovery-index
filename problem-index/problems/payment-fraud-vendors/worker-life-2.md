# The Risk Strategist Tuning Blind

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Worker Life Changing
**One-liner:** Risk strategists move thresholds and write rules in response to a loss spike or a merchant complaint, and cannot measure the cost of either direction because half the outcomes do not exist.
**Tags:** #causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #worker-facing #revenue-impact

## The Problem
The strategist owns the policy layer: rules on top of the model, thresholds per merchant and segment, review routing, and the response when something changes.

Something changes constantly. A fraud ring finds a weakness and losses spike in a segment. A merchant complains that good customers are being declined. A new payment method arrives with unfamiliar behaviour. A model retrains and shifts the score distribution.

The strategist responds by tightening or loosening, writing a rule, adjusting a routing threshold. The effect on fraud loss is measurable in a few weeks. The effect on good customers declined is not measurable at all, because those transactions produce no data.

So every tuning decision is made on one visible axis and one invisible one. The visible axis is losses, which are loud, attributed and discussed in a monthly meeting. The invisible axis is false declines, which show up as a merchant's vague dissatisfaction, a slow decline in approval rate, or nothing.

Rule libraries accumulate. A rule written during an attack two years ago is still firing, declining a small number of transactions daily, for a pattern that ended long ago. Nobody retires it, because retiring it is a risk with no measurable reward.

And merchants are inconsistent. One demands aggressive protection, another demands approvals, and both judge the vendor on the axis they did not emphasise when something goes wrong.

## Why It Matters to the Worker
The role is accountable for a tradeoff it cannot measure. That is a professionally corrosive position: every decision is defensible and none is demonstrable, and the strategist knows the asymmetry is pushing them steadily toward over-declining.

Blame is asymmetric. A loss event is investigated, attributed and remembered. A year of quietly over-declining is nobody's incident.

The work is reactive. Time goes to responding to spikes and complaints, not to the analysis that would reduce either, because the analysis requires data that does not exist.

And the rule library is a growing liability that only this role can see, and cleaning it requires an argument they cannot evidence.

## What a Solution Looks Like
Randomised allowance as standard infrastructure. A permanent small approval sample in the decline region converts the invisible axis into a measured one, and it is the foundation for everything else in this role.

Rule-level grading. Volume, precision and the estimated cost of each rule, computed from the allowance data, identifies the ones that are now pure cost. Retiring them becomes an evidenced recommendation rather than a gamble.

Counterfactual estimation for changes. Before a threshold moves, estimate what it will do to both axes with intervals, from historical score distributions and allowance-derived outcomes.

Attack detection separated from drift. A loss spike caused by an attack requires a targeted rule; one caused by a shifting merchant population requires recalibration. Treating both with a blanket tightening is how rule libraries accumulate, and distinguishing them is a change-point problem on labelled history.

Merchant-specific objectives made explicit. Each merchant's true cost of a false decline — customer lifetime value — differs enormously, and asking for it converts an argument about preferences into an optimisation with a stated objective.

## Impact If Solved
This role is the control point for a multi-million dollar tradeoff and is operating with one axis unmeasured, which produces a predictable and permanent drift in one direction. Randomised allowance data, rule-level grading and counterfactual estimation give the strategist the evidence to tune deliberately, and give the vendor a defensible account of where its thresholds are set and why.
