# Tcl Tooling

## Commands
- `python3 scripts/validate_scaffold.py`
- `tclsh tests/cli.test`
- `tclsh bin/tcl-stakeholder --output-format json --seed 42`
- `docker build -t tcl-stakeholder .`
- `docker run --rm tcl-stakeholder --list-values --output-format json`

## Notes
- Tcl has no formatter or static analyzer in this repo baseline.
- Deterministic normalized JSON is the quality gate.
- CI covers native Tcl validation and Docker smoke validation.
