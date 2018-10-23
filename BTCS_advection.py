#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:45:48 2018

@author: ms1409
"""

import numpy as np
import scipy as sp
import scipy.linalg as la

def BTCS(phiOld, c, nt):
    
    nx = len(phiOld)
    
    
    A = np.zeros((nx, nx))
    
    for i in range (0, nx):
        A[i,i] = 1
    
    for j in range (0, nx-1):
        A[j+1,j] = -c/2
        A[j,j+1] = c/2
        

    A[0,nx-1] = -c/2
    A[nx-1,0] = c/2

    # new time-step array for phi
    phi = phiOld.copy()
    
    # BTCS for each time-step
    for it in range(nt):
        phi = la.solve(A,phi)
                     
        
        # update arrays for next time-step
#        phiOld = phi.copy()

    return phi    


