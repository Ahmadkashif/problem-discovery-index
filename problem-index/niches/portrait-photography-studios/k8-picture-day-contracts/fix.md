# The Yearbook Page With the Wrong Name

**Niche:** [[niches/portrait-photography-studios/k8-picture-day-contracts/profile|K-8 Picture Day Contracts]]
**Industry:** [[industries/portrait-photography-studios|Portrait Photography Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Two children swap barcode cards in line, nobody notices, and their photos are printed under each other's names in a book the school keeps forever.
**Tags:** #contrastive-learning #k-nearest-neighbors #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver everything a K-8 school asks of picture day — every child photographed, ID cards within days, yearbook and SIS files, free retakes — right the first time and under a privacy agreement the district trusts, and whoever asks least of the school office keeps the contract.

## The Problem
The barcode card is the only link between a child and a frame. Cards get swapped, lost or scanned twice; retake-day children give nicknames; siblings share surnames. Errors surface when the yearbook is printed, ID cards are handed out or a parent opens a gallery of someone else's child.

## Why It's Still Broken
Checking every image against a roster by eye is impossible at tens of thousands of children, so studios check samples. Face matching could catch swaps, but studios avoid it because of biometric law and their own privacy pledges.

## What a Fix Looks Like
Within-job checks that flag only anomalies: two cards with one face, one card with two faces, a frame whose class or grade doesn't match the station schedule, a retake that doesn't resemble the original. Embeddings exist only for the job and are deleted at delivery; flagged images go to a coordinator.

## Who Feels the Pain
School office managers who field the complaint; families; the studio coordinator; the contract at renewal.

## Impact If Fixed
Mismatches caught before publication instead of after, at a cost of minutes per school.
