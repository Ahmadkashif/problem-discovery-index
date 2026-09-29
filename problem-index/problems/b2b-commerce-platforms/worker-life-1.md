# Inside Sales Rep Quoting from a Spreadsheet

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Worker Life Changing
**One-liner:** Inside sales reps assemble quotes by hand from an ERP, a spreadsheet and their memory of what this customer usually pays, for orders the storefront was supposed to handle.
**Tags:** #gradient-boosting #confidence-intervals #large-language-models #bert #evaluation-metrics #optimization-fundamentals #workflow-orchestration #worker-facing

## The Problem
A customer emails a list of parts and asks for a quote. The inside sales rep looks up each item, checks stock, checks the customer's contract pricing, decides whether to apply a discount, checks lead times on anything not in stock, finds substitutes for discontinued items, and assembles a document.

For a list of forty line items this takes an hour or more, and much of it is lookup rather than judgement. The judgement — what discount to apply, whether to propose an alternative, how hard to compete on a specific line — is a small part of the time and the whole of the value.

The pricing decision is made largely on memory and instinct. The rep knows this customer pushes on price, that this competitor is aggressive on this brand, that this item carries decent margin. What they do not have is any evidence: whether the quote will be accepted at this price, what similar customers paid for similar items, or what happened the last several times they quoted this way.

Quote outcomes are frequently not tracked at all, so nobody knows the win rate by product, customer or discount level.

## Why It Matters to the Worker
Inside sales is where distribution relationships are actually held, and the role is dominated by clerical assembly. The relationship work — understanding a customer's business, proposing better solutions — happens in whatever time the quoting leaves.

Quoting under time pressure produces errors that are visible and consequential: a wrong price honoured, a missed lead time, a substitute that does not fit. The rep is accountable for accuracy across dozens of lines assembled quickly.

The absence of feedback is the professional frustration. A rep who has produced thousands of quotes has no way to know whether their discounting instincts are good, because outcomes are not tracked against decisions. They may be leaving margin on the table or losing business on price and cannot tell which.

And the storefront's failure lands on them. Every customer who cannot find a part, cannot trust the price online, or cannot get their procurement system connected becomes an inside sales contact, which means platform shortcomings arrive as workload.

## What a Solution Looks Like
Assemble the quote automatically. Parts identified from a customer's list including their own part numbers, priced against their contract, checked for stock and lead time, with substitutes proposed for unavailable items — this is lookup and it is the bulk of the hour.

Win probability at a given price. The distributor holds quote and order history and can estimate acceptance probability by customer, product and discount level, which turns the pricing decision from instinct into a supported judgement and is the single most useful thing a rep could be given.

Substitute recommendation from specifications rather than from memory, which depends on the catalogue attributes being structured and is the clearest downstream benefit of fixing them.

Outcome tracking as a default. Recording quote outcomes and connecting them to the decisions made is a small change that makes every subsequent improvement measurable and is absent at a remarkable number of distributors.

Margin visibility at line level as the rep quotes, so the discount decision is made against the number that matters.

## Impact If Solved
Inside sales capacity determines how much business a distributor can quote, and most of it is spent on assembly rather than on judgement. Automating the lookup and supplying win probability converts an hour of clerical work into a supported decision, and outcome tracking is the precondition for the pricing function ever improving.
