# First-push families for tcl-stakeholder

## Classic six dedicated families
- `src/generators/code_analyzer.rs` -> `lib/stakeholder_cli.tcl` `code-analyzer`: normalized-equivalent dedicated descriptor.
- `src/generators/data_processing.rs` -> `lib/stakeholder_cli.tcl` `data-processing`: normalized-equivalent dedicated descriptor.
- `src/generators/jargon.rs` -> `lib/stakeholder_cli.tcl` `jargon`: normalized-equivalent dedicated descriptor.
- `src/generators/metrics.rs` -> `lib/stakeholder_cli.tcl` `metrics`: normalized-equivalent dedicated descriptor.
- `src/generators/network_activity.rs` -> `lib/stakeholder_cli.tcl` `network-activity`: normalized-equivalent dedicated descriptor with `grpc` protocol.
- `src/generators/system_monitoring.rs` -> `lib/stakeholder_cli.tcl` `system-monitoring`: normalized-equivalent dedicated descriptor.

## Modern-core dedicated families
- `agent-workflows`, `ai-inference-ops`, `platform-engineering`, `supply-chain-security`, `observability-ai-runtime`, `delivery-preview-ops`, `evaluation-and-guardrails`, `knowledge-retrieval`, `edge-client-runtime`, `identity-and-trust`, `aibom-provenance`, `agent-boundary-security`, `data-governance-compliance`, and `finops-capacity` are implemented as dedicated Tcl descriptors in `lib/stakeholder_cli.tcl`.

## Grouped fallback later families
- Post-modern-core families remain available to `--list-values` and `--focus-family` but route through an explicit grouped fallback descriptor until dedicated phrase-bank parity is assigned.
