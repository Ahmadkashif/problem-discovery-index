# Dredging Pay Quantities Argued From Before-and-After Surveys

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hydrographic software computes volumes perfectly well. What it doesn't do is apply each Corps contract's pay prism, allowable and unpaid overdepth and side-slope rules, so dredging contractors reconcile what they moved against what they'll be paid in spreadsheets, after the money has been decided.
**Tags:** #numerical-methods #gaussian-processes #feature-engineering #hypothesis-testing #data-integration #revenue-impact #automation

## The Problem
A dredging contractor is paid by the cubic yard, but not for every cubic yard it moves. Under the Corps' dredging specification (UFGS-35 20 23), the pay quantity is the volume difference between soundings taken before and after dredging. It counts material inside the required depth plus a stated allowable overdepth, paid at full price, and the side slopes to a stated ratio. Material below that is unpaid overdepth, and beyond a further limit it can trigger deductions. Monthly progress payments come from progress soundings or, at the Contracting Officer's option, 85% of scow measurement. The government's surveys decide the final quantity, and the contractor "has the option of being present".

So the contractor runs its own surveys, a sounding boat and a surveyor running lines before, during and after, to know where it stands. The surveyor then reconciles four numbers: the contract's estimated quantity (subject to FAR 52.211-18 variation in quantity), the contractor's survey volumes cut to the pay template, the production the dredge's own sensors say it pumped, and the government's pay volume. When they disagree, the explanation is usually spatial: a shoaled reach resurveyed late, overdredging in soft material, side slopes cut steep. The analysis to prove it is done by hand.

## What Already Exists
Hydrographic acquisition and processing packages (HYPACK and its peers) clean multibeam and single-beam soundings and compute surface-to-surface volumes. Civil design software builds the channel template. Dredge monitoring systems feed the Corps' Dredging Quality Management programme. The earthwork version of this reconciliation, design surface against machine control, survey and truck counts, is mapped at [[niches/construction-tech-platforms/earthwork-quantity-reconciliation/profile|Earthwork & Sitework — Quantity Reconciliation]].

## The Customisation Gap
The dredging layer that has to be added is the contract's pay geometry: required depth, paid allowable overdepth and the unpaid limit by reach, side-slope ratios, dredging limits, placement-area quantities, and the survey timing rules. It also has to account for the survey uncertainty that the Corps' hydrographic standards accept, and shoaling between the before survey and the dredge's arrival. On top of that it needs a running pay estimate by reach from the contractor's own surveys and DQM production, so the project manager sees paid versus moved weekly. Volume software reports a number; it doesn't report what fraction of that number is payable or why.

## Impact If Solved
If unpaid overdepth on a maintenance or capital dredging job runs ~5–15% of material moved (estimate), seeing it by reach in the week it happens lets the crew correct cut depth before the money is gone. On a $20M dredging contract (illustrative) a few points of recovered pay volume is worth more than the survey crew's annual cost.
