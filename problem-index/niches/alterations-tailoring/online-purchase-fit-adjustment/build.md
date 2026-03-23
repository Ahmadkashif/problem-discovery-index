# Photo-Based Fit Assessment & Alteration Scoping

**Niche:** [[niches/alterations-tailoring/online-purchase-fit-adjustment/profile|Online-Purchase Fit Adjustment Services]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool lets a consumer photograph themselves wearing an ill-fitting online purchase and receive an automated assessment of what alterations are needed, estimated cost, and nearby tailor recommendations.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #pose-estimation

## The Problem
A consumer receives a dress shirt from an online retailer. It fits in the shoulders but is too long in the sleeves and too loose in the torso. They're deciding: return it (hassle, shipping, waiting for replacement) or get it altered (unknown cost, unknown tailor, unknown if the alterations are even worthwhile for a $50 shirt). They lack the knowledge to assess what alterations are needed ("take in the side seams, shorten the sleeves by 1.5 inches"), whether the garment is worth altering (some construction doesn't allow easy alteration), and how much it should cost. An experienced tailor could answer all these questions in 30 seconds by looking at the garment on the body — but the consumer can't get that assessment without visiting a shop.

## Why Nobody Has Built This
Fit assessment from photos requires visual understanding of how fabric should drape on a body — the same tacit knowledge that tailors develop over years. Building a photo-based assessment tool requires: training data pairing photos of ill-fitting garments with expert tailor assessments (alteration type, difficulty, estimated cost), pose estimation to understand the body underneath the garment, and garment type classification (the same excess fabric means different things on a suit jacket vs. a casual shirt). No labeled dataset of "garment fit problems with expert assessments" exists at scale.

## What to Build
A mobile tool where the consumer takes 3-4 photos (front, back, side, detail of problem area) wearing the garment. The system identifies fit issues (too long, too wide, shoulder misalignment, sleeve length, dart needs), recommends specific alterations, estimates the cost range, and assesses whether the garment is worth altering (based on garment quality vs. alteration cost). If the consumer decides to proceed, the system recommends nearby tailors and pre-fills the alteration specification — so the consumer arrives at the tailor knowing exactly what they need.

## Target Customer
Online clothing shoppers who receive items that are close to fitting (estimated 15-20% of online purchases), particularly consumers of mid-range clothing ($40-150) where the garment is worth the cost of a $15-40 alteration.

## Impact If Built
Diverts 10-20% of "didn't fit" returns to alterations (saving consumers shipping hassle and retailers return processing costs), creates a new customer acquisition channel for local alteration shops, and captures the tacit knowledge of fit assessment in a scalable digital tool.
