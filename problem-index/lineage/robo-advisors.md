# Lineage: Robo-Advisors

**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Rule 3a-4 under the Investment Company Act (17 CFR 270.3a-4, adopted 1997), the safe harbour that stops a managed-account programme counting as a mutual fund, and the client profile it requires: financial situation and investment objectives taken at account opening, re-asked at least annually
**Builder:** Securities and Exchange Commission
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Run the same model portfolio for a hundred thousand clients and a regulator may see a mutual fund.

The Investment Company Act of 1940 regulates pooled vehicles strictly: registration, a board, custody rules, a prospectus. A discretionary advisory programme that puts many small accounts into the same handful of allocations, and trades them together, starts to look like one. Every client's money moves on one decision and ends up in one set of positions. Before 1997 there was no clear line between that kind of programme and an unregistered investment company. The SEC's 1995 release on the *Status of Investment Advisory Programs under the Investment Company Act of 1940* (Release No. 21260, 27 July 1995) set out when such a programme might be treated as one.

For the sponsors of these programmes, the risk of being reclassified hung over the whole business.

## What Got Built

A safe harbour, published 31 March 1997 and codified at 17 CFR 270.3a-4. A programme is not an investment company if every account is treated as individual. The conditions list what "individual" means:

- each account is managed "on the basis of the client's financial situation and investment objectives";
- that information is obtained **at account opening**;
- the sponsor contacts the client **at least annually** to ask whether anything has changed, and sends a notice **at least quarterly** reminding the client to report changes;
- the client can impose reasonable restrictions, such as naming securities not to buy;
- the client keeps the rights of direct ownership: to withdraw, vote, receive confirmations and sue issuers.

**The client profile is how the programme proves it is not a fund.** The individual inputs are what make a hundred thousand identical portfolios legally a hundred thousand separate accounts.

## Who Built It, And Why Them

The SEC, because only the regulator that could reclassify a programme could also promise not to. The Commission was not trying to design investment advice. It was deciding where the Investment Company Act stops. So it named the minimum signs of individual treatment it could check at examination. Each can be shown with a document: the intake form, the annual letter, the quarterly notice, the restriction log.

Twenty years later the SEC's staff found that robo-advisers had built their onboarding on exactly this minimum. IM Guidance Update No. 2017-02 (February 2017) directs robo-advisers to Rule 3a-4. It then observes that many "rely solely on questionnaires", that some questionnaires ask only age, income and goals, and that many give the client no chance to add context and no human to ask a follow-up or resolve inconsistent answers. It asks whether the questions "elicit sufficient information". It does not require more than the rule does.

## What It Cost

**The rule required that the profile be collected, not that it be correct.** The questionnaire at opening and the annual "has anything changed?" were designed as evidence of individual treatment, and that is all they have been asked to do. Nothing requires the programme to test the stated risk tolerance against what the client actually does.

A software platform can therefore satisfy the rule with a six-question form and an annual email, while holding years of evidence it never compares with the form: every login during a drawdown, every panicked allocation change, every withdrawal at the bottom. The data to validate the profile is collected by default. The rule never asks for it.

## What You Still Touch

The risk questionnaire you fill in on sign-up, and the yearly "please confirm your information is up to date" email, are Rule 3a-4's paragraph (a)(2), turned into onboarding screens.

- [[problems/robo-advisors/high-impact|🔴 Risk Tolerance Assessed Once and Never Validated]] — the profile the rule demands, never checked against behaviour
- [[problems/robo-advisors/worker-life-2|🟢 The Supervision Analyst Reading Everything]]
- [[niches/robo-advisors/risk-tolerance-measurement/profile|Risk Tolerance Measurement]]
- [[niches/robo-advisors/client-understanding/profile|Client Understanding]]
- [[niches/robo-advisors/drawdown-intervention/profile|Drawdown Intervention]]

**Sources:** 17 CFR § 270.3a-4 via Cornell LII (preliminary note; conditions (a)(1)–(a)(5), quoted; source note 62 FR 15109, 31 March 1997); SEC Division of Investment Management, *IM Guidance Update No. 2017-02: Robo-Advisers* (February 2017), read from the SEC PDF: the Rule 3a-4 reference and footnote 9, citing Investment Company Act Release No. 21260 (27 July 1995); the questionnaire observations quoted above; footnote 22's citation of the Rule 3a-4 adopting release on suitability. ⚠️ **Not established:** the adopting release's number and the SEC staff who drafted it. I have only the Federal Register page from the CFR source note. Also not established: whether the 1995–97 rulemaking was driven by specific wrap-fee sponsors. The usual account says brokerage wrap programmes were the target, but I did not confirm this from the releases, so the note says "managed-account programme" throughout. The claim that robo-advisers' onboarding follows the rule's minimum is the SEC staff's observation in the 2017 update, not a survey of platforms. The session's web-search budget was exhausted, and no founding dates for individual robo-advisers are given for that reason.
