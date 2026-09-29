# Lineage: Insurtech Platforms

**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** SERFF — the System for Electronic Rate and Form Filing, the shared electronic channel through which an insurer submits a rate or policy-form filing to each state insurance department
**Builder:** National Association of Insurance Commissioners
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An American insurer does not have one regulator. It has one per state.

The arrangement is old and deliberate. In 1944 the Supreme Court's *South-Eastern Underwriters* decision held that insurance sold across state lines was interstate commerce; Congress answered with the McCarran–Ferguson Act of March 9 1945, which left the business of insurance to state law. So every rate change and every new policy form a carrier wants to use must be filed with each state where it will be sold, reviewed by that state's department, and approved or at least accepted before use.

For a carrier writing commercial lines in forty states, one product change meant forty filings — each a bundle of rate pages, supporting actuarial exhibits and policy forms, assembled to a state's own requirements, sent to a state examiner and answered by letter. **The cost was not the review. It was the envelope:** assembling, tracking and answering the same change forty ways, on paper.

## What Got Built

SERFF, a single system the carrier files into and each state reviews from.

Instead of a separate paper packet per state, the insurer prepares its filing electronically and routes it to the states it chooses. Examiners open it in the same system, raise objections there, and the insurer answers there. The filing, the questions and the disposition share one record rather than forty correspondence files. The NAIC still describes it as "the most cost-effective and efficient way to submit rates and forms filings to the states and jurisdictions," and a majority of states that publish health insurance rate filings link to them through SERFF.

## Who Built It, And Why Them

The National Association of Insurance Commissioners — the body whose members are the state regulators themselves.

The NAIC dates to 1871, when state commissioners formed the National Insurance Convention after *Paul v. Virginia*; at its first session members adopted a uniform annual statement. Its whole history is building shared instruments for regulators who are legally separate. SERFF is the same move applied to filings.

**That is why it was the NAIC and not a software vendor.** The hard part was never the software. It was persuading fifty independent departments, each with its own statute, to accept filings through one door. A vendor could build the system and still not make a single state use it; the association of the commissioners could. The carriers benefited most, but carriers are the regulated party and could not design the regulator's inbox.

I could not establish when SERFF was conceived, when the first electronic filing was made, or who inside the NAIC led it — see Sources.

## What It Cost

**SERFF standardised the envelope and left the contents alone.** Each state keeps its own requirements, its own examiners and its own view of what a filing must show. A carrier still prepares state-specific exhibits; it just sends them through one channel.

And the contents stayed documents. An approved rate lives in a filing as pages — rate tables, rules, factors, written for an examiner to read. Nothing in the channel turns an approved rate into the configuration a rating engine runs. So every carrier employs people to read its own approved filings and re-key them into Guidewire, Duck Creek or whatever policy system it runs, and a mismatch between what was filed and what is charged is a regulatory exposure rather than a bug.

## What You Still Touch

Any commercial premium quoted in the US was priced from a rate that passed through a state filing, very probably through SERFF, and then was typed into a rating engine by hand.

- [[problems/insurtech-platforms/low-impact-1|🟡 Rate Filing to Configuration Translation]] — the job SERFF's document format left behind
- [[problems/insurtech-platforms/high-impact|🔴 Commercial Submission Ingestion and Triage]] — the same pattern at the other end of the policy: structure the envelope, leave the content as documents
- [[niches/insurtech-platforms/rate-filing-to-configuration/profile|Rate Filing to Configuration]]
- [[niches/insurtech-platforms/carrier-core-systems/profile|Carrier Core Systems]]

**Sources:** Wikipedia, *Affordable Care Act Health Insurance Rate Review Program* ("the majority use System for Electronic Rate and Form Filing (SERFF), which was developed by the National Association of Insurance Commission"); content.naic.org/industry/serff (current description quoted; no history given); Wikipedia, *National Association of Insurance Commissioners* (1871, *Paul v. Virginia*, uniform annual statement); Wikipedia, *McCarran–Ferguson Act* (March 9 1945; *South-Eastern Underwriters*, 1944). Guidewire and Duck Creek as dominant carrier core systems come from this vault's `industries/insurtech-platforms.md` (vault material, not independent corroboration). ⚠️ **Not established:** WebSearch hit its session cap before this note was researched, so checks were WebFetch only. serff.com returned 403, the IRMI glossary returned 403, there is no Wikipedia article on SERFF, and the NAIC page gives no timeline. SERFF's conception date, first filing, pilot states, internal champion and any industry co-sponsors are therefore all left unstated rather than guessed. The description of pre-SERFF paper filing is general, not documented against a primary source.
