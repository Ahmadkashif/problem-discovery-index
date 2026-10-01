# The Diligence Q&A Log

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Data rooms route diligence questions; nobody notices that thirty buyers asked the same question forty ways, or that the answer given to one contradicts the CIM.
**Tags:** #bert #large-language-models #word-embeddings #k-means-clustering #evaluation-metrics #workflow-orchestration #automation

## The Problem
In the second round of a sell-side process, eight to fifteen bidders each submit diligence request lists and ad hoc questions through the data room — often several hundred items per bidder. The banker's associate triages them, routes each to the right person at the client (the CFO, the controller, the head of operations, outside counsel), chases the answers, and posts responses, while making sure that what is told to one bidder is consistent with what was told to the others and with the CIM, the management presentation and the model.

The questions overlap heavily. "Customer concentration by top ten", "revenue by top customers FY22–FY24" and "please provide churn by largest accounts" are one question. The client's CFO, already running the business and the process at once, receives them as three. Answers drift — a figure updated for one bidder is not updated in an earlier answer to another — and the inconsistencies surface in confirmatory diligence or, worse, in a post-close dispute.

## What Already Exists
Datasite, Intralinks, Ansarada and Firmex all have Q&A modules with routing, approval workflow, permissions by bidder group and audit trails. Some have added AI-assisted redaction and document categorisation. Generic LLM tools can draft answers from documents.

## The Customisation Gap
The data room treats each question as a ticket. The process needs questions treated as a set: clustered across bidders so the client answers once, matched to the existing answer library and to documents already in the room, and checked against what the CIM and management presentation stated. The consistency check is the M&A-specific part — an answer that differs from a CIM figure must be flagged before it is posted, because the CIM is the document disclosure schedules and later disputes are argued from.

The second part is bidder signal. The questions a bidder asks reveal how seriously they are diligencing and what they are worried about; a bidder asking about working capital seasonality and customer contracts in week two is behaving differently from one asking for the org chart. That signal belongs in the buyer tracker and currently stays in the Q&A log.

## Impact If Solved
A client's finance team spends weeks of a sale process answering duplicated questions while running the company. Clustering, answer reuse and CIM-consistency checking reduce that load substantially and remove a recurring source of post-signing disputes, while turning the Q&A log into engagement evidence the deal team can actually use.
