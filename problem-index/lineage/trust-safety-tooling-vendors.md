# Lineage: Trust & Safety Tooling Vendors

**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** Perspective API's TOXICITY score — a single number between 0 and 1 returned for any comment sent to the API, calibrated from June 2017 so that 0.8 reads as "80% of people would consider this toxic", with the threshold left to the customer
**Builder:** Jigsaw
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A publisher that let readers comment had to read the comments.

Blocklists caught spelling, not intent. Human moderators caught intent and cost money per comment. So comment sections were rationed or abandoned. The binding cost was not deciding what was abusive; it was deciding it for every comment, in time.

The research that preceded the product quantified the shape of the problem. **Ex Machina: Personal Attacks Seen at Scale** (Wulczyn, Thain, Dixon; submitted 27 October 2016) labelled over 100,000 English Wikipedia talk-page comments by crowd workers, trained a classifier "as good as the aggregate of 3 crowd-workers", and used it to machine-label 63 million more. Its finding was that most attacks did not come from a few bad actors or from anonymous users — so you could not moderate by banning people, only by scoring comments.

## What Got Built

An HTTP endpoint. A developer sends a comment's text; the API returns a score per attribute, of which TOXICITY is the flagship.

The model card defines toxic as **"a rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion"**, trained on comments from Wikipedia and the New York Times with crowdsourced labels, described as a CNN over fine-tuned GloVe embeddings.

**Jigsaw and Google launched it free on 23 February 2017**, with the New York Times, the Guardian, the Economist and Wikipedia named as partners. By June 2017 the Times had opened comments on 80% of its articles.

Then came the decision that defines the artefact. On **13 June 2017** Perspective switched to **normalised scores**, using isotonic regression on a **50/50 class-balanced** subset of the test set, so a score could be read as a probability. The release note told customers they "need to take action" if they used "specific thresholds" — for holding comments for review or auto-approving them. The threshold, in other words, was never the API's. It was the customer's.

## Who Built It, And Why Them

Jigsaw — Google Ideas until its rename in **February 2016** — a Google-then-Alphabet unit founded in 2010 under Jared Cohen to work on technology and geopolitics.

Why them and not a vendor: Jigsaw did not need the API to earn money. It was given away, and Jigsaw was later reported as "not generating revenue" when about a third to a half of its staff were cut in January 2023. A free, general score could be adopted by newspapers that would never have paid for moderation. A commercial vendor would have sold a tuned decision per customer. Jigsaw shipped a raw, uniform score and let the customer decide — which is the only shape a free, one-size API can take.

## What It Cost

**The operating point was exported.** Calibration on a 50/50 set means scores are inflated wherever the harm is rare, as the release note itself warns; and the number that trades missed abuse against removed speech is chosen by each customer, usually without a method.

**The model card forbids the obvious use.** It lists "fully automated moderation" as a use to avoid — the very use a single score with a threshold invites.

**Each version is graded on its own exam.** The model card states that each new model has a different training and testing set, "so overall results are not directly comparable across models". Bias is measured on synthetic identity-term templates, which the card concedes are "not comprehensive".

In January 2026 Jigsaw said the API would sunset after 2026.

## What You Still Touch

The vault's own industry note says the typical product "ships a single confidence score and leaves the choice to a customer". That division of labour — the vendor owns the number, the buyer owns the consequence — was Perspective's by necessity, and became the category's by default.

- [[problems/trust-safety-tooling-vendors/low-impact-1|🟡 The Threshold Is Where the Policy Actually Lives]] — the direct descendant
- [[problems/trust-safety-tooling-vendors/high-impact|🔴 Every Vendor Reports Accuracy on Its Own Exam]]
- [[niches/trust-safety-tooling-vendors/operating-point/profile|Operating Point & Threshold Setting]]
- [[niches/trust-safety-tooling-vendors/performance-evaluation/profile|Performance Evaluation & Benchmarking]]

**Sources:** conversationai/perspectiveapi GitHub repository, read via the GitHub API: `model-cards/English/toxicity.md` (definition, training data, architecture, uses to avoid, evaluation caveats, TOXICITY@1 February 2017 and TOXICITY@6 August 2018) and `releases/20170613-score_normalization_v1.md` (13 June 2017 normalisation, isotonic regression, 50/50 calibration set, threshold warning); Wikipedia, *Perspective API* (23 February 2017 launch, partners, NYT 80% expansion, sunset notice); Wikipedia, *Jigsaw (company)* (Google Ideas 2010, rename February 2016, January 2023 layoffs); arXiv 1610.08914, *Ex Machina*; this vault's `industries/trust-safety-tooling-vendors.md` (quoted as vault material, not independent corroboration). WebSearch was unavailable this session (budget exhausted); research was by WebFetch on known URLs. ⚠️ **Not established:** the names of the Jigsaw and Google Counter Abuse Technology engineers who built the API; whether Jigsaw ever published recommended threshold values. Sap et al., *The Risk of Racial Bias in Hate Speech Detection* (ACL 2019), was checked — its abstract reports dialect bias in hate-speech models but does not name Perspective, so no claim about Perspective's bias is made from it.
