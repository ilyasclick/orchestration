#!/usr/bin/env python3
"""Isolated reference-model fixtures, not ChatGPT Library or OrchVoice runtime tests."""
import unittest


class Blocked(Exception):
    pass


def resolve_local_pin(markers):
    by_id = {}
    for marker in markers:
        key = marker["object_id"]
        if key in by_id and by_id[key] != marker:
            raise Blocked("CONFLICTING_ALIAS")
        by_id[key] = marker
    values = list(by_id.values())
    if any(m["state"] in ("UNREADABLE", "INVALID", "PENDING") for m in values):
        raise Blocked("LOCAL_PROTOCOL_UNRESOLVED")
    active = [m for m in values if m["state"] == "CONFIRMED_ACTIVE" and m.get("receipt")]
    if len(active) != 1:
        raise Blocked("LOCAL_PROTOCOL_UNRESOLVED")
    if any(m["state"] == "CONFIRMED_ACTIVE" and not m.get("receipt") for m in values):
        raise Blocked("LOCAL_PROTOCOL_UNRESOLVED")
    return active[0]["version"]


def branch_location(active_ids, archive_ids, branch_id):
    if not branch_id or "/" in branch_id or branch_id in (".", ".."):
        raise Blocked("INVALID_BRANCH_ID")
    if branch_id in active_ids and branch_id in archive_ids:
        raise Blocked("AMBIGUOUS_BRANCH")
    if branch_id in active_ids:
        return "ACTIVE"
    if branch_id in archive_ids:
        return "ARCHIVED"
    raise Blocked("BRANCH_NOT_FOUND")


def delivery_retry_decision(loaded, task_id, post_submit_task_id, status):
    if not loaded:
        return "CONVERSATION_NOT_LOADED"
    if status == "DELIVERY_UNKNOWN":
        return "RECONCILE_FIRST"
    if status == "DELIVERED":
        return "NO_RETRY"
    if status == "READBACK_CONFIRMED_NO_SUBMISSION" and task_id == post_submit_task_id:
        return "NEW_TASK_ID_REQUIRED"
    return "BLOCKED"


def monitor_allowed(request):
    return bool(
        request.get("explicit_monitoring_request")
        and request.get("target")
        and request.get("cadence")
        and request.get("stop_condition")
        and request.get("permitted_actions")
    )


class ReferenceModelTests(unittest.TestCase):
    def test_single_confirmed_marker(self):
        self.assertEqual(resolve_local_pin([
            {"object_id": "a", "version": "0.4.3", "state": "CONFIRMED_ACTIVE", "receipt": "r"}
        ]), "0.4.3")

    def test_legacy_marker_superseded(self):
        self.assertEqual(resolve_local_pin([
            {"object_id": "old", "version": "0.3.0", "state": "HISTORICAL_SUPERSEDED"},
            {"object_id": "new", "version": "0.4.3", "state": "CONFIRMED_ACTIVE", "receipt": "r"}
        ]), "0.4.3")

    def test_multiple_active_markers_block(self):
        with self.assertRaises(Blocked):
            resolve_local_pin([
                {"object_id": "a", "version": "0.4.2", "state": "CONFIRMED_ACTIVE", "receipt": "r1"},
                {"object_id": "b", "version": "0.4.3", "state": "CONFIRMED_ACTIVE", "receipt": "r2"},
            ])

    def test_no_marker_blocks(self):
        with self.assertRaises(Blocked):
            resolve_local_pin([])

    def test_unreadable_marker_blocks(self):
        with self.assertRaises(Blocked):
            resolve_local_pin([
                {"object_id": "a", "version": "0.4.3", "state": "CONFIRMED_ACTIVE", "receipt": "r"},
                {"object_id": "b", "version": "0.4.1", "state": "UNREADABLE"}
            ])

    def test_marker_without_receipt_blocks(self):
        with self.assertRaises(Blocked):
            resolve_local_pin([
                {"object_id": "a", "version": "0.4.3", "state": "CONFIRMED_ACTIVE"}
            ])

    def test_active_branch(self):
        self.assertEqual(branch_location({"b"}, set(), "b"), "ACTIVE")

    def test_archived_branch(self):
        self.assertEqual(branch_location(set(), {"b"}, "b"), "ARCHIVED")

    def test_branch_collision_blocks(self):
        with self.assertRaises(Blocked):
            branch_location({"b"}, {"b"}, "b")

    def test_nested_branch_blocks(self):
        with self.assertRaises(Blocked):
            branch_location({"b/x"}, set(), "b/x")

    def test_unloaded_chat_never_proves_no_submission(self):
        self.assertEqual(delivery_retry_decision(False, "task1", None, "READBACK_CONFIRMED_NO_SUBMISSION"), "CONVERSATION_NOT_LOADED")

    def test_unknown_delivery_requires_reconciliation(self):
        self.assertEqual(delivery_retry_decision(True, "task1", None, "DELIVERY_UNKNOWN"), "RECONCILE_FIRST")

    def test_delivered_never_replayed(self):
        self.assertEqual(delivery_retry_decision(True, "task1", "task1", "DELIVERED"), "NO_RETRY")

    def test_confirmed_nonsubmission_uses_new_task_id(self):
        self.assertEqual(delivery_retry_decision(True, "task1", "task1", "READBACK_CONFIRMED_NO_SUBMISSION"), "NEW_TASK_ID_REQUIRED")

    def test_no_implicit_monitor(self):
        self.assertFalse(monitor_allowed({"target": "a", "cadence": "daily"}))

    def test_bounded_monitor(self):
        self.assertTrue(monitor_allowed({
            "explicit_monitoring_request": True, "target": "a",
            "cadence": "daily", "stop_condition": "date",
            "permitted_actions": ["read"]
        }))


if __name__ == "__main__":
    unittest.main()
