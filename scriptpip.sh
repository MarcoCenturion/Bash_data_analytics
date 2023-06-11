#!/bin/bash
set -e

 # Set PY_MAJ and PY_MIN with your own python "major.minor" version
 # Example for python 3.8
 # PY_MAJ='3'
 # PY_MIN='8'
 cd /usr/lib/python${PY_MAJ}.${PY_MIN}/site-packages/ \
 && rm -rf pip/ \
 && rm -rf pip-*/ \
 ; cd -