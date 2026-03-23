# Predictive Patient Outreach and Order Conversion Engine

**Niche:** [[niches/medical-supply-retail/recurring-supply-fulfillment/profile|Recurring Supply Fulfillment]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool predicts the optimal outreach time, channel, and supply mix for each recurring patient — so suppliers blast fixed-schedule phone calls and convert only 15-20% of outreach attempts into orders.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
A DME supplier with 3,000 recurring supply patients generates a daily outreach list: patients whose insurance eligibility window has opened. Customer service reps make 80-100 calls per day, reaching 40-50 patients, and converting 12-20 into confirmed orders. The remaining 60-70 calls result in voicemail, no answer, "call me next week," or "I still have supplies." This 15-20% conversion rate means the supplier employs 4-5 reps to generate the same revenue that 1-2 reps could handle with better targeting. The root problem is treating all patients identically: calling everyone on the eligibility date regardless of their actual supply need, contact preference, or likelihood of ordering.

## Why Nobody Has Built This
Predicting individual patient ordering behavior requires combining: historical order patterns (this patient typically orders 2 weeks after eligibility opens), supply usage data (CPAP hours/night indicates mask wear rate, diabetic testing supply usage varies by medication regimen), engagement signals (did they answer last time? did they open the email? do they prefer morning or afternoon calls?), and seasonal patterns (some patients order supplies before winter travel). This data exists across the billing system (order history), device platforms (CPAP usage), and CRM (communication history) but has never been integrated into a predictive model for outreach optimization.

## What to Build
A patient outreach optimization engine that scores each patient weekly on: order probability (how likely to order this week vs. next week vs. next month), best contact channel (phone, text, email — based on historical response patterns), best contact time (morning vs. afternoon vs. evening), and recommended supply mix (based on usage data and time since last order). The daily outreach list is ranked by order probability, so reps call the most likely converters first. Low-probability patients receive automated text/email outreach instead of live calls. The system learns from outcomes: every call result (ordered, declined, not reached) updates the model.

## Target Customer
DME suppliers with 1,000+ recurring supply patients who employ 3+ customer service reps for resupply outreach and want to increase conversion rate without adding staff.

## Impact If Built
Increases outreach-to-order conversion from 15-20% to 30-40% by contacting patients at the right time via the right channel. Enables the same team of 4 reps to cover a patient base that currently requires 6-8 reps, saving $100K-200K/year in labor. Increases recurring supply revenue by 15-25% by capturing orders from patients who are currently unreachable by phone but respond to text or email.
