# Tcl Experimental Surface

Live-provider execution is not implemented in Tranche C. Passing `--experimental-provider PROVIDER` exits non-zero with a clear fail-fast message.

This keeps deterministic JSON fixtures independent from provider availability, credentials, network latency, and model output drift.
