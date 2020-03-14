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

drift1_mc = np.loadtxt('./ke_8ppd_mc', comments = '#')
drift2_mc = np.loadtxt('./ke_16ppd_mc', comments = '#')
drift3_mc = np.loadtxt('./ke_32ppd_mc', comments = '#')
drift4_mc = np.loadtxt('./ke_64ppd_mc', comments = '#')  

drift1_non = np.loadtxt('./ke_8ppd_non', comments = '#')
drift2_non = np.loadtxt('./ke_16ppd_non', comments = '#')
drift3_non = np.loadtxt('./ke_32ppd_non', comments = '#')
drift4_non = np.loadtxt('./ke_64ppd_non', comments = '#')                        
                                        
                      
fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(211) 
ax.set_title('Momentum consistent (MC) vs. Momentum non-consistent (NON)')
ax.plot(iner1_mc[:,0]*1e-3, iner1_mc[:,1], color='red', marker = 's', markersize = 3.0 , linewidth=1.0, label=r'MC : $D/\Delta x = 8$' )
ax.plot(iner2_mc[:,0]*1e-3, iner2_mc[:,1], color='blue', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 16$' )
ax.plot(iner3_mc[:,0]*1e-3, iner3_mc[:,1], color='green', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 32$' )
ax.plot(iner4_mc[:,0]*1e-4, iner4_mc[:,1], color='black', marker = 's', markersize = 3.0, linewidth=1.0, label=r'MC : $D/\Delta x = 64$' )

ax.plot(iner1_non[:,0]*1e-3, iner1_non[:,1], color='red', marker = '^', markersize = 4.0 , linewidth=1.0, label=r'NON : $D/\Delta x = 8$' )
ax.plot(iner2_non[:,0]*1e-3, iner2_non[:,1], color='blue', marker = '^', markersize = 4.0, linewidth=1.0, label=r'NON : $D/\Delta x = 16$' )
ax.plot(iner3_non[:,0]*1e-3, iner3_non[:,1], color='green', marker = '^', markersize = 4.0, linewidth=1.0, label=r'NON : $D/\Delta x = 32$' )
ax.plot(iner4_non[:,0]*1e-3, iner4_non[:,1], color='black', marker = '^', markersize = 4.0, linewidth=1.0, label=r'NON : $D/\Delta x = 64$' )

plt.ylabel(r'Droplet Moment of Inertia ($I_{xx}$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 4)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
plt.legend(fontsize = '13')
plt.grid()



ax2 = fig.add_subplot(212)
ax2.set_title('Momentum consistent method')
ax2.plot(iner1_mc[:,0]*1e-3, iner1_mc[:,1], color='red', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 8$' )
ax2.plot(iner2_mc[:,0]*1e-3, iner2_mc[:,1], color='blue', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 16$' )
ax2.plot(iner3_mc[:,0]*1e-3, iner3_mc[:,1], color='green', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 32$' )
ax2.plot(iner4_mc[:,0]*1e-4, iner4_mc[:,1], color='black', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 64$' )

plt.ylabel(r'Droplet Moment of Inertia ($I_{xx}$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 10)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
#plt.ylim(top = 6e-5, bottom = 4e-5)
plt.legend(fontsize = '12')
plt.grid()
plt.show()