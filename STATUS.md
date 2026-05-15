# tcl-stakeholder Status

- Role: local-only Tcl parity target
- Parity class: deterministic-first full-parity target
- State: Tranche C implemented, validation pending per change
- Rewrite completeness: 45%
- Functionality completeness: 35%
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

## Remaining
- Dedicated later-family generators.
- Cross-repo fixture comparison against `stakeholder-core` once the workspace parity gate assigns this repo.
- Publication/governance wave and remote wiring.
