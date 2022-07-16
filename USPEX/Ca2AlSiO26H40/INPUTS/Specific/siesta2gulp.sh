#!/bin/bash
#Coger los vectores de celda
a=$(sed '5q;d' STRUC | tr -s " " | cut -d " " -f 2)
b=$(sed '6q;d' STRUC | tr -s " " | cut -d " " -f 3)
c=$(sed '7q;d' STRUC | tr -s " " | cut -d " " -f 4)

#Copiar opciones de gulp al input de gulp
cat goptions > input_gulp.in
echo "cell" >> input_gulp.in
echo $a $b $c "90.0 90.0 90.0" >> input_gulp.in
echo "fractional" >> input_gulp.in
awk 'NR==11, NR==80' STRUC | awk '{ print $4" "$1" "$2" "$3 }' | sed 's/^1/Ca/' | sed 's/^2/Al/' | sed 's/^3/Si /' | sed 's/^4/O /' | sed 's/^5/H /'| awk '{ print $1" core "$2" "$3" "$4 }' >> input_gulp.in
echo " " >> input_gulp.in

cat ginput >> input_gulp.in

