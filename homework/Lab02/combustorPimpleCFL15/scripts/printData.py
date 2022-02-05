# THIS PROGRAM PRINTS OpenFOAM RESIDUALS
# RESIDUAL EXTRACTION PROCESS 
#   PRESSURE                                    -- p
#   VELOCITY                                    -- Ux | Uy
#   TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- k
#   DISSIPATION RATE         nu  * < sij  sij > -- epsilon 

# importing libraries 
import time 
import numpy             as np 
import matplotlib.pyplot as plt 

# initializing check strings
tCheck           = 'Time = '
UxCheck          = 'Solving for Ux'
UyCheck          = 'Solving for Uy'
pCheck           = 'Solving for p' 
epsCheck         = 'Solving for epsilon' 
kCheck           = 'Solving for k' 
convergenceCheck = 'Doing final iteration'

# initializing file name 
simulationName = 'pimpleFoam'
fileName       = 'logfiles/log.' + simulationName

# initializing time variables 
lastTime     = 0.0  # initial simulation time 
totalTime    = 0.5  # last simulation time 
timeInterval = 10.0 # waiting time in the loop 
plotTime     = 1.0  # time waiting for graphs plotting 

# plotting initialization
plt.ion() # setting on interactive plot mode
fig = plt.figure("RESIDUALS PLOT", figsize=(10, 8))

# naming storing variables -- needed for line? to be declared 
pResidual       = []
timeVec         = []
UxResidual      = []
UyResidual      = []
epsilonResidual = []
kResidual       = [] 

# initializing plot lines properties
line1, = plt.semilogy(timeVec, pResidual,       '-b', label=r'$p$',           linewidth=1)
line2, = plt.semilogy(timeVec, UxResidual,      '-r', label=r'$U_x$',         linewidth=1)
line3, = plt.semilogy(timeVec, UyResidual,      '-g', label=r'$U_y$',         linewidth=1)
line4, = plt.semilogy(timeVec, epsilonResidual, '-c', label=r'$\varepsilon$', linewidth=1)
line5, = plt.semilogy(timeVec, kResidual,       '-m', label=r'$\kappa$',      linewidth=1)

# setting up plot properties
plt.ylim([1e-12, 1e-2])
plt.xlim([0, totalTime])
plt.minorticks_on 
plt.xticks(np.arange(0, 0.6, 0.1))
plt.xlabel(r'time $[s]$')
plt.ylabel('residual')
plt.grid(True, which='both', linestyle='--')
plt.legend(bbox_to_anchor=(1,1), loc='upper left')

# analysing file 
with open(fileName, 'r') as FILE: 
    # initializing initial position 
    lineSaved = FILE.tell()
    inPos     = int(0)
    
    # this loop will last untill lastTime will reach the final time of the simulation 
    while lastTime < totalTime:
        # waiting for OpenFOAM to print data
        time.sleep(timeInterval)

        # setting file pointer to lineSaved 
        FILE.seek(lineSaved)
        # reading all lines till EOF
        lines = FILE.readlines() 
        # reading from inPos line till the end --> avoiding to get multiple times the same data (already stored)
        lines = lines[inPos::]
        # storing lines array dimension
        linesDim = len(lines)
        
        # loop for data save
        for ii in range(linesDim):
            if tCheck in lines[ii][0:7]:
                lastTimeRelativePos = ii 
                lastTimeSaved       = float(lines[ii].rsplit('=')[1])

            elif convergenceCheck in lines[ii] and (ii + 15) < linesDim: # 2nd condition -> ensuring there are enough lines to be read (not at the EOF)

                # moving to Ux line
                while UxCheck not in lines[ii]:
                    ii += 1
                # Ux extraction 
                UxRES = float((lines[ii].rsplit(',')[1]).rsplit('=')[1])

                # moving to Uy line 
                while UyCheck not in lines[ii]:
                    ii += 1
                # Uy extraction 
                UyRES = float((lines[ii].rsplit(',')[1]).rsplit('=')[1])

                # moving to p line 
                while pCheck not in lines[ii]:   
                    ii += 1 
                # p extraction 
                pRES = float((lines[ii].rsplit(',')[1]).rsplit('=')[1])

                # moving to epsilon line 
                while epsCheck not in lines[ii]:
                    ii += 1
                # epsilon extraction
                epsilonRES = float((lines[ii].rsplit(',')[1]).rsplit('=')[1])

                # moving to k line 
                while kCheck not in lines[ii]:              
                    ii += 1
                # k extraction 
                kRES = float((lines[ii].rsplit(',')[1]).rsplit('=')[1])

                # updating last time step
                lastTime = lastTimeSaved

                # saving data in arrays
                timeVec.append(lastTime)
                UxResidual.append(UxRES)
                UyResidual.append(UyRES)
                pResidual.append(pRES)
                epsilonResidual.append(epsilonRES)
                kResidual.append(kRES)
        
        # updating FILE line number to start from
        inPos = inPos + lastTimeRelativePos 

        # plotting data
        line1.set_xdata(timeVec)
        line1.set_ydata(pResidual)

        line2.set_xdata(timeVec)
        line2.set_ydata(UxResidual)

        line3.set_xdata(timeVec)
        line3.set_ydata(UyResidual)

        line4.set_xdata(timeVec)
        line4.set_ydata(epsilonResidual)

        line5.set_xdata(timeVec)
        line5.set_ydata(kResidual)

        # updating figure
        plt.title('OpenFOAM residuals\n' + r'$\mathtt{lastTime} = $' + '%0.4f s'%lastTime)
        plt.pause(plotTime)
        plt.draw()

plt.ioff() # setting off interactive plot mode 
plt.show() # keeping plot active 
