# The Assistant Is Recommending a Deprecated Method

**Niche:** [[niches/technical-content-agencies/assistant-readiness/profile|Assistant Readiness]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Developers are being told to use a method the product removed two versions ago, and nobody at the company knows.
**Tags:** #quick-win #evaluation-metrics #compliance #descriptive-statistics #large-language-models #automation #data-integration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make a corpus that produces correct answers when the reader is a machine synthesising from it — and whoever establishes that takes the account.

## The Problem
Assistants answer questions about products using whatever documentation they absorbed, including pages describing versions that no longer exist. Developers receive confident wrong answers, write code against removed methods, and either fail or open a support ticket. The company has no visibility of any of it: the reader never arrived, the assistant is a third party, and nothing in the documentation team's tooling shows what is being said about the product.

## Why It's Still Broken
Nobody asks the assistants — a wrong answer delivered by a third party to a reader who never visits is invisible to every metric the documentation team has. Deprecated content stays published for historical reasons. Version context is implicit in the site structure. And nobody owns the question.

## What a Fix Looks Like
Ask the assistants what they say, and fix the corpus where they are wrong. Run a set of common questions against the major assistants periodically and record the answers, which is the fix and takes an afternoon to set up. Compare the answers against the current product truth, which the team knows and the assistant may not. Trace wrong answers to the pages that produced them, since there is usually a specific source and it is usually fixable. Mark deprecated and version-specific content unambiguously in the text itself rather than only in the site's navigation. Remove or clearly archive documentation for versions no longer supported, which is a decision rather than a project. Publish a canonical current-state statement for the facts most often got wrong. Repeat the check after changes to see whether the answers improved. Track the categories of wrong answer, which shows where the corpus is systematically ambiguous. Tell support what assistants are saying, since they receive the consequences. And treat a wrong synthesised answer as a documentation defect rather than as somebody else's model behaving badly.

## Who Feels the Pain
Developers writing code against methods that do not exist; support teams handling the consequences; product teams whose product is misrepresented; and documentation teams judged on traffic while this happens.

## Impact If Fixed
A wrong answer delivered by a third party to a reader who never visits is invisible to every metric the team has. Running a question set against the assistants is an afternoon that makes it visible.
