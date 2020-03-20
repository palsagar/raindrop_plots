import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit

plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}",r'\boldmath']
params = {'backend': 'pdf',
        'text.usetex' : True,
        "font.serif": [],
        'font.size' : 10,
        'legend.fontsize': 8,
        'legend.fancybox' : True, 
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'lines.linewidth': 1.0,
        'lines.markersize' : 3,
        'axes.linewidth' : 1.0,
        'axes.labelsize' : 10,
        'grid.linestyle' : ':',
        'grid.linewidth' : 1.0, 
        'text.latex.unicode': True
          }

plt.rcParams.update(params)

stats1_mc = np.loadtxt('../8ppd/mc/stats', comments = '#')
stats2_mc = np.loadtxt('../16ppd/mc/stats', comments = '#')                    
stats3_mc = np.loadtxt('../32ppd/mc/stats', comments = '#')
stats4_mc = np.loadtxt('../64ppd/mc/stats', comments = '#')
  
iner1_mc = np.loadtxt('../8ppd/mc/inertia_data.dat', comments = '#')
iner2_mc = np.loadtxt('../16ppd/mc/inertia_data.dat', comments = '#')                    
iner3_mc = np.loadtxt('../32ppd/mc/inertia_data.dat', comments = '#')
iner4_mc = np.loadtxt('../64ppd/mc/inertia_data.dat', comments = '#')                       
                        
                       
stats1_non = np.loadtxt('../8ppd/non_mc/stats', comments = '#')
stats2_non = np.loadtxt('../16ppd/non_mc/stats', comments = '#')                    
stats3_non = np.loadtxt('../32ppd/non_mc/stats', comments = '#')
stats4_non = np.loadtxt('../64ppd/non_mc/stats', comments = '#')                       

iner1_non = np.loadtxt('../8ppd/non_mc/inertia_data.dat', comments = '#')
iner2_non = np.loadtxt('../16ppd/non_mc/inertia_data.dat', comments = '#')                    
iner3_non = np.loadtxt('../32ppd/non_mc/inertia_data.dat', comments = '#')
iner4_non = np.loadtxt('../64ppd/non_mc/inertia_data.dat', comments = '#') 

drift1_mc = np.loadtxt('./ke_8ppd_mc', comments = '#')
drift2_mc = np.loadtxt('./ke_16ppd_mc', comments = '#')
drift3_mc = np.loadtxt('./ke_32ppd_mc', comments = '#')
drift4_mc = np.loadtxt('./ke_64ppd_mc', comments = '#')  

drift1_non = np.loadtxt('./ke_8ppd_non', comments = '#')
drift2_non = np.loadtxt('./ke_16ppd_non', comments = '#')
drift3_non = np.loadtxt('./ke_32ppd_non', comments = '#')
drift4_non = np.loadtxt('./ke_64ppd_non', comments = '#')                        
                                        
                      
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(221) 
ax.plot(iner1_mc[:,0]*1e-3, iner1_mc[:,1] , color='red', marker = 'x',  label=r'$D/h = 8$' , markevery = 4)
ax.plot(iner2_mc[:,0]*1e-3, iner2_mc[:,1], color='blue', marker = 's',  label=r'$D/h = 16$' , markevery = 4)
ax.plot(iner3_mc[:,0]*1e-3, iner3_mc[:,1], color='green', marker = 'o', label=r'$D/h = 32$' , markevery = 4)
ax.plot(iner4_mc[:,0]*1e-4, iner4_mc[:,1], color='black', marker = '^', label=r'$D/h = 64$' , markevery = 4)

plt.ylabel(r'Droplet Moment of Inertia ($I_{xx}$)', fontsize = 10)
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 10.0)
plt.xticks()
plt.yticks()
plt.legend()
plt.grid()



ax2 = fig.add_subplot(222)
ax2.plot(iner1_mc[:,0]*1e-3, iner1_mc[:,2] , color='red', marker = 'x', label=r'$D/h = 8$' , markevery = 4)
ax2.plot(iner2_mc[:,0]*1e-3, iner2_mc[:,2], color='blue', marker = 's', label=r'$D/h = 16$' , markevery = 4)
ax2.plot(iner3_mc[:,0]*1e-3, iner3_mc[:,2], color='green', marker = 'o', label=r'$D/h = 32$' , markevery = 4)
ax2.plot(iner4_mc[:,0]*1e-4, iner4_mc[:,2], color='black', marker = '^', label=r'$D/h = 64$' , markevery = 4)

