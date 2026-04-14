  # Tcl Toolchain

  - State: scaffold-only next-20 prep
  - Toolchain source: `brew`

  ## Planned commands after promotion
    - `brew install tcl-tk`
- `export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"`
- `tclsh <<< 'puts [info patchlevel]'`

  ## Scaffold-time checks
  - `python3 scripts/validate_scaffold.py`
  - `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' flake lock`

  ## Current limitation
  - Use Brew Tcl/Tk, not the system Tcl 8.5 runtime.
