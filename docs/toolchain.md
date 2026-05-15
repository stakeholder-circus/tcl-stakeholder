# Tcl Toolchain

- Runtime: Tcl 8.6+ via `tclsh`
- Validation: Python 3 plus Tcl `tcltest`
- Preferred macOS install: `brew install tcl-tk`

## Native commands
```bash
tclsh <<< 'puts [info patchlevel]'
python3 scripts/validate_scaffold.py
tclsh tests/cli.test
```

## Nix commands
```bash
nix develop
nix run .#check
nix run . -- --list-values --output-format json
```

## Docker commands
```bash
docker build -t tcl-stakeholder .
docker run --rm tcl-stakeholder --list-values --output-format json
```
