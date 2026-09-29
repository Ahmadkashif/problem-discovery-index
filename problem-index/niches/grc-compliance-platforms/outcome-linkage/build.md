# Build: The Confidential Outcome Registry

**Niche:** Outcome Linkage
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A governed registry where organisations contribute incident outcomes under confidentiality strong enough to make participation safe, joined to control state, so the field acquires a denominator.
**Tags:** #causal-inference #bayesian-inference #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #data-integration
**Contested on:** Whether what actually happened to organisations can be joined to their control state at all.

## The Problem

Security has incident data and no denominator. Breach reports describe what happened to organisations that were breached and disclosed it. Nothing describes the population they were drawn from — how many comparable organisations had the same control state and were not breached — so no rate can be computed and no control's effect can be estimated.

The missing half is outcomes from organisations that did not make the news. Incidents detected and contained. Attempted intrusions that failed at a specific control. Ransomware that encrypted a subset and was stopped. Credential compromise that went nowhere because of a second factor. These are far more common than disclosed breaches and are recorded by nobody outside the organisation they happened to.

Every organisation has this data in its own incident records and none of them will publish it. The reasons are entirely rational: legal exposure, customer confidence, regulatory attention, competitive perception. An organisation that describes a contained incident in public has taken a real risk for no benefit to itself.

So the field has excellent data on rare catastrophes and none on the far more informative near-misses, and the parties who hold the near-misses have every reason to keep holding them.

## Why Nobody Has Built This

**Confidentiality is the whole problem and it is institutional.** No organisation will contribute incident data to a system it does not trust completely. Building that trust requires governance, legal structure, independence and a track record — none of which a product can supply and all of which take years.

**The platforms are the wrong host.** A commercial vendor holding a registry of its customers' incidents has a conflict that participants will see immediately, and a data breach of that registry would be catastrophic in a way that makes the whole thing hard to insure.

**Legal exposure attaches to contribution.** In several jurisdictions, documenting an incident in a shared system creates discoverable material. Without legal protection — privilege, safe harbour, statutory shielding — counsel will advise against participation, and counsel will be right.

**Rare events need enormous samples.** Serious incidents are infrequent per organisation per year. A registry needs many thousands of participants over several years before it can say anything, which is a long time before any value appears.

**Definitions are contested.** What counts as an incident varies enormously between organisations. Without a shared taxonomy the contributed data is not comparable, and agreeing a taxonomy is itself a multi-year standards exercise.

**No one is funded to do it.** It benefits the field rather than any participant, which is the classic public-goods problem and is why the analogous institutions in other fields were built by regulators, professional bodies or research funders rather than by companies.

## What to Build

**Establish the institution before the technology.** An independent body — research institution, consortium or regulator-adjacent entity — with governance that participants control, a legal structure that protects contribution, and no commercial interest in the findings. This is the build, and the software is the easy part.

**Secure legal protection first.** Statutory or regulatory shielding for good-faith contribution, modelled on the protections that made aviation and medical incident reporting viable. Without it, counsel blocks participation and nothing else matters. The precedents exist and are well documented.

**Start with near-misses, not breaches.** Contained incidents and blocked attempts are far more numerous, far less sensitive, and far more informative about which controls stopped what. Aviation's safety record was built on near-miss reporting rather than on crash investigation, and the same logic applies exactly here.

**Collect the control state at the time of the event.** The join's whole value depends on knowing what was configured when the incident occurred, not what is configured now. Platforms hold historical control state and this is the specific contribution only they can make.

**Design contribution to be cheap.** Structured, short, integrated with the incident tooling organisations already run, so contributing is a checkbox at incident closure rather than a separate exercise. Every reporting system that required effort has failed.

**Publish aggregates only, with strong disclosure control.** No organisation identifiable, no event reconstructable, minimum cell sizes enforced. The governance has to be visible and auditable, because participation depends on it being believed rather than merely true.

**Use the sparse data properly.** Hierarchical models, credibility weighting and explicit uncertainty, because the honest early output is wide intervals and a small number of findings — and overclaiming in year two would destroy the institution.

## Target Customer

Regulators and government security agencies are the most plausible sponsors, having both the convening power and the ability to create the legal protection, and several already operate voluntary incident reporting with limited uptake for want of exactly this structure.

Cyber insurers are the best-funded interested party, since control-effect estimates improve underwriting directly, and an insurer consortium is a realistic alternative host.

The platforms as data contributors rather than owners, supplying the historical control state that nobody else has.

## Impact If Built

Security acquires the denominator it has never had, which is the precondition for any empirical claim about what works. Every current statement about control effectiveness is expert opinion with a plausible story attached.

Near-miss reporting is where the information density is. Aviation transformed its safety record on exactly this insight, and security has the same structure — plentiful contained events, rare catastrophic ones, and attention focused entirely on the latter.

And an institution with legal protection and credible governance would outlast any vendor, which matters because this is a decades-long observational programme rather than a product.
