# Build: Identifiability, Not Pattern Matching

**Niche:** Personal Data Classification
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Classification that reasons about whether a dataset identifies a person given everything else the holder can access, rather than matching formats that look like personal data.
**Tags:** #bert #large-language-models #word-embeddings #graph-theory #entropy-cross-entropy-kl-divergence #evaluation-metrics #confidence-intervals #compliance
**Contested on:** Whether a system can determine that data is personal, whose it is and what category it falls into.

## The Problem

Classification products look for things that look like personal data. An email address has a recognisable shape. So does a card number, a national identifier, a phone number. Finding these is largely solved.

Identifiability does not work that way. A table of integers, timestamps and category codes contains no recognisable personal data and may identify individuals completely, if one of those integers is a customer identifier that joins to a table holding names. A postcode is not personal data; a postcode with a birth date and a gender very often is, because the combination is unique for a substantial fraction of a population. A device identifier is personal data in one regulatory reading and contested in another.

So pattern matching produces a characteristic error profile: it reliably finds the obvious email column and misses the join key that makes an entire warehouse personal, which is exactly the column a deletion request most needs to follow.

The harder layer sits above it. Which lawful basis covers this processing, and for what purpose, are determinations about the organisation's intentions and contracts, recorded today by a privacy manager typing into a form about systems they have not seen. They are the fields on which the entire legal position rests and they are the least evidenced things in the record.

## Why Nobody Has Built This

**Pattern matching demonstrates well.** A scan that finds ten thousand email addresses produces an impressive result in an evaluation. A system that reasons about identifiability by linkage produces a more useful and less demonstrable one.

**Linkage requires the whole estate.** Determining that a column is a join key to identifying data means understanding relationships across systems, which requires the flow and lineage picture the category does not have. The two sub-niches are genuinely dependent here.

**Identifiability is contested in law.** Whether pseudonymised data is personal depends on who holds the key and what re-identification effort is reasonable, and regulators and courts have not fully settled it. A product asserting a determination is taking a legal position.

**Unstructured content is hard and is where the data is.** Documents, tickets, logs, chat and free-text fields hold enormous amounts of personal data and are covered worst by every product in the category.

**Basis and purpose cannot be observed at all.** They are facts about intent and contract. The most a system can do is check consistency between declared purpose and observed use, which is useful and is not classification.

**Over-classification is punished quietly.** A system that flags everything as personal is useless, so products are tuned conservatively, which means they miss the non-obvious cases — and the non-obvious cases are the ones that matter.

## What to Build

**Reason about linkage, not format.** Identify join keys and quasi-identifiers by analysing relationships across tables and systems: which columns join to identifying data, which combinations are near-unique across the population, and which datasets become identifying when combined with something else the organisation holds. This is where the real classification value is.

**Measure re-identification risk quantitatively.** For a dataset, how uniquely its records distinguish individuals given the organisation's other holdings. The statistical disclosure control literature has done this for decades and it is essentially absent from privacy tooling.

**Cover unstructured content properly.** Documents, tickets, logs and free text, with context-aware extraction rather than pattern matching — a name in a support ticket is personal data and a name in a code comment attributing authorship may not be. This is where language models genuinely help and where the category has barely started.

**Determine whose data it is.** Subject resolution — which records belong to which individual across systems — is what makes a deletion request fulfillable and is rarely attempted. Without it, fulfilment is a search for an email address across systems that may not store it.

**Handle special categories semantically.** A field implying health, belief, union membership or sexuality frequently contains no keyword identifying it as such. Identifying the implication requires understanding what the field means in its system's context.

**Check declared purpose against observed use.** Basis and purpose cannot be derived, and consistency can be tested: data declared as processed for service delivery flowing to an advertising platform is a finding. This is the achievable and useful version of automating the legal layer.

**Report confidence and route the uncertain cases to a human.** The valuable output is a prioritised queue of determinations a lawyer should make, not a confident classification of everything. Designing for the lawyer's attention rather than around it is the correct posture for a domain where judgement is irreducible.

## Target Customer

Privacy engineering and data governance at data-intensive organisations, where the warehouse is large, the join structure is complex, and pattern matching demonstrably misses the important columns.

Privacy counsel as the buyer for the basis and purpose consistency checks, which speak directly to their exposure.

DSPM and data catalogue vendors as adapters, both of whom have the estate view that linkage reasoning requires and neither of whom does the reasoning.

## Impact If Built

Classification would start finding the columns that make datasets personal rather than the ones that look personal, which is where the error currently concentrates and where deletion and access requests fail.

Quantified re-identification risk would let organisations reason about pseudonymisation and anonymisation claims properly, rather than asserting them — an area where the gap between practice and the statistical literature is enormous.

And purpose-versus-use consistency checking is the one part of the legal layer that can be evidenced, and it would catch the most common substantive privacy failure: data collected for one purpose flowing to another.
