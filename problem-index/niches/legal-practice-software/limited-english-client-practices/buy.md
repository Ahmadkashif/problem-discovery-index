# Machine Translation Adapted to Legal Client Communication

**Niche:** [[niches/legal-practice-software/limited-english-client-practices/profile|Limited-English-Client Practices]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine translation is a solved commodity that firm staff already use by copy-paste, and no legal platform has integrated it, which means it is used constantly, unreviewed, unlogged and at exactly the quality the free tier provides.
**Tags:** #seq2seq #transformers #attention-mechanisms #evaluation-metrics #confidence-intervals #compliance #automation #quick-win
**Contested on:** Every serious competitor selling to firms whose clients do not speak English is fighting to make the entire client-facing path — intake, documents, status, signature, court communication — work in the client's language without a bilingual staff member in the middle, and whoever covers that path end to end takes the account.

## The Problem
Staff at these firms translate all day using whatever is free and open in another browser tab — client emails, document requests, sometimes passages of legal documents. The translations are frequently fine and occasionally wrong in ways that matter, nobody reviews them, no record is kept of what was produced, and confidential client material is being pasted into services whose terms nobody in the firm has read. This is the actual state of practice in a large segment of the profession, and it is a confidentiality question before it is a quality one.

## What Already Exists
Neural machine translation is mature and inexpensive across all the languages this segment needs, with strong quality in the high-resource pairs that cover most of the population. Terminology management, translation memory and quality estimation are established components from the localisation industry. Certified human translation is purchasable for the documents that require it. Every piece is available; none is integrated into legal practice software.

## The Customization Gap
The adaptation is about governance, terminology and knowing when not to rely on it. It requires: (1) translation inside the platform under the firm's confidentiality posture, so client material stops leaving through a browser tab — which is most of the value on its own; (2) a legal terminology layer per language pair, since the terms that matter most are precisely the ones general engines handle inconsistently, and a firm's own reviewed translations should accumulate as memory; (3) quality estimation that routes low-confidence output to human review rather than sending it, with the threshold set by document class — a status update and a release are not the same risk; (4) hard policy gates that require reviewed human translation for binding documents, enforced by the product rather than left to a busy paralegal; and (5) a log of every translation produced and sent, which is what converts an invisible practice into a reviewable one.

## Target Customer
Firms with substantial limited-English-proficient caseloads, and practice management vendors serving them who currently ship an English-only client portal.

## Impact If Solved
The confidentiality correction alone justifies the work, because the current state is untenable and nearly universal. Beyond that, integrated translation with terminology memory removes the copy-paste cycle from staff workflow, and the reviewed-translation gate on binding documents closes the firm's largest quiet exposure in this segment.
