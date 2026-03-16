# Barista Repetitive Strain from High-Volume Espresso Production

**Industry:** [[coffee-shops-independent|Independent Coffee Shops]]
**Type:** Worker Life Changing
**One-liner:** A busy barista pulls 300+ shots per shift, each requiring a precise tamp with 30lbs of force — their wrists, shoulders, and lower backs pay the price within months.
**Tags:** #lstm #anomaly-detection #signal-processing #worker-facing #tacit-knowledge-ml

## The Problem
A barista on a busy morning shift produces 250-400 espresso-based drinks in 6-8 hours. Each drink requires grinding (twisting a portafilter into a grinder), dosing, tamping (applying ~30lbs of downward force with a level wrist), locking the portafilter into the group head (a twisting motion under load), and steaming milk (holding a pitcher at an angle while controlling a steam valve). These motions are repeated every 60-90 seconds. Within 3-6 months of full-time bar work, baristas commonly develop wrist tendinitis, shoulder impingement, lower back pain from standing on hard floors in a hunched posture, and trigger finger. Most shops have no ergonomic assessment, no rotation protocol, and no way to detect when a barista's movement pattern is degrading before injury occurs.

## Why It Matters to the Worker
Baristas are typically young (18-28), hourly ($14-$18/hr plus tips), and uninsured or underinsured. A repetitive strain injury can end their ability to work the bar, which is the highest-tip position in the shop. They often push through pain because calling out means a coworker covers their shift and they lose income. The injury follows them to their next job. There is no workers' comp culture in coffee — most baristas do not even know their wrist pain qualifies.

## What a Solution Looks Like
A wearable sensor (wristband or smart watch) or machine-mounted accelerometer tracks tamping force, wrist angle, and repetition frequency throughout a shift. An LSTM model trained on healthy movement baselines detects deviation patterns — increased force compensation, wrist angle drift, cadence irregularity — that precede injury. The system alerts the barista and shift lead when cumulative strain crosses a threshold, recommending a rotation to register or prep tasks. Over time, the data identifies which equipment setups (grinder height, tamper weight, mat thickness) reduce strain for each barista's body mechanics.

## Impact If Solved
Reduces barista RSI incidence by an estimated 40-60%, extending average tenure on bar by 4-8 months. For the worker, this means fewer medical bills, less chronic pain, and the ability to continue earning in the highest-tip role. For the shop, it reduces turnover-driven retraining costs of $1,500-$2,500 per barista.
