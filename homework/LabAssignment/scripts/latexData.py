#####################################################################
# LAB07 -- COMPUTATIONAL TECHNIQUES FOR THEMOCHEMICAL PROPULSION    #
# ------------------------------------------------------------------# 
#   PLOTTING DATA FOR FINAL REPORT                                  #  
#   1 -- GETTING DATA FROM FILES:                                   #
#        combustorReactingFoam                                      #
#                                                                   #    
#   2 -- PLOTTING DATA:                                             #
#       1 residuals                                                 #                  
#           [combustorReactingFoam]                                 #
#                                                                   #    
#       2 [inlet, outlet] average pressure and temperature          #
#           [combustorReactingFoam]                                 #
#                                                                   #
#####################################################################

# importing libraries 
import matplotlib
from os import TMP_MAX
from   matplotlib        import gridspec
import matplotlib.pyplot as plt 
import numpy             as np
from os.path             import exists
import matplotlib.ticker as mticker

#------------------------------------------------------------------#
#   GETTING DATA FROM FILES:                                       #
#   FROM OPENFOAM INTERNAL LIBRARIES                               #
#       residuals:                                                 #
#           PRESSURE                                    -- p       #
#           VELOCITY                                    -- Ux | Uy #
#           TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- K       #
#           DISSIPATION RATE         nu  * < sij  sij > -- EPSILON #
#           ENTHALPY                                    -- h       #
#           CONCENTRATIONS                              -- C7H16   #     
#                                                       -- CO2     #
#                                                       -- H2O     #
#                                                       -- O2      #
#       [inlet, outlet] average pressure and temperature           #
#------------------------------------------------------------------#

# setting matplotlib LaTeX export 
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# pgf plot size 
W = 5      # width
H = 8      # height

# combustor
combustor_residuals = []
combustor_phase     = []
combustor_WH        = []

# setting data folder 
WH        = 'wallHeight directory'                     # wall height data
phase     = 'log.reactingFoam'                         # phase       data
diameter  = '/lagrangian/cloud/d'                      # diameter    data
residuals = 'postProcessing/residuals/0/residuals.dat' # residuals   data
# setting variable folder for each case 
combustor_mainPATH = ['../combustorRhoPimple/', '../combustorReactingFoam/']   
figTitle           = [r'$\mathtt{rhoPimpleFoam}$', r'$\mathtt{reactingFoam}$']

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       1 residuals                                                # 
#------------------------------------------------------------------#
figRes, ax0 = plt.subplots(len(combustor_mainPATH), 1)
figRes.set_size_inches(w=W, h=H)

# getting data for combustorRhoPimple 
# residuals
combustor_residuals = np.loadtxt(combustor_mainPATH[0] + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=3)

# residuals plot
# combustorRhoPimple 
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,1], '-', label=r'$p$',           linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,6], '-', label=r'$h$',           linewidth=2)
ax0[0].set_xticks(np.arange(0, 0.0505, 0.01))
ax0[0].set_xlim(0, 0.05)
ax0[0].set_xlabel(r'time $[s]$')
ax0[0].set_ylabel(r'residual')
ax0[0].set_title(figTitle[0] + '\nresiduals')
ax0[0].minorticks_on
ax0[0].grid(True, which='both', linestyle='--')
ax0[0].legend(bbox_to_anchor=(1,1), loc='upper left')

# getting data for combustorReactingFoam 
# residuals
combustor_residuals = np.loadtxt(combustor_mainPATH[1] + residuals, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), skiprows=3)

# residuals plot
# combustorReactingFoam 
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,1], '-', label=r'$p$',           linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,6], '-', label=r'$h$',           linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,7], '-', label=r'$C_7 H_{16}$',  linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,8], '-', label=r'$CO_2$',        linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,9], '-', label=r'$H_2O$',        linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,10], '-', label=r'$O_2$',        linewidth=2)
ax0[1].set_xticks(np.arange(0, 0.105, 0.02))
ax0[1].set_xlim(0, 0.1)
ax0[1].set_xlabel(r'time $[s]$')
ax0[1].set_ylabel(r'residual')
ax0[1].set_title(figTitle[1] + '\nresiduals')
ax0[1].minorticks_on
ax0[1].grid(True, which='both', linestyle='--')
ax0[1].legend(bbox_to_anchor=(1,1), loc='upper left')

# saving figure in LaTeX format
figRes.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/labAssignment/residuals.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       2 95% liquid phase                                         # 
#------------------------------------------------------------------#
figTot = plt.figure()
figTot.set_size_inches(w=W, h=H)

# figure setting
grid = plt.GridSpec(ncols=1, nrows=3, hspace=0.6)

# subplot setup
liquidPhase = figTot.add_subplot(grid[0])
liquidPhase.set_axis_off()

# create subgrid for two subplots without space between them
gs = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=grid[0])

# axes setup
ax1 = figTot.add_subplot(gs[0])

