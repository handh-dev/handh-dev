# Local H&H software delivery

Status: implemented and production-qualified on November 5, 2026.
Tracking: https://github.com/handh-dev/handh-infra/issues/99

## Outcome

A routine Bubba website change should reach healthy production in approximately
60 seconds on a prepared workstation. GitHub stores source and reviews; local
commands own checks, artifact production and releases. No paid hosted Actions,
new CI server, human approval gate, or per-release helper source patch is required.
Shane clarified on November 5 that one minute is a target, not a hard limit or
release gate. Finish functional delivery and report measured timing rather than
extending optimization indefinitely.
A target is not a measured result. Record cold, warm, prepared and total times
separately. Never hide required preparation outside the change-to-live clock.

## Ownership and boundaries

- handh-dev owns this shared policy and architecture description.
- handh-infra owns generic Rust verification and administration mechanics.
- bubbas-mono owns maintained Bubba source, application checks and its existing
  ops/web-release adapter. Its pinned H&H interfaces remain compatible.
- Core retains business rules/data; Website releases must not rebuild, restart,
  migrate or modify Core, HQ, Bulk, Social, Studio or unrelated services.
- Keep AWS, ECR, OpenTofu and Compose. Preserve URLs, permissions, real data,
  artwork rights, existing release receipts and known-good recovery artifacts.
- Existing provider authentication is required; never bypass identity checks,
  expose credentials, or invent success if a provider is inaccessible.

## User interface

Use project-owned commands for checks, release, status and rollback. Existing
command names may remain as compatible aliases. One release invocation must
prepare missing inputs, verify, publish, activate and check the result. Prepared
artifacts may be reused only when their source, build inputs and tools match.
Noninteractive errors explain the failed stage and safe next step; no embedded
approval prompts. An agent and a human invoke the same commands.

## Verification contract

1. Fast checks during development; exact clean committed source for release.
2. Plain non-executable documentation gets light validation. Known isolated
   components get their complete relevant checks. Shared code, lockfiles,
   recipes, CI and unknown paths select the full applicable checks.
3. Include deletions and renames. Generated/executable documentation is code.
4. Record source SHA, base, commands, tool identity, pass/fail and elapsed time.
   Missing, interrupted, dirty or changed-source results cannot produce success.
5. Verify final merged source, or prove its release input tree is identical to
   the tested tree. Never carry an earlier branch's green status to changed code.
6. Native platform distribution qualification is separate from an ordinary
   Website release. Do not claim Windows support was tested on a Mac.
7. Infrastructure validation includes both isolated, backend-disabled OpenTofu
   configurations, recursive format, router, Compose and Linux host contracts.

## Artifacts and performance

Build once and deploy the exact tested digest. Image layers separate stable
runtime/dependencies from application output. Do not rebuild siblings for a
Website-only change. Warm caches include toolchain, platform, lockfiles and
relevant source/configuration identity; correctness takes precedence over hits.

Initial routine-change budget: checks/build 30s, publication 10s, activation and
public verification 20s. Report cache misses, upload time, queue/lock waits and
health time explicitly. Cold installs, migrations, dependency upgrades and full
infrastructure validation are separate measured classes, not falsely fast paths.
Keep caches bounded; delete task-owned temporary outputs. Registry retention
must protect current and compatible rollback images.

## Reusable release admission

Replace the need to compile a new hard-coded source/image allowlist entry for
every Website change with a reusable qualified release record. Admission must
still bind source/input identity, tested image digest, expected predecessor,
Core compatibility and target configuration. Source and image strings supplied
by a caller alone are not evidence. Retain legacy receipts and recovery paths.
Reject altered artifacts, stale predecessors/targets and unqualified changes.

## Deployment and recovery

Serialize writers on the production host. Recheck target and predecessor under
the lock before mutation. Use bounded checks and durable transaction state so
interruptions cannot silently mark a release healthy. Prefer ready-before-switch
where supported; record any existing availability limitation accurately.
After activation check the actual public website and its Core proxy contract.
Failures return nonzero and restore the previous compatible artifact or leave
an explicit recoverable state. A rollback never rebuilds or restores production
data; incompatible schema transitions require their own migration procedure.

## Implementation and acceptance

First inspect current main and the live release owner; preserve active checkouts.
Implement vertical slices with failing-first tests at public boundaries:
verification CLI scope/failure reporting; artifact/source admission; deployment
lock, stale-target refusal, health failure and recovery. Reuse existing fixtures.
Run focused tests during implementation and the applicable full suite at the end.
Obtain separate automated standards and specification reviews; fix findings.
Commit, publish truthful exact-head statuses, merge and verify final source.

Completion requires:
- documented working local commands and no hosted Actions dependency;
- reliable checks and identity-bound reusable release admission;
- real publication, activation and compatible rollback/recovery qualification;
- a real routine Website change measured end to end, with the 60-second target
  either met or explicitly reported as a remaining performance improvement;
- unchanged unrelated services/data, and task-owned disposable outputs removed.

No application feature redesign, broad monorepo migration, new paid services,
DNS/mail changes or wholesale native-platform rewrite belongs to this work.

## Observed acceptance — November 5, 2026

The shared policy, infrastructure verification and Bubba release adapter landed
in handh-dev PR3, handh-infra PR100, and bubbas-mono PR156/158. Bubba PR159
added a deployed-revision field to readiness responses for the routine benchmark.

- Full local qualification passed: Rust tests/Clippy, build/types/unit tests,
  catalog and metadata audits, browser journeys, editing/staff/owner checks,
  unavailable-Core behavior and isolated-fixture cleanup.
- A real Website-only release of `1ecdc56d92ac0eb5cb2cc36146cae97d5286affb`
  completed in **141.817 seconds**: preparation 117.859s (including 16.611s
  bootstrap), publication 3.956s, activation/readback 20.001s. This was a real
  source change with a warm dependency/toolchain cache, not an activation-only
  measurement. The small endpoint contract test also ran before merge.
- The preceding full-scope rollout completed in 208.721 seconds.
- Real rollback to the prior compatible Website completed in 18.86 seconds.
  The final rollout restored forward progress; production is on the new source.
- Core and 17 other containers retained their identities, images and start times.
  `handh-email` also changed during the measurement window; this Website-only
  workflow performed no email deployment. The initial deployment/rollback check
  had preserved all 19 other containers.
- Linux host and native Mac ARM64 verification passed. Windows was not qualified
  on this workstation. Crash-recovery and drift refusal were exercised by tests;
  no production crash injection is claimed.

One minute remains an improvement target, not a hard limit. No further speed
work is required for this delivery. Existing single-container replacement can
briefly interrupt Website requests. Temporary task outputs are removed; signing
configuration, the installed host helper and deployed/rollback records remain.
