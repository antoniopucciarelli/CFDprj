####################################################################
# LAB02 -- COMPUTATIONAL TECHNIQUES FOR THEMOCHEMICAL PROPULSION   #
# -----------------------------------------------------------------# 
#   PLOTTING DATA FOR FINAL REPORT                                 # 
#   1 -- GETTING DATA FROM FILES:                                  #
#       combustorSimple                                            #
#       combustorPimple1                                           #
#       combustorPimple15                                          #
#                                                                  #
#   2 -- PLOTTING DATA:                                            #   
#       1 residuals                                                #   
#           [combustorSimple]                                      #   
#           [combustorPimple1]                                     #   
#           [combustorPimple15]                                    #   
#                                                                  #
#       2 forces                                                   #   
#           [combustorSimple]                                      #   
#           [combustorPimple1]                                     #   
#           [combustorPimple15]                                    #   
#                                                                  #
#       3 y+                                                       #   
#           [combustorSimple]                                      #   
#           [combustorPimple1]                                     #   
#           [combustorPimple15]                                    #   
####################################################################                                  

# importing libraries 
import matplotlib
import matplotlib.pyplot as plt 
import numpy             as np
import matplotlib.ticker as tck

# -----------------------------------------------------------------#
#   1 -- GETTING DATA FROM FILES:                                  #
#   FROM OPENFOAM INTERNAL LIBRARIES                               #
#       residuals:                                                 #
#           PRESSURE                                    -- p       #
#           VELOCITY                                    -- Ux | Uy #
#           TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- K       #
#           DISSIPATION RATE         nu  * < sij  sij > -- EPSILON #
#       forces:                                                    #
#           PRESSURE FORCE                                         #
#           VISCOUS FORCE                                          #
#       y+                                                         #
# -----------------------------------------------------------------#

# setting matplotlib LaTeX export 
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# pgf plot size 
W = 5       # width
H = 8      # height

# naming storing variables 
# combustorSimple
combustorSimple_residuals     = []
combustorSimple_Uy            = []
combustorSimple_forces        = []
combostorSimple_yPlusBack     = []
combostorSimple_yPlusSides    = []
combostorSimple_yPlusSplitter = []
# combustorPimple1
combustorPimple1_residuals     = []
combustorPimple1_Uy            = []
combustorPimple1_forces        = []
combostorPimple1_yPlusBack     = []
combostorPimple1_yPlusSides    = []
combostorPimple1_yPlusSplitter = []
# combustorPimple15
combustorPimple15_residuals     = []
combustorPimple15_Uy            = []
combustorPimple15_forces        = []
combostorPimple15_yPlusBack     = []
combostorPimple15_yPlusSides    = []
combostorPimple15_yPlusSplitter = []

# setting data folder 
yPlus       = 'yPlus/0/yPlus.dat'                                   # y+        data
force       = 'force/0/forces.dat'                                  # forces    data
axialLine   = 'axialLine/'                                          # axialLine data 
residuals   = 'residuals(p,U,k,epsilon)/0/residuals.dat'            # residuals data
# setting variable folder for each case 
combustorSimple_mainPATH   = '../combustorSimple/postProcessing/'      # combustorSimple   folder 
combustorPimple1_mainPATH  = '../combustorPimpleCFL1/postProcessing/'  # combustorPimple1  folder 
combustorPimple15_mainPATH = '../combustorPimpleCFL15/postProcessing/' # combustorPimple15 folder 

# getting data for combustorSimple 
# residuals
combustorSimple_residuals = np.loadtxt(combustorSimple_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5), skiprows=3)

# Uy 
combustorSimple_time = np.array([0, 400, 800, 1200, 1600, 2000])
combustorSimple_Uy   = np.zeros((100, len(combustorSimple_time)+1))
for ii,tt in enumerate(combustorSimple_time):
    FILEname                   = combustorSimple_mainPATH + axialLine + str(tt) + '/line_U.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,2))
    combustorSimple_Uy[:,ii+1] = savingData[:,1]
combustorSimple_Uy[:,0] = savingData[:,0]

# forces 
combustorSimple_forces = np.loadtxt(combustorSimple_mainPATH + force, usecols=(0,2,5))

