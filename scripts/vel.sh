#!/bin/bash

A=$1

awk 'NR ==1{old = $8; next} {print $1*1E-7,($8-old)/1E-4; old = $8}' $A/droplet_results.dat > ./data

sed -e '1i\
0.0 0.0' data > data1 

rm data 

awk '{print $1, 0.5*996.57*$2*$2*(14.137166)*10**(-9)}' data1 > ke_data


exit 1
