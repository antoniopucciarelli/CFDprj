# THIS PROGRAM PRINTS OpenFOAM RESIDUALS
# RESIDUAL EXTRACTION PROCESS 
#   PRESSURE 
#   VELOCITY 
#   TURBULENT KINETIC ENERGY 0.5 * < ui ui >    -- K
#   DISSIPATION RATE         nu  * < sij  sij > -- EPSILON 

# importing libraries 
import matplotlib.pyplot as plt 
import numpy             as np 
import time 

startingTime = 5
timeInterval = 1e-2
plotTime     = 0.01

lastTime  = 1 
totalTime = 2000

tCheck   = 'Time = '
UxCheck  = 'Solving for Ux'
UyCheck  = 'Solving for Uy'
pCheck   = 'Solving for p' 
epsCheck = 'Solving for epsilon' 
kCheck   = 'Solving for k' 

simulationName = 'simpleFoam'
fileName       = 'logfiles/log.' + str(simulationName)

with open(fileName, 'r') as FILE:
    line      = FILE.readline()
    lineSaved = FILE.tell()
    
    time.sleep(startingTime)

    # naming storing variables 
    pResidual        = []
    timeVec          = []
    UxResidual       = []
    UyResidual       = []
    epsilonResidual  = []
    kResidual        = [] 

    # plotting 
    plt.ion()
    fig= plt.figure(figsize=(10, 8))

    line1, = plt.semilogy(timeVec, pResidual,       '-b', label=r'$p$',           linewidth=2)
    line2, = plt.semilogy(timeVec, UxResidual,      '-r', label=r'$U_x$',         linewidth=2)
    line3, = plt.semilogy(timeVec, UyResidual,      '-g', label=r'$U_y$',         linewidth=2)
    line4, = plt.semilogy(timeVec, epsilonResidual, '-c', label=r'$\varepsilon$', linewidth=2)
    line5, = plt.semilogy(timeVec, kResidual,       '-m', label=r'$\kappa$',      linewidth=2)

    plt.xticks(np.arange(0, 2100, 500))
    plt.ylim([1e-7, 1])
    plt.xlabel(r'$time$')
    plt.ylabel(r'$residual$')
    plt.title('OpenFoam residuals')
    plt.legend(bbox_to_anchor=(1,1), loc='upper left')
    plt.minorticks_on 
    plt.grid(True, which='both', linestyle='--')

    while lastTime < totalTime:

        startT = time.time()
        deltaT = 0.0
        FILE.seek(lineSaved) 

        while deltaT <= timeInterval:
            if tCheck in line[0:7]:
                lineSaved = FILE.tell()

                lastTime = float(line.rsplit('=')[1])

                ii = 0

                while line and ii<=10:
                    ii += 1
                    if FILE.readline() == "":
                        FILE.seek(lineSaved)
                
                FILE.seek(lineSaved)

                while UxCheck not in line:
                   line = FILE.readline()
                
                UxRES = float((line.rsplit(',')[1]).rsplit('=')[1])

                while UyCheck not in line:
                    line = FILE.readline()

                UyRES = float((line.rsplit(',')[1]).rsplit('=')[1])

                while pCheck not in line:   
                    line = FILE.readline()  
    
                pRES = float((line.rsplit(',')[1]).rsplit('=')[1])

                while epsCheck not in line:
                    line = FILE.readline()
                
                epsilonRES = float((line.rsplit(',')[1]).rsplit('=')[1])

                while kCheck not in line:              
                    line = FILE.readline()
    
                kRES = float((line.rsplit(',')[1]).rsplit('=')[1])
                
                UxResidual.append(UxRES)
                UyResidual.append(UyRES)
                pResidual.append(pRES)
                epsilonResidual.append(epsilonRES)
                kResidual.append(kRES)
                timeVec.append(lastTime)

            deltaT = time.time() - startT
            line   = FILE.readline()    

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

        plt.pause(plotTime)
        plt.draw()
    
plt.ioff()
plt.show()
