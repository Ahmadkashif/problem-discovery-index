# Mature Components, Unassembled Obligations

**Niche:** [[niches/headless-commerce-vendors/checkout-compliance/profile|Checkout Compliance]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tax engines, payment authentication and accessibility tooling are all mature bought components, and assembling them into a checkout that is correct in every jurisdiction the retailer sells into is left to whoever built the checkout.
**Tags:** #compliance #evaluation-metrics #automation #workflow-orchestration #data-integration #confidence-intervals #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to deliver a checkout that is correct in every jurisdiction the retailer sells into, from components that each solve one part — and whoever does that takes the risk off the retailer, because the assembly is where all of it lands.

## The Problem
A retailer sells into eleven countries. The tax service calculates correctly given the right inputs, and the checkout passes a customer address that is sometimes the billing address where the delivery address governs. The payment provider handles authentication, and the checkout applies an exemption the retailer is not entitled to claim. The accessibility audit passed at launch and four releases have since introduced keyboard traps. The price display satisfies one country's rules about showing tax inclusively and not another's. Every component works; the assembly is wrong in four ways; and the party responsible is a development team that was not told what the obligations were.

## Why Nobody Has Built This
Each component vendor scopes their responsibility to their component, correctly, and the composition is explicitly out of scope in every contract. The retailer's legal function reviews at launch and has no mechanism to review continuously. The obligations are spread across tax, payments, accessibility, consumer protection and data protection, which are five different specialisms and no single advisor covers them. And the developer building the checkout has no way to know what they do not know.

## What to Build
Verify the assembled checkout against the obligations continuously. Enumerate the obligations per jurisdiction the retailer sells into — tax treatment and display, authentication and exemptions, accessibility, pre-contractual information, cancellation rights, consent — as a machine-checkable specification, which is the artefact that does not exist and which everything else depends on. Test the running checkout against it automatically on every release and continuously in production, which turns a launch review into a control. Track regulatory change and map it to the specific checks it affects, so a rule change produces a failing test rather than a newsletter. Verify the inputs to each component as well as its output, since the tax engine's correctness depends on what the checkout passes it and that is where the errors are. Test accessibility on every release rather than at launch, which the fix note develops. Report conformance per jurisdiction, so the retailer can see where they are exposed and decide whether to sell there. Produce the evidence a regulator or an auditor would ask for, since the retailer currently has a launch report and a hope. And position the verification independently of the component vendors, since each of them disclaims exactly this and the gap is the product.

## Target Customer
Retail engineering and legal functions, the developers carrying the obligation, the integrators who built it, and the component vendors who disclaim the assembly.

## Impact If Built
Every component works, the assembly is wrong, and the party responsible was never told what the obligations were. A machine-checkable specification per jurisdiction is the missing artefact, and verifying the inputs to each component catches the errors that component-level correctness cannot.
