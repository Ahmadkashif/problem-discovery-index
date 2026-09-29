# Marketing Attribution Methods for the Development Office

**Niche:** [[niches/crm-platforms/nonprofit-membership-crm/profile|Nonprofit & Membership CRM]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Commercial marketing has spent two decades on multi-touch attribution and incrementality testing, and a development office credits a gift to whichever appeal was mailed most recently.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in donor and member software is fighting to attribute a gift or a renewal to what actually caused it — and whoever answers that credibly takes the development office.

## The Problem
A major donor gives in November. The gift is coded to the autumn appeal because that was the last thing mailed. In fact a gift officer had four meetings with them over eighteen months, they attended a programme site visit in June, a board member called them in October, and the appeal arrived as a reminder rather than as a cause. The development office's channel performance report therefore credits direct mail and undercredits the relationship work, and next year's budget follows the report. This misallocation is systematic and well recognised in the sector, and the attribution methods developed for exactly this problem in commercial marketing have not been imported.

## What Already Exists
Multi-touch attribution, media mix modelling and incrementality testing through holdout design are all mature commercial marketing disciplines with published methods, open implementations and a substantial literature on their limitations. Randomised holdout testing — mailing an appeal to a random 90% and withholding from 10% — is the gold standard, is cheap, and is standard practice in commercial direct marketing. Bayesian media mix models are available as open source. The methodological content is entirely available.

## The Customization Gap
The adaptation is to a small organisation, a long cultivation cycle and a relationship-heavy channel mix. It requires: (1) relationship touches as a first-class channel alongside mail and email, since officer meetings and board contacts are the highest-value activity and are excluded from every commercial attribution model because commercial marketing has no analogue; (2) holdout testing designed for small populations, since a development office with four thousand donors cannot detect small effects and should be told what it can and cannot learn rather than given a spuriously precise attribution; (3) long lag structures, because a cultivation touch may precede a gift by two years and attribution windows built for e-commerce are useless here; (4) explicit separation of the questions — which appeal caused this gift, and what would have happened with no appeal at all — since the second is the one that matters for budget and is only answerable with a holdout; and (5) presentation to a board, which is the real audience for a fundraising performance conversation and which needs the uncertainty stated plainly rather than a point estimate it will treat as fact.

## Target Customer
Development offices at organisations with enough volume to test, nonprofit CRM vendors, and the direct response agencies serving the sector who already understand holdout design from their commercial work.

## Impact If Solved
Holdout testing on appeals is inexpensive, immediately interpretable and almost entirely absent in the sector, and it typically shows that a portion of appeal-attributed revenue would have arrived anyway. Bringing relationship touches into the attribution model is the specific adaptation that matters, because it is the channel the current reporting systematically undercredits and the one the budget should be protecting.
