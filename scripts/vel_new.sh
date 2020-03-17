#!/bin/bash

A=$1
B=$2

# change the value to 1E-6 for 8,16,32 ppds, and set it to 1E-7 for 64ppd

awk 'NR ==1{old = $8; next} {print $1*1E-7,($8-old)/1E-4; old = $8}' $A/droplet_results.dat > ./data

sed -e '1i\
0.0 0.0' data > data1 

rm data 

awk '{print $0}' data1 > vel_data_$B


exit 1