# y+ 
combustorSimple_yPlus         = np.loadtxt(combustorSimple_mainPATH + yPlus, usecols=(0,2,3))
length                        = int(len(combustorSimple_yPlus)/3)
combustorSimple_yPlusBack     = np.zeros([length, 3])
combustorSimple_yPlusSides    = np.zeros([length, 3])
combustorSimple_yPlusSplitter = np.zeros([length, 3])
# yPlus back
for ii in range(length):
    combustorSimple_yPlusBack[ii,[0,1,2]] = combustorSimple_yPlus[ii*3, [0,1,2]]
# yPlus sides
for ii in range(length):
    combustorSimple_yPlusSides[ii,[0,1,2]] = combustorSimple_yPlus[ii*3+1, [0,1,2]]
# yPlus splitter
for ii in range(length):
    combustorSimple_yPlusSplitter[ii,[0,1,2]] = combustorSimple_yPlus[ii*3+2, [0,1,2]]

# getting data for combustorPimple1 
combustorPimple1_residuals = np.loadtxt(combustorPimple1_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5), skiprows=4)

# Uy 
combustorPimple1_time = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']
combustorPimple1_Uy   = np.zeros((100, len(combustorPimple1_time)+1))
for ii,tt in enumerate(combustorPimple1_time):
    FILEname                    = combustorPimple1_mainPATH + axialLine + tt + '/line_U.xy'
    savingData                  = np.loadtxt(FILEname, usecols=(0,2))
    combustorPimple1_Uy[:,ii+1] = savingData[:,1]
combustorPimple1_Uy[:,0] = savingData[:,0]

# forces 
combustorPimple1_forces = np.loadtxt(combustorPimple1_mainPATH + force, usecols=(0,2,5))

# y+ 
combustorPimple1_yPlus         = np.loadtxt(combustorPimple1_mainPATH + yPlus, usecols=(0,2,3))
length                         = int(len(combustorPimple1_yPlus)/3)
combustorPimple1_yPlusBack     = np.zeros([length, 3])
combustorPimple1_yPlusSides    = np.zeros([length, 3])
combustorPimple1_yPlusSplitter = np.zeros([length, 3])
# yPlus back
for ii in range(length):
    combustorPimple1_yPlusBack[ii,[0,1,2]] = combustorPimple1_yPlus[ii*3, [0,1,2]]
# yPlus sides
for ii in range(length):
    combustorPimple1_yPlusSides[ii,[0,1,2]] = combustorPimple1_yPlus[ii*3+1, [0,1,2]]
# yPlus splitter
for ii in range(length):
    combustorPimple1_yPlusSplitter[ii,[0,1,2]] = combustorPimple1_yPlus[ii*3+2, [0,1,2]]

# getting data for combustorPimple15 
combustorPimple15_residuals = np.loadtxt(combustorPimple15_mainPATH + residuals, usecols=(0, 1, 2, 3, 4, 5), skiprows=4)

# Uy 
combustorPimple15_time = ['0', '0.1', '0.2', '0.3', '0.4', '0.5']
combustorPimple15_Uy   = np.zeros((100, len(combustorPimple15_time)+1))
for ii,tt in enumerate(combustorPimple15_time):
    FILEname                   = combustorPimple15_mainPATH + axialLine + tt + '/line_U.xy'
    savingData                 = np.loadtxt(FILEname, usecols=(0,2))
    combustorPimple15_Uy[:,ii+1] = savingData[:,1]
combustorPimple15_Uy[:,0] = savingData[:,0]

# forces 
combustorPimple15_forces = np.loadtxt(combustorPimple15_mainPATH + force, usecols=(0,2,5))

# y+ 
combustorPimple15_yPlus         = np.loadtxt(combustorPimple15_mainPATH + yPlus, usecols=(0,2,3))
length                          = int(len(combustorPimple15_yPlus)/3)
combustorPimple15_yPlusBack     = np.zeros([length, 3])
combustorPimple15_yPlusSides    = np.zeros([length, 3])
combustorPimple15_yPlusSplitter = np.zeros([length, 3])
# yPlus back
for ii in range(length):
    combustorPimple15_yPlusBack[ii,[0,1,2]] = combustorPimple15_yPlus[ii*3, [0,1,2]]
