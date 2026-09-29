# The Error Message That Goes to the Wrong Person

**Niche:** [[niches/no-code-app-builders/citizen-developer-support-load/profile|Citizen Developer Support Load]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** When an automation fails, the platform logs it for the app's editor and shows the user nothing, so the user messages the builder and the builder becomes the error handler.
**Tags:** #descriptive-statistics #bert #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop the person who built a useful app becoming its unpaid support desk — and whoever does that takes the builder's loyalty, which is what determines whether the platform spreads inside a company.

## The Problem
A user submits a shift swap. The automation that notifies the manager fails because the connected calendar's token expired. The user sees a success message, because the form saved. The manager receives nothing. Two days later the user asks the builder why nothing happened. The builder opens the run history, finds the error, reconnects the account, and re-runs the automation. Every part of that sequence — including the user's belief that it had worked — was determined by a design decision that errors are for editors.

## Why It's Still Broken
The runtime reports to whoever can fix things, which sounds correct and means the person affected learns nothing. Automations are asynchronous, so the user has already left the screen and there is no obvious place to tell them, and nobody has built one. Error messages are also written for a technical reader, so showing them to a user would not help without translation. And the resulting load lands on the builder, who is not the customer, so the cost never appears in any vendor's prioritisation.

## What a Fix Looks Like
Tell the person affected, in terms they can act on. Notify the user when an action they initiated fails, which is the entire fix for the most damaging case — believing something happened when it did not. Translate the error into consequence and next step: what did not happen, whether it will retry, what they should do now, and who has been told. Notify the builder separately with the technical detail, which is what they need and is not what the user needs. Retry transparently where retrying is safe, and say so, since most of these failures are transient and a visible automatic retry removes the message entirely. Group recurring errors so a token expiry affecting thirty runs is one notification rather than thirty. And report the app's error rate to the builder as a trend, so they can fix the cause rather than handling instances — which is the difference between being a support desk and being a maintainer.

## Who Feels the Pain
Users who believe something worked and find out days later that it did not; builders acting as the error-handling layer for their own applications; and the processes that depend on automations nobody noticed had stopped.

## Impact If Fixed
Notifying the affected user is a small runtime change addressing the most damaging failure mode in the category, and error translation plus grouping removes most of the remaining message volume. The error-rate trend turns the builder from a responder into a maintainer.
