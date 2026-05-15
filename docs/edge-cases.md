# Tcl Edge Cases

- Same-seed JSON output must be byte-stable for deterministic arguments.
- `--focus-family` constrains activity events to one family.
- `--duration 0` means run until interrupted; validation uses finite durations.
- `--experimental-provider` fails fast and never calls a live provider.
- Empty `--framework` is allowed and omitted from JSON context.
- Text output is intentionally plain so terminal color differences do not affect parity.
