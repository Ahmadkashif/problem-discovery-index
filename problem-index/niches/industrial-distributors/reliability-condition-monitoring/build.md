# Alerts Joined to What Was Found on Teardown

**Niche:** [[niches/industrial-distributors/reliability-condition-monitoring/profile|Reliability & Condition Monitoring Services]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Condition-monitoring models are trained on alerts and work orders, almost never on what the removed bearing actually looked like.
**Tags:** #cnns #semantic-segmentation #gradient-boosting #survival-analysis #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to call a bearing, gearbox or coupling failure weeks before it stops the line, with few enough false alarms that planners keep acting on the alerts, and whoever posts the best caught-to-false-alarm record on the plant's own critical assets takes the account.

## The Problem
An alert says "outer race defect, bearing 2, fan 14." Maintenance replaces the bearing at the next shutdown and throws the old one in the scrap bin. Nobody photographs it, classifies the damage, or records whether the alert was right, early, late or wrong about the cause. The model never learns from its own outcomes, and repeat failures caused by lubrication, misalignment or stray current go unnoticed.

## Why Nobody Has Built This
Teardown is done by the plant's technicians, who have no reason to document it. Failure analysis by application engineers is slow and reserved for expensive or repeat failures. The distributor sells the replacement but rarely sees the removed part.

## What to Build
A teardown capture loop: when an alerted component is replaced, the technician photographs it with a phone, the image is classified into ISO 15243 damage families with a root-cause suggestion, and the result is attached to the original alert as its label. Over time this yields per-asset survival curves, a measured caught-to-false-alarm record by machine class, and repeat-failure flags that route to an application engineer.

## Target Customer
Reliability service managers at BPT distributors and condition-monitoring vendors; plant reliability engineers who must justify their programme.

## Impact If Built
If labelled teardowns cut false alarms by ~30–50% within a year (estimate) and root-cause fixes reduce replacements on the worst ~10% of assets by a quarter (estimate), the programme can show a verified catch rate and win renewals on evidence.
