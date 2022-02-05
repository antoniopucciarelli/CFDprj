#####################################################################
# LAB05|06 -- COMPUTATIONAL TECHNIQUES FOR THEMOCHEMICAL PROPULSION #
# ------------------------------------------------------------------# 
#   PLOTTING DATA FOR FINAL REPORT                                  #  
#   1 -- GETTING DATA FROM FILES:                                   #
#        combustorSprayWallReitzKHRT                                #
#        combustorSprayWallReitzDiwakar                             #
#        combustorSprayWallReitzKHRT450                             #
#                                                                   #    
#   2 -- PLOTTING DATA:                                             #
#       1 residuals                                                 #                  
#           [combustorSprayWallReitzKHRT]                           #
#           [combustorSprayWallReitzDiwakar]                        #
#           [combustorSprayWallReitzKHRT450]                        #
#                                                                   #    
#       2 95% liquid phase -- jet property                          #
#           [combustorSprayWallReitzKHRT]                           #
#           [combustorSprayWallReitzDiwakar]                        #
#           [combustorSprayWallReitzKHRT450]                        #
#                                                                   #
#       3 particles diameter histogram                              #
#           [combustorSprayWallReitzKHRT]                           #
#           [combustorSprayWallReitzDawakar]                        #
#           [combustorSprayWallReitzKHRT450]                        #
#                                                                   #
#       4 wall film height                                          #
#           [combustorSprayWallReitzKHRT]                           #
#           [combustorSprayWallReitzDiwakar]                        #
#           [combustorSprayWallReitzKHRT450]                        #
#####################################################################

# importing libraries 
from os import TMP_MAX
import matplotlib
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
#       95% liquid phase                                           #
#       particles diameter                                         #
#       wall film height                                           #
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

# naming storing variables and working variables
tmax                = 0.1
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
combustor_mainPATH = ['../combustorSprayWallFilmReitzKHRT/', '../combustorSprayWallFilmReitzDiwakar/', '../combustorSprayWallFilmReitzKHRT450/'] # combustorSprayWallFilm folders array 
figTitle = [r'$\mathtt{reactingFoam}_{ReitzKHRT}$', r'$\mathtt{reactingFoam}_{ReitzDiwakar}$', r'$\mathtt{reactingFoam}_{ReitzKHRT450}$']

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       1 residuals                                                # 
#------------------------------------------------------------------#
figRes, ax0 = plt.subplots(len(combustor_mainPATH),1)
figRes.set_size_inches(w=W, h=H)

for ii in range(len(combustor_mainPATH)):
    # getting data for combustorSimple 
    # residuals
    combustor_residuals = np.loadtxt(combustor_mainPATH[ii] + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=3)
    
    # residuals plot
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,1], '-', label=r'$p$',           linewidth=2)
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
    ax0[ii].semilogy(combustor_residuals[:,0], combustor_residuals[:,6], '-', label=r'$h$',           linewidth=2)
    ax0[ii].set_xticks(np.arange(0, 0.105, 0.02))
    ax0[ii].set_xlim(0, tmax)
    ax0[ii].set_xlabel(r'time $[s]$')
    ax0[ii].set_ylabel(r'residual')
    ax0[ii].set_title(figTitle[ii] + '\nresiduals')
    ax0[ii].minorticks_on
    ax0[ii].grid(True, which='both', linestyle='--')
    ax0[ii].legend(bbox_to_anchor=(1,1), loc='upper left')

# saving figure in LaTeX format
figRes.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab0506/residuals.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       2 95% liquid phase                                         # 
#------------------------------------------------------------------#
figPhase, ax1 = plt.subplots(len(combustor_mainPATH),1)
figPhase.set_size_inches(w=W, h=H)

for ii in range(len(combustor_mainPATH)):
    # getting 95% liquid phase from log.reactionFoam
    # data declaration 
    timeCheck        = 'deltaT = '
    convergenceCheck = 'Liquid penetration 95% mass (m) ='
    # file check
    with open(combustor_mainPATH[ii] + phase, 'r') as FILE:
        line     = FILE.readline()
        timeVec  = []
        phaseVec = []

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

    ax1[ii].set_xlim(0, tmax)
    ax1[ii].grid(True, linestyle='--')
    ax1[ii].plot(timeVec, phaseVec, linewidth=2)
    ax1[ii].set_xlabel(r'time $[s]$')
    ax1[ii].set_ylabel(r'95% liquid penetration mass $[kg]$')
    ax1[ii].set_title(figTitle[ii] + '\n95% liquid penetration')
    ax1[ii].set_xticks(np.arange(0, 0.105, 0.02))
    ax1[ii].set_ylim(0,)

# saving figure in LaTeX format
figPhase.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab0506/phase95.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       3 diameter                                                 # 
#------------------------------------------------------------------#
figDiam, ax2 = plt.subplots(len(combustor_mainPATH),1)
figDiam.set_size_inches(w=W, h=H)

# setting particles diameter
# variables declaration 
time = ['0.08', '0.05', '0.02'] # plotting time -- homeWork.pdf 
alfa = np.array([1, 0.5, 0.5])  # histogram properties -> fading
BINS = 50                       # histogram properties -> bins number4
bins = [1e-04, 5e-05, 5e-05]    # histogram properties -> x ticks properties
 
# axis properties
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))

for kk in range(len(combustor_mainPATH)):
    print('\n' + combustor_mainPATH[kk])
    ax2[kk].set_title(figTitle[kk] + '\nparcels particles diameter histrogram')
    ax2[kk].set_xlabel('particles diameter' + r' [m]')
    ax2[kk].set_ylabel('number of parcels' + r' [-]')
    ax2[kk].grid(True, linestyle='--')
    ax2[kk].yaxis.set_major_formatter(mticker.FuncFormatter(g))
    ax2[kk].xaxis.set_major_formatter(mticker.FuncFormatter(g))

    for ii,tt in enumerate(time):
        print('time = ' + tt + ' s')
        totDIAM = []
        for procNum in range(4):
            if exists(combustor_mainPATH[kk] + 'processor' + str(int(procNum)) + '/' + tt + diameter):
                with open(combustor_mainPATH[kk] + 'processor' + str(int(procNum)) + '/' + tt + diameter, 'r') as FILE:
                    print('\tprocessor #', procNum)
                    lines = FILE.readlines()

                    # number of particles for processor
                    dim  = int(lines[17])
                    DIAM = np.zeros((dim)) 

                    for jj in range(dim):
                        DIAM[jj] = float(lines[19 + jj])

                    totDIAM = np.append(totDIAM, DIAM)

        _, x, _=ax2[kk].hist(totDIAM, bins=BINS, alpha=alfa[ii], label=tt + ' s', edgecolor='black', rwidth=0.9, linestyle='solid')
        ax2[kk].legend(loc='upper right')
        ax2[kk].set_xlim(0,)
        ax2[kk].set_xticks(np.arange(0, max(x)+max(x)/5, bins[kk]))

# saving figure in LaTeX format
figDiam.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab0506/diam.pgf', bbox_inches='tight')