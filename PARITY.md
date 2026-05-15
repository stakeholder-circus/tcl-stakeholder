# Tcl Parity

- Role: local-only full-parity target in the next-20 wave
- Parity class: deterministic-first full-parity

## Current coverage
- Exact CLI support for deterministic extensions: `--list-values`, `--focus-family`, `--output-format text|json`, and `--seed`.
- Normalized-equivalent JSON events include stable sequence, synthetic timestamp, family, protocol, schemaRef, generationProvenance, and context.
- Same-seed JSON stability is enforced by `scripts/validate_scaffold.py` and `tests/cli.test`.
- Classic six families and modern-core families have dedicated Tcl descriptors.
- Later families are intentionally grouped under a fallback descriptor with explicit traceability.

## Intentional fail-fast
- `--experimental-provider` always exits non-zero in this tranche because live-provider execution is outside deterministic parity.

## Promotion prerequisites
- Native and Docker validation green.
- Later-family dedicated generator tranche complete or explicitly accepted as grouped fallback.
- Publication/governance wave complete and remote access available.
