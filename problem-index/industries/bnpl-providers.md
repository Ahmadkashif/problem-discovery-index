# BNPL Providers

## Profile
**Category:** Fintech
**Market Size:** ~$110B US annual originations across pay-in-four and longer instalment products, with revenue split between merchant discount and consumer interest and fees
**Tech Maturity:** Fast where it is visible, thin where it is consequential — Klarna, Affirm, Afterpay, Zip, Sezzle and PayPal's instalment product make an approval decision inside a checkout in a few hundred milliseconds, on applicants who frequently have no usable credit file. The underwriting stack is modern; the outcome data that would improve it is fragmented across the provider, the bureaus and the six other providers the same consumer is using.
**Workforce:** Credit risk modellers, fraud analysts, collections and hardship agents, merchant integration and account management, compliance and complaints staff, customer support

## Key Pain Themes
The defining problem is that the decision and the evidence are separated by six weeks and by the industry's own structure. A provider approves a $180 purchase split into four payments, on a consumer identified by an email address and a debit card, using bureau data that may not exist, device and behavioural signals, and the provider's own history with that customer if there is any. The repayment outcome arrives over the following six weeks. Between approval and outcome sits the thing nobody can see: the same consumer taking five more plans from five other providers on the same afternoon.

Furnishing to the bureaus is partial and inconsistent across providers, and the products that furnish tend to be the longer-term interest-bearing ones rather than pay-in-four. So the sector's central risk — accumulation across providers — is invisible to every participant by construction, and the consumers most exposed to it are the ones the sector's own marketing reaches most effectively.

Around that sit merchant integration and placement, collections and hardship handling, and dispute processing where the provider is neither the merchant nor the card issuer and is treated as both.

## Current Tech Landscape
Underwriting blends bureau data where available (Experian, Equifax, TransUnion, plus alternative files from LexisNexis and Clarity), cashflow data through Plaid or MX where the consumer connects an account, device and behavioural signals from Sardine or Socure, and the provider's own repayment history. Decisioning runs on internal platforms with gradient-boosted models and a rule layer. Collections use a mixture of automated retries against the stored card, messaging, and eventually agency placement. Bureau furnishing is uneven — Equifax and TransUnion have accepted BNPL tradelines in various forms and adoption has been partial — and the CFPB's 2024 interpretive rule brought pay-in-four explicitly under Regulation Z's credit card dispute and refund provisions.

## Problems
- [[problems/bnpl-providers/high-impact|🔴 High Impact: Underwriting Blind to Accumulation]]
- [[problems/bnpl-providers/low-impact-1|🟡 Low Impact: Merchant Integration and Checkout Placement]]
- [[problems/bnpl-providers/low-impact-2|🟡 Low Impact: Dispute and Refund Handling Under Reg Z]]
- [[problems/bnpl-providers/worker-life-1|🟢 Worker Life: The Collections Agent on a Ninety-Dollar Balance]]
- [[problems/bnpl-providers/worker-life-2|🟢 Worker Life: The Merchant Risk and Dispute Handler]]
- [[problems/bnpl-providers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/bnpl-providers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
BNPL generated, in under a decade, one of the largest repayment datasets on consumers with thin or no credit file — tens of millions of people making small, frequent, observable payment decisions. That is genuinely new empirical ground, and the sector has used it almost entirely to score its own next approval. The two questions it is positioned to answer and does not are: what does repayment behaviour on small instalments actually predict about a person's capacity, measured against outcomes rather than against a bureau score; and what happens to a consumer holding concurrent plans across multiple providers. The first is a research opportunity. The second is a consumer protection question that the sector's data structure prevents anyone — including the sector — from answering, and which will be answered eventually by a regulator using worse data.
