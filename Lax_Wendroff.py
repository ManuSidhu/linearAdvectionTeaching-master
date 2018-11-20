#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:05:38 2018

@author: ms1409
"""

import numpy as np

def LaxWendroff(phiOld, c, nt):
    "Linear advection of profile in phiOld using Lax Wendroff, Courant number c"
    "for nt time-steps"
    
    nx = len(phiOld)

    # new time-step array for phi
    phi = phiOld.copy()

    # FTBS for each time-step
    for it in range(nt):
        # Loop through all space using remainder after division (%)
        # to cope with periodic boundary conditions
        for j in range(nx):
            phi[j] = (c/2)*(c+1)*phiOld[(j-1)%nx] + (1-c**2)*\
                     phiOld[(j)%nx] + (c/2)*(c-1)*phiOld[(j+1)%nx]
                     
        
        # update arrays for next time-step

        phiOld = phi.copy()

    return phi