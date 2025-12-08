{
  lib,
  python3,
}:

python3.pkgs.buildPythonApplication rec {
  pname = "ldifj";
  version = "0.1.1";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = [
    python3.pkgs.setuptools
    python3.pkgs.setuptools-scm
    python3.pkgs.wheel
  ];

  propagatedBuildInputs = with python3.pkgs; [
    python-ldap
    rich
    rich-argparse
  ];

  pythonImportsCheck = [ "ldifj" ];

  meta = with lib; {
    description = "LDAP LDIF to JSON";
    homepage = "https://pypi.org/project/ldifj/";
    license = licenses.gpl3Only;
    maintainers = with maintainers; [ pschmitt ];
    mainProgram = "ldifj";
  };
}
