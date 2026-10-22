# The LIMS Built in Access by a Chemist Who Retired

**Niche:** [[niches/testing-laboratories/small-independent-labs/profile|Small Independent Accredited Labs]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** Many small labs run on a database written years ago by someone who has left, and nobody dares touch it.
**Tags:** #large-language-models #data-integration #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to give a five- to twenty-five-person accredited lab a system it can run without an IT person or LIMS administrator, and whoever gets a small lab live and assessment-ready in weeks rather than a year wins a long tail the enterprise vendors ignore.

## The Problem
The home-built system holds clients, samples, results and report templates. It works until the operating system is upgraded, a new client wants a different report, or an assessor asks for an audit trail it doesn't have.

## Why It's Still Broken
Migration means mapping years of idiosyncratic tables and logic, and the owner fears losing history clients still ask about.

## What a Fix Looks Like
A migration service that reads the legacy database and its reports, infers the data model and business rules, maps them to a modern LIMS, and verifies by regenerating historical reports from the migrated data.

## Who Feels the Pain
Owners of small labs, the one staff member who knows how the old system works, and assessors asking for audit trails.

## Impact If Fixed
The lab gets a supported system and an audit trail without losing its history.
