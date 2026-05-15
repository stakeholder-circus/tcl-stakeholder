# Tcl Language Specialties

- The implementation uses Tcl 8.6 core features only.
- JSON is emitted by a small deterministic encoder to avoid package dependencies.
- Tests use the standard `tcltest` package.
- The scheduler uses a local LCG so same-seed behavior does not depend on Tcl build details.
