# Contributing to tcl-stakeholder

## Rules
- Treat Rust plus `stakeholder-core` as the behavioral source-of-truth.
- Use Conventional Commits.
- Do not land silent behavioral changes; update traceability and gap docs in the same tranche.
- Keep deterministic seeded JSON stable unless the change is documented as baseline evolution.

## Local workflow
```bash
python3 scripts/validate_scaffold.py
tclsh tests/cli.test
docker build -t tcl-stakeholder .
docker run --rm tcl-stakeholder --list-values --output-format json
```

## Change discipline
- Dedicated family additions must update docs, tests, and traceability.
- Experimental provider work must stay separated from deterministic parity paths.
- Preserve the upstream MIT license notice.
