#!/usr/bin/python3

# Outer code for setting up the linear advection problem on a uniform
# grid and calling the function to perform the linear advection and plot.

### Copy out most of this code. Code commented with 3#s (like this) ###
### is here to help you to learn python and need not be copied      ###

### The command at the top means that this python function can be  ###
### run directly from the command line (you will also need to do   ###
### "chmod u+x linearAdvect.py" in unix or linux and then execute: ###
### ./linearAdvect.py                                              ###

### Note that blocks are defined by indentation in Python. You     ###
### should never mix tabs and spaces for indentation - use 4 spaces.###
### Setup your text editor to insert 4 spaces when you press tab    ###

### If you are using Python 2.7 rather than Python 3, import various###
### functions from Python 3 such as to use real number division     ###
### rather than integer division. ie 3/2  = 1.5  rather than 3/2 = 1###
#from __future__ import absolute_import, division, print_function

### The matplotlib package contains plotting functions              ###
import matplotlib.pyplot as plt
import numpy as np

# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from initialConditions import *
from advection_schemes import *
from diagnostics import *
#from FTBS_advectionScheme import *
#from CTCS_advectionscheme import *
#from BTCS_advection import *
#from Lax_Wendroff import *
from TotalVar import *

### The main code is inside a function to avoid global variables    ###
def main():
    "Advect the initial conditions using various advection schemes and"
    "compare results"

    # Parameters
    xmin = 0
    xmax = 1
    nx = 80
    nt = 80
    c = 0.2

    # Derived parameters
    dx = (xmax - xmin)/nx
    
    # spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)

    # Initial conditions
    phiOld = squareWave(x, 0, 0.75)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin), 0, 0.75)

    # Advect the profile using finite difference for all the time steps
    phiFTCS = FTCS(phiOld.copy(), c, nt)
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    #print(phiCTCS)
#    TotalVarFTBS_sum = TotalVar(phiOld.copy(), c, nt)
#    TotalVarCTCS_sum = TotalVar(phiOld.copy(), c, nt)
#    TotalVarLaxWendroff_sum = TotalVar(phiOld.copy(), c, nt)
    TotalVarFTBS_sum, TotalVarLaxWendroff_sum, TotalVarCTCS_sum = TotalVar(phiOld.copy(), c, nt)
    
    # Calculate and print out error norms
    print("FTCS l2 error norm = ", l2ErrorNorm(phiFTCS, phiAnalytic))
    print("FTCS linf error norm = ", lInfErrorNorm(phiFTCS, phiAnalytic))
    
    print("FTBS l2 error norm = ", l2ErrorNorm(phiFTBS, phiAnalytic))
    print("FTBS linf error norm = ", lInfErrorNorm(phiFTBS, phiAnalytic))
    
    print("CTCS l2 error norm = ", l2ErrorNorm(phiCTCS[nt-1,:], phiAnalytic))
    print("CTCS linf error norm = ", lInfErrorNorm(phiCTCS, phiAnalytic))
    
    print("BTCS l2 error norm = ", l2ErrorNorm(phiBTCS, phiAnalytic))
    print("BTCS linf error norm = ", lInfErrorNorm(phiBTCS, phiAnalytic))
    
    print("LaxWendroff l2 error norm = ", l2ErrorNorm(phiLaxWendroff, phiAnalytic))
    print("LaxWendroff linf error norm = ", lInfErrorNorm(phiLaxWendroff, phiAnalytic))

    # Plot the solutions
    font = {'size'   : 16}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, phiOld, label='Initial', color='blue')
    plt.plot(x, phiAnalytic, label='Analytic', color='black', 
             linestyle='--', linewidth=2)
    
    #plt.plot(x, phiFTCS, label='FTCS', color='yellow')
    plt.plot(x, phiFTBS, label='FTBS', color='darkviolet', marker='.')
    plt.plot(x, phiCTCS[nt-1,:], label='CTCS', color='red')
    #plt.plot(x, phiBTCS, label='BTCS', color='blue')
    plt.plot(x, phiLaxWendroff, label ='LW', color ='yellow')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.3,1.6])
    plt.legend(bbox_to_anchor=(0.2, 1), fontsize=8)
    plt.title('Numerical solutions of linear advection equation', fontsize=16)
    plt.xlabel('$x$')
    plt.ylabel('$u$')
#    input('press return to save file and continue')
#    plt.savefig('plots/changeThisName.pdf')
    
    

    font = {'size'   : 16}
    plt.rc('font', **font)
    time = np.linspace(2,(nt-2),(nt-2))
    plt.figure(2)
    plt.clf()
    plt.ion()
    plt.plot(time, TotalVarFTBS_sum, label='FTBS', color='darkviolet', marker='.')
    plt.plot(time, TotalVarCTCS_sum, label='CTCS', color='red', marker='*')
    plt.plot(time, TotalVarLaxWendroff_sum, label='LW', color='yellow', marker ='o')
    #plt.ylim([1.875,2.05])
    plt.legend(bbox_to_anchor=(0.2, 1), fontsize=8)
    plt.title('Total Variation', fontsize=16)
    plt.xlabel('Number of time steps')
    plt.ylabel('$L2 Error$')

### Run the function main defined in this file                      ###
main()


        