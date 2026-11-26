# Incident, execution and delivery evidence — candidate S1/S4/S5

This reference is a proposed protocol rule. It does not repair source systems or authorize monitoring or external communication.

## S1: incident identity and acceptance

- Canonicalize one primary incident per independently distinct failure family. Link addenda, observations, reviews, recovery reports and closure records; do not count each file as a separate incident.
- Every row must include `incident_id`, `source_project`, `source_branch`, `owner`, `severity`, `source_reported_status`, `independently_verified_status`, `evidence_refs`, `measurable_postcondition`, `next_action`, `disposition`, and `checked_at`. Unknowns must be `NOT_NAMED` or `UNVERIFIED`, not inferred.
- A source-system technical incident is not closed by a documentation-only reconciliation or an archived historical cohort. Preserve original evidence and append new events; do not overwrite prior observations.
- Cross-project evidence is referenced by exact pointer only unless the source project's authorization explicitly permits reading. An incident does not grant remediation rights.
- Historical snapshot: 18-Nov C1 read 79 direct incident files and grouped 52 incident/limitation families plus 2 observations; later counts and postconditions require fresh Library evidence. The 23-Nov 96 incident files count is a different snapshot, not a new family count.

## S5: state and proof

Use distinct evidence levels:

```text
PLANNED → SCHEDULED → QUEUED → LAUNCHED → EXECUTED → SUBMITTED → DELIVERED → ACCEPTED → REMEDIATED
```

This is a vocabulary, **not** a guarantee every workflow passes through all stages. `SCHEDULED` means scheduler receipt, not a run. `QUEUED` means durable queue item, not send. `LAUNCHED` means process or automation began, not finished. `EXECUTED` means action completed with verifiable result, not necessarily external submission. `SUBMITTED` means provider/host accepted the action with a unique receipt. `DELIVERED` needs destination-visible readback or authoritative delivery receipt. `ACCEPTED` needs the relevant downstream acceptance. `REMEDIATED` requires the source incident's measurable postcondition.

`CONVERSATION_NOT_LOADED` is an **unknown**, never `READBACK_CONFIRMED_NO_SUBMISSION`. `DELIVERY_UNKNOWN` is fail-closed: reconcile exact target, existing Task ID, unique post-submit marker and history before retry. Do not create a new Task ID or re-send until non-delivery is proven; after proven non-delivery use a fresh Task ID and append-only intent. Preserve an idempotency key and per-item cursor for partially executed batches. Never replay confirmed sends, archives or irreversible operations.

For external messages: validate the exact recipient identity and provenance, target, subject, full body and attachments, scope of owner authorization, and post-submit readback. A second send does not undo a wrong-recipient disclosure. Never claim recall without proof.

## S4: monitoring opt-in

Default: no new recurring Automation, background polling or scheduled follow-up for "fix", "finish", "check now", "wait for support", or a generic handoff. Do the permitted one-time check and report blockers. A specific owner request to monitor must name target, cadence, stop condition and permitted actions. Preserve existing user-authorized Automations and production cron; stopping an unauthorized monitor does not resolve its underlying incident. A `VERSION_CHECK` is a one-time check unless separately authorized as recurring.

## Acceptance gates

- T01–T04: incident family, addenda, independent postconditions and delivery-state distinctions
- T12–T16: monitoring negative/positive cases and preservation of existing schedules
- T21–T23: unloaded conversation, unknown retry and wrong-recipient controls
- M01–M05: only after an authorized isolated test matrix is enumerated and linked to exact run receipts

Text review or CI string checks alone do not prove these guards run in a host.
