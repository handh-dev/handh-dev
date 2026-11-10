---
status: accepted
date: 2026-11-10
---

# Ship, check live, undo if unhealthy

The companies handh.dev serves have low user volume, and a short outage affects few people. Speed from request to live matters more than avoiding every blip. So agents ship first, check the live result, and undo if it is unhealthy, instead of proving a change safe before it goes out.

This applies the same way every day of the year, to every company and every page. There are no busy-season rules and no specially protected pages.

## Considered options

- **Slower, tested-first releases during each company's busy season.** Rejected by the owner: one way of working, no exceptions to remember.
- **Adopting Kamal for health-checked, no-interruption switchovers.** Not adopted. Its main benefit is avoiding the brief interruptions this decision accepts, and it does not shorten a release. The existing tools stay.

## Consequences

- Pre-release checks should be cut to what is fast. Measured on November 5, 2026, a routine release took 142 seconds, of which 118 were checks and build.
- Undo must be fast and always available, because it is the only safety net.
- This decision should be revisited if a company's volume grows to where minutes of downtime cost real sales.
