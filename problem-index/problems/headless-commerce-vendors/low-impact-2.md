# Checkout Compliance by Jurisdiction

**Industry:** [[headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tax engines, payment authentication and accessibility tooling are all mature bought components, and assembling them into a checkout that is correct in every jurisdiction the retailer sells into is left to whoever built the checkout.
**Tags:** #large-language-models #bert #change-point-detection #hypothesis-testing #evaluation-metrics #compliance #workflow-orchestration

## The Problem
A checkout must satisfy a growing set of jurisdictional requirements. Sales tax and value-added tax calculation and display rules vary by state and country, including whether prices must be shown inclusive of tax. Strong customer authentication applies in Europe with specific exemption handling. Accessibility standards are increasingly enforced through litigation in the US and by statute in Europe. Consumer protection rules govern cancellation rights, disclosure and how subscriptions may be sold and cancelled. Payment method availability and regulation differ everywhere.

In a monolithic platform much of this arrived with the product. In a composed stack, the tax engine calculates tax and the checkout must display it correctly; the payment provider supports authentication and the checkout must invoke it correctly; accessibility is a property of a front end the retailer built.

So compliance becomes the integrator's responsibility, implemented once at launch against the rules then applicable, and the rules change while the checkout does not.

## What Already Exists
Tax calculation engines (Avalara, Vertex, Stripe Tax) handle rate determination and filing well. Payment providers implement authentication and exemption logic. Accessibility testing tools identify many violations automatically. Consent management platforms handle privacy notices. Legal publishers track regulatory developments. Compliance requirements are documented publicly.

## The Customisation Gap
The bought components handle calculation and the composed checkout handles presentation and flow, and the requirements are increasingly about presentation and flow. A tax engine returning the correct amount does not ensure the price is displayed inclusive where that is required.

Nothing monitors regulatory change against a deployed checkout. Requirements change, and a retailer discovers it through a demand letter or an audit rather than through a system watching for it — which is a document monitoring problem on public sources.

Verification of the deployed experience is missing. Whether the live checkout actually displays what a jurisdiction requires, for a customer in that jurisdiction, is testable by automated journeys from representative locations, and is generally checked at launch and not since.

Accessibility regression is the clearest case. Front ends change continuously, accessibility violations are introduced routinely by ordinary feature work, automated testing catches a meaningful share, and it is rarely wired into the deployment pipeline for the checkout specifically — which is the flow that attracts litigation.

## Impact If Solved
Checkout compliance failures produce demand letters, tax liabilities and blocked payments, and they arise because requirements move while a deployed checkout does not. Monitoring regulatory change against the specific deployment and verifying the live experience per jurisdiction converts a launch-time exercise into a maintained position.
