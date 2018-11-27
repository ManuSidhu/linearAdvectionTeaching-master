#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:49:24 2018

@author: ms1409
"""

import matplotlib.pyplot as plt
import numpy as np


# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from initialConditions import *
from advection_schemes import *
from diagnostics import *
from TotalVar import *

def convergence_exp():
    "Experiment to test the convergence of methods as we increase the"
    "reolution"
    n_exp_size = 30  ##number of times we are increasing the spacial and time resolution 
    u = 0.2  #constant wind speed
    xmin = 0
    xmax = 1
    
    ##initialise error and l2error vectors for each of the methods
    l2FTBS_dx_err = np.zeros(n_exp_size)
    l2CTCS_dx_err = np.zeros(n_exp_size)
    l2LaxWendroff_dx_err = np.zeros(n_exp_size)
    errorFTBS = np.zeros(n_exp_size)
    errorCTCS = np.zeros(n_exp_size)
    errorLaxWendroff = np.zeros(n_exp_size)
    
    
    dx_it = np.zeros(n_exp_size)
    
    ##initialise control lines for graph
    delta_x = np.zeros(n_exp_size)
    delta_x2 = np.zeros(n_exp_size)
    
    ##loop for increasing resolution
    for i in range(0,n_exp_size):
        nx = i*10 + 10  ##increasing spacial step
        dx = (xmax - xmin)/nx
        nt = nx ##keeping overall time constant
        dx_it[i] = dx
        c = 0.2*(nx/nt)
     
        
        # spatial points for plotting and for defining initial conditions
        x = np.arange(xmin, xmax, dx)
        
        # Initial conditions
        phiOld = cosBell(x, 0.25, 0.75)
        # Exact solution is the initial condition shifted around the domain
        phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0.25, 0.75)
        
        # Advect the profile using finite difference for all the time steps
        phiFTBS = FTBS(phiOld, c, nt)
        phiCTCS = CTCS(phiOld, c, nt)
        phiLaxWendroff = LaxWendroff(phiOld, c, nt)
        
        ##computing points for control lines 
        delta_x[i] = dx
        delta_x2[i] = dx**2       
        
        ##calculating the l2error for each method
        l2FTBS_dx_err[i] = l2ErrorNorm(phiFTBS, phiAnalytic)
        l2CTCS_dx_err[i] = l2ErrorNorm(phiCTCS[nt-1,:], phiAnalytic)
        l2LaxWendroff_dx_err[i] = l2ErrorNorm(phiLaxWendroff, phiAnalytic)
    
    ##plotting l2 error against increase in dx on a loglog graph
    font = {'size'   : 12}
    plt.figure(1)
    plt.clf()
    plt.loglog(dx_it, l2FTBS_dx_err, label='FTBS', color = 'darkviolet')
    plt.loglog(dx_it, l2CTCS_dx_err, label='CTCS', color = 'red')
    plt.loglog(dx_it, l2LaxWendroff_dx_err, label = 'LW', color = 'yellow')
    plt.loglog(dx_it, delta_x, label='$\Delta x$', linestyle='--', color = 'black')
    plt.loglog(dx_it, delta_x2, label = '$\Delta x^{2}$', linestyle = '--', color = 'blue')
    plt.ylabel('$L_{2}$ error norm')
    plt.xlabel('$\Delta x$')
    plt.legend()
    plt.title('Loglog plot of $L_2$ error norms')
    
    
convergence_exp()