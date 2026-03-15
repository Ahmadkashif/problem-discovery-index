# Driver Performance Coaching and Safety Event Detection

**Industry:** [[last-mile-delivery|Last-Mile Delivery]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic fleet telematics platforms flag speeding and hard braking events but don't diagnose which driver behaviors are causing delivery inefficiency (address search time, inefficient vehicle loading pattern) vs. which are safety concerns requiring coaching.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #signal-processing

## The Problem

Driver performance in last-mile delivery varies 15-25% between high-performing and average drivers on the same route — a gap worth 5-8 extra stops per day. The performance gap comes from multiple behaviors: efficient vehicle loading (organized by delivery sequence), familiarity with addresses and access, optimal parking decisions, and recipient interaction speed. Current telematics platforms measure driving behavior (speed, harsh braking) but not the delivery execution behaviors that drive the performance gap.

A manager who can identify specifically which behavior is causing a driver's lower performance can coach for improvement. A manager who only sees "Driver A averaged 38 stops/day vs. Driver B's 45" can't target a coaching intervention.

## What Already Exists

Samsara and Verizon Connect provide safety event logging and driver scorecards. These score driving behavior — not delivery execution behavior. Amazon's Mentor app scores DSP driver behavior but only surfaces scores, not diagnostic coaching for specific execution gaps.

## The Customisation Gap

A delivery execution coaching tool needs: (1) per-stop time breakdown from telematics (time from stop to curb, time at address, drive time to next stop); (2) classification of time-at-address into driver behavior categories (rapid delivery vs. long recipient search time vs. access difficulty — which are coachable vs. structural); (3) route execution efficiency score (did the driver follow the optimized stop sequence, or deviate? when deviations were made, were they better or worse?); (4) targeted coaching suggestion per driver per identified behavior gap.

## Impact If Solved

A 3-stop improvement per driver per day (from coaching) on a 20-driver operation adds 60 additional stops daily, or $300-$600 in additional revenue per day at $5-$10/stop.
