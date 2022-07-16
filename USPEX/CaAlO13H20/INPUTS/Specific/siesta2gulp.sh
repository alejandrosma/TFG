#!/bin/bash

a=$(sed '5q;d' STRUC | tr -s " " | cut -d " " -f 2)
b=$(sed '6q;d' STRUC | tr -s " " | cut -d " " -f 3)
c=$(sed '7q;d' STRUC | tr -s " " | cut -d " " -f 4)

cat goptions > input_gulp.in
echo "cell" >> input_gulp.in
echo $a $b $c "90.0 90.0 90.0" >> input_gulp.in
echo "fractional" >> input_gulp.in
awk 'NR==11, NR==45' STRUC | awk '{ print $4" "$1" "$2" "$3 }' | sed 's/^1/Ca/' | sed 's/^2/Al/' | sed 's/^3/O /' | sed 's/^4/H /' | awk '{ print $1" core "$2" "$3" "$4 }' >> input_gulp.in
echo " " >> input_gulp.in

cat ginput >> input_gulp.in

