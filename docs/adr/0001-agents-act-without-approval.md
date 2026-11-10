---
status: accepted
date: 2026-11-10
---

# Agents act without approval; only backups are out of reach

The owner does not write or read code, so a human approval step adds delay and no safety. Agents therefore build, merge, deploy, fix, remove and reconfigure everything handh.dev runs on their own authority, with write access to production. Safety comes from undo instead of review.

The one limit is enforced by the storage itself, not by a person: protected backups cannot be deleted or altered by anyone, agent or owner, for a set period. Removing a service archives its data instead of destroying it.

## Considered options

- **Truly unlimited agents.** Rejected: one confused agent, or one malicious instruction read from an email or web page, could erase a company's data and every copy of it, and nothing would bring it back.
- **Read-only agents with a human making changes.** This was the rule in handh-infra until this decision. Rejected: the human cannot judge the changes, so it only slowed work down.

## Consequences

- Rules that restrict agents to read-only production access, or that wait on "owner approval" for technical changes, are obsolete and should be removed where found.
- Receipts and qualification records written to earn approval are no longer needed. History lives in git.
- Agents check each other's work, since no person can.
