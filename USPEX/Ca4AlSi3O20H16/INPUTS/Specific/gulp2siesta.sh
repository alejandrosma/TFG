#!/bin/bash

head -n 79 input.fdf > input_siesta.fdf

tail -n +3 out.xyz | sed 's/Ca/1 /' | sed 's/Al/2 /' | sed 's/Si /3 /' | sed 's/O /4 /' | sed 's/H /5 /'| awk '{ print $2" "$3" "$4" "$1 }' >> input_siesta.fdf

tail -n 6 input.fdf >> input_siesta.fdf

sed -i 's/Fractional/Ang/' input_siesta.fdf

mv input_siesta.fdf input.fdf
