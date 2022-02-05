#####################################################################
# LAB07 -- COMPUTATIONAL TECHNIQUES FOR THEMOCHEMICAL PROPULSION    #
# ------------------------------------------------------------------# 
#   PLOTTING DATA FOR FINAL REPORT                                  #  
#   1 -- GETTING DATA FROM FILES:                                   #
#        combustorRhoPimple                                         #
#        combustorReaction                                          #
#                                                                   #    
#   2 -- PLOTTING DATA:                                             #
#       1 residuals                                                 #                  
#           [combustorRhoPimple]                                    #
#           [combustorReaction]                                     #
#####################################################################

# importing libraries 
from os import TMP_MAX
import matplotlib
import matplotlib.pyplot as plt 
import numpy             as np

#------------------------------------------------------------------#
#   GETTING DATA FROM FILES:                                       #
#   FROM OPENFOAM INTERNAL LIBRARIES                               #
#       residuals:                                                 #
#           PRESSURE                                    -- p       #
#           VELOCITY                                    -- Ux | Uy #
#           TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- K       #
#           DISSIPATION RATE         nu  * < sij  sij > -- EPSILON #
#           ENTHALPY                                    -- h       #
#           SPECIES                                     -- CH4     #
#                                                       -- CO2     #
#                                                       -- H2O     #
#                                                       -- O2      #
#                                                       -- N2      #
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
tmax                = [0.5, 0.1]
# combustor
combustor_residuals = []

# setting data folder 
residuals = 'postProcessing/residuals/0/residuals.dat' # residuals   data
# setting variable folder for each case 
combustor_mainPATH = ['../combustorRhoPimple/', '../combustorReaction/']  
figTitle           = [r'$\mathtt{rhoPimpleFoam}$', r'$\mathtt{reactingFoam}$']

#------------------------------------------------------------------#
#   PLOTTING DATA:                                                 #     
#       1 residuals                                                # 
#------------------------------------------------------------------#
figRes, ax0 = plt.subplots(len(combustor_mainPATH),1)
figRes.set_size_inches(w=W, h=H)

# combustorRhoPimple STUDY
# residuals
combustor_residuals = np.loadtxt(combustor_mainPATH[0] + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=3)

# residuals plot
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,1], '-', label=r'$p$',           linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
ax0[0].semilogy(combustor_residuals[:,0], combustor_residuals[:,6], '-', label=r'$h$',           linewidth=2)
ax0[0].set_xticks(np.arange(0, 0.505, 0.1))
ax0[0].set_xlim(0, tmax[0])
ax0[0].set_xlabel(r'time $[s]$')
ax0[0].set_ylabel(r'residual')
ax0[0].set_title(figTitle[0] + '\nresiduals')
ax0[0].minorticks_on
ax0[0].grid(True, which='both', linestyle='--')
ax0[0].legend(bbox_to_anchor=(1,1), loc='upper left')

# combustorReaction STUDY 
# residuals
combustor_residuals = np.loadtxt(combustor_mainPATH[1] + residuals, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), skiprows=3)

# residuals plot
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,1],  '-', label=r'$p$',           linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,2],  '-', label=r'$U_x$',         linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,3],  '-', label=r'$U_y$',         linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,5],  '-', label=r'$\kappa$',      linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,4],  '-', label=r'$\varepsilon$', linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,6],  '-', label=r'$h$',           linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,7],  '-', label=r'$CH_4$',        linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,8],  '-', label=r'$CO_2$',        linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,9],  '-', label=r'$H_2O$',        linewidth=2)
ax0[1].semilogy(combustor_residuals[:,0], combustor_residuals[:,10], '-', label=r'$O_2$',         linewidth=2)
ax0[1].set_xticks(np.arange(0, 0.105, 0.02))
ax0[1].set_xlim(0, tmax[1])
ax0[1].set_xlabel(r'time $[s]$')
ax0[1].set_ylabel(r'residual')
ax0[1].set_title(figTitle[1] + '\nresiduals')
ax0[1].minorticks_on
ax0[1].grid(True, which='both', linestyle='--')
ax0[1].legend(bbox_to_anchor=(1,1), loc='upper left')

# saving figure in LaTeX format
figRes.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab07/residuals.pgf', bbox_inches='tight')