# getting 95% liquid phase from log.reactionFoam
# data declaration 
timeCheck        = 'deltaT = '
convergenceCheck = 'Liquid penetration 95% mass (m) ='
# file check
with open(combustor_mainPATH[1] + phase, 'r') as FILE:
    line     = FILE.readline()
    timeVec  = []
    phaseVec = [0]

    while line:

        #tCheck = timeCheck in line 

        if timeCheck in line: 
            line    = FILE.readline()
            time    = line.rsplit('=')[1]
            time    = float(time.rsplit('\n')[0])
            timeVec = np.append(timeVec, time) 
        
        #convCheck = convergenceCheck in line
        
        if convergenceCheck in line: 
            combustor_phase = line.rsplit('=')[1]
            combustor_phase = float(combustor_phase.split('\n')[0])
            phaseVec        = np.append(phaseVec, combustor_phase)

        line = FILE.readline()

ax1.set_xlim(0, 0.1)
ax1.grid(True, linestyle='--')
ax1.plot(timeVec, phaseVec, linewidth=2)
ax1.set_xlabel(r'time $[s]$')
ax1.set_ylabel(r'95\% liquid penetration mass $[kg]$')
ax1.set_title(figTitle[1] + '\n95% liquid penetration')
ax1.set_xticks(np.arange(0, 0.105, 0.02))
ax1.set_ylim(0,)

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       3 diameter                                                 # 
#------------------------------------------------------------------#
# subplot setup
diam = figTot.add_subplot(grid[1])
diam.set_axis_off()

# create subgrid for two subplots without space between them
gs = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=grid[1])

# axes setup
ax2 = figTot.add_subplot(gs[0])

# setting particles diameter
# variables declaration 
time = ['0.05', '0.02']         # plotting time -- homeWork.pdf 
alfa = np.array([1, 1, 1])      # histogram properties -> fading
BINS = 50                       # histogram properties -> bins number

# axis properties
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))

ax2.set_title(figTitle[1] + '\nparcels particles diameter histrogram')
ax2.set_xlabel('particles diameter' + r' [m]')
ax2.set_ylabel('number of parcels' + r' [-]')
ax2.grid(True, linestyle='--')
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(g))
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(g))

for ii,tt in enumerate(time):
    print('time = ' + tt + ' s')
    totDIAM = []
    for procNum in range(4):
        if exists(combustor_mainPATH[1] + 'processor' + str(int(procNum)) + '/' + tt + diameter):
            with open(combustor_mainPATH[1] + 'processor' + str(int(procNum)) + '/' + tt + diameter, 'r') as FILE:
                print('\tprocessor #', procNum)
                lines = FILE.readlines()

                # number of particles for processor
                dim  = int(lines[17])
                DIAM = np.zeros((dim)) 

                for jj in range(dim):
                    DIAM[jj] = float(lines[19 + jj])

                totDIAM = np.append(totDIAM, DIAM)

    _, x, _ = ax2.hist(totDIAM, bins=BINS, alpha=alfa[ii], label=tt + ' s', edgecolor='black', rwidth=0.9, linestyle='solid')
    ax2.set_xticks(np.arange(0, max(x)+5e-05, 5e-05))
    #ax2.legend(bbox_to_anchor=(1,1), loc='upper left')
    ax2.legend(loc='upper right')

ax2.set_xlim(0,)

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       4 [inlet, outlet] average pressure and temperature         # 
#------------------------------------------------------------------#

# figure setup
InOut = figTot.add_subplot(grid[2])
InOut.set_axis_off()

# create subgrid for two subplots without space between them
gs = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=grid[2], wspace=0.4)

# axes setup
ax = figTot.add_subplot(gs[0])

file = ['postProcessing/InletAve/', 'postProcessing/OutletAve/']
pLab = [r'$p_{Inlet}$', r'$p_{Outlet}$']
TLab = [r'$T_{Inlet}$', r'$T_{Outlet}$']
name = '/surfaceFieldValue.dat'
time = ['0', '0.01', '0.02', '0.03', '0.04', '0.05']#, '0.06', '0.07', '0.08', '0.09']

for ii in range(len(file)):
    combustor_pressure = np.zeros((len(time), 2))
    for jj,t in enumerate(time):
        combustor_pressure[jj, :] = np.loadtxt(combustor_mainPATH[1] + file[ii] + t + name, usecols=(0, 1), skiprows=4)
    
    ax.plot(combustor_pressure[:,0], combustor_pressure[:,1], label=pLab[ii])

ax.grid(True, linestyle='--')
ax.legend()
ax.set_xticks(np.arange(0, 0.11, 0.02))
ax.set_xlabel('time [s]')
ax.set_ylabel('pressure [Pa]')
ax.set_title(r'$\mathtt{reactingFoam}$' + '\npressure average')
ax.set_xlim(0,0.09)

# axes setup
ax = figTot.add_subplot(gs[1])

for ii in range(len(file)):
    combustor_temperature = np.zeros((len(time), 2))
    for jj,t in enumerate(time):
        combustor_temperature[jj, :] = np.loadtxt(combustor_mainPATH[1] + file[ii] + t + name, usecols=(0, 2), skiprows=4)
        
    ax.plot(combustor_temperature[:,0], combustor_temperature[:,1], label=TLab[ii])

ax.grid(True, linestyle='--')
ax.legend(loc='upper right')
ax.set_xticks(np.arange(0, 0.11, 0.02))
ax.set_xlabel('time [s]')
ax.set_ylabel('temperature [K]')
ax.set_title(r'$\mathtt{reactingFoam}$' + '\ntemperature average')
ax.set_xlim(0,0.09)

plt.savefig('../../../thermochemicalCFD/latexFIGS/labAssignment/figTot.pgf', bbox_inches='tight')