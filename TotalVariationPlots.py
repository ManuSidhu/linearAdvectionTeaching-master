#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:28:09 2018

@author: ms1409
"""

### The matplotlib package contains plotting functions              ###
import matplotlib.pyplot as plt
import numpy as np

# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from initialConditions import *
from advection_schemes import *
from diagnostics import *
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
    phiOld = cosBell(x, 0, 0.75)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)

    # Advect the profile using finite difference for all the time steps
    phiFTCS = FTCS(phiOld.copy(), c, nt)
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
#    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    TotalVarFTBS_sum, TotalVarLaxWendroff_sum, TotalVarCTCS_sum = TotalVar(phiOld.copy(), c, nt)
    
    font = {'size'   : 16}
    plt.rc('font', **font)
    time = np.linspace(2,(nt-2),(nt-2))
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(time, TotalVarFTBS_sum, label='FTBS', color='darkviolet', marker='.')
    plt.plot(time, TotalVarCTCS_sum, label='CTCS', color='red', marker='*')
    plt.plot(time, TotalVarLaxWendroff_sum, label='LW', color='yellow', marker ='o')
    #plt.ylim([1.875,2.05])
    plt.legend(bbox_to_anchor=(0.2, 1), fontsize=8)
    plt.title('Total Variation cosine wave', fontsize=16)
    plt.xlabel('Number of time steps')
    plt.ylabel('$L2 Error$')
      
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
#    phiBTCS = BTCS(phiOld.copy(), c, nt)
    phiLaxWendroff = LaxWendroff(phiOld.copy(), c, nt)
    TotalVarFTBS_sum, TotalVarLaxWendroff_sum, TotalVarCTCS_sum = TotalVar(phiOld.copy(), c, nt)
     
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
    plt.title('Total Variation square wave', fontsize=16)
    plt.xlabel('Number of time steps')
    plt.ylabel('$L2 Error$')

### Run the function main defined in this file                      ###
main()