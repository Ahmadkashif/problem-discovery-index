# History: Synthetic Data Providers

**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Primary Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** omitted — see below
**Episode Tier:** 1
**Transferable Pattern:** A vendor can choose which metric to report about its own guarantee, and no model compels an honest one. Underneath that sits a second, genuine question that research has not settled either way — whether training recursively on generated data degrades a model at all, and under what conditions. Keep the two apart: one is a disclosure choice, the other is contested science.

> **Origin Parent — absent, and this industry actually predates its own primary wave.** No `origins/*/legacy.md` file claims this industry, and unlike most Wave 12 children, the reason is not simply "too new to have a parent" — this industry has **two older lineages of its own**, neither of which is a transformer-era invention, that only got folded under one label recently.

## Before Transformers Had a Name for It — two separate histories, one category

**The privacy lineage.** Differential privacy was formalised by **Cynthia Dwork, Frank McSherry, Kobbi Nissim and Adam Smith in 2006**, in "Calibrating Noise to Sensitivity in Private Data Analysis" — a mathematical guarantee that an algorithm's output should barely change whether or not any single person's record is included, tuned by a privacy parameter **epsilon**: smaller epsilon means more noise and stronger protection, larger epsilon means less noise and better utility. That is sixteen years before ChatGPT, and it is the theoretical foundation the tabular-privacy side of this industry still runs on. **The Synthetic Data Vault (SDV)**, built at MIT by Neha Patki, Roy Wedge and Kalyan Veeramachaneni and released in **2016**, is the clearest dated open-source milestone in the tabular thread — a general-purpose synthetic data generator that predates the transformer wave by a year and remains a common baseline today.

**The simulation lineage.** Separately, commercial autonomous-vehicle and robotics programmes from the mid-2010s needed labelled sensor data covering rare and dangerous edge cases — a pedestrian stepping out from behind a parked van, a sensor failure at highway speed — at a scale and diversity no real-world fleet could safely or affordably collect by driving. Simulation platforms generating synthetic sensor data with perfect ground-truth labels became the answer for that problem, entirely independently of the privacy lineage above; the two share almost nothing except the word "synthetic."

**Wave 12 is a third, later thread**, layered on top of both: large language models increasingly used as a generation method for tabular and text data, alongside the older GAN and diffusion approaches. Treat this industry the way the origins spine treats containerisation and Matson versus McLean — **two independent lines converging under one label, not one lineage** — and note that unlike most children of Wave 12, its oldest verified component (differential privacy, 2006) sits in the Big Data era's own timeframe, which is exactly why this file carries Wave 7 as its secondary rather than treating Wave 12 as a clean origin.

## The Origin Event — there isn't a single one, by construction

Consistent with the two lineages above: there is no SABRE moment here, and manufacturing one would misstate the industry. The nearest thing to a founding date for the thread this vault's hub note treats as central — tabular privacy synthesis — is **SDV's 2016 release**. This session's research could not verify specific founding dates for named commercial vendors in this space (Gretel, MOSTLY AI, Tonic, Hazy) with confidence; that is recorded as a gap rather than papered over with an estimate.

## What Became Cheap

Producing a dataset that is statistically faithful to real data without being composed of real individuals' records — and, on the simulation side, generating rare or dangerous physical scenarios a real sensor fleet would take years, or never manage, to encounter.

## How It Was Actually Solved

Tabular synthesis runs on GAN and diffusion-based generative models, with the open SDV library as a common baseline and large-language-model-based generation increasingly substituting for or supplementing both, per this vault's own hub note. Differential privacy remains the only formal mathematical guarantee available for the privacy side of the trade-off, applied through the epsilon parameter described above. Membership-inference and attribute-inference attacks are the standard empirical privacy evaluations. For perception, simulation platforms generate labelled sensor data at scale, with the sim-to-real gap as the persistent, acknowledged limitation.

## The Declined Join — the epsilon nobody is told about

Here is the point worth making central, because it is exactly the structure the wave-12 era file warns against mistaking for a technology problem. This vault's own hub note records that **epsilon values are "often chosen for utility rather than for meaningful protection."** That is not a measurement failure — the mathematics of differential privacy is well defined and epsilon is precisely computable. It is a **choice**, made by whoever configures the generator, about which epsilon to report and which trade-off to optimise for, and the customer receiving "a set of summary statistics comparisons and a differential privacy epsilon they do not understand" has no way to know whether the number in front of them was chosen to protect them or to make the dataset look good.

The vault's Analysis section states the mechanism behind this bluntly: providers hold thousands of generation runs paired with fidelity evaluations, privacy attack results and, occasionally, downstream model performance — **exactly the corpus a certification standard would need — and no vendor has assembled it, "partly because the results would constrain what they are able to claim."** State this the way the wave-12 era file requires: **a party that chooses not to compute, or not to disclose, an honest number will not be compelled to by a better model.** A more capable LLM-based generator does not change the incentive to report the flattering epsilon rather than the honest one.

## The Contested Technical Question — model collapse, represented honestly

This is the genuine open science this file owes the reader, separate from the disclosure problem above. **Shumailov et al., "The Curse of Recursion: Training on Generated Data Makes Models Forget," posted to arXiv 27 May 2023** and later published in **Nature (2024)**, describe **"model collapse"**: training generative models — variational autoencoders, Gaussian mixture models and large language models alike — recursively on their own or other models' generated output causes **irreversible loss of the tails of the original data distribution**. The Nature paper's mathematical framing treats each generation as a step in a random walk of model parameters, with an early stage where minority, low-frequency data disappears first, and a late stage of severe, compounding performance loss.

**This is genuinely contested, not settled, and the file should say so rather than pick a side.** Gerstgrasser et al. found that collapse can be avoided by **accumulating** synthetic data alongside real data across generations rather than **replacing** the real data with synthetic data outright — a meaningfully different, and more realistic, description of how synthetic data actually enters most training pipelines in practice. Other proposed mitigations include watermarking generated content and entropy regularisation during fine-tuning. There is, in the sources checked, **no unified consensus** on how severe or how avoidable model collapse is at production scale.

**One distinction is worth drawing carefully, because conflating it would overclaim in either direction.** The model-collapse literature is substantially about uncontrolled, internet-scale recursive training — the open question of what happens to a foundation model trained on a web increasingly full of prior models' output. That is a related but different situation from a vendor selling an audited, fidelity-tested synthetic dataset under contract for a specific downstream task. The research bears on this industry's long-run viability; it is not a direct verdict on any single vendor's product.

## Regulatory Status — unsettled, and one hard negative finding

Regulatory acceptance of synthetic data as de-identified data is unsettled in both the US and EU, per this vault's own hub note. On the clinical side specifically: **no drug or medical device has been approved using solely or predominantly synthetic data**, with the FDA and EMA still evaluating methodologies rather than having settled a standard — a negative finding worth stating plainly rather than rounding up to "regulators are moving toward acceptance."

## What's Still Open

- [[problems/synthetic-data-providers/high-impact|🔴 Certifying the Privacy-Utility Trade-Off]]
- [[problems/synthetic-data-providers/low-impact-1|🟡 Relational and Constraint Preservation]]
- [[problems/synthetic-data-providers/worker-life-2|🟢 Privacy Officer Signing Off]]
- [[niches/synthetic-data-providers/utility-privacy-certification/profile|Utility-Privacy Certification]]
- [[niches/synthetic-data-providers/regulated-domain-generation/profile|Regulated-Domain Generation]]
- [[niches/synthetic-data-providers/the-privacy-officer/profile|The Privacy Officer]]
- [[niches/synthetic-data-providers/simulation-for-perception/profile|Simulation for Perception]]

## The Transferable Pattern

> **When a vendor hands you a guarantee, ask which half is a number nobody has computed yet, and which half is a number they chose not to compute in your favour. The first improves with better models. The second does not improve until someone with no stake in the answer is allowed to check it.**

This industry displays both failure modes side by side more clearly than most in this batch: a genuine open measurement problem (certifying fidelity and privacy simultaneously, and the unresolved state of model-collapse research) sitting directly next to a disclosure choice (which epsilon gets reported) that a better model does nothing to fix. An FDE evaluating a synthetic-data vendor's claim should ask which kind of gap they are looking at before proposing to close it with more modelling.

**The existential question, framed and not answered.** Whether an independent certification standard for the privacy-utility trade-off ever gets built — by a regulator, a standards body, or a customer coalition with no stake in flattering any single vendor — is open. So is whether model collapse turns out to be a production-relevant risk or a lab-scale finding that realistic data-accumulation patterns avoid. Ask again in a few years, per this wave's own governing instruction.

**Sources:** Dwork, McSherry, Nissim and Smith, *Calibrating Noise to Sensitivity in Private Data Analysis* (2006); Wikipedia, *Differential privacy*, *Synthetic data*, *Model collapse*; Patki, Wedge and Veeramachaneni, Synthetic Data Vault (MIT, 2016); Shumailov et al., *The Curse of Recursion: Training on Generated Data Makes Models Forget*, arXiv:2305.17493 (27 May 2023), and the related 2024 Nature publication; Gerstgrasser et al. on data accumulation versus replacement; this vault's `industries/synthetic-data-providers.md`, `problems/synthetic-data-providers/*.md`, and `series/eras/wave-12-transformers.md`. Founding dates for named tabular-synthesis vendors (Gretel, MOSTLY AI, Tonic, Hazy) could not be verified in this session and are omitted rather than estimated.
