{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.python-ldap
    pkgs.python3Packages.rich
    pkgs.python3Packages.rich-argparse
    pkgs.python3Packages.black
    pkgs.python3Packages.ipython
    pkgs.openssl # For SSL/TLS support, might be required by some Python packages
  ];

  # shellHook = ''
  #   echo "Environment prepared. You can now run your Python scripts."
  # '';
}
