# Lineage: AI Agent Platforms

**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** OpenAI function calling — the `functions` and `function_call` parameters on the `/v1/chat/completions` endpoint, where a developer describes each function in JSON Schema and the model answers with a JSON object of arguments instead of prose; announced 13 June 2023, renamed `tools` on 6 November 2023
**Builder:** OpenAI
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A language model returns text. An agent has to do something.

Before mid-2023, the gap between the two was closed with string parsing. A developer wrote a prompt that told the model to answer in a particular shape — a line beginning "Follow up:", a line beginning "So the final answer is:" — and then split the reply on newlines and colons to recover the next step. The first commit of LangChain, on 24 October 2022, shipped exactly this: a `SelfAskWithSearchChain` that scraped the model's output for the next search query.

**The cost was brittleness, and it scaled with the number of tools.** Every tool needed its own output convention, every model upgrade could drift the formatting, and a malformed line did not throw an error — it silently became the wrong action or no action at all. Builders could demo an agent; they could not say how often it would pick the right function.

## What Got Built

On 13 June 2023 OpenAI added two parameters to its chat endpoint. **`functions` took a list of function descriptions — a name, a plain-language description, and the arguments written as JSON Schema. `function_call` let the developer let the model choose, or force a specific function.** The model's reply could then be a structured call rather than a sentence.

The announcement's example: turn "Email Anya to see if she wants to get coffee next Friday" into `send_email(to, body)`.

Two design choices matter. First, **the API never runs the function.** OpenAI's cookbook is explicit that executing the call is the developer's job — the model only proposes. Second, the capability sat in the weights, not in a parser: `gpt-4-0613` and `gpt-3.5-turbo-0613` were described as fine-tuned both to detect when a function should be called and to emit JSON matching the signature.

`functions` became `tools` on 6 November 2023; on 6 August 2024 Structured Outputs promised adherence to the supplied schema.

## Who Built It, And Why Them

OpenAI had already shipped ChatGPT plugins in alpha before June 2023 — its own agent product, calling third-party APIs — and the post says so: "Since the alpha release of ChatGPT plugins, we have learned much about making tools and language models work together safely." A plugin platform is a function-calling system with a storefront; OpenAI needed tool selection to work for itself first.

**The decisive advantage was that the fix required changing the model.** A framework author could only write better parsers around outputs they did not control. Only the owner of the weights could fine-tune the model to emit schema-conforming JSON and then promise the format at the API boundary. That is why the artefact is an API parameter and not a library.

The individual engineers who designed the parameter are not named in the announcement and could not be established here.

## What It Cost

**Agency moved into the model's judgement and out of the developer's code.** The developer lost the explicit if-this-then-call-that path; the model now decides when and which function to call, and that decision is probabilistic.

The same post names the security bill: a proof-of-concept showed that "untrusted data from a tool's output can instruct the model to perform unintended actions." OpenAI's recommended mitigation was a human confirmation step before actions like sending email or making a purchase — an approval gate the whole category still argues about.

## What You Still Touch

Every agent framework and platform now speaks in JSON-Schema tool definitions, and connector standards describe tools in the same shape. What the parameter did not deliver is a number for how often the model calls the right tool with the right arguments on *your* systems — which is the category's central sales problem.

- [[problems/ai-agent-platforms/high-impact|🔴 Predicting Whether a Task Will Succeed]] — the reliability question function calling moved into the model
- [[problems/ai-agent-platforms/low-impact-1|🟡 Tool and Connector Coverage]] — the tool call is standard; the tools are not
- [[problems/ai-agent-platforms/low-impact-2|🟡 Action Authorisation Scoping]] — the confirmation step the launch post recommended
- [[niches/ai-agent-platforms/action-authorisation-policy/profile|Action Authorisation Policy]]
- [[niches/ai-agent-platforms/task-reliability-prediction/profile|Task Reliability Prediction]]

**Sources:** OpenAI, "Function calling and other API updates" (openai.com/index/function-calling-and-other-api-updates, 13 June 2023; direct fetch returned HTTP 403, text read through a reader proxy), for the parameters, models, examples, plugins sentence and the prompt-injection warning; OpenAI API changelog (developers.openai.com/api/docs/changelog) for the 6 November 2023 `tools` deprecation and 6 August 2024 Structured Outputs; openai-cookbook `How_to_call_functions_with_chat_models.ipynb`, first committed 13 June 2023 per the GitHub API, for "the API will not actually execute any function calls"; GitHub tree of LangChain commit `18aeb72` (Harrison Chase, 24 October 2022) for the pre-function-calling parsing pattern. WebSearch was unavailable this session (budget exhausted). ⚠️ **Not established:** the named OpenAI engineers behind the design; the exact date ChatGPT plugins entered alpha (given here only as "before June 2023", which the post implies); any earlier structured tool-call API from another vendor — not searched for, so "first" is not claimed.
