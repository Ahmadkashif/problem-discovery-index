# Fix: The Bridge That Breaks on the Hard Cases

**Niche:** Low-Resource Language Moderation
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Fix (Pain Point)
**One-liner:** Where there are no in-language reviewers, content is machine-translated and reviewed by someone who does not speak the language — and translation loses precisely the context that determines whether something is a threat.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #compliance
**Contested on:** Whether moderation capability is allocated to where the offline consequences of failure are most severe, or to where the training data and the advertising revenue already are.

## The Problem

When a platform has volume in a language and no reviewers who speak it, the standard response is machine translation. The item is translated, a reviewer in a different market reads the translation, applies the policy and decides.

For ordinary content this works acceptably. For the content that matters it fails in a specific and predictable way: translation preserves denotation and destroys everything else. Coded terminology, which exists precisely to evade detection, translates to its literal surface meaning and becomes invisible. Irony and sarcasm flatten. A reference to a local political figure, an ethnic slur that is a common word in another register, a phrase whose threat value comes entirely from a recent local event — all of it arrives at the reviewer as neutral text. Transliterated and code-switched material, which is how much of the online speech in these markets is actually written, translates badly or not at all.

So the bridge holds for the easy cases and collapses for the hard ones. The reviewer applies the policy correctly to a rendering that has removed the evidence, and a decision is recorded with the same confidence as any other. Nothing in the system marks that decision as having been made through a lossy channel.

## Why It's Still Broken

**Translation is the only option that scales instantly.** Recruiting and training in-language reviewers takes a year. Translation is available the moment a language has volume, and an operation facing a queue it cannot read has to do something.

**The failure is invisible in the metrics.** A translation-mediated decision that is wrong looks exactly like one that is right. The auditor is usually reading the same translation, so audit agreement is high and quality reporting shows no problem — the measurement inherits the same blindness as the decision.

**Nobody marks the channel.** Decisions do not record whether they were made on original or translated content, so no operation can report what fraction of its output in a given market went through a lossy path, let alone compare error rates between the two.

**Translation quality is worst exactly where it is most needed.** The languages with the fewest reviewers are the languages with the weakest translation, and the registers most used in crisis — coded, transliterated, code-switched — are the ones translation handles worst. The failure modes compound rather than offsetting.

**Local context cannot be translated at all.** Much of what determines whether a phrase is a threat is knowledge of what happened in that town last month. No translation system carries that, and no policy document supplies it.

**It is a defensible-looking answer.** "We provide coverage in that language" is true in the sense that decisions are being made, and the distinction between reviewed and translated-then-reviewed is not one that appears in any public reporting.

## What a Fix Looks Like

**Mark the channel on every decision.** Record whether the reviewer read original or translated content, and report the split by language and category. This costs nothing, requires no new capability, and is the precondition for everyone understanding the actual coverage picture — including the platform, which frequently does not know.

**Audit the bridge directly.** Take a sample of translation-mediated decisions and re-review them with in-language speakers. The disagreement rate is the error the bridge introduces, it is measurable today at modest cost, and no operation currently produces it. Publishing it per language is what would move resources.

**Route by translatability, not by availability.** Categories where meaning survives translation reasonably — graphic imagery, many spam and commerce violations — can go through the bridge with acceptable loss. Categories that turn on linguistic and cultural context — incitement, harassment, coordinated inauthentic behaviour, coded hate speech — should not, and should queue for an in-language reviewer even at the cost of latency. This triage is straightforward and almost nobody does it.

**Give the reviewer the original and the uncertainty.** Show the source text alongside the translation, flag low-confidence segments, surface detected coded terms with local annotations, and attach a short local context brief maintained by regional specialists. A reviewer told that a phrase is uncertain and may be coded behaves very differently from one handed fluent neutral text.

**Let reviewers refuse the item.** A one-click "I cannot judge this through translation" that routes to an in-language queue or to a regional specialist, with no accuracy penalty. Reviewers can usually tell when the translation has left them without enough to go on, and they currently have no option but to decide anyway.

**Treat the bridge as temporary and say so.** Translation coverage should be reported as an interim measure with a stated plan and timeline for in-language capability, not presented as coverage. The honest framing is what creates the pressure to replace it.

## Who Feels the Pain

The people in those markets, who receive moderation that works on ordinary content and fails on incitement — the inverse of what they need, in the situations where the offline consequences are most severe.

The reviewer, asked to make consequential judgements on material they cannot properly read, and graded on the result.

The platform, carrying real risk in markets where its capability is substantially weaker than its own reporting suggests, because the reporting does not distinguish the channel.

And local civil society organisations, who flag coded incitement repeatedly, are told the content does not violate policy, and have no way to explain that the decision was made on a translation that removed the thing they were pointing at.

## Impact If Fixed

Marking the channel and auditing the bridge are cheap and would immediately reveal the size of a problem the industry currently cannot see. Most of the value here comes from measurement, because the absence of measurement is what allows translation coverage to be reported as coverage.

Routing by translatability directs scarce in-language capacity at the cases where it changes the outcome, which is the highest-return allocation available with existing headcount.

And letting reviewers decline an untranslatable item converts a silent, confident error into an explicit gap — which is worse-looking and far better, because a gap can be staffed and a silent error cannot be found.
