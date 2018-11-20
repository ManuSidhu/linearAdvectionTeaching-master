#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:47:39 2018

@author: ms1409
"""

#import numpy as np
#
#def CTCS(phiOld, c, nt):
#    "Linear advection of profile in phiOld using CTCS, Courant number c"
#    "for nt time-steps"
#    
#    nx = len(phiOld)
#
#    # new time-step array for phi
#    phi = phiOld.copy()
#    phi2Old = phiOld.copy()
#
#    # FTBS for each time-step
#    for it in range(nt):
#        # Loop through all space using remainder after division (%)
#        # to cope with periodic boundary conditions
#        for j in range(nx):
#            phi[j] = phi2Old[j] - c*\
#                     (phiOld[(j+1)%nx] - phiOld[(j-1)%nx])
#                     
#        
#        # update arrays for next time-step
#        phi2Old = phiOld.copy()
#        phiOld = phi.copy()
#
#    return phi

import numpy as np
from advectionSchemes import *

def CTCS(phiOld, c, nt):
    "Linear advection of profile in phiOld using CTCS, Courant number c"
    "for nt time-steps"
    nx=len(phiOld)
    phi = np.zeros((nt,nx))

    # new time-step array for phi
    phi[0,:] = phiOld.copy()
    phi[1,:] = FTCS(phi[0,:], c, 1)

    # FTBS for each time-step
    for n in range(1, nt-1):
        # Loop through all space using remainder after division (%)
        # to cope with periodic boundary conditions
        for j in range(nx):
            phi[n+1,j] = phi[n-1,j] - c*(phi[n,(j+1)%nx] - phi[n,(j-1)%nx])
                     
    

    return phi