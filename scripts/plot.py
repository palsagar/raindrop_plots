import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit

plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}",r'\boldmath']
params = {'backend': 'pdf',
        'text.usetex' : True,
        "font.serif": [],
        'font.size' : 14,
        'legend.fontsize': 16,
        'legend.fancybox' : True, 
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'lines.linewidth': 2.0,
        'lines.markersize' : 8,
        'axes.linewidth' : 1.5,
        'axes.labelsize' : 16,
        'grid.linestyle' : ':',
        'grid.linewidth' : 1.2, 
        'text.latex.unicode': True
          }

plt.rcParams.update(params)

stats1_mc = np.loadtxt('./8ppd/mc/stats', comments = '#')
stats2_mc = np.loadtxt('./16ppd/mc/stats', comments = '#')                    
stats3_mc = np.loadtxt('./32ppd/mc/stats', comments = '#')
stats4_mc = np.loadtxt('./64ppd/mc/stats', comments = '#')
  
iner1_mc = np.loadtxt('./8ppd/mc/inertia_data.dat', comments = '#')
iner2_mc = np.loadtxt('./16ppd/mc/inertia_data.dat', comments = '#')                    
iner3_mc = np.loadtxt('./32ppd/mc/inertia_data.dat', comments = '#')
iner4_mc = np.loadtxt('./64ppd/mc/inertia_data.dat', comments = '#')                       
                        
                       
stats1_non = np.loadtxt('./8ppd/non_mc/stats', comments = '#')
stats2_non = np.loadtxt('./16ppd/non_mc/stats', comments = '#')                    
stats3_non = np.loadtxt('./32ppd/non_mc/stats', comments = '#')
stats4_non = np.loadtxt('./64ppd/non_mc/stats', comments = '#')                       

iner1_non = np.loadtxt('./8ppd/non_mc/inertia_data.dat', comments = '#')
iner2_non = np.loadtxt('./16ppd/non_mc/inertia_data.dat', comments = '#')                    
iner3_non = np.loadtxt('./32ppd/non_mc/inertia_data.dat', comments = '#')
iner4_non = np.loadtxt('./64ppd/non_mc/inertia_data.dat', comments = '#') 

fig = plt.figure(figsize=(8, 10))

ax = fig.add_subplot(211) 
ax.set_title('Momentum consistent (MC) vs. Momentum non-consistent (NON)')
ax.plot(stats1_mc[:,0]*1000.0, stats1_mc[:,12]  , color='red', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'MC : $D/\Delta x = 8$' )
ax.plot(stats2_mc[:,0]*1000.0, stats2_mc[:,12] , color='blue', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 16$' )
ax.plot(stats3_mc[:,0]*1000.0, stats3_mc[:,12] , color='green', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 32$' )
ax.plot(stats4_mc[:,0]*1000.0, stats4_mc[:,12] , color='black', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 64$' )

ax.plot(stats1_non[:,0]*1000.0, stats1_non[:,12]*1e7  , color='red', marker = '^', markersize = 3.0 , linewidth=1.0, label=r'NON : $D/\Delta x = 8$' )
ax.plot(stats2_non[:,0]*1000.0, stats2_non[:,12]*1e7 , color='blue', marker = '^', markersize = 3.0, linewidth=1.0, label=r'NON : $D/\Delta x = 16$' )
ax.plot(stats3_non[:,0]*1000.0, stats3_non[:,12]*1e7 , color='green', marker = '^', markersize = 3.0, linewidth=1.0, label=r'NON : $D/\Delta x = 32$' )
ax.plot(stats4_non[:,0]*1000.0, stats4_non[:,12]*1e7 , color='black', marker = '^', markersize = 3.0, linewidth=1.0, label=r'NON : $D/\Delta x = 64$' )
plt.ylabel(r'Droplet Kinetic Energy ($\times 10^{-7}$ Kg.m/$s^2$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 4)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
plt.legend(fontsize = '13')
plt.grid()
#ax2 = fig.add_axes([0.65, 0.67, 0.3, 0.25])
ax2 = fig.add_subplot(212)
ax2.set_title('Momentum consistent method')
ax2.plot(stats1_mc[:,0]*1000.0, stats1_mc[:,12]*1e7  , color='red', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 8$' )
ax2.plot(stats2_mc[:,0]*1000.0, stats2_mc[:,12]*1e7 , color='blue', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 16$' )
ax2.plot(stats3_mc[:,0]*1000.0, stats3_mc[:,12]*1e7 , color='green', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 32$' )
ax2.plot(stats4_mc[:,0]*1000.0, stats4_mc[:,12]*1e7 , color='black', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 64$' )


#plt.plot(stats3_non[:,0]*1000.0, stats3_non[:,12] , color='green', linewidth=2.0, marker= '^',label=r'$D/\Delta x = 32$' )
plt.ylabel(r'Droplet Kinetic Energy ($\times 10^{-7}$ Kg.m/$s^2$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 10)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
#plt.ylim(top = 6e-5, bottom = 4e-5)
plt.legend(fontsize = '12')
plt.grid()
plt.show()