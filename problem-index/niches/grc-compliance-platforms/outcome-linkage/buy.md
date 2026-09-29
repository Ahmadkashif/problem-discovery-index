# Buy: Claims Data and Actuarial Access

**Niche:** Outcome Linkage
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cyber insurers already hold the outcome data the field needs, price risk against it daily, and have only self-asserted questionnaire answers to relate it to.
**Tags:** #causal-inference #survival-analysis #bayesian-inference #logistic-regression #evaluation-metrics #confidence-intervals #compliance #revenue-impact
**Contested on:** Whether what actually happened to organisations can be joined to their control state at all.

## The Problem

The dependent variable exists and is held by an industry whose entire business is relating characteristics to outcomes.

Cyber insurers underwrite tens of thousands of organisations, collect security information at inception and renewal, and observe claims — incidents with financial consequence, investigated in detail, with cause analysis attached. That is outcome data of a quality no other party holds, gathered systematically, with strong incentives for accuracy.

Their limitation is the other half. Underwriting information is self-asserted questionnaire response: does the organisation use multi-factor authentication, does it have backups, does it patch. Answered by someone at the organisation, unverified, at a single point in time, and known within the industry to correlate imperfectly with reality.

So insurers have excellent outcomes and poor covariates, while compliance platforms have excellent covariates and no outcomes. The two datasets are complementary to an unusual degree, sit in different companies, and have never been joined.

## What Already Exists

Cyber insurance: a substantial market with underwriting questionnaires, claims databases, incident response panels and increasingly sophisticated risk modelling. Several carriers publish aggregate claims analysis, and some have begun requiring or offering security scanning at underwriting.

Actuarial practice: loss modelling, credibility theory for sparse data, and the regulatory apparatus requiring rating factors to be empirically justified — which is exactly the discipline this problem needs.

Security ratings services: BitSight, SecurityScorecard and their peers, which produce externally observable security scores and have been partially adopted in underwriting, with a well-documented debate about how well they predict anything.

Compliance platforms: continuous, verified, internal control state across tens of thousands of organisations, which is a far better covariate set than anything underwriting currently uses.

Reinsurance and modelling: catastrophe modellers extending into cyber, who need exactly this relationship and currently estimate it.

## The Customization Gap

**The join has no mechanism.** An organisation's insurer and its compliance platform are different companies with no data relationship. Constructing a consented, privacy-preserving join — with the customer's permission, which many would give in exchange for a premium reduction — is the adaptation, and it is commercial and legal rather than technical.

**Verified covariates would replace self-assertion.** The single largest improvement available to cyber underwriting is replacing questionnaire answers with verified continuous control state. Insurers would pay for it, and the platforms hold it.

**Point-in-time versus continuous.** Underwriting captures state at inception and renewal. Control state drifts substantially in between, and an incident's relevant question is what was configured at the time, which only continuous data answers.

**Security ratings already tried the external route and hit a ceiling.** Externally observable signals are a weak proxy for internal control state, which is why the predictive performance debate exists. Internal verified state is the obvious next step and is held by a different set of vendors.

**Claims data is commercially guarded.** Carriers regard loss experience as a competitive asset, which is exactly the dynamic actuarial data bureaus were created to resolve in other lines — pooled, anonymised loss data under industry governance. Cyber has no equivalent bureau.

**Selection effects run through everything.** Insured organisations differ from uninsured ones, claiming organisations from non-claiming ones, and any analysis has to model that rather than ignore it.

## Target Customer

Cyber insurers, singly at first and ideally through a pooled data arrangement. The commercial argument is direct: verified control state is a better rating factor than a questionnaire, and better rating is the core of the business.

The compliance platforms as the covariate supplier, with the customer's consent and a premium reduction as the customer's incentive — which makes the whole arrangement voluntary and mutually beneficial rather than extractive.

A data bureau or reinsurer as the pooling institution, since no single carrier has enough events and the bureau model is well established in other lines.

## Impact If Solved

The two halves of the only empirical question in security compliance are currently in different companies, and joining them requires a commercial arrangement rather than a research breakthrough.

Verified control state would improve cyber underwriting substantially, which is a large business currently pricing on self-assertion — and the improvement would be felt as better-priced insurance for organisations that genuinely implement controls well.

And an actuarial data bureau for cyber would give the field the pooled loss experience that every mature insurance line has, which is the institution that makes evidence possible in a domain with rare events and dispersed data.
