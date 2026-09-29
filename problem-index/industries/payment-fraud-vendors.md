# Payment Fraud Vendors

## Profile
**Category:** Fintech
**Market Size:** ~$7B US revenue across transaction fraud decisioning, chargeback guarantee and merchant risk platforms
**Tech Maturity:** Mature modelling on a structurally incomplete label — Sift, Forter, Signifyd, Riskified, Kount, Stripe Radar, Ravelin and Sardine run large ensembles over device, behavioural, network and consortium signals, and train them on chargebacks, which exist only for transactions that were approved. The decisions the model made to decline are the ones it will never learn from.
**Workforce:** Fraud data scientists and risk strategists, manual review analysts, merchant integration and onboarding staff, chargeback representment specialists, customer success and policy teams

## Key Pain Themes
The central defect is the missing counterfactual. A declined transaction produces no outcome: the merchant never learns whether that customer would have paid, whether they went elsewhere, or whether they were the fraudster the model believed. Labels arrive only for approvals, and only as chargebacks, which are themselves a lagged, noisy and partially adversarial signal — a chargeback can mean fraud, or it can mean a customer who forgot a subscription. The models are trained on this and then evaluated on it, which makes every published accuracy number a statement about a population the model itself selected.

False declines are the commercial consequence and are estimated to exceed actual fraud losses by a wide margin across card-not-present commerce, largely without being measured directly. Merchants feel them as lost revenue they cannot see and as customers who never return.

Around it sit merchant onboarding — where every new vertical requires a model to learn a new definition of normal from scratch — and a manual review function that exists precisely where the model is least certain and is staffed by people making irreversible decisions in forty seconds.

## Current Tech Landscape
Signals come from device fingerprinting, behavioural biometrics, email and phone intelligence, IP and proxy detection, velocity across a consortium, and merchant-supplied order context. Decisioning is a model ensemble plus a merchant-configurable rule layer. Chargeback guarantee providers take the liability, which aligns their incentive to approvals but not to the merchant's full customer lifetime. Manual review is offered as a service or performed by the merchant. Network tokens, three-domain-secure and liability shifts change the economics without changing the label problem. Consortium data is the durable moat and its value depends on the cross-merchant identity graph rather than on model architecture.

## Problems
- [[problems/payment-fraud-vendors/high-impact|🔴 High Impact: The Declines Nobody Ever Grades]]
- [[problems/payment-fraud-vendors/low-impact-1|🟡 Low Impact: Merchant Onboarding and Cold Start]]
- [[problems/payment-fraud-vendors/low-impact-2|🟡 Low Impact: Chargeback Representment Evidence]]
- [[problems/payment-fraud-vendors/worker-life-1|🟢 Worker Life: The Manual Review Analyst at Forty Seconds a Case]]
- [[problems/payment-fraud-vendors/worker-life-2|🟢 Worker Life: The Risk Strategist Tuning Blind]]
- [[problems/payment-fraud-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/payment-fraud-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry is the cleanest example in commerce of a discipline that measures what it did and not what it should have done. The evidence required to fix it is neither exotic nor expensive: a small randomised approval allowance on transactions the model would have declined produces unbiased labels in the region where the model is weakest, and a large network running it continuously would obtain the only honest estimate of false decline rates that exists anywhere. Every participant knows this. Almost nobody runs it, because the cost of the experiment is visible and immediate while the bias it corrects is invisible and permanent. The vendor that does it first will be able to say something about its own accuracy that no competitor can contradict or match.
