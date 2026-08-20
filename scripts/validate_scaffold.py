#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'AI_DISCLOSURE.md', 'PARITY.md', 'GAPS.md', 'AGENTS.md', 'LICENSE',
    'bin/tcl-stakeholder', 'lib/stakeholder_cli.tcl', 'tests/cli.test',
    'docs/remotes.md', 'docs/provenance.md', 'docs/toolchain.md', 'docs/tooling.md',
    'docs/traceability/README.md', 'docs/traceability/first-push-families.md',
    '.githooks/commit-msg', '.githooks/pre-push', '.github/CODEOWNERS',
    '.github/PULL_REQUEST_TEMPLATE.md', '.github/dependabot.yml',
    '.github/workflows/actionlint.yml', '.github/workflows/dependency-review.yml',
    '.github/workflows/ci-native.yml', '.github/workflows/docker-smoke.yml',
    '.github/workflows/sast.yml', 'flake.nix', 'Dockerfile', 'flake.lock',
]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=check)


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        raise SystemExit('missing scaffold files: ' + ', '.join(missing))
    tclsh = shutil.which('tclsh')
    if not tclsh:
        raise SystemExit('tclsh not found; install Tcl 8.6+ or use nix develop')
    values = run([tclsh, 'bin/tcl-stakeholder', '--list-values', '--output-format', 'json']).stdout
    parsed = json.loads(values)
    for family in ['code-analyzer', 'system-monitoring', 'agent-workflows', 'finops-capacity']:
        if family not in parsed['generatorFamilies']:
            raise SystemExit(f'missing family from list-values: {family}')
    one = run([tclsh, 'bin/tcl-stakeholder', '--output-format', 'json', '--seed', '99', '--complexity', 'high']).stdout
    two = run([tclsh, 'bin/tcl-stakeholder', '--output-format', 'json', '--seed', '99', '--complexity', 'high']).stdout
    if one != two:
        raise SystemExit('same-seed JSON output is not stable')
    for line in one.splitlines():
        json.loads(line)
    focused = run([tclsh, 'bin/tcl-stakeholder', '--output-format', 'json', '--seed', '1', '--focus-family', 'network-activity']).stdout
    if '"family":"network-activity"' not in focused:
        raise SystemExit('focus-family did not constrain output')
    failed = run([tclsh, 'bin/tcl-stakeholder', '--experimental-provider', 'openai'], check=False)
    if failed.returncode == 0 or 'explicit fail-fast' not in failed.stdout:
        raise SystemExit('experimental provider did not fail fast')
    tests = run([tclsh, 'tests/cli.test']).stdout
    if 'Failed' in tests and 'Failed\t0' not in tests and 'Failed 0' not in tests:
        raise SystemExit(tests)
    print('tcl-stakeholder validation passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
