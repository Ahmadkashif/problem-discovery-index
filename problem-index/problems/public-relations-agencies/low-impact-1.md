# Coverage Reports Built From Monitoring Exports

**Industry:** [[public-relations-agencies|Public Relations Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every agency already pays for monitoring that finds the coverage; what it rebuilds by hand each month for each client is the report that says which coverage mattered, whether it carried the messages, and what it did.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #descriptive-statistics #data-integration #automation #worker-facing

## The Problem
At the end of each month an account executive opens the monitoring platform, exports the client's mentions, and spends the better part of a day turning them into a deck. Syndicated wire copies have to be collapsed into one story. Passing mentions and false matches (another company with a similar name) have to be removed. Each remaining article is tagged by outlet tier against the client's priority list, by whether a spokesperson was quoted, by sentiment, and, at the better agencies, by which of the client's three or four key messages it carried. Then reach and share-of-voice charts are pasted in, a few highlight clips are screenshotted, and a narrative is written. Many agencies still add an advertising value equivalent because a client once asked for one.

The report is the agency's main evidence that the retainer is working, and it is assembled by the most junior person, under time pressure, with coding rules that differ between account executives and between months.

## What Already Exists
Meltwater, Cision, Muck Rack and Onclusive all provide monitoring with automated sentiment, reach estimates, share of voice and dashboard exports, and some offer analyst-written measurement reports for an extra fee. General reporting tools such as Looker Studio and PowerPoint templates fill the rest. AMEC's Integrated Evaluation Framework and Barcelona Principles 4.0 (June 2025) describe what good measurement should contain and again reject AVEs and their renamed variants.

## The Customisation Gap
The generic tools count coverage; the agency needs it judged against this client's plan. The missing logic is client-specific: the priority outlet list and its tiers; the message house, with each message defined by examples so that "carried the message" is coded the same way every month; syndication and duplicate rules for the client's markets; spokesperson and product entity lists; competitor sets for share of voice; and the campaign calendar, so coverage is attributed to the announcement that earned it rather than to background noise. On top of that sits a Barcelona-compliant outcome layer (web visits from coverage, branded search lift, AI-answer citations, survey movement) that the client holds and the vendor never sees. Monitoring vendors' sentiment models are trained across all customers and are not tuned to one client's messages, and their analyst services are priced beyond most independent agencies.

## Impact If Solved
A report that is drafted, coded and checked against the client's own message house would cut most of the day an account executive spends per client per month, make month-on-month comparisons honest, and replace AVEs with evidence a chief communications officer can take to a budget meeting.
