# Build: Which Controls Actually Matter

**Niche:** Control Efficacy Measurement
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Join a normalised corpus of control implementation across tens of thousands of organisations to what actually happened to them, and report which controls carry evidence of effect.
**Tags:** #causal-inference #logistic-regression #survival-analysis #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance
**Contested on:** Whether the relationship between implementing a framework's controls and actually suffering fewer incidents has ever been measured, by anyone.

## The Problem

Security compliance operates on an untested hypothesis. A framework lists controls, an organisation implements them, an auditor confirms it, and the resulting certificate is treated throughout the economy as evidence of reduced risk. The size of that belief is enormous — it gates enterprise sales, sets insurance premiums, satisfies regulators and directs engineering budgets.

The evidence for it is essentially the plausibility of each control read individually. Frameworks are consensus documents produced by committees of experienced practitioners, which is a reasonable way to start and is not the same as knowing. Controls persist across revisions because removing one requires someone to argue it does not matter, and nobody has the evidence to argue that either.

So a hundred controls are treated as roughly equally important, when it is nearly certain that a small number carry most of the protective effect, a larger number carry some, and a meaningful tail carries approximately none and consumes real engineering time.

The data to sort them exists, split across two parties. Platforms hold continuous control state at scale. Insurers hold claims. Regulators hold breach notifications. Nobody has joined them, and the party with the largest half has a business model that benefits from all controls being treated as necessary.

## Why Nobody Has Built This

**The answer is commercially uncomfortable.** A platform that demonstrates a third of the controls it certifies against carry no measurable effect has undermined part of the product it sells and the framework its customers pursue. This is the central reason and it is not subtle.

**The outcome data is somewhere else.** Incidents are disclosed reluctantly, claims are held by insurers as competitive information, and public breach reporting captures only the largest events with substantial selection bias. The dependent variable is the hard half and it is covered in [[niches/grc-compliance-platforms/outcome-linkage/profile|🎯 Outcome Linkage]].

**Confounding is severe.** Organisations that implement controls well differ from those that do not in every way that matters — resources, maturity, sector, threat exposure. Separating the effect of a control from the effect of being the kind of organisation that implements controls is genuinely hard, and a naive analysis would produce confidently wrong answers that would discredit the whole effort.

**Control state is not comparable across organisations.** A control marked passing at two companies may describe entirely different configurations. Without normalisation the independent variable is noise, which is the subject of [[niches/grc-compliance-platforms/control-state-normalisation/profile|🎯 Control State Normalisation]].

**Base rates are low.** Serious incidents are rare per organisation per year, so detecting an effect requires very large samples and long observation — which is precisely why only a platform with tens of thousands of customers could attempt it.

**Nobody is asking.** Buyers accept the certificate, insurers accept the questionnaire, regulators accept the framework. There is no external pressure forcing the question, and the only parties who could answer it have a reason not to.

## What to Build

**Normalise the independent variable first.** A comparable measure of control implementation across organisations — not a pass flag but a graded description of what is actually configured, derived from the integration data the platform already collects. Nothing downstream is possible without this and it has independent value.

**Assemble outcomes from every available direction.** Voluntary customer incident reporting under strong confidentiality, public breach disclosures, regulatory notifications, and — the most promising route — partnership with a cyber insurer holding claims. Each source is biased differently, and using several with their biases modelled explicitly is better than waiting for one clean one.

**Design for confounding from the start.** Matched comparisons on organisation size, sector, maturity and exposure; within-organisation change analysis, which is the strongest available design — did incident rates change after this control was implemented, in the same organisation; and instrumental approaches where framework revisions or customer mandates forced implementation for reasons unrelated to the organisation's own risk. Natural experiments of that kind are the credible path and they exist in this data.

**Report effect with honest uncertainty, and report nulls.** Controls with evidence of effect, controls with evidence of no effect, and controls where the data cannot distinguish — which will be the largest category and should be stated as such. Publishing the nulls is what would make the work credible rather than promotional.

**Start with the questions that are answerable now.** Some relationships have enough events to study with existing data — multi-factor authentication coverage against account compromise, patch latency against exploitation, logging coverage against detection time. Demonstrating the method on those builds the credibility needed for the harder questions.

**Publish, do not productise.** The finding's value is in being believed, which means peer review, open methodology and independence from the commercial interest. A vendor publishing self-serving efficacy research would be correctly discounted, so the work should be structured as research with external collaborators from the start.

## Target Customer

Cyber insurers are the best-aligned partner and the most motivated: they price risk, they hold the outcome data, and every control-effect finding directly improves their underwriting. A platform-insurer research partnership is the single most plausible route to this existing.

Regulators and framework bodies as the eventual audience, since evidence-weighted frameworks would be a genuine improvement over consensus ones and they have no data of their own.

Enterprise security buyers, who allocate budget across controls with no basis for prioritising, and would use an efficacy weighting immediately.

## Impact If Built

Security compliance would acquire an evidence base, which is the single largest missing foundation in enterprise security practice. Billions in spend is currently directed by committee consensus.

Weighting controls by evidence would let organisations concentrate scarce engineering effort where it demonstrably matters, rather than spreading it evenly across a list because no other allocation is defensible.

And the nulls matter as much as the positives. Retiring controls that carry no measurable effect would free real capacity and would force frameworks to justify what they ask for — which is a discipline the field has never had.