# yPlus sides
for ii in range(length):
    combustorPimple15_yPlusSides[ii,[0,1,2]] = combustorPimple15_yPlus[ii*3+1, [0,1,2]]
# yPlus splitter
for ii in range(length):
    combustorPimple15_yPlusSplitter[ii,[0,1,2]] = combustorPimple15_yPlus[ii*3+2, [0,1,2]]

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #     
#       1 residuals                                                # 
#------------------------------------------------------------------#
figRes, axis = plt.subplots(3,1)
figRes.set_size_inches(w=W, h=H)

# residuals plot
# combustorSimple 
axis[0].semilogy(combustorSimple_residuals[:,0], combustorSimple_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[0].semilogy(combustorSimple_residuals[:,0], combustorSimple_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[0].semilogy(combustorSimple_residuals[:,0], combustorSimple_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[0].semilogy(combustorSimple_residuals[:,0], combustorSimple_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
axis[0].semilogy(combustorSimple_residuals[:,0], combustorSimple_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
axis[0].set_xticks(np.arange(0, 2100, 250))
axis[0].set_xlabel(r'$step$')
axis[0].set_ylabel(r'$residual$')
axis[0].set_title(r'$\mathtt{simpleFoam}$' + '\nresiduals')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_xlim(0,2000)

# combustorPimple1
axis[1].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[1].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[1].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[1].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
axis[1].semilogy(combustorPimple1_residuals[:,0], combustorPimple1_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
axis[1].set_xticks(np.arange(0, 0.55, 0.1))
axis[1].set_xlabel(r'$time$')
axis[1].set_ylabel(r'$residual$')
axis[1].set_title(r'$\mathtt{pimpleFoam}$ CFL < 1' + '\nresiduals')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=24)
axis[1].yaxis.set_minor_locator(locmin)
axis[1].set_yticks([1e-0,1e-1,1e-2,1e-3,1e-4,1e-5])
axis[1].yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
axis[1].grid(b=True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_xlim(0,0.5)

# combustorPimple15
axis[2].semilogy(combustorPimple15_residuals[:,0], combustorPimple15_residuals[:,1], '-', label=r'$p$',           linewidth=2)
axis[2].semilogy(combustorPimple15_residuals[:,0], combustorPimple15_residuals[:,2], '-', label=r'$U_x$',         linewidth=2)
axis[2].semilogy(combustorPimple15_residuals[:,0], combustorPimple15_residuals[:,3], '-', label=r'$U_y$',         linewidth=2)
axis[2].semilogy(combustorPimple15_residuals[:,0], combustorPimple15_residuals[:,4], '-', label=r'$\varepsilon$', linewidth=2)
axis[2].semilogy(combustorPimple15_residuals[:,0], combustorPimple15_residuals[:,5], '-', label=r'$\kappa$',      linewidth=2)
axis[2].set_xticks(np.arange(0, 0.55, 0.1))
axis[2].set_xlabel(r'$time$')
axis[2].set_ylabel(r'$residual$')
axis[2].set_title(r'$\mathtt{pimpleFoam}$ CFL < 15' + '\nresiduals')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_xlim(0,0.5)

# saving figure in LaTeX format
figRes.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab02/residuals.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #
#       2 Uy                                                       #
#------------------------------------------------------------------#
figUy, axis = plt.subplots(3,1)
figUy.set_size_inches(w=W, h=H)

# Uy plot 
# combustorSimple 
for ii,tt in enumerate(combustorSimple_time):
    axis[0].plot(combustorSimple_Uy[:,0], combustorSimple_Uy[:,ii+1], '-', label=str(tt) + ' step', linewidth=2)

axis[0].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[0].set_xlabel(r'$x$')
axis[0].set_ylabel(r'$U_y \ \Big[\frac{m}{s} \Big]$')
axis[0].set_title(r'$\mathtt{simpleFoam}$' + '\n' + r'$U_y$')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_xlim(-0.12,0.12)

# combustorPimple1 
for ii,tt in enumerate(combustorPimple1_time):
    axis[1].plot(combustorPimple1_Uy[:,0], combustorPimple1_Uy[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[1].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[1].set_xlabel(r'$x$')
axis[1].set_ylabel(r'$U_y \ \Big[\frac{m}{s} \Big]$')
axis[1].set_title(r'$\mathtt{pimpleFoam}$ CFL < 1' + '\n' + r'$U_y$')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_xlim(-0.12,0.12)

# combustorPimple15 
for ii,tt in enumerate(combustorPimple15_time):
    axis[2].plot(combustorPimple15_Uy[:,0], combustorPimple15_Uy[:,ii+1], '-', label=str(tt) + ' s', linewidth=2)

axis[2].set_xticks(np.arange(-0.12, 0.125, 0.03))
axis[2].set_xlabel(r'$x$')
axis[2].set_ylabel(r'$U_y \ \Big[\frac{m}{s} \Big]$')
axis[2].set_title(r'$\mathtt{pimpleFoam}$ CFL < 15' + '\n' + r'$U_y$')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_xlim(-0.12,0.12)

# saving figure in LaTeX format
figUy.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab02/Uy.pgf', bbox_inches='tight')

#------------------------------------------------------------------#
#   2 -- PLOTTING DATA:                                            #
#       3 forces                                                   #
#------------------------------------------------------------------#
figForces, axis = plt.subplots(3,1)
figForces.set_size_inches(w=W, h=H)

# combustorSimple 
axis[0].plot(combustorSimple_forces[:,0], combustorSimple_forces[:,1], '-', label=r'$D_{pressure}$', linewidth=2)
axis[0].plot(combustorSimple_forces[:,0], combustorSimple_forces[:,2], '-', label=r'$D_{\mu}$', linewidth=2)
axis[0].set_xlabel(r'step$')
axis[0].set_ylabel(r'force $[N]$')
axis[0].set_title(r'$\mathtt{simpleFoam}$' + '\nforce')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_ylim(-0.05, 0.2)
axis[0].set_xlim(0,2000)

# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.6)

# combustorPimple1 
axis[1].plot(combustorPimple1_forces[:,0], combustorPimple1_forces[:,1], '-', label=r'$D_{pressure}$', linewidth=2)
axis[1].plot(combustorPimple1_forces[:,0], combustorPimple1_forces[:,2], '-', label=r'$D_{\mu}$', linewidth=2)
axis[1].set_xlabel(r't $[s]$')
axis[1].set_ylabel(r'force $[N]$')
axis[1].set_title(r'$\mathtt{pimpleFoam}$ CFL < 1' + '\nforce')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_ylim(-0.05, 0.2)
axis[1].set_xlim(0,0.5)

# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.6)

# combustorPimple15 
axis[2].plot(combustorPimple15_forces[:,0], combustorPimple15_forces[:,1], '-', label=r'$D_{pressure}$', linewidth=2)
axis[2].plot(combustorPimple15_forces[:,0], combustorPimple15_forces[:,2], '-', label=r'$D_{\mu}$', linewidth=2)
axis[2].set_xlabel(r't $[s]$')
axis[2].set_ylabel(r'force $[N]$')
axis[2].set_title(r'$\mathtt{pimpleFoam}$ CFL < 15' + '\nforce')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_ylim(-0.05, 0.2)
axis[2].set_xlim(0,0.5)

# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.6)

# saving figure in LaTeX format
figForces.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab02/forces.pgf', bbox_inches='tight')

#------------------------------------------------------------------# 
#   2 -- PLOTTING DATA:                                            # 
#       4 y+                                                       # 
#------------------------------------------------------------------# 
figyPlus, axis = plt.subplots(3,1)
figyPlus.set_size_inches(w=W, h=H)

# combustorSimple 
axis[0].plot(combustorSimple_yPlusSides[:,0],    combustorSimple_yPlusSides[:,1], '-', label=r'$y^+_{min_{sides}}$', linewidth=2)
axis[0].plot(combustorSimple_yPlusSides[:,0],    combustorSimple_yPlusSides[:,2], '-', label=r'$y^+_{max_{sides}}$', linewidth=2)
axis[0].plot(combustorSimple_yPlusBack[:,0],     combustorSimple_yPlusBack[:,1], '-', label=r'$y^+_{min_{back}}$', linewidth=2)
axis[0].plot(combustorSimple_yPlusBack[:,0],     combustorSimple_yPlusBack[:,2], '-', label=r'$y^+_{max_{back}}$', linewidth=2)
axis[0].plot(combustorSimple_yPlusSplitter[:,0], combustorSimple_yPlusSplitter[:,1], '-', label=r'$y^+_{min_{splitter}}$', linewidth=2)
axis[0].plot(combustorSimple_yPlusSplitter[:,0], combustorSimple_yPlusSplitter[:,2], '-', label=r'$y^+_{max_{splitter}}$', linewidth=2)
axis[0].set_xlabel(r'step$')
axis[0].set_ylabel(r'$y^+$ $[-]$')
axis[0].set_title(r'$\mathtt{simpleFoam}' + '\n' + r'$y^+$')
axis[0].minorticks_on
axis[0].grid(True, which='both', linestyle='--')
axis[0].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[0].set_ylim(0)
axis[0].set_xlim(0,2000)

# combustorPimple1
axis[1].plot(combustorPimple1_yPlusSides[:,0],    combustorPimple1_yPlusSides[:,1], '-', label=r'$y^+_{min_{sides}}$', linewidth=2)
axis[1].plot(combustorPimple1_yPlusSides[:,0],    combustorPimple1_yPlusSides[:,2], '-', label=r'$y^+_{max_{sides}}$', linewidth=2)
axis[1].plot(combustorPimple1_yPlusBack[:,0],     combustorPimple1_yPlusBack[:,1], '-', label=r'$y^+_{min_{back}}$', linewidth=2)
axis[1].plot(combustorPimple1_yPlusBack[:,0],     combustorPimple1_yPlusBack[:,2], '-', label=r'$y^+_{max_{back}}$', linewidth=2)
axis[1].plot(combustorPimple1_yPlusSplitter[:,0], combustorPimple1_yPlusSplitter[:,1], '-', label=r'$y^+_{min_{splitter}}$', linewidth=2)
axis[1].plot(combustorPimple1_yPlusSplitter[:,0], combustorPimple1_yPlusSplitter[:,2], '-', label=r'$y^+_{max_{splitter}}$', linewidth=2)
axis[1].set_xlabel(r't $[s]$')
axis[1].set_ylabel(r'$y^+$ $[-]$')
axis[1].set_title(r'$\mathtt{pimpleFoam} \ CFL < 1' + '\n' + r'$y^+$')
axis[1].minorticks_on
axis[1].grid(True, which='both', linestyle='--')
axis[1].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[1].set_ylim(0)
axis[1].set_xlim(0,0.5)

# combustorPimple15
axis[2].plot(combustorPimple15_yPlusSides[:,0],    combustorPimple15_yPlusSides[:,1], '-', label=r'$y^+_{min_{sides}}$', linewidth=2)
axis[2].plot(combustorPimple15_yPlusSides[:,0],    combustorPimple15_yPlusSides[:,2], '-', label=r'$y^+_{max_{sides}}$', linewidth=2)
axis[2].plot(combustorPimple15_yPlusBack[:,0],     combustorPimple15_yPlusBack[:,1], '-', label=r'$y^+_{min_{back}}$', linewidth=2)
axis[2].plot(combustorPimple15_yPlusBack[:,0],     combustorPimple15_yPlusBack[:,2], '-', label=r'$y^+_{max_{back}}$', linewidth=2)
axis[2].plot(combustorPimple15_yPlusSplitter[:,0], combustorPimple15_yPlusSplitter[:,1], '-', label=r'$y^+_{min_{splitter}}$', linewidth=2)
axis[2].plot(combustorPimple15_yPlusSplitter[:,0], combustorPimple15_yPlusSplitter[:,2], '-', label=r'$y^+_{max_{splitter}}$', linewidth=2)
axis[2].set_xlabel(r't $[s]$')
axis[2].set_ylabel(r'$y^+$ $[-]$')
axis[2].set_title(r'$\mathtt{pimpleFoam} \ CFL < 15' + '\n' + r'$y^+$')
axis[2].minorticks_on
axis[2].grid(True, which='both', linestyle='--')
axis[2].legend(bbox_to_anchor=(1,1), loc='upper left')
axis[2].set_ylim(0)
axis[2].set_xlim(0,0.5)

# saving figure in LaTeX format
figyPlus.tight_layout()
plt.savefig('../../../thermochemicalCFD/latexFIGS/lab02/yPlus.pgf', bbox_inches='tight')
