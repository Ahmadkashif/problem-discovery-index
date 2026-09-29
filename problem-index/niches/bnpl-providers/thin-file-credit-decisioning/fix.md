# The Model Trained Only on Who Was Approved

**Niche:** [[niches/bnpl-providers/thin-file-credit-decisioning/profile|Thin-File Credit Decisioning]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Every model in the stack is trained on applicants who were approved, which is the population the previous model selected, and the declined population has never been observed at all.
**Tags:** #hypothesis-testing #evaluation-metrics #confidence-intervals #logistic-regression #quick-win #causal-inference #gradient-boosting #compliance
**Contested on:** Every serious competitor in this niche is fighting to infer capacity from device, behaviour, basket and their own history when the bureau has nothing to say — and whoever does that best approves the people competitors decline and still gets repaid.

## The Problem
The model learns from approved applicants and their repayment outcomes. Declined applicants produce no outcome, so they are absent from training. The model therefore learns the relationship between features and repayment within the region the previous model already considered acceptable, and knows nothing about the region it excluded. Over successive retraining cycles this narrows: the model becomes confident about the population it has seen and the declined region stays unexplored indefinitely. Growth is left in that region and the model is structurally incapable of finding it.

## Why It's Still Broken
Reject inference is standard in conventional credit and largely absent here, because the sector's modelling came from an engineering tradition rather than a credit one — the practice exists and the people building these systems were not trained in it. Deliberately approving applicants the model rejects means accepting known losses, which requires a budget nobody has allocated. The narrowing is gradual and invisible. And approval rate pressure is applied through thresholds rather than through better models.

## What a Fix Looks Like
Observe the declined region deliberately. Approve a random sample of declined applicants and observe the outcome, which is the fix, costs a known and small amount of loss, and is the only way to learn anything about the excluded population — every other approach is inference about a region with no data in it. Size the sample against the value of what might be found, so it is an investment decision rather than an act of faith. Apply reject inference techniques to extend what the sample teaches across the declined population, which is standard credit practice and is what makes a small sample go far. Monitor the approved population's feature distribution for narrowing, since that is the symptom and it is visible before the growth is lost. Vary thresholds experimentally by segment, which is cheaper than a random sample and reveals the local shape of the boundary. Report the estimated value of the declined-but-good population, which is the argument that gets the loss budget approved. Feed the sample's outcomes into the model explicitly rather than treating them as an anomaly. Track how the model's coverage changes over retraining cycles, because the narrowing is a property of the process rather than of any one model. Handle the fairness implications, since a narrowing model concentrates on a population that may differ systematically from the excluded one. And treat the loss on the exploration sample as a research cost rather than as a risk failure, because that accounting distinction is what determines whether it ever happens.

## Who Feels the Pain
Applicants permanently outside a boundary nobody has tested; providers leaving growth in a region their models cannot see; and a sector whose approval rates are shaped by a feedback loop nobody has interrupted.

## Impact If Fixed
The modelling came from an engineering tradition rather than a credit one, so a standard technique is simply absent and the model narrows each cycle. A small random sample of declined applicants is the only way to learn about the excluded region, and reject inference makes that sample go far.
