# Lineage: Developer Tools Vendors

**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Language Server Protocol — JSON-RPC messages between an editor and a separate per-language server process that supplies completion, go-to-definition and hover documentation; announced 27 June 2016
**Builder:** Microsoft
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Every editor had to learn every language by itself.

Autocomplete, jump-to-definition, inline errors and documentation on hover all require something that understands the language — a parser, a type checker, a model of the project. Each editor exposed its own extension API, so that understanding was rebuilt for each one. The protocol's own overview states the cost plainly: this work "must be repeated for each development tool, as each provides different APIs for implementing the same features."

**N languages times M editors.** A popular language on a popular editor got good support. Everything off that diagonal — a niche language, a new editor — got a syntax highlighter and not much else. A new editor was therefore close to unsellable, because it arrived knowing no languages.

## What Got Built

A contract that split the editor from the language.

Under the Language Server Protocol, the language intelligence runs as its own process, a *language server*, and the editor talks to it with JSON-RPC messages: the document opened, this range changed, what completes here, where is this symbol defined. One server per language can serve any editor that speaks the protocol; one protocol client per editor can use any server. N×M becomes N+M.

Microsoft, Red Hat and Codenvy announced it on **27 June 2016** at DevNation in San Francisco. At launch, JSON, C++ and PowerShell servers worked in VS Code, with C# via OmniSharp and others promised.

## Who Built It, And Why Them

Microsoft — and the reason is that Microsoft had just shipped an editor that knew no languages.

LSP was developed for Visual Studio Code, Microsoft's free cross-platform editor. Unlike Visual Studio, which Microsoft had spent years teaching C#, C++ and its other languages, VS Code had to compete with Sublime Text, Atom and Vim across dozens of languages Microsoft did not own and would never staff. The only way to be good at all of them was to make it cheap for someone else to supply the intelligence.

It had also already paid the cost twice. Erich Gamma, the Microsoft Distinguished Engineer leading the work — earlier a principal of Eclipse — said at the announcement: "Having done a language server integration twice, it became obvious that a common protocol is a win-win for both tool and language providers." The two earlier integrations were TypeScript's language service and OmniSharp for C#, each wired to VS Code over its own ad hoc protocol.

**Why a protocol and not a plug-in API:** a plug-in API would have tied language authors to VS Code; a protocol let them target every editor at once, which is what made the offer attractive enough to accept.

## What It Cost

**The file on disk stopped being the truth.** The overview notes that once a server is in play, "the truth about the contents of the document is no longer on the file system but kept by the tool in memory," and every keystroke must be synchronised to a separate process. That is a second copy of the project's state, held by a process the editor does not control.

It also fixed the unit of understanding at *one language, one open workspace*. A server loads the project into memory to answer questions about it, which is cheap for a small repository and punishing for a very large one, and it has no notion of code spread across repositories. Quality moved, too: a language's editor support is now exactly as good as whoever maintains its server.

## What You Still Touch

When a new editor launches supporting fifty languages on day one, or an obscure language gets working autocomplete in your editor of choice, that is the protocol. When completion stalls on a very large repository, that is also the protocol.

- [[problems/developer-tools-vendors/low-impact-1|🟡 Long-Tail Language and Framework Support]] — what N+M made possible, and whose server quality it now depends on
- [[problems/developer-tools-vendors/low-impact-2|🟡 Large Repository Performance]] — the workspace-in-memory model at scale
- [[niches/developer-tools-vendors/long-tail-language-ecosystems/profile|Long-Tail Language Ecosystems]]
- [[niches/developer-tools-vendors/monorepo-scale-performance/profile|Monorepo & Scale Performance]]

**Sources:** Language Server Protocol overview, microsoft.github.io/language-server-protocol (the "repeated for each development tool" and "truth about the contents" quotations; JSON-RPC); Red Hat press release, "Red Hat, Codenvy and Microsoft Collaborate on Language Server Protocol", San Francisco, 27 June 2016 (DevNation; Gamma quotation; launch servers); Wikipedia, *Language Server Protocol* ("originally developed for Microsoft Visual Studio Code"). ⚠️ **Not established:** that the two earlier integrations Gamma mentions were TypeScript and OmniSharp comes from a secondary summary (ppc.land, *Explaining LSP*), not a Microsoft primary source. Gamma's earlier Eclipse role is from general knowledge, not rechecked this session. The competitive reasoning about Sublime Text and Atom is this note's inference; no Microsoft statement of that rationale was found.