plt.ylabel(r'Droplet Moment of Inertia ($I_{yy}$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 10.0)
plt.xticks()
plt.yticks()
plt.legend()
plt.grid()


ax3 = fig.add_subplot(223)
ax3.plot(stats1_mc[:,0]*1000.0, stats1_mc[:,12] - drift1_mc[:,1], color='red', marker = 'x', label=r'$D/h = 8$' , markevery = 2)
ax3.plot(stats2_mc[:,0]*1000.0, stats2_mc[:,12] - drift2_mc[:,1], color='blue', marker = 's', label=r'$D/h = 16$' , markevery = 2 )
ax3.plot(stats3_mc[:,0]*1000.0, stats3_mc[:,12] - drift3_mc[:,1], color='green', marker = 'o', label=r'$D/h = 32$' , markevery = 2 )
ax3.plot(stats4_mc[:,0]*1000.0, stats4_mc[:,12] - drift4_mc[:,1], color='black', marker = '^', label=r'$D/h = 64$'  , markevery = 2)

plt.ylabel(r'Droplet Kinetic Energy (Kg.$m^{2}$/$s^2$)')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 5.1)
plt.ylim(bottom = 0, top = 6e-7)
plt.xticks()
plt.yticks()
plt.legend()
plt.grid()



ax4 = fig.add_subplot(224)
ax4.plot(stats1_mc[:,0]*1000.0, 1e6*(stats1_mc[:,10]-stats1_mc[0,10])/stats1_mc[0,10] , color='red', marker = 'x', label=r'$D/h = 8$' , markevery = 2)
ax4.plot(stats2_mc[:,0]*1000.0, 1e6*(stats2_mc[:,10]-stats2_mc[0,10])/stats2_mc[0,10] , color='blue', marker = 's', label=r'$D/h = 16$' , markevery = 2 )
ax4.plot(stats3_mc[:,0]*1000.0, 1e6*(stats3_mc[:,10]-stats3_mc[0,10])/stats2_mc[0,10] , color='green', marker = 'o', label=r'$D/h = 32$' , markevery = 2 )
ax4.plot(stats4_mc[:,0]*1000.0, 1e6*(stats4_mc[:,10]-stats4_mc[0,10])/stats2_mc[0,10] , color='black', marker = '^', label=r'$D/h = 64$'  , markevery = 2)

plt.ylabel(r'Change in Droplet Mass ($\times 10^{-4} $ \% )')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 5.1)
plt.ylim(bottom = -2.0, top =2.0)
plt.xticks()
plt.yticks()
plt.legend()
plt.grid()



# =============================================================================
# ax2 = fig.add_subplot(212)
# ax2.set_title('Momentum consistent method')
# ax2.plot(stats1_mc[:,0]*1000.0, stats1_mc[:,12]*1e7 - drift1_mc[:,1]*1e7, color='red', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 8$' )
# ax2.plot(stats2_mc[:,0]*1000.0, stats2_mc[:,12]*1e7 - drift2_mc[:,1]*1e7, color='blue', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 16$' )
# ax2.plot(stats3_mc[:,0]*1000.0, stats3_mc[:,12]*1e7 - drift3_mc[:,1]*1e7, color='green', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 32$' )
# ax2.plot(stats4_mc[:,0]*1000.0, stats4_mc[:,12]*1e7 - drift4_mc[:,1]*1e7, color='black', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 64$' )
# 
# plt.ylabel(r'Droplet Kinetic Energy ($\times 10^{-7}$ Kg.$m^{2}$/$s^2$)')
# plt.xlabel(r'Time ($\times 10^{-3}$ s)')
# plt.xlim(left = 0, right = 10)
# plt.xticks(fontsize = 12)
# plt.yticks(fontsize = 12)
# #plt.ylim(top = 6e-5, bottom = 4e-5)
# plt.legend(fontsize = 12)
# plt.grid()
# =============================================================================
plt.show()