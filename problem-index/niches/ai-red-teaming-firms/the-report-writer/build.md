# The Best Researchers Writing Documents

**Niche:** [[niches/ai-red-teaming-firms/the-report-writer/profile|The Report Writer]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most experienced researchers spend the end of every engagement writing documents, translating what they found into something an engineering team can act on and a compliance team can file.
**Tags:** #large-language-models #worker-facing #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to get a finding from a researcher's head into two audiences' hands without the researcher writing documents for a week — and whoever does that takes the account, because that week is the industry's most expensive time spent on its least skilled task.

## The Problem
Week four of a four-week engagement. The researcher stops researching and starts writing. They reconstruct each finding from notes taken three weeks earlier, write a description, recreate a reproduction, assign a severity, draft a recommendation, and map it to the client's regulatory framework. Five days. It is the least skilled work of the engagement performed by the most expensive person, at the point where their accumulated context would make further research most productive, and the resulting document is a reconstruction of what they found rather than a record of it.

## Why Nobody Has Built This
Reports are the deliverable and are treated as the researcher's responsibility. Capturing findings during the work is administrative overhead that interrupts research flow, so it does not happen and the reconstruction becomes necessary. Firms are small and the tooling is a template. And the cost sits inside a fixed-price engagement where nobody outside sees it.

## What to Build
Capture during, generate after. Structure finding capture into the research tooling — the probe, the response, the classification, the observed rate, the affected component and a one-line note — so a finding is recorded at the moment it is found with a few seconds of effort, which eliminates the reconstruction and is the precondition for everything else. Generate both documents from the structured findings, since the engineering write-up and the compliance write-up are two renderings of the same facts and generating them is now straightforward. Leave the researcher reviewing and adding judgement rather than composing, which is where their value is and is a fraction of the current effort. Attach the reproduction automatically from the recorded probe, which is both better evidence and zero effort. Map findings to regulatory obligations from a maintained mapping rather than per client, since the mapping is largely sector-general and is redone every engagement. Draft the recommendation from the finding's class and the client's architecture, for the researcher to correct. Produce the client's tracker entries directly rather than as a document they retype. And measure the write-up share of every engagement, since it is a large fraction of the cost of delivery and is currently unmeasured.

## Target Customer
Assessment delivery organisations, the researchers writing reports, and the clients receiving documents they then have to translate again.

## Impact If Built
The least skilled work of an engagement is done by the most expensive person at the moment their context is most valuable. Structured capture during the research eliminates the reconstruction, and generating both documents from the same records leaves the researcher adding judgement rather than composing.
