# Approvals Graded Against the Claims They Produce

**Niche:** [[niches/title-insurance-carriers/agency-channel-underwriting/profile|Agency-Channel Residential Underwriting]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Underwriters approve thousands of insure-over and high-liability requests a year and never learn which kinds of approval turn into claims, so authority limits are set by habit rather than evidence.
**Tags:** #logistic-regression #survival-analysis #large-language-models #k-nearest-neighbors #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep independent agents writing residential files on its paper by answering their approval and insure-over requests inside the closing window on terms it can stand behind, and whoever approves fastest without the approvals turning into claims takes the account.

## The Problem
An approval is a small underwriting decision with a long tail. Counsel agrees to insure over a paid but unreleased mortgage against the seller's indemnity, to give mechanics' lien coverage before the lien period runs, or to raise an agent's liability limit for a single file. Each approval is made on the facts in front of counsel and recorded thinly. The claims that follow arrive years later, in a different department, and are almost never traced back to the approval category that let the risk through. So underwriters cannot answer a basic question: which approvals are safe enough to push down into the agent's own authority, and which ones should get more scrutiny?

## Why Nobody Has Built This
Approvals live in email and portal logs that are not keyed to policy numbers. Claims are coded for payment rather than root cause. Approved risks rarely produce claims, so any one counsel's experience is too thin to learn from. Vendors sell to agents, not to the underwriting counsel who make these calls.

## What to Build
A record that captures every approval as structured data: risk type, state, liability, conditions imposed and the agent. It joins those approvals to later claims and their cost through the policy number. On top sit retrieval of similar past approvals for counsel at decision time, and survival models of claim emergence by approval category with honest intervals. A quarterly report then tells the chief underwriting counsel which categories can be delegated, which need conditions and which need a second reviewer.

## Target Customer
Chief underwriting counsel and agency operations leaders at the four families and the larger regional underwriters.

## Impact If Built
Faster approvals where the evidence says the risk is low, and tighter conditions where it is not. The underwriter wins agent loyalty in the contest that matters to agents without buying it with future claims.
