import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit

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
                                        
                      
fig = plt.figure(figsize=(6, 6))

column = 2
time = 10

ax = fig.add_subplot(111) 
ax.set_title('Momentum consistent (MC) vs. Momentum non-consistent (NON)')
ax.plot(stats1_mc[1:,0]*1e3, stats1_mc[1:,column], color='red', marker = 's', markersize = 2.0 , linewidth=1.0, label=r'MC : $D/\Delta x = 8$' )
ax.plot(stats2_mc[1:,0]*1e3, stats2_mc[1:,column], color='blue', marker = 's', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 16$' )
ax.plot(stats3_mc[1:,0]*1e3, stats3_mc[1:,column], color='green', marker = 's', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 32$' )
ax.plot(stats4_mc[1:,0]*1e3, stats4_mc[1:,column], color='black', marker = 's', markersize = 2.0, linewidth=1.0, label=r'MC : $D/\Delta x = 64$' )

ax.plot(stats1_non[1:,0]*1e3, stats1_non[1:,column], color='red', marker = 'x', markersize = 6.0 , linewidth=1.0, label=r'NON : $D/\Delta x = 8$' )
ax.plot(stats2_non[1:,0]*1e3, stats2_non[1:,column], color='blue', marker = 'x', markersize = 6.0, linewidth=1.0, label=r'NON : $D/\Delta x = 16$' )
ax.plot(stats3_non[1:,0]*1e3, stats3_non[1:,column], color='green', marker = 'x', markersize = 6.0, linewidth=1.0, label=r'NON : $D/\Delta x = 32$' )
ax.plot(stats4_non[1:,0]*1e3, stats4_non[1:,column], color='black', marker = 'x', markersize = 6.0, linewidth=1.0, label=r'NON : $D/\Delta x = 64$' )

plt.ylabel(r'Global Momentum along flow direction')
plt.xlabel(r'Time ($\times 10^{-3}$ s)')
plt.xlim(left = 0, right = time)
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