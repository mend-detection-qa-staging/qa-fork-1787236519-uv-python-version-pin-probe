# uv-python-version-pin-probe

## Probe Metadata

| Field | Value |
|---|---|
| Pattern | `python-version-pin` |
| Generator | uv test-project generator |
| Generated | 2026-04-29T10:26:17 |
| Target | remote |
| Python version | 3.10.2 (pinned via `.python-version` and `requires-python = "==3.10.2"`) |

## Purpose

Minimal probe targeting Mend SCA detection of a uv project with an exact Python
version pin. Tests whether Mend correctly identifies the dependency tree when
the project uses `requires-python = "==3.10.2"` and a `.python-version` file
both containing the same exact version.

## Direct Dependencies

| Package | Version |
|---|---|
| requests | 2.31.0 |
| click | 8.1.7 |

## Transitive Dependencies

| Package | Version | Required by |
|---|---|---|
| certifi | 2026.4.22 | requests |
| charset-normalizer | 3.4.7 | requests |
| idna | 3.13 | requests |
| urllib3 | 2.6.3 | requests |
| colorama | 0.4.6 | click (Windows only) |

## Expected Dependency Tree

See `expected-tree.json` for the full expected tree structure.