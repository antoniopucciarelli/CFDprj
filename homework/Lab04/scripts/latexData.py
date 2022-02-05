####################################################################
# LAB04 -- COMPUTATIONAL TECHNIQUES FOR THEMOCHEMICAL PROPULSION   #
#------------------------------------------------------------------# 
#   PLOTTING DATA FOR FINAL REPORT                                 #  
#   1 -- GETTING DATA FROM FILES:                                  #
#       combustorRhoPimple_lowT_lowRe                              #
#       combustorRhoPimple_highT_lowRe                             #
#       combustorRhoPimple_highT_highRe                            #
#                                                                  #    
#   2 -- PLOTTING DATA:                                            #
#       1 residuals                                                #
#           [combustorRhoPimple_lowT_lowRe]                        #
#           [combustorRhoPimple_highT_lowRe]                       #
#           [combustorRhoPimple_highT_highRe]                      #
#                                                                  #
#       2 T @ y = 100mm                                            #
#           [combustorRhoPimple_lowT_lowRe]                        #
#           [combustorRhoPimple_highT_lowRe]                       #
#           [combustorRhoPimple_highT_highRe]                      #
#                                                                  #
#       3 Uy @ y = 100mm                                           #
#           [combustorRhoPimple_lowT_lowRe]                        #
#           [combustorRhoPimple_highT_lowRe]                       #
#           [combustorRhoPimple_highT_highRe]                      #
####################################################################

# importing libraries 
import matplotlib
import matplotlib.pyplot as plt 
import numpy             as np

#------------------------------------------------------------------#
#   1 -- GETTING DATA FROM FILES:                                  #
#   FROM OPENFOAM INTERNAL LIBRARIES                               #
#       residuals:                                                 #
#           PRESSURE                                    -- p       #
#           VELOCITY                                    -- Ux | Uy #
#           TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- K       #
#           DISSIPATION RATE         nu  * < sij  sij > -- EPSILON #
#       T  @ y = 100 mm                                            #
#       Uy @ y = 100 mm                                            #
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

# naming storing variables 
# combustorPimple_lowT_lowRe
combustorPimple1_residuals      = []
combustorPimple1_T              = []
# combustorPimple_highT_lowRe
combustorPimple2_residuals      = []
combustorPimple2_T              = []
# combustorPimple_highT_highRe
combustorPimple3_residuals      = []
combustorPimple3_T              = []

# setting data folder 
axialLine   = 'axialLine/'                           # axialLine data 
residuals   = 'residuals/0/residuals.dat'            # residuals data
# setting variable folder for each case 
combustorPimple1_mainPATH = '../combustorRhoPimple_lowT_lowRe/postProcessing/'   # combustorPimple_lowT_lowRe   folder 
combustorPimple2_mainPATH = '../combustorRhoPimple_highT_lowRe/postProcessing/'  # combustorPimple_highT_lowRe  folder 
combustorPimple3_mainPATH = '../combustorRhoPimple_highT_highRe/postProcessing/' # combustorPimple_highT_highRe folder 

# getting data for combustorPimple_lowT_lowRe 
# residuals
combustorPimple1_residuals = np.loadtxt(combustorPimple1_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=4)

# T 
combustorPimple1_time = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']
combustorPimple1_T    = np.zeros((100, len(combustorPimple1_time)+1))
for ii,tt in enumerate(combustorPimple1_time):
    FILEname                   = combustorPimple1_mainPATH + axialLine + str(tt) + '/line_T.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,1))
    combustorPimple1_T[:,ii+1] = savingData[:,1]
combustorPimple1_T[:,0] = savingData[:,0]

# U
combustorPimple1_U    = np.zeros((100, len(combustorPimple1_time)+1))
for ii,tt in enumerate(combustorPimple1_time):
    FILEname                   = combustorPimple1_mainPATH + axialLine + tt + '/line_U.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,2))
    combustorPimple1_U[:,ii+1] = savingData[:,1]
combustorPimple1_U[:,0] = savingData[:,0]

# getting data for combustorPimple_highT_lowRe
combustorPimple2_residuals = np.loadtxt(combustorPimple2_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=4)

# T
combustorPimple2_time = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']
combustorPimple2_T    = np.zeros((100, len(combustorPimple2_time)+1))
for ii,tt in enumerate(combustorPimple2_time):
    FILEname                    = combustorPimple2_mainPATH + axialLine + tt + '/line_T.xy'
    savingData                  = np.loadtxt(FILEname, usecols=(0,1))
    combustorPimple2_T[:,ii+1] = savingData[:,1]
combustorPimple2_T[:,0] = savingData[:,0]

# U
combustorPimple2_U    = np.zeros((100, len(combustorPimple2_time)+1))
for ii,tt in enumerate(combustorPimple2_time):
    FILEname                    = combustorPimple2_mainPATH + axialLine + tt + '/line_U.xy'
    savingData                  = np.loadtxt(FILEname, usecols=(0,2))
    combustorPimple2_U[:,ii+1] = savingData[:,1]
combustorPimple2_U[:,0] = savingData[:,0]

# getting data for combustorPimple_highT_highRe
combustorPimple3_residuals = np.loadtxt(combustorPimple3_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=4)

# T 
combustorPimple3_time = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']
combustorPimple3_T    = np.zeros((100, len(combustorPimple3_time)+1))
for ii,tt in enumerate(combustorPimple3_time):
    FILEname                   = combustorPimple3_mainPATH + axialLine + tt + '/line_T.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,1))
    combustorPimple3_T[:,ii+1] = savingData[:,1]
combustorPimple3_T[:,0] = savingData[:,0]

