# Lineage: UX Research Agencies

**Industry:** [[industries/ux-research-agencies|UX Research Agencies]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the "test with five users" rule: Nielsen and Landauer's problem-discovery curve N(1−(1−L)^n) with L = 31%, published as the 18 March 2000 Alertbox "Why You Only Need to Test with 5 Users"
**Builder:** Nielsen Norman Group
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Usability testing was expensive per participant, and nobody knew how many participants were enough.

Each session meant recruiting a person and running them through tasks while someone watched and took notes, then analysing the result. A lab study with dozens of participants could cost more than the design change it was meant to inform. Most teams therefore did not test at all.

The question had a sharp commercial edge by the late 1990s. Websites were being redesigned on cycles of weeks. A method that took a quarter and a large budget would simply be skipped.

## What Got Built

A number, with a curve behind it.

The curve came first. In April 1993, at INTERCHI in Amsterdam, **Jakob Nielsen and Thomas Landauer** presented "A mathematical model of the finding of usability problems". It fitted data from 11 studies and showed that problem discovery behaves like a Poisson process. The number of problems found after *n* users is N(1−(1−L)<sup>n</sup>), where L is the share of problems a single user reveals.

They were not alone. Robert Virzi at GTE Laboratories had reported in *Human Factors* in 1992 that four or five subjects detected about 80 per cent of problems. MeasuringU's history traces the idea back further, to Alphonse Chapanis in 1981 and to a binomial model by Jim Lewis in 1982.

The *rule* is a separate artefact. On **18 March 2000**, Nielsen's Alertbox column, "Why You Only Need to Test with 5 Users", set L at 31 per cent averaged across many projects. It concluded that five users find about 85 per cent of problems and that observing more is mostly waste. It then turned that into a budget instruction: rather than one study with 15 users, run three studies with five. Quantitative studies, it noted separately, need about 20.

## Who Built It, And Why Them

**Nielsen Norman Group**, founded on 28 August 1998 in Fremont, California, by Jakob Nielsen and Don Norman.

The model's roots are older and institutional. Nielsen did the 1993 work at Bellcore, which he left in 1994 for Sun Microsystems before founding NN/g. But the rule a practitioner quotes is the 2000 column, and it was published by a consultancy selling usability to web companies.

That explains its shape. Nielsen had spent a decade arguing for "discount usability engineering", meaning methods cheap enough that teams would actually use them. A commercial practice needed a defensible, small, fixed participant count it could quote in a proposal and repeat every sprint. The academic results offered a curve with a free parameter. The column fixed the parameter, named the number and attached a spending rule. That is the step from finding to product.

## What It Cost

The rule is a claim about **finding problems**, not about **measuring how common they are** or whether fixing them helps.

It assumes one user population doing the same tasks on the same product. It finds only problems that affect a large share of users. Critics arrived quickly. Spool and Schroeder reported in 2001 that serious problems kept appearing after dozens of users. Laura Faulkner in 2003 found that samples of five ranged from 55 to 99 per cent of problems found, around an 85 per cent average.

The deeper cost is cultural. Five became the default size of a study, and a five-person study cannot support the generalisations a findings deck makes. No study that small can be checked against outcomes either, so the method never had to be.

## What You Still Touch

A research proposal that budgets "5–8 participants per round" is quoting the 2000 column. A findings report that states a conclusion with confidence its sample cannot carry is its side effect.

- [[problems/ux-research-agencies/high-impact|🔴 Nobody Ever Finds Out Whether the Finding Was Right]]: a method built to find, never to be checked
- [[problems/ux-research-agencies/low-impact-1|🟡 Participant Recruitment and Screening Fraud]]: small fixed samples make each participant count
- [[niches/ux-research-agencies/predictive-track-record/profile|Predictive Track Record]]
- [[niches/ux-research-agencies/the-professional-participant/profile|The Professional Participant]]

**Sources:** Nielsen Norman Group, "Why You Only Need to Test with 5 Users" (nngroup.com, dated 18 March 2000; formula, L = 31%, ~85%, three studies of five, 20 users for quantitative work; citation of the 1993 paper as ACM INTERCHI'93, Amsterdam, 24–29 April 1993, pp. 206–213); ACM Digital Library and dblp records for Nielsen & Landauer 1993 (Poisson model across 11 studies); Virzi, R. A. (1992), *Human Factors* 34(4), 457–468 (GTE Laboratories, Waltham MA; 80% with four or five subjects), via SAGE and search-result summaries; MeasuringU, "A Brief History of the Magic Number 5 in Usability Testing" (Chapanis 1981, Lewis 1982, Spool & Schroeder 2001, Woolrych & Cockton 2001, Faulkner 2003 55–99% range), secondary; Wikipedia and nngroup.com on Nielsen Norman Group (founded 28 August 1998, Fremont CA) and on Nielsen's career (Bellcore until 1994, Sun Microsystems 1994–1998, "discount usability engineering"). ⚠️ **Keying note:** the underlying curve has several originators (Chapanis, Lewis at IBM, Virzi at GTE, Nielsen and Landauer at Bellcore). The key is NN/g because the named artefact is the 2000 rule with its fixed parameter and spending instruction. The Chapanis and Lewis dates were read only in MeasuringU's secondary account and are not independently verified. The link between the rule and agency proposal norms is the vault's own observation, not a surveyed finding.
