# A Methodology Applied to Millions of Families and Never Validated

**Niche:** [[niches/k12-private-schools/financial-aid-need-assessment/profile|Financial Aid Need Assessment Services]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The expected family contribution decides whether a child attends, and nobody has checked whether the families it says can pay actually do.
**Tags:** #tabular-ml #gradient-boosting #causal-inference #evaluation-metrics #revenue-impact

## The Problem
The need methodology takes a family's income, assets, debts, household size, and business interests and produces a single number: what they can be expected to contribute. Schools award aid against it. Pass 1 puts the stakes plainly — a school missing enrolment by 5% faces a six-figure gap with no public backstop, and aid is the largest lever it has.

The methodology is a formula with tables, allowances, and treatment rules, refined by committee over decades. It is thoughtful and it is unvalidated. Nobody has established whether families the formula rates as able to contribute $18,000 actually enrol at that price, whether they persist, or whether they fall behind on payments.

The company can answer all three. It sees the family's submission, the school's award, and — through its own tuition billing operations — whether the family enrolled, paid on schedule, and returned the following year. The loop is closable inside one business and it is not closed.

## Why Nobody Has Built This
The methodology is a fairness instrument, not a prediction. It was designed to treat comparable families comparably, and its authority rests on being principled and transparent rather than on being predictive. Validating it against enrolment behaviour feels like changing the question.

It is not. A family who declines because the contribution was set beyond what they could actually manage is a family the methodology got wrong on its own terms — able to pay is a factual claim, and it is testable.

The organizational split does the rest. Need assessment, billing, and payment plans are separate product lines with separate data, and joining them is a project nobody owns.

## What to Build
Validate and extend the methodology against observed family behaviour.

**Measure yield against contribution.** For families with similar profiles awarded different net prices, what happened? Enrolment response to net price is estimable from the natural variation across schools' different award policies, and it is the single most valuable number in private school enrolment.

**Model payment difficulty.** Delinquency, plan changes, and mid-year withdrawal are observable in the billing operation and are the direct test of whether a contribution was set too high. A family who enrols and then cannot pay is a worse outcome for everyone than one who was awarded correctly.

**Find where the formula is systematically off.** Self-employment income, variable compensation, multi-generational households, families with recently changed circumstances — these are the cases where a formula built on wage-and-salary assumptions is most likely to be wrong, and where the volume of appeals concentrates.

**Give schools a net revenue model.** Schools set aid budgets and discount policy blind. A tool that projects enrolment and net tuition revenue under alternative award policies is a genuinely new product, and the company is uniquely positioned to build it.

## Target Customer
Chief Product Officer or VP of Data at a need assessment provider. The commercial argument is that schools are the buyer and enrolment is their existential problem: a provider that helps a school hit its net revenue target is selling something categorically different from a calculation service.

## Impact If Built
Aid decisions determine which children attend which schools, and they are made with a formula nobody has tested against what families actually do. Validating it improves fairness in the direction the methodology already claims to care about, and gives schools facing a demographic squeeze the one analysis that would let them price deliberately rather than by precedent.
