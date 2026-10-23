# Every Call Scored Against Its Own Account's Rules

**Niche:** [[niches/answering-services/call-quality-scoring/profile|Call Quality & Escalation Compliance Scoring]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Answering services record every call and score a handful against a generic rubric; scoring all of them against each client's rules would turn quality from a sample into evidence.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to prove, call by call, that each client's script was followed and every escalation was made inside its time limit, and whoever can put that evidence for every call in front of the client at renewal takes the account.

## The Problem
A service handling hundreds of thousands of calls a year reviews perhaps a percent or two of them (estimate), chosen at random or after complaints. Whether operators asked the required questions, chose the disposition the account requires and escalated on time is unknown for everything else. Clients have no evidence either way until something goes wrong.

## Why Nobody Has Built This
General speech analytics scores against a single rubric. The answering-service problem needs each call scored against the rules of the account it was for, and those rules exist only as prose in script notes. Until scripts are structured, there is nothing to score against.

## What to Build
A scorer that transcribes every call, retrieves the account's rule table as it stood that day, and checks required questions, disposition and escalation timing, plus HIPAA identity and disclosure steps on medical accounts. Low-confidence calls go to human review, and the results roll up into a per-client monthly compliance report and per-operator coaching queues.

## Target Customer
Quality and operations managers at answering services with 25+ seats and a medical or property book; TAS platform vendors as embedders.

## Impact If Built
Quality review covers every call. Clients receive a compliance record at renewal, and the coaching effort goes to the operators and accounts where escalation errors actually happen.
