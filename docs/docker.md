# Tcl Docker

## Build and test
```bash
docker build -t tcl-stakeholder .
docker run --rm tcl-stakeholder --list-values --output-format json
docker run --rm tcl-stakeholder --focus-family network-activity --output-format json --seed 42
```

## Rationale
- The image installs Tcl and Python, runs native validation during build, and exposes the Tcl CLI as the entrypoint.