# U
combustorPimple3_U    = np.zeros((100, len(combustorPimple3_time)+1))
for ii,tt in enumerate(combustorPimple3_time):
    FILEname                   = combustorPimple3_mainPATH + axialLine + tt + '/line_U.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,2))
    combustorPimple3_U[:,ii+1] = savingData[:,1]
combustorPimple3_U[:,0] = savingData[:,0]

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #     
#       1 residuals                                                # 
#------------------------------------------------------------------#
figRes, axis = plt.subplots(3,1)
figRes.set_size_inches(w=W, h=H)

# residuals plot
# combustorPimple_lowT_lowRe 
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,4], '-', label=r'$\kappa$',      linewidth=2)
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,5], '-', label=r'$\varepsilon$', linewidth=2)
axis[0].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,6], '-', label=r'$h$',           linewidth=2)
axis[0].set_xticks(np.arange(0, 0.55, 0.1))
axis[0].set_xlabel(r'$time$')
axis[0].set_ylabel(r'$residual$')
axis[0].set_title(r'$\mathtt{rhoPimpleFoam}_{lowT|lowRe}$' + '\nresiduals')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_xlim(0,0.5)

# combustorPimple_highT_lowRe
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,4], '-', label=r'$\kappa$',      linewidth=2)
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,5], '-', label=r'$\varepsilon$', linewidth=2)
axis[1].semilogy(combustorPimple2_residuals[:,0], combustorPimple2_residuals[:,6], '-', label=r'$h$',           linewidth=2)
axis[1].set_xticks(np.arange(0, 0.55, 0.1))
axis[1].set_xlabel(r'$time$')
axis[1].set_ylabel(r'$residual$')
axis[1].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|lowRe}$' + '\nresiduals')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_xlim(0,0.5)

# combustorPimple_highT_highRe
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,4], '-', label=r'$\kappa$',      linewidth=2)
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,5], '-', label=r'$\varepsilon$', linewidth=2)
axis[2].semilogy(combustorPimple3_residuals[:,0], combustorPimple3_residuals[:,6], '-', label=r'$h$',           linewidth=2)
axis[2].set_xticks(np.arange(0, 0.55, 0.1))
axis[2].set_xlabel(r'$time$')
axis[2].set_ylabel(r'$residual$')
axis[2].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|highRe}$' + '\nresiduals')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_xlim(0,0.5)

# saving figure in LaTeX format
figRes.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab04/residuals.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #
#       2 T                                                        #
#------------------------------------------------------------------#
figT, axis = plt.subplots(3,1)
figT.set_size_inches(w=W, h=H)

# T plot 
# combustorPimple_lowT_lowRe 
for ii,tt in enumerate(combustorPimple1_time):
    axis[0].plot(combustorPimple1_T[:,0], combustorPimple1_T[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[0].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[0].set_xlabel(r'$x$')
axis[0].set_ylabel(r'$T \ [ K ]$')
axis[0].set_title(r'$\mathtt{rhoPimpleFoam}_{lowT|lowRe}$' + '\n' + 'T')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_xlim(-0.12,0.12)

# combustorPimple_highT_lowRe
for ii,tt in enumerate(combustorPimple2_time):
    axis[1].plot(combustorPimple2_T[:,0], combustorPimple2_T[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[1].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[1].set_xlabel(r'$x$')
axis[1].set_ylabel(r'$T \ [ K ]$')
axis[1].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|lowRe}$' + '\n' + 'T')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_xlim(-0.12,0.12)

# combustorPimple_highT_highRe
for ii,tt in enumerate(combustorPimple3_time):
    axis[2].plot(combustorPimple3_T[:,0], combustorPimple3_T[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[2].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[2].set_xlabel(r'$x$')
axis[2].set_ylabel(r'$T \ [ K ]$')
axis[2].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|highRe}$' + '\n' + 'T')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_xlim(-0.12,0.12)

# saving figure in LaTeX format
figT.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab04/T.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #
#       3 Uy                                                       #
#------------------------------------------------------------------#
figUy, axis = plt.subplots(3,1)
figUy.set_size_inches(w=W, h=H)

# U plot 
# combustorPimple_lowT_lowRe 
for ii,tt in enumerate(combustorPimple1_time):
    axis[0].plot(combustorPimple1_U[:,0], combustorPimple1_U[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[0].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[0].set_xlabel(r'$x$')
axis[0].set_ylabel(r'$U_y \ \Big[ \frac{m}{s} \Big]$')
axis[0].set_title(r'$\mathtt{rhoPimpleFoam}_{lowT|lowRe}$' + '\n' + r'$U_y$')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_xlim(-0.12,0.12)

# combustorPimple_highT_lowRe
for ii,tt in enumerate(combustorPimple2_time):
    axis[1].plot(combustorPimple2_U[:,0], combustorPimple2_U[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[1].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[1].set_xlabel(r'$x$')
axis[1].set_ylabel(r'$U_y \ \Big[ \frac{m}{s} \Big]$')
axis[1].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|lowRe}$' + '\n' + r'$U_y$')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_xlim(-0.12,0.12)

# combustorPimple_highT_highRe
for ii,tt in enumerate(combustorPimple3_time):
    axis[2].plot(combustorPimple3_U[:,0], combustorPimple3_U[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[2].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[2].set_xlabel(r'$x$')
axis[2].set_ylabel(r'$U_y \ \Big[ \frac{m}{s} \Big]$')
axis[2].set_title(r'$\mathtt{rhoPimpleFoam}_{highT|highRe}$' + '\n' + r'$U_y$')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_xlim(-0.12,0.12)

# saving figure in LaTeX format
figUy.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab04/Uy.pgf', bbox_inches='tight')