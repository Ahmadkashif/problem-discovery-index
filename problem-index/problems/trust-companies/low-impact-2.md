# Reading the Trust Instrument at Account Acceptance

**Industry:** [[trust-companies|Trust Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Before taking on a trust, an officer must read a 30-to-100-page instrument and its amendments and code its standards, powers, parties and termination events into the trust accounting system, and the contract-abstraction tools that do this for leases and credit agreements have no schema for dispositive provisions.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #automation #data-integration

## The Problem
A national bank must review a prospective fiduciary account before accepting it (12 CFR 9.6(a)), and every trust company does the same in practice: can we administer this trust, and on what terms? The officer reads the instrument, often a scan of a typed original with handwritten amendments, a restatement and a pour-over will attached. They identify the grantor, trustees, co-trustees, trust protector and any directed investment or distribution adviser; the beneficiaries and remaindermen by class; each distribution standard; powers of appointment; spendthrift, decanting and situs provisions; the governing law; tax character (grantor or non-grantor, GST exemption allocation); and the events that end the trust. Then they translate all of it into system fields — income and principal allocation rules, distribution frequencies, fee codes, tax reporting flags — and an acceptance memo for the committee. A complex instrument takes most of a day (estimate), and an error made here propagates for decades.

## What Already Exists
Contract-abstraction platforms (Kira within Litera, Luminance, Evisort within Workday) extract clauses from commercial agreements, and general large language models summarise any document. Trust accounting platforms provide account setup screens. Law firms supply summaries for the trusts they drafted.

## The Customisation Gap
The commercial tools have no model of a trust. The needed layer is a fiduciary schema: ascertainable versus non-ascertainable standards (which change both the trustee's discretion and the tax result), the difference between mandatory income and discretionary principal, per stirpes and per capita classes, contingent beneficiaries, Crummey withdrawal powers and their lapse dates, protector and directed-trust powers that move liability between parties, and state-specific default rules where the instrument is silent. It needs amendment-chain logic so the operative version of each provision is clear, field-level citations back to the page, and a mapping from the extracted provisions to the specific codes of FIS, SEI or InnoTrust. It also needs acceptance-risk flags — unusual assets, hostile co-trustees, ambiguous standards — written in the form an acceptance committee reviews.

## Impact If Solved
Cutting abstraction and setup from most of a day to ~1–2 hours of review (estimate) speeds onboarding for every new trust, and catching coding errors at acceptance avoids years of misallocated income, wrong K-1s and distributions made under the wrong standard.
