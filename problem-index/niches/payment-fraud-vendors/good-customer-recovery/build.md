# A Route Through Instead of a Wall

**Niche:** [[niches/payment-fraud-vendors/good-customer-recovery/profile|Good-Customer Recovery]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product's answer to uncertainty is to stop the customer, when the customer could simply be asked to prove something.
**Tags:** #gradient-boosting #evaluation-metrics #revenue-impact #confidence-intervals #automation #workflow-orchestration #logistic-regression #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to give a wrongly declined customer a way through instead of a dead end — and whoever recovers them turns the category's largest invisible loss into revenue.

## The Problem
The decision is binary because the interface is binary: approve or decline, in milliseconds, with nothing in between. Yet the uncertain cases are precisely the ones where a small amount of additional evidence would resolve the question — a verification code, a card confirmation, a brief delay for review with a follow-up email, an offer of a different payment method. Instead the customer hits a wall, and a genuine customer's response to being treated as a criminal is usually to leave for good.

## Why Nobody Has Built This
The decision interface was designed as a binary authorisation response, so intermediate outcomes had nowhere to live — the protocol shaped the product and nobody pushed back on the frame. Adding friction is assumed to lose conversions, which is true of friction applied indiscriminately and untested when applied selectively. The vendor is measured on fraud rate. And nobody tracks whether a declined customer ever came back.

## What to Build
Make the outcome space larger than two. Introduce graduated responses — step-up verification, delayed review with follow-up, alternative payment method, reduced order value — which is the core and is what a binary decision has been suppressing. Choose the response by predicted customer type rather than applying one policy, since the right treatment for a probable good customer and a probable fraudster are entirely different. Measure recovery rate by response type, because the assumption that friction loses the sale is testable and is currently an article of faith. Follow up with declined customers where the merchant relationship allows, as a message inviting them to complete an order recovers a meaningful share and nobody sends it. Track whether declined customers return and transact, which is the observable proxy for a false decline and is not measured. Prioritise recovery by customer value, since a first-time small order and a repeat high-value customer warrant different effort. Offer the merchant control over the treatment, as tolerance for friction varies enormously by business. Measure the revenue recovered as the product metric, which is the number that makes this fundable. Handle the genuine fraudster's response to step-up as a signal, because an attacker who abandons at verification confirms the decision. And feed recovery outcomes back into the model, since a customer who passed step-up is a label in the decline region obtained for free.

## Target Customer
Merchant success and product leadership, merchants losing revenue invisibly, customers turned away wrongly, and conversion optimisation vendors with no fraud integration.

## Impact If Built
The authorisation protocol is binary, so intermediate outcomes had nowhere to live and the frame was never challenged. Graduated responses recover revenue and produce labels in the decline region as a by-product.
