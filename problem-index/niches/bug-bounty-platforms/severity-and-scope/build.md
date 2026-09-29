# Build: Rules Knowable Before the Work

**Niche:** Severity & Scope Adjudication
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A machine-checkable scope definition and a cross-programme severity reference, so a researcher can tell what counts and roughly what it is worth before spending a week.
**Tags:** #evaluation-metrics #confidence-intervals #gradient-boosting #bayesian-inference #graph-theory #compliance #automation #worker-facing
**Contested on:** Whether the rules a researcher works under are knowable before the work, or decided afterwards by the party who pays.

## The Problem

The bounty model asks researchers to invest unpaid effort against rules they cannot fully read. A programme policy is a page of prose. It lists domains and exclusions, and it does not anticipate the specific question the researcher has on Tuesday afternoon: this host is not listed but belongs to the company, this endpoint is on a listed domain but is operated by a vendor, this technique is not prohibited but might be, this issue is low impact alone and severe when chained with an out-of-scope one.

The researcher guesses. Sometimes they guess right and are paid. Sometimes they spend a week and are told it was out of scope, or that the severity is two bands below what they expected, and there is no appeal beyond asking the programme to reconsider.

The same ambiguity costs the programme. A large share of triage effort goes to submissions that were never in scope, which a machine could have rejected at submission if scope had been expressed as anything other than paragraphs.

And the platform holds the data that would fix the severity half entirely. Every rating ever assigned, for every finding class, across every programme, sitting in the database, while a researcher has no way to know that this class is typically rated medium and this programme typically rates it low.

## Why Nobody Has Built This

**Ambiguity favours the payer.** A programme that can decide scope and severity after the fact has an option it would be giving up. Nobody has to be acting badly for this to be a real disincentive — it is simply cheaper to keep the discretion.

**Scope is genuinely hard to enumerate.** A company's real attack surface is larger than any list it can write, and much of the value of a bounty programme comes from researchers finding things the company did not know it had. A rigidly enumerated scope would exclude exactly those findings, which is the strongest argument against machine-checkable scope and has to be designed around rather than dismissed.

**Severity comparison exposes programmes.** Publishing cross-programme severity distributions would show which programmes systematically under-rate, which is commercially awkward for a platform whose customers are the programmes.

**The platform's customer is one side of the market.** Programmes pay the fees. Researchers are supply. Any feature that constrains programme discretion in favour of researchers is a cost to the paying side, which is the structural reason this has not been built.

**Severity is partly contextual and legitimately so.** The same flaw genuinely is more severe on a payment system than on a marketing site. A naive cross-programme comparison that ignores context would be wrong in a way programmes would rightly reject.

## What to Build

**A structured scope definition with an explicit unknown-asset path.** Assets, domains, patterns, techniques, conditions, expressed as data rather than prose — plus a first-class category for assets not on the list, with a stated policy: what happens when a researcher finds something the company did not know it owned. This preserves the discovery value while removing the ambiguity, and it is the design choice that makes machine-checkable scope acceptable to programmes.

**A pre-work scope query.** A researcher submits a target and gets an answer before investing: in scope, out of scope, or unknown-and-here-is-the-policy. Binding for a stated window. This is the single feature researchers would value most and it is not technically hard.

**Scope checking at submission.** Automatic rejection of clearly out-of-scope submissions before a human reads them, which removes a large slice of triage cost and pays for the whole build from the programme's side — which is the commercial argument that gets it approved.

**A severity reference from the platform's own corpus.** For a given finding class, on a given asset type, in a given sector: the distribution of severities assigned across all programmes. Not a mandate — a reference. A researcher can see the typical rating, a triager can see whether their assessment is an outlier, and a dispute becomes a conversation about a distribution rather than a contest of assertions.

**Context factors stated explicitly.** Where a programme rates above or below the reference, the reason recorded — payment system, regulated data, compensating control, deprecated asset. This preserves legitimate contextual variation while making arbitrary variation visible.

**Published programme severity history.** Each programme's own distribution of ratings and payouts by class, visible before a researcher commits time. Programmes that rate fairly benefit immediately; the ones that do not are exactly the ones researchers should be avoiding.

**Precedent from disputes.** Resolved disputes recorded as anonymised precedent, so the same argument stops recurring and both sides can point at how it went last time.

## Target Customer

The platforms themselves — HackerOne, Bugcrowd, Intigriti, YesWeHack — where the scope-checking half pays for itself in triage cost and the severity half is a researcher-supply investment.

Programme managers are the direct beneficiaries of scope automation, since out-of-scope submissions are their largest source of wasted triage.

The researcher community is the constituency for the severity half, and researcher supply is the binding constraint on the whole marketplace — which is the argument for building it despite the paying customer being on the other side.

## Impact If Built

Researchers can decide where to spend a week with information instead of a guess, which directly increases participation in a market whose product is participation.

Scope checking at submission removes a large slice of the triage burden mechanically, which is the clearest cost saving available in this industry.

And a severity reference turns the most common dispute in the community from an unresolvable disagreement into a comparison against a distribution — which does not eliminate disagreement and does make it adjudicable.
