# An Exposure Answer for Every Lost Key

**Niche:** [[niches/locksmiths/master-key-systems-key-control/profile|Master-Key Systems & Key Control]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a sub-master key goes missing, the campus asks which doors it opens and what rekeying costs, and the answer takes a week of digging through charts that may not match what is installed.
**Tags:** #combinatorics-and-counting #graph-theory #optimization-fundamentals #large-language-models #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to hold the authoritative record of who can open which door, and whoever can answer a lost master or a termination with a costed rekey plan the same day takes the account.

## The Problem
In a hierarchical system a lost key exposes every cylinder that accepts its bitting. That is the doors in its branch, and possibly others through accidental cross-keying or a sloppy extension years ago. Without a working model, cautious owners rekey far more than they need to and careless ones rekey nothing. Both are expensive in different ways.

## Why Nobody Has Built This
The data sits on paper and is fragmented across lock shops, factory records and the designing locksmith. Existing software designs new systems; it does not ingest an old one and reason about it. The market looks small per client, so nobody has invested.

## What to Build
An engine that digitises existing bitting charts, pinning records and key-issue logs, with a language model reading handwritten and scanned documents. It reconciles them against field checks. It represents keys and cylinders as a graph and computes, for any key, the exact set of doors it opens, including unintended ones. Given a loss or a change it solves for the cheapest rekey: which cylinders to re-pin or which cores to swap, while preserving the hierarchy and expansion capacity. Exposure answers and rekey plans arrive the same day, with parts and labour.

## Target Customer
Commercial locksmiths who design and maintain large systems, and in-house lock shops at universities, hospitals and government campuses.

## Impact If Built
Rekeys shrink to what the exposure actually requires. That often saves tens of thousands of dollars per incident on a large campus (estimate). The locksmith holding the model becomes the default vendor for every future change.
