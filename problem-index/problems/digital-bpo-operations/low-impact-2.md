# Knowledge Base Accuracy and Agent Assist

**Industry:** [[digital-bpo-operations|Digital BPO Operations]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The agent is answering from a knowledge base the client maintains inconsistently, and the assist tool retrieves confidently from whatever is in it.
**Tags:** #bert #large-language-models #transformers #k-nearest-neighbors #change-point-detection #evaluation-metrics #confidence-intervals #data-integration

## The Problem
An agent handling a contact needs the correct answer quickly. That answer lives in a knowledge base maintained by the client, supplemented by internal process documents, policy updates circulated by email, and the accumulated informal knowledge of the team.

The knowledge base is frequently wrong. Policies change and the article does not; a product update ships and the documentation lags; two articles contradict each other and neither has a date that helps. Agents learn which articles to trust and route around the rest, which means the official source is bypassed and the real knowledge lives in team chat.

Agent assist tooling — retrieval and generative suggestion during the contact — has been deployed widely and quickly, and it inherits this problem entirely. A confident suggestion drawn from a stale article is worse than no suggestion, because the agent is under time pressure and the tool's confidence is indistinguishable between a current article and an obsolete one.

The feedback loop that would fix it does not exist. When an agent finds an article wrong, there is usually no mechanism that reaches the person who maintains it, so the same wrong article misleads the next agent and the one after.

## What Already Exists
Knowledge management platforms are standard and integrated into contact centre desktops. Agent assist from the major contact centre vendors and specialist providers retrieves and suggests in real time, with rapid recent adoption of generative summarisation and response drafting. Search over knowledge bases is usually keyword or basic semantic retrieval. Article feedback buttons exist and are rarely acted upon. Some platforms track article usage.

## The Customisation Gap
Staleness detection is the missing capability and is directly measurable. An article whose suggested answers precede escalations, corrections or repeat contacts is probably wrong, and that signal is present in the contact record. So is contradiction between articles, and divergence between what articles say and what experienced agents actually tell customers — which is derivable from transcripts and is the most direct evidence available that the documented process and the real one have separated.

Confidence calibration is the second gap and matters most now that generative assist is deployed at scale. A suggestion should carry an honest indication of how well-grounded it is, and should decline rather than generate when the knowledge base does not support an answer. An agent under handle-time pressure will use what they are given, so the burden of restraint sits entirely on the tool.

The feedback loop is the third and is almost free. An agent marking a suggestion as wrong should generate a ticket to the article owner with the contact context attached, and the resulting correction should close the loop back to the agents who reported it.

And the informal knowledge should be captured. Team chat contains the current correct answers that the official base lacks, and mining it identifies both the gaps and the answers to fill them.

## Impact If Solved
Agents answer from a source they have learned not to trust, and generative assist has industrialised the confident delivery of whatever that source contains. Staleness detection from contact outcomes turns article maintenance from a neglected backlog into a prioritised queue, calibrated confidence with genuine abstention prevents the assist tool from amplifying errors, and a working feedback loop is the mechanism the whole knowledge function has always lacked.
