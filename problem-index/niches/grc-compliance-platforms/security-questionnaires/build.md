# Build: Answers Bound to Control State

**Niche:** Security Questionnaires
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A questionnaire system where each answer is derived from live control state rather than from a stored sentence, so responses cannot drift away from what is actually configured.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #automation #revenue-impact
**Contested on:** Whether a certificate substitutes for answering three hundred questions, or whether every enterprise buyer sends their own regardless.

## The Problem

A questionnaire arrives with three hundred questions and a deadline set by a deal. Someone works through it, mostly by searching a library of previous answers, adapting wording, and asking colleagues about the twenty that are new.

The library is a collection of sentences someone wrote at some point. It says the organisation enforces multi-factor authentication on all administrative access, encrypts data at rest, retains logs for a year and reviews access quarterly. Each was true when written. Some are still true. Some describe a configuration that changed, a process that lapsed, or a control that has an exception nobody updated the library about.

So an organisation with a compliance platform actively monitoring its control state answers questions about that state from a text file, and the two can disagree without anyone noticing. The questionnaire response is a statement to a customer, sometimes contractually binding, and it is sourced from the least reliable artefact in the building.

The join is obvious and nobody has built it. The platform knows whether multi-factor authentication is enforced, on what proportion of accounts, with what exceptions, right now.

## Why Nobody Has Built This

**Questionnaire tooling and compliance platforms are different products with different buyers.** Answer automation is sold to sales engineering; control monitoring is sold to compliance and security. Joining them crosses an organisational boundary inside the customer and a product boundary between vendors.

**Live answers are uncomfortably honest.** An answer derived from actual state might say coverage is at eighty-seven per cent with four exceptions. The library version says yes. Sales engineering prefers the library version, and that preference is the real obstacle.

**Question matching is genuinely hard.** The same requirement appears in thousands of phrasings across buyers' bespoke questionnaires. Matching a new question to the right underlying control is a semantic problem that lexical search handles badly.

**Not every question maps to a control.** Many ask about process, organisational structure, subprocessors or contractual terms, which no integration observes. The system has to handle a mixed corpus where some answers are derivable and most are not.

**Answers are contractual.** A wrong answer in a questionnaire can be a misrepresentation. That argues for deriving from live state and also makes any automation legally sensitive, which slows adoption.

**The buyer is under deadline.** Anything that makes completing a questionnaire slower loses to copy-paste, regardless of accuracy.

## What to Build

**Derive what can be derived.** For every question that maps to a monitored control, generate the answer from current state, including coverage and exceptions, with the underlying evidence attached. For everything else, retrieve from the library with its age and owner shown.

**Match questions semantically to controls.** Embedding-based matching from a question's text to the underlying control concept, trained on the accumulating corpus of questions across customers, which is exactly the asset a platform serving many organisations would build and none has.

**Flag stale library answers loudly.** Every non-derivable answer shown with when it was last reviewed and by whom, with anything past a threshold blocked from auto-fill until confirmed. Most of the risk in questionnaire responses is old text reused confidently.

**Detect contradiction against control state.** Where a library answer asserts something the platform can observe and disagrees with it, stop and surface it. This is the single highest-value check and it is a straightforward comparison.

**Answer honestly with nuance and make that easy.** A response of "enforced on ninety-four per cent of accounts, with four documented exceptions, reviewed monthly" is more accurate and more credible than a yes, and the system should make producing it easier than producing the yes.

**Learn from what happened.** Track which answers triggered follow-up questions, security review escalation or deal friction. That is the feedback loop that would improve the corpus and nobody collects it.

**Publish a pre-answered trust profile.** A maintained, live, machine-readable profile of the derivable answers, so a buyer can consume it directly. Some buyers will still send their spreadsheet; enough would not to make it worth doing, and it is the only path that actually reduces the volume.

## Target Customer

Growing technology companies selling into enterprise, where questionnaire volume is high, each one is a deal blocker, and the burden falls on a small team already stretched.

The compliance platforms, for whom this is a natural extension — they hold the control state, they hold the customer relationship, and the questionnaire is the customer's most frequent compliance pain.

Questionnaire automation vendors as the alternative adapters, holding the answer corpus and needing the control state join.

## Impact If Built

Answers stop drifting from reality. An organisation whose questionnaire responses are derived from monitored state cannot accidentally misrepresent itself, which is a real contractual risk currently managed by hope.

Contradiction detection alone would catch the most consequential failure — a confident library answer that is no longer true — at essentially no cost.

And a live machine-readable trust profile is the only mechanism that could genuinely reduce questionnaire volume, because it gives the asking side something better than their spreadsheet rather than asking them to accept less.
