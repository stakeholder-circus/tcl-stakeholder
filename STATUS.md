# tcl-stakeholder Status

- Role: local-only Tcl parity target
- Parity class: deterministic-first full-parity target
- State: native-validated local deterministic tranche
- Rewrite completeness: 49%
- Functionality completeness: 39%
- Branch: `main`
- Origin: `git@github.com:stakeholder-circus/tcl-stakeholder.git`
- Upstream: `https://github.com/giacomo-b/rust-stakeholder`

## Implemented
- Tcl CLI runtime in `bin/tcl-stakeholder` and `lib/stakeholder_cli.tcl`.
- `--list-values`, `--focus-family`, `--output-format text|json`, `--seed`, `--trace`, and parity baseline flags.
- Dedicated deterministic descriptors for classic six plus modern-core families.
- Grouped fallback for post-modern-core families.
- Explicit `--experimental-provider` fail-fast.
- Native validation script, Tcl tests, Dockerfile, Nix flake, and CI workflows.

## Evidence
- `python3 scripts/validate_scaffold.py`
- `tclsh tests/cli.test`
- `tclsh bin/tcl-stakeholder --list-values --output-format json`
- same-seed deterministic JSON diff for `platform-engineering`
- explicit `--experimental-provider local-demo` fail-fast smoke

## Remaining
- Dedicated later-family generators.
- Cross-repo fixture comparison against `stakeholder-core` once the workspace parity gate assigns this repo.
- Publication/governance wave and remote wiring.
