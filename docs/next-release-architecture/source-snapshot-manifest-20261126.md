# Development source snapshot manifest — NOT a protocol release

Snapshot commit: `7d635a8c129a93b45b7f2c38ecc35ee72fc03e8c`
Source: `ilyasclick/orchestration` feature branch `next-release-architecture-20261125`
Purpose: reproducible source review of PR #8 after first remediation, not STABLE promotion.
Status: DEVELOPMENT_SNAPSHOT / RELEASE_NOT_READY / CANONICAL_LIBRARY_SAVE_BLOCKED

| Order | File | UTF-8 bytes | SHA-256 |
|---:|---|---:|---|
| 1 | `skills/orchestration/SKILL.md` | 5681 | `0c17925aab579b0fadf5ba0c964d3d4a1248146e775aa6cabefa689da031078e` |
| 2 | `skills/orchestration/references/COMMANDS.md` | 6128 | `cb1d674a2365bb63e59fe760161291e16eaf9a023dbc6f877e1bb12210c8b2ad` |
| 3 | `skills/orchestration/references/RESOLVER.md` | 4206 | `db948a49628e52842f4578df6cb4910e8070c826e0ba32d08fb63733cec0f610` |
| 4 | `skills/orchestration/references/STORAGE.md` | 5665 | `23a508d33bb5813daafcc1e53cb872ab6575b45f12e1eab51ba6461b042eacde` |
| 5 | `skills/orchestration/references/MIGRATION.md` | 2175 | `2ecd793fdbf4261b00e0b72ce744a66cd6a5472d82528c9fd1af0ff49682c527` |
| 6 | `skills/orchestration/references/RELEASE.md` | 3837 | `edb334638449efbe6cbe495cd65a2bf2a5edd378845b1d7d053d378f6eb7615c` |
| 7 | `skills/orchestration/references/EVIDENCE.md` | 4014 | `4f4ee96fa00127ab9f0166820c03a3db7280940c1acfbf298fe1e78688efba67` |
| 8 | `tests/validate_contracts.py` | 2131 | `bb8d63fca7eb4fd15c143b72d39e3212cc042ce38e30bde92ba5e192830a786a` |
| 9 | `tests/test_candidate_model.py` | 5162 | `27ef7782f8d65093115275d7f97b56697bd5612ba40c865af54dc77cb7e490e7` |

Digest input: UTF-8 concatenation of `path + "\\n" + lowercase SHA-256 + "\\n"` for each row in **the exact numbered order above**, with no other separators. SHA-256 of digest input:
`1bc065894abf8d06c6b49accfd0a406aaa8164fc382a1f83c659951411e6bb2b`.

The hashes were computed over exact UTF-8 text returned by GitHub fetch_file at the pinned commit and validated against the known SHA-256 test vector "abc". Git blob SHAs are a separate hash type. This manifest does not include itself, docs, or workflow files and is not a complete protocol payload or Library manifest.

Static CI and 16 isolated reference-model fixtures do not establish real Library moves, installed host routing, source-project remediation, or independent auditor identity. F02/F04/F05/F06/F09 remain blocking; owner approval remains required.
