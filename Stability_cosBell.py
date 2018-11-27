#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:17:23 2018

@author: ms1409
"""

# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from initialConditions import *
from advection_schemes import *
from diagnostics import *
from TotalVar import *

"This programme will look at the 3 stability plots of the squareWave, with different Courant Numbers"

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
    phiOld = cosBell(x, 0, 0.75)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)

    # Advect the profile using finite difference for all the time steps
    phiFTCS = FTCS(phiOld.copy(), c, nt)
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    
    
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
    font = {'size'   : 12}
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
    plt.title('Stability analysis when c = 0.2', fontsize=12)
    plt.xlabel('$x$')
    plt.ylabel('$u$')
#    input('press return to save file and continue')
#    plt.savefig('plots/changeThisName.pdf')
    
    
    # Parameters
    xmin = 0
    xmax = 1
    nx = 80
    nt = 20
    c = 0.8

    # Derived parameters
    dx = (xmax - xmin)/nx
    
    # spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)

    # Initial conditions
    phiOld = cosBell(x, 0, 0.75)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)

    # Advect the profile using finite difference for all the time steps
    phiFTCS = FTCS(phiOld.copy(), c, nt)
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    
    
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
    font = {'size'   : 12}
    plt.rc('font', **font)
    plt.figure(2)
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
    plt.title('Stability analysis when c = 0.8', fontsize=12)
    plt.xlabel('$x$')
    plt.ylabel('$u$')
    
    # Parameters
    xmin = 0
    xmax = 1
    nx = 80
    nt = 10
    c = 1.6

    # Derived parameters
    dx = (xmax - xmin)/nx
    
    # spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)

    # Initial conditions
    phiOld = cosBell(x, 0, 0.75)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)

    # Advect the profile using finite difference for all the time steps
    phiFTCS = FTCS(phiOld.copy(), c, nt)
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
#    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    
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
    font = {'size'   : 12}
    plt.rc('font', **font)
    plt.figure(3)
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
    plt.title('Stability analysis when c = 1.6', fontsize=12)
    plt.xlabel('$x$')
    plt.ylabel('$u$')


### Run the function main defined in this file                      ###
main()