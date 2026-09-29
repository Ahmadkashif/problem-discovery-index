# Lineage: API Infrastructure Providers

**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Swagger specification — a JSON description of an HTTP API's resources, operations, parameters and models, from which documentation and client libraries are generated; renamed the OpenAPI Specification in 2016
**Builder:** Wordnik
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An HTTP API has no contract of its own.

SOAP had one: a WSDL file, verbose but machine-readable, so tools could generate a client from it. The JSON-over-HTTP style that replaced SOAP threw that file away along with the verbosity. What was left was a hand-written web page listing endpoints, and a client library that somebody at the provider wrote by hand for each language they cared to support.

**So every change to the API cost three edits** — the server, the documentation page and every client library — made by different people at different times. Nothing forced them to agree. The provider paid for each language it supported, and the consumer paid, in debugging time, for every place the page and the server disagreed.

## What Got Built

A single JSON document describing the API — its resources, the operations on each, their parameters, and the models they return — published by the server itself at a known URL.

Two things were generated from it. **Swagger UI** rendered the document as a live page where a developer could fill in parameters and fire a real request from the browser. **Swagger Codegen** read the same document and emitted client libraries.

Version 1.0 of the specification was released on **10 August 2011**, and the project was open-sourced in **September 2011**. The name was a jab at the other contender, Sun's WADL: *"Why WADL when you can Swagger?"* Swagger 2.0 followed on 8 September 2014.

## Who Built It, And Why Them

Wordnik, an online dictionary — and the reason is that Wordnik's product *was* its API.

Tony Tam, Wordnik's technical co-founder, started the work in early 2010. Wordnik offered its dictionary data to outside developers through that API, so its documentation and SDKs were not a support cost bolted onto a product; they were the storefront. By Wikipedia's account of the project, "the need for automation of API documentation and client SDK generation became a major source of frustration" during Wordnik's development. A company that needed third parties to integrate quickly, across several client languages, felt the three-edits problem more sharply than an enterprise exposing an API as a side door.

Tam designed the JSON format; Ayush Gupta contributed the UI concepts, Ramesh Pidikiti led code generation, and Zeke Sikelianos coined the name.

**Then the inheritors.** SmartBear Software bought the specification in March 2015 from Reverb Technologies, Wordnik's parent. In November 2015 SmartBear announced the OpenAPI Initiative under the Linux Foundation, with Google, IBM and Microsoft among the founding members, and on 1 January 2016 the specification was renamed the OpenAPI Specification. The key here is the originator, not the later standards body.

## What It Cost

**The specification describes what the API is meant to do. Nothing makes it true.**

Swagger removed the drift between documentation and client libraries by generating both from one file — but it moved all the risk onto the gap between that file and the running server. Whether the document is annotated from code or written first and implemented afterwards, it records intent. A field declared required that the server treats as optional, an enum value added in a bug fix, an undocumented status code: none of it shows up, because no part of the toolchain watches real traffic.

The second cost is scope. The format describes one API in isolation. It says nothing about who calls that API, which fields they read, or what breaks if an endpoint is removed — so the provider can publish a perfect contract and still not know its own blast radius.

## What You Still Touch

Every `/docs` page with a "Try it out" button descends from Wordnik's dictionary API. The problems this industry still carries are the two things the format left out: behaviour, and dependants.

- [[problems/api-infrastructure-providers/low-impact-1|🟡 Documentation Drift from Behaviour]] — the gap between the specification and the running server
- [[problems/api-infrastructure-providers/high-impact|🔴 Knowing What Depends on an API]] — the consumer map the format never described
- [[problems/api-infrastructure-providers/worker-life-2|🟢 API Product Manager Deprecating Blind]]
- [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/profile|Traffic-Derived Contract Intelligence]]
- [[niches/api-infrastructure-providers/breaking-change-and-deprecation/profile|Breaking Change & Deprecation]]

**Sources:** Wikipedia, *Swagger (software)* (Tam, Wordnik, early-2010 start, contributor roles, September 2011 open-sourcing, "Why WADL when you can Swagger?"); Wikipedia, *OpenAPI Specification* (release dates for 1.0, 10 August 2011, and 2.0, 8 September 2014; SmartBear purchase from Reverb Technologies, March 2015; OpenAPI Initiative, November 2015; rename, 1 January 2016; 3.0.0, July 2017); OpenAPI Initiative post of 7 March 2016 linking Tony Tam's own recorded account (listed, not watched). ⚠️ **Not established:** Wordnik's revenue model and the size of its engineering team at the time — the "API as storefront" reading is inferred from Wordnik being an API-first dictionary service, not from a primary source stating it. A secondary site dates 1.0 to "August 2011" without the day; the day comes from Wikipedia's version table only. WADL's own submission date was not checked.
