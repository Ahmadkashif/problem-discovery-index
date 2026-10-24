# The MRI Technologist Clearing an Implant With a Patient on the Table

**Industry:** [[diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Worker Life Changing
**One-liner:** An MRI technologist working alone has to decide, in minutes and on their own licence, whether a patient's pacemaker, stimulator or aneurysm clip is safe to scan, and gets back the confidence and the lost hour when the device's conditions are found and checked for them.
**Tags:** #large-language-models #transformers #bert #k-nearest-neighbors #worker-facing #compliance #automation

## The Problem
Every MRI patient fills out a safety screening form, and a growing share list an implant: a cardiac device, a spinal cord or deep-brain stimulator, a cochlear implant, an insulin pump, a programmable shunt, surgical clips, a foreign body from years ago. The technologist must identify the exact make and model, often from a patient's memory or a wallet card. They must find the manufacturer's MR Conditional labelling and check the scanner's field strength, the gradient slew limit, the specific absorption rate mode and any required device programming against it. Some devices need a cardiology rep or a radiologist on site. All of this happens while the patient waits on the table and the next two patients wait in the lobby (recalled practice under ACR MR safety guidance).

The information is scattered: a device registry website, a manufacturer's PDF, an operative note faxed from another hospital, a phone call to the implanting surgeon's office. When it cannot be found, the scan is cancelled and rebooked, the slot is lost, and the patient goes back to a referrer who may send them somewhere else.

## Why It Matters to the Worker
The technologist carries the decision. Scanning a patient whose device was not cleared can cause heating, device malfunction or worse, and the technologist's ARRT credential and job are on the line. Refusing a scan that was safe draws complaints from the patient, the referrer and the manager watching the schedule. With MRI technologist vacancies at 17.4% in 2025 (ASRT), many centres run one technologist per magnet on evenings and weekends, so there is no second opinion in the building.

The work is also unrecognised. A 20-minute implant search counts as nothing on a productivity report built on completed exams per hour, and the technologist who is careful looks slower than the one who is not.

## What a Solution Looks Like
An implant-clearance assistant that starts at booking, not at the scanner. It reads the screening form, the referral and any attached operative notes, and asks the patient for a photo of the implant card days before the exam. It identifies the device model, retrieves the manufacturer's current MR Conditional conditions and maps them onto this centre's scanner settings. It flags what still needs a human: device reprogramming, a radiologist's sign-off, a rep visit. The technologist sees a one-page clearance sheet with every condition sourced to its document and a clear "cleared", "cleared with conditions" or "needs radiologist" status, and signs it.

## Impact If Solved
Moving implant research from the scanner room to the days before the exam would save the technologist roughly 15–30 minutes per implant patient (estimate). It would rescue most same-day cancellations for "unable to verify device", and give a lone evening technologist a documented, sourced basis for a decision they currently make on memory and nerve.
