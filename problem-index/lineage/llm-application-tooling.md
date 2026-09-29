# Lineage: LLM Application Tooling

**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** LangChain's `Prompt` template and `LLMChain` — a validated, JSON-serialisable prompt object (`template` plus `input_variables`) and a chain that formats it and calls a model, published as the `langchain` Python package on 25 October 2022; the prompt class is today's `PromptTemplate`
**Builder:** Harrison Chase
**Builder in vault:** **ABSENT**
**Verification:** verified — from the initial commit and package index; see Sources for gaps

## The Problem That Came First

In autumn 2022 the way to get a useful answer out of a large language model was to write text around the question — instructions, worked examples, a closing cue. The example prompt in LangChain's first README ends with the words "Let's think step by step."

That made the prompt the most important piece of the application and the least engineered. It lived as a Python f-string inside whatever script called the API. Nothing checked that the variables in the text matched the variables passed in. Nothing let two developers share a prompt except copy-and-paste. The interesting demos — a model that searched before answering, a model whose arithmetic Python ran — were one-off scripts chaining strings by hand.

**The constraint was reuse.** Every new application started from a blank file.

## What Got Built

Harrison Chase's initial commit to LangChain, on 24 October 2022, has a README that describes three aims: "a comprehensive collection of pieces you would ever want to combine," "a flexible interface for combining pieces into a single comprehensive 'chain'," and "a schema for easily saving and sharing those chains."

Two objects carry that design.

**`Prompt`** — "Schema to represent a prompt for an LLM" — held a `template` string, a list of `input_variables` and a `template_format`. A validator formatted the template against dummy inputs at construction time and refused to build a prompt whose variables did not match. Its test fixtures stored prompts as two-key JSON files. The prompt became data.

**`LLMChain`** — "Chain that just formats a prompt and calls an LLM" — took a prompt and a model object and exposed `predict()`. Model wrappers for OpenAI and Cohere sat behind one interface, so the chain did not care which provider answered.

The rest of the commit was reproductions: a `SelfAskWithSearchChain` and an `LLMMathChain`. The package went to PyPI as version 0.0.1 the next day, 25 October 2022, under the summary "Building applications with LLMs through composability."

## Who Built It, And Why Them

One person, working on the side. Wikipedia records that Chase launched LangChain in October 2022 "as an open source project … while working at machine learning startup Robust Intelligence"; the commit author is Chase himself. The company came later — by April 2023 it had incorporated and raised seed money from Benchmark and a larger round led by Sequoia.

**Why an individual and not a model vendor?** The README answers it: the project was "largely inspired by a few projects seen on Twitter for which we thought it would make sense to have more explicit tooling," and the first features were attempts to recreate them. The model vendors sold completions per token and had no reason to ship a provider-neutral abstraction over their competitors. A developer outside every vendor could.

Being early mattered more than being deep. The whole package was under 800 lines of Python; what it claimed was the vocabulary — *prompt template*, *chain* — that the category then built on.

## What It Cost

**The prompt stayed a string.** `Prompt` validated that the blanks matched, not that the output was any good. Serialising a template made it shareable and versionable in files; it did nothing to say what changing one word would do to every downstream answer.

The abstraction also aged fast. `LLMChain` is now marked deprecated since version 0.1.17, with `prompt | llm` named as the alternative — a composition operator replacing the class that gave the library its name.

## What You Still Touch

Every prompt library, prompt registry and prompt-versioning product stores roughly what that first fixture stored: a template, its variables, a format. The regression testing it never offered is what the tooling category now sells.

- [[problems/llm-application-tooling/high-impact|🔴 Prompt Changes Have Unbounded Blast Radius]] — the cost of a prompt that is data but not tested
- [[problems/llm-application-tooling/worker-life-2|🟢 Maintaining a Prompt Library]] — templates that became easy to create and hard to delete
- [[niches/llm-application-tooling/application-frameworks/profile|Application Frameworks]]
- [[niches/llm-application-tooling/prompt-library-hygiene/profile|Prompt Library Hygiene]]
- [[niches/llm-application-tooling/prompt-change-regression/profile|Prompt Change Regression]]

**Sources:** GitHub, `langchain-ai/langchain` initial commit `18aeb72` (author Harrison Chase, 24 October 2022) — README, `langchain/prompt.py`, `langchain/chains/llm.py` and `tests/unit_tests/data/prompts/simple_prompt.json` read directly; PyPI JSON API for `langchain` 0.0.1 (uploaded 25 October 2022); current `langchain_core/prompts/prompt.py` (`PromptTemplate`) and `langchain_classic/chains/llm.py` (`@deprecated(since="0.1.17", alternative="RunnableSequence, e.g., prompt | llm")`); Wikipedia, *LangChain*, for Robust Intelligence and the April 2023 incorporation and funding. WebSearch was unavailable this session (budget exhausted). ⚠️ **Not established:** the exact incorporation date; when `Prompt` was renamed `PromptTemplate`; the date of the 0.1.17 release; no claim is made about how much any particular prompt phrasing changed model output. Line count (788 lines across the `langchain/` `.py` files) measured from the initial commit's tree via the GitHub API.
