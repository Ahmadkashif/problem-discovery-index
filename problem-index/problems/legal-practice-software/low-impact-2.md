# Practice-Area Document Assembly

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document automation has been a solved technology for twenty years and remains unadopted at small firms, because the templates that matter are practice-area and county specific and somebody has to build them.
**Tags:** #large-language-models #transformers #bert #word-embeddings #transfer-learning #workflow-orchestration #quick-win

## The Problem
Most of what a small firm produces is a variation on something it has produced before. A retainer agreement, a discovery request, a motion to compel, a settlement demand, a will, a lease, a form pleading for a specific county. The variable content is small and structured: parties, dates, amounts, jurisdiction, the specific facts.

Document assembly automates exactly this, and it works. Adoption at small firms remains low. The reason is not the technology but the setup: somebody must convert the firm's existing documents into templates with defined variables and conditional logic, and that somebody is a lawyer whose time is worth more elsewhere. Firms start, get through four templates, and stop.

## What Already Exists
HotDocs and its descendants are mature and powerful. Every practice management platform ships mail-merge from matter fields. Practice-area template libraries are sold by bar associations, publishers and specialist vendors. LLM-based drafting now produces credible first drafts from a prompt, which has changed the landscape considerably. Clause libraries and contract lifecycle tools serve the transactional side well.

## The Customisation Gap
Generic template libraries are the wrong altitude. A family law practitioner does not need a generic separation agreement; they need the one that satisfies their county's standing order, uses the local court's caption format, and reflects how the judges there actually treat a particular provision. That specificity is the value, and it is local knowledge held by practitioners, not publishers.

The unexploited asset is the firm's own document history. A firm has hundreds of past examples of each document it produces. Inferring the template from that corpus — identifying what is boilerplate, what varies, and what varies together — turns template creation from an authoring project into a review of something already drafted. Extending that across the platform's whole customer base, per practice area and per jurisdiction, produces the local template library that no publisher can economically build.

Generative drafting alone does not close this. A model that writes a plausible motion is a liability in a context where a specific court expects a specific form; the requirement is a template grounded in what has actually been filed and accepted, with the firm's own language preserved.

## Impact If Solved
Drafting is where small-firm lawyers spend time that is hard to bill in full and impossible to bill at their rate. Removing the setup barrier is the difference between automation being a project a firm never finishes and a capability that works from the first week.
