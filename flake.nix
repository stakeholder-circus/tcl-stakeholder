{
  description = "tcl-stakeholder deterministic Tcl CLI";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: builtins.listToAttrs (map (system: { name = system; value = f system; }) systems);
    in {
      packages = forAllSystems (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.writeShellApplication {
            name = "tcl-stakeholder";
            runtimeInputs = [ pkgs.tcl ];
            text = ''
              exec ${pkgs.tcl}/bin/tclsh ${self}/bin/tcl-stakeholder "$@"
            '';
          };
          check = pkgs.writeShellApplication {
            name = "check";
            runtimeInputs = [ pkgs.python3 pkgs.tcl ];
            text = ''
              python3 scripts/validate_scaffold.py
            '';
          };
        });
      apps = forAllSystems (system: {
        default = { type = "app"; program = "${self.packages.${system}.default}/bin/tcl-stakeholder"; };
        check = { type = "app"; program = "${self.packages.${system}.check}/bin/check"; };
      });
      devShells = forAllSystems (system:
        let pkgs = import nixpkgs { inherit system; };
        in { default = pkgs.mkShell { packages = [ pkgs.tcl pkgs.python3 ]; }; });
    };
}
