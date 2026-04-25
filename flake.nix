{
  description = "Open Ortho Terminology — FHIR terminology resources for orthodontics";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python311;
      in {
        devShells.default = pkgs.mkShell {
          packages = [
            python
            pkgs.stdenv.cc  # needed by some pip wheels (e.g. pydantic-core)
          ];

          shellHook = ''
            if [ ! -d .venv ]; then
              echo "Creating virtual environment..."
              ${python}/bin/python -m venv .venv
            fi
            source .venv/bin/activate
            pip install -e . build twine --quiet
          '';
        };
      }
    );
}
