# Speech and Summarisation Infrastructure Off the Shelf

**Niche:** [[niches/crm-platforms/conversation-intelligence/profile|Conversation Intelligence]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Transcription, speaker diarisation and summarisation have become commodity infrastructure priced in cents, and the conversation intelligence category was built when they were the expensive part.
**Tags:** #transformers #seq2seq #attention-mechanisms #large-language-models #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor in conversation intelligence is fighting to turn a recorded sales call into coaching a manager acts on and deal signal a forecast can use — and whoever converts recordings into acted-upon change takes the account.

## The Problem
The category's original moat was accurate transcription and speaker separation of noisy multi-party business calls, which was genuinely hard and expensive. It is now a commodity API call. That collapse means the defensible position has moved entirely to what is done with the transcript, and a great deal of the product surface — recording, transcribing, storing, searching — is now infrastructure that any competitor can assemble in a fortnight.

## What Already Exists
Speech recognition at production quality is available from every cloud provider and as open weights, with strong performance on conference call audio. Speaker diarisation is standard. Meeting summarisation is built into the conferencing platforms themselves, which is a strategic problem for the category as well as a commodity opportunity. Long-context language models handle a full call trivially. Recording infrastructure and conferencing platform integrations are well documented.

## The Customization Gap
The adaptation is to a sales conversation's specific structure and to the constraints around it. It requires: (1) domain-adapted recognition for product names, competitor names, technical vocabulary and the acronym-heavy speech of enterprise sales, which is where generic transcription visibly fails and where the errors are on exactly the words that matter; (2) role inference — who on the call is the buyer, who is technical, who is the economic decision maker — since almost every downstream analysis depends on it and it is not in the calendar invite; (3) commitment and next-step extraction, which is the single most useful per-call output and is what a representative would actually value, as the parent niche's fix note argues; (4) multi-call deal narrative rather than per-call summary, because the unit that matters is the deal and the category persistently delivers the call; and (5) retention and deletion handled properly, since recordings of customers are held indefinitely by default in most deployments and that is a liability and an ethical position rather than a storage decision.

## Target Customer
Conversation intelligence vendors whose infrastructure moat has evaporated, the conferencing platforms extending into the space, and the CRM incumbents who could integrate rather than partner.

## Impact If Solved
The commoditisation means the category has to move up or be absorbed by the conferencing platforms, and the deal-level narrative and commitment extraction are where the remaining value is. Domain adaptation is the cheap and immediate win, since generic transcription errors concentrate on the product and competitor names that every downstream analysis keys on.
