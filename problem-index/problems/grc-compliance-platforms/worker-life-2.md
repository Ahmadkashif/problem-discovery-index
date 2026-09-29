# The Engineer Filling In the Fortieth Questionnaire

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Worker Life Changing
**One-liner:** Every enterprise customer sends a three-hundred-question security questionnaire, the certificate was supposed to prevent this, and it did not.
**Tags:** #large-language-models #bert #transformers #k-nearest-neighbors #contrastive-learning #evaluation-metrics #worker-facing #automation

## The Problem
A company selling to enterprises receives security questionnaires with each deal. They run from dozens to several hundred questions, arrive in the customer's own spreadsheet format, and cover much of the same ground as the certification the company already holds — which the customer has usually also been sent.

The answers are largely the same every time, rephrased to match each questionnaire's wording, and they must be accurate because they are contractual representations. So the work lands on someone who knows the actual security posture, which means a security engineer or a technical founder rather than a salesperson.

The volume scales with sales. A company doing well receives more questionnaires, each on a deal timeline, each urgent because it gates a contract. Engineers describe losing days per deal to this, repeatedly, on content that exists in a previous response.

Accuracy under time pressure is the risk nobody discusses. An engineer completing a three-hundred-question document at speed, on a deal deadline, will approximate — and those answers are contractual. The gap between the answer given and the reality is a liability that nobody is measuring.

And the certificate did not solve it. The entire promise of standardised frameworks was that an attestation would replace bespoke enquiry, and in practice enterprise procurement asks anyway.

## Why It Matters to the Worker
This is highly skilled, expensive time spent transcribing existing information into someone else's format, on a deadline set by a sales process, with contractual liability attached to speed.

It is also demoralising in the specific way that repetition with no product value is. The engineer knows the answers exist, knows the customer has the certificate, and does it anyway because a deal depends on it.

The interruption pattern is the operational cost. Questionnaires arrive unpredictably with short deadlines, which fragments engineering work in a way that is difficult to plan around — and the person answering is usually the person the rest of the security programme also depends on.

And the liability sits uncomfortably. Signing accurate representations about a complex and changing posture, repeatedly, at speed, is a risk that is accepted because refusing costs a deal.

## What a Solution Looks Like
Answer from the evidence corpus rather than from memory. The platform already holds control state, configuration detail and policy documents, and generating an answer grounded in that — with the supporting evidence linked — is both faster and more accurate than an engineer recalling. Where the evidence does not support a confident answer, the system should say so rather than produce plausible text, because a fluent wrong answer on a contractual document is worse than a blank.

Match questions to previous answers semantically. The same question in forty wordings is one question, and retrieval against a curated answer library with the engineer approving rather than composing is most of the volume.

Maintain the library as a product. Answers change as posture changes, and an answer library that flags when its own basis has drifted — a control that changed, a policy that was revised — prevents the slow decay into inaccurate representations.

Push the trust centre harder. A published, continuously-updated trust centre with evidence that customers can self-serve is the structural fix, and its adoption depends on enterprise procurement accepting it — which is a market coordination problem the platforms are better placed to push than any individual vendor.

And measure the accuracy risk. How often an answered representation is contradicted by the organisation's own control state is checkable, and nobody checks it.

## Impact If Solved
Security questionnaires are one of the largest unpriced costs in enterprise software sales and they fall on the most expensive technical people at the least convenient moments. Grounded generation with explicit deferral, semantic matching to a maintained library, and a trust centre the platforms push procurement to accept would return that time — and would reduce a contractual accuracy risk that currently exists because the work is done at speed by people who have done it thirty-nine times already.
