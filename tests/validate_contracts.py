#!/usr/bin/env python3
"""Static checks for Orchestration candidate references; not runtime acceptance."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "skills" / "orchestration" / "references"
NAMES = ["COMMANDS.md", "RESOLVER.md", "STORAGE.md", "MIGRATION.md", "RELEASE.md", "EVIDENCE.md"]
INTENTS = [
    "PROJECT_BOOTSTRAP", "BRANCH_LIST", "BRANCH_CREATE", "BRANCH_RESUME",
    "BRANCH_CLOSURE_CRITERIA", "BRANCH_ARCHIVE", "BRANCH_RESTORE",
    "SELF_ARCHIVE_PREPARE", "PROJECT_UPGRADE", "VERSION_CHECK",
    "INDEPENDENT_AUDIT", "HANDOFF", "STATUS_READ", "HELP",
]

def main():
    for name in NAMES:
        assert (REF / name).is_file(), f"missing reference: {name}"
    docs = {name: (REF / name).read_text(encoding="utf-8") for name in NAMES}
    rows = [line.split("|")[1].strip().strip("`") for line in docs["COMMANDS.md"].splitlines() if line.startswith("| `")]
    assert rows == INTENTS, f"14 semantic intents mismatch: {rows!r}"
    assert "Strictly read-only" in docs["COMMANDS.md"]
    assert "Explicit monitoring opt-in" in docs["COMMANDS.md"]
    assert "LOCAL_PROTOCOL_UNRESOLVED" in docs["RESOLVER.md"]
    assert "0.3.0" in docs["RESOLVER.md"] and "0.4.0" in docs["RESOLVER.md"]
    assert "history/" in docs["STORAGE.md"] and "atomic" in docs["STORAGE.md"]
    assert "marker LAST" in docs["MIGRATION.md"]
    assert "explicit owner approval" in docs["RELEASE.md"]
    assert "separate non-author agent/context" in docs["RELEASE.md"]
    assert all(f"| D{i:02d} |" in docs["STORAGE.md"] for i in range(1, 26))
    assert all(f"| S{i} " in docs["RELEASE.md"] for i in range(1, 7))
    assert "CONVERSATION_NOT_LOADED" in docs["EVIDENCE.md"]
    assert "DELIVERY_UNKNOWN" in docs["EVIDENCE.md"]
    assert "SUBMITTED" in docs["EVIDENCE.md"]
    assert "Deterministic multi-marker" in docs["RESOLVER.md"]
    assert docs["COMMANDS.md"].count("| BRANCH_ARCHIVE |") == 1
    print("PASS: 14 intents, 25 roles, S1-S6, 6 references, 15 static checks")
    print("NOT_VERIFIED: runtime behavior, Library move, independent audit")

if __name__ == "__main__":
    main()
