import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}",r'\boldmath']
params = {'backend': 'pdf',
        'text.usetex' : True,
        "font.serif": [],
        'font.size' : 12,
        'legend.fontsize': 10,
        'legend.fancybox' : True, 
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'lines.linewidth': 2.0,
        'lines.markersize' : 8,
        'axes.linewidth' : 1.5,
        'axes.labelsize' : 12,
        'grid.linestyle' : ':',
        'grid.linewidth' : 1.2, 
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
                        
velocity_gnuplot = [2.89042, 7.08403, 5.7005, 5.82924]
error_gnuplot = [11.1]                

vel_8 =  np.loadtxt('../scripts/8_data_vel')
vel_16 = np.loadtxt('../scripts/16_data_vel')
vel_32 = np.loadtxt('../scripts/32_data_vel')
vel_64 = np.loadtxt('../scripts/64_data_vel')                      

def fit_line(x,A,B):
    return ( A*x + B )

popt_8,  pcov_8  = curve_fit(fit_line, xdata=vel_8[:,0], ydata=vel_8[:,1])
popt_16, pcov_16 = curve_fit(fit_line, xdata=vel_16[:,0], ydata=vel_16[:,1])
popt_32, pcov_32 = curve_fit(fit_line, xdata=vel_32[:,0], ydata=vel_32[:,1])
popt_64, pcov_64 = curve_fit(fit_line, xdata=vel_64[:,0], ydata=vel_64[:,1])


acceleration = [popt_8[0],popt_16[0],popt_32[0],popt_64[0]]
err_8 = np.sqrt(np.diag(pcov_8))
err_16= np.sqrt(np.diag(pcov_16))
err_32= np.sqrt(np.diag(pcov_32))
err_64= np.sqrt(np.diag(pcov_64))

error_acc = [err_8[0],err_16[0],err_32[0],err_64[0]]
ppd = np.array([8,16,32,64])


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111) 
ax.set_title('Momentum consistent (MC)')
ax.plot(vel_8[:,0]*1e3 , vel_8[:,1], color='red', marker = 'x', markersize = 2.0 , linewidth=1.0, label=r'MC : $D/\Delta x = 8$' )
ax.plot(vel_16[:,0]*1e3, vel_16[:,1], color='blue', marker = 'x', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 16$' )
ax.plot(vel_32[:,0]*1e3, vel_32[:,1], color='green', marker = 'x', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 32$' )
ax.plot(vel_64[:,0]*1e3, vel_64[:,1], color='black', marker = 'x', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 64$' )
plt.ylabel(r'Droplet Velocity')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = 5)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
plt.legend(fontsize = '13')
plt.grid()


ax2 = fig.add_axes([0.6, 0.6, 0.36, 0.33])
#l , caps , c = ax2.errorbar(ppd, acceleration, yerr=error_acc, uplims=True, lolims=True, fmt='o', capthick= 1.5, linewidth = 1.5)
ax2.errorbar(ppd, acceleration, yerr=error_acc, uplims=True, lolims=True, fmt='o', capthick= 1.5, linewidth = 1.5)

#for cap in caps:
#    cap.set_marker("_")



plt.ylabel(r'Droplet Acceleration')
plt.xlabel(r'Resolution')
plt.xlim(left = 0, right = 5)
plt.xticks(fontsize = '14')
plt.yticks(fontsize = '14')
plt.legend(fontsize = '13')
plt.grid()



# =============================================================================
# ax2 = fig.add_subplot(212)
# ax2.set_title('Momentum consistent method')
# ax2.plot(stats1_mc[1:,0]*1e3, stats1_mc[1:,8], color='red', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 8$' )
# ax2.plot(stats2_mc[1:,0]*1e3, stats2_mc[1:,8], color='blue', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 16$' )
# ax2.plot(stats3_mc[1:,0]*1e3, stats3_mc[1:,8], color='green', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 32$' )
# ax2.plot(stats4_mc[1:,0]*1e3, stats4_mc[1:,8], color='black', marker = 'o', markersize = 3.0 , linewidth=1.0, label=r'$D/\Delta x = 64$' )
# 
# plt.ylabel(r'Global Momentum along flow direction')
# plt.xlabel(r'Time ($\times 10^{-3}$ s)')
# plt.xlim(left = 0, right = 10)
# plt.xticks(fontsize = '14')
# plt.yticks(fontsize = '14')
# #plt.ylim(top = 6e-5, bottom = 4e-5)
# plt.legend(fontsize = '12')
# plt.grid()
# =============================================================================
plt.show()