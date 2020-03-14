
set multiplot
set size 0.48,0.48
set origin 0.0, 0.0
set xrange[:10]
set xlabel 'Time (ms)'
set ylabel 'WallVel'
p '32ppd/non_mc/inertia_data.dat' u ($1*1e-3):8 w l lw 2 lc 'red'   t 'mc:32ppd', \
  '16ppd/non_mc/inertia_data.dat' u ($1*1e-3):8 w l lw 2 lc 'blue'  t 'mc:16ppd', \
   '8ppd/non_mc/inertia_data.dat' u ($1*1e-3):8 w l lw 2 lc 'green' t 'mc:8ppd'
 

set size 0.48,0.48
set origin 0.0,0.5
set xrange[:10]
set xlabel 'Time (ms)'
set ylabel 'Kinetic Energy'
p '32ppd/non_mc/stats' u ($1*1e3):13 w l lw 2 lc 'red'   t 'mc:32ppd', \
  '16ppd/non_mc/stats' u ($1*1e3):13 w l lw 2 lc 'blue'  t 'mc:16ppd', \
   '8ppd/non_mc/stats' u ($1*1e3):13 w l lw 2 lc 'green' t 'mc:8ppd' 
 

set size 0.48,0.48
set origin 0.5,0.0
set xrange[:10]
set xlabel 'Time (ms)'
set ylabel '% Deviation of Droplet COM'
p '32ppd/non_mc/droplet_results.dat' u ($1*1e-3):(($8 - 0.006)/0.00006) w l lw 2 lc 'red'   t 'mc:32ppd', \
  '16ppd/non_mc/droplet_results.dat' u ($1*1e-3):(($8 - 0.006)/0.00006) w l lw 2 lc 'blue'  t 'mc:16ppd', \
   '8ppd/non_mc/droplet_results.dat' u ($1*1e-3):(($8 - 0.006)/0.00006) w l lw 2 lc 'green' t 'mc:8ppd'

set size 0.48,0.48
set origin 0.5,0.5
set xrange[:10]
set xlabel 'Time (ms)'
set ylabel 'Droplet Mass'
p '32ppd/non_mc/stats' u ($1*1e3):11 w l lw 2 lc 'red'   t 'mc:32ppd', \
  '16ppd/non_mc/stats' u ($1*1e3):11 w l lw 2 lc 'blue'  t 'mc:16ppd', \
   '8ppd/non_mc/stats' u ($1*1e3):11 w l lw 2 lc 'green' t 'mc:8ppd' 

unset multiplot

pause 5
reread
