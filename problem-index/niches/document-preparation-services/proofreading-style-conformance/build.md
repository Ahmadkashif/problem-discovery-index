# House Style as Executable Checks

**Niche:** [[niches/document-preparation-services/proofreading-style-conformance/profile|Proofreading & Style-Guide Conformance]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every organisation's style guide is a Word file of rules that a proofreader applies from memory, though most of the rules could be tested mechanically on every page.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to bring a document into line with a named style guide while changing nothing the guide doesn't require, and whoever returns a change log the client can accept without rereading the document takes the account.

## The Problem
A law firm, a university communications office or a pharmaceutical writer's client has a style guide: serial commas or not, how to write numbers and dates, defined terms, capitalisation of titles, preferred spellings, banned phrases. A proofreader applies it across a 100-page document. Some rules are missed, some are applied inconsistently, and new staff take months to learn the house quirks.

## Why Nobody Has Built This
Style guides are written for people, in prose with exceptions. Grammar tools ship their own rules and resist local ones, and editing firms are too small to build tooling.

## What to Build
A converter that reads a style guide and turns each rule into a test: deterministic where possible (spellings, number formats, capitalisation lists) and language-model-judged where it isn't ("avoid passive voice in summaries"), each with examples from the guide. Tests run on the client's document and propose changes tagged with the rule that requires them, separate from the editor's discretionary suggestions. Rules the editor overrides become documented exceptions.

## Target Customer
Editing and proofreading firms serving corporate, legal and institutional clients; in-house publications teams.

## Impact If Built
Style rules applied completely and consistently, new editors productive on a client's style in days, and change logs the client can trust.
