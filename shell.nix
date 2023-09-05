{ pkgs ? import <nixpkgs> {} }:

let
  myPythonEnv = pkgs.python310.withPackages(ps: [
    ps.numpy
    ps.pandas
    ps.networkx
    # ... otros paquetes de Python que puedas necesitar
  ]);
in
pkgs.mkShell {
  buildInputs = [
    myPythonEnv
    # ... otras dependencias que puedas necesitar
  ];
}
