# Early Arrears Detection Wired to an Intervention

**Niche:** [[niches/proptech-platforms/delinquency-payment-operations/profile|Delinquency & Payment Operations]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A household's payment behaviour changes months before it misses rent entirely, the operator records every one of those payments, and the first action anyone takes is a late notice.
**Tags:** #survival-analysis #change-point-detection #logistic-regression #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in rental payment operations is fighting to identify a household moving into arrears early enough that a payment plan or an assistance referral still works — and whoever finds them earliest, without turning the capability into a screening tool, takes the account.

## The Problem
A household paid on the first of the month for twenty-six months. In March they paid on the seventh. In April they paid half on the third and half on the nineteenth. In May they did not pay. The operator's first action was a late fee in March and a notice in May. By the time anyone spoke to the household about what was happening, the arrears were two months deep, an assistance application would take weeks they no longer had, and the process had moved into a legal track that costs the operator thousands of dollars and costs the household its home. The trajectory was legible from February.

## Why Nobody Has Built This
Delinquency management was built around a legal sequence because the legal sequence is what the operator's counsel specified, and no product has been asked for an earlier, supportive branch. There is also a reasonable institutional wariness: a model that flags households as likely to fall behind is one step away from a model that excludes them, and vendors have not wanted to build the first without a clear answer about the second. That is a legitimate concern and it has a design answer — restrict the signal architecturally to intervention use, prohibit its availability at screening and renewal, and log every access — rather than a reason to leave households to reach a filing.

## What to Build
A trajectory model over payment behaviour — timing drift, partial payments, method changes, payment source changes — that identifies households whose pattern resembles those that went on to serious arrears, weeks to months before the first missed payment. The output is not a score on a household's record; it is a prompt to offer something specific, and the product should be built so that the signal has exactly one destination. The offer is determined by what has worked: a payment plan with terms the household can actually meet, a referral to an assistance programme with the application started rather than named, or a conversation. Every intervention and its outcome is recorded, which produces the evaluation nobody currently has — what proportion of flagged households resolved, under which intervention, versus a comparison group. The constraints belong in the architecture: no export to screening, no availability at renewal pricing, access logged, and the model's features restricted to payment behaviour with this operator rather than anything purchased about the household.

## Target Customer
Property operators whose eviction costs and vacancy losses are substantial, housing assistance programme administrators, and tenant support organisations — the last of whom would use the same capability for the same purpose from the other side.

## Impact If Built
An eviction costs an operator thousands of dollars, months of vacancy and a unit turn, and costs a household vastly more than that. Intervention at the point where a payment plan can still work resolves a meaningful share of cases that currently reach a filing. This is one of the clearest cases in the vault where the operator's financial interest and the resident's welfare point the same direction — provided the capability is confined to the use that makes that true.
