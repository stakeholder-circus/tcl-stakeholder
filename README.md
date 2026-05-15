> [!WARNING]
> This repository is AI-assisted and manually reviewed. It is a local-only Tcl parity target until publication governance completes.

# tcl-stakeholder

Deterministic-first Tcl CLI port of the stakeholder terminal simulation.

## Status
- Tranche C implementation target: deterministic `classic-six + modern-core`.
- Dedicated Tcl descriptors exist for the classic six families and modern-core families.
- Later families use an explicit grouped fallback descriptor until their dedicated tranche lands.
- Live/experimental provider execution is intentionally fail-fast via `--experimental-provider`.

## Run
```bash
tclsh bin/tcl-stakeholder --list-values --output-format json
tclsh bin/tcl-stakeholder --output-format json --seed 42 --focus-family network-activity
tclsh bin/tcl-stakeholder --project hospital-ocpp --framework "mcp grpc" --team --trace --seed 11
```

## CLI contract
Required parity flags are supported: `--dev-type`, `--jargon`, `--complexity`, `--duration`, `--alerts`, `--project`, `--minimal`, `--team`, and `--framework`.

Deterministic extensions are supported: `--list-values`, `--focus-family`, `--output-format text|json`, `--seed`, `--no-color`, and `--trace`.

`--experimental-provider PROVIDER` exits non-zero with an explicit fail-fast message.

## Validation
```bash
python3 scripts/validate_scaffold.py
tclsh tests/cli.test
docker build -t tcl-stakeholder .
docker run --rm tcl-stakeholder --list-values --output-format json
```

## Documentation
- [STATUS.md](STATUS.md)
- [PARITY.md](PARITY.md)
- [GAPS.md](GAPS.md)
- [docs/toolchain.md](docs/toolchain.md)
- [docs/tooling.md](docs/tooling.md)
- [docs/traceability/first-push-families.md](docs/traceability/first-push-families.md)
