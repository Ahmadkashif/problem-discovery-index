# Ranking for Connection

**Niche:** [[niches/membership-community-platforms/feed-and-surfacing/profile|Feed & Surfacing]]
**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The feed is either everything in order or the loudest things first, and neither is what a member needs to see.
**Tags:** #matrix-decompositions #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #contrastive-learning #causal-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show a member the three things in this community that concern them rather than everything in reverse order — and whoever does it makes a large community feel like a small one.

## The Problem
A member opens the app. In a quiet community there is nothing; in an active one there are two hundred items. The chronological feed makes them scroll past everything to find anything; the engagement-ranked feed shows them what is popular, which is the loud core's conversation and not theirs. Either way the newcomer's unanswered question is buried, the quiet member's post is invisible, and the thing this member could usefully reply to is somewhere in the middle.

## Why Nobody Has Built This
Feed ranking was inherited from social platforms, so the objective is engagement and the mechanics amplify popularity — a ranking imported from a business that sells attention will optimise attention. The community objective is different and was never specified. Connection is harder to optimise than clicks. And smaller communities were assumed not to need ranking at all.

## What to Build
Rank for the outcome the business actually sells. Define the objective as a reply given or received rather than as time spent, which is the core and inverts what the ranking amplifies. Surface posts this member is well placed to answer, using their expertise, history and relationships, since the most valuable action a member can take is answering someone. Prioritise unanswered posts, particularly from newcomers, because an unanswered post is the community's most costly failure and the feed currently buries it. Personalise by interest and relationship rather than by popularity, which is what makes a large community feel navigable. Suppress the loud core's dominance deliberately, as it crowds out everyone else without anyone intending it. Surface the quiet member's contribution, since visibility is what turns a first post into a second. Show fewer items rather than more, because a short relevant list is read and a long one is scrolled. Measure whether the feed produced a reply, which is the honest evaluation and is not currently computed. Handle the quiet community, where the problem is emptiness rather than volume and the answer is prompting rather than ranking. And test against retention, since that is the outcome and the surface is clean.

## Target Customer
Product leadership, members overwhelmed or underserved by the feed, founders whose newcomers are invisible, and community platform vendors.

## Impact If Built
A ranking imported from a business that sells attention will optimise attention, and this business sells belonging. Ranking on replies given and received, with unanswered newcomers prioritised, is what makes the feed serve the product.
