#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:52:18 2018

@author: ms1409
"""
import numpy as np 
#from FTBS_advectionScheme import *
#from CTCS_advectionscheme import *
#from BTCS_advection import *
#from Lax_Wendroff import *
from advection_schemes import *

def TotalVar(phiOld, c, nt):
    "finding the total variation of each scheme, plotted against time"
    
    nx = len(phiOld)
    
    TotalVarFTBS = np.zeros(nx)
    TotalVarFTBS_sum = np.zeros(nt-2)
    TotalVarCTCS = np.zeros(nx)
    TotalVarCTCS_sum = np.zeros(nt-2)
    TotalVarLaxWendroff = np.zeros(nx)
    TotalVarLaxWendroff_sum = np.zeros(nt-2)
    
    for i in range (2,nt):
        phiFTBS2 = FTBS(phiOld.copy(), c, i)
        phiCTCS2 = CTCS(phiOld.copy(), c, i)
        phiLaxWendroff2 = LaxWendroff(phiOld.copy(), c, i)
        phiCTCS2=phiCTCS2[i-2,:]
        #phiCTCS[nt-1,:]
        for j in range(nx):
            TotalVarFTBS[j] = abs(phiFTBS2[(j+1)%nx] - phiFTBS2[j])
            TotalVarCTCS[j] = abs(phiCTCS2[(j+1)%nx] - phiCTCS2[j])
            TotalVarLaxWendroff[j] = abs(phiLaxWendroff2[(j+1)%nx] - phiLaxWendroff2[j])
            
        TotalVarFTBS_sum[i-2] = sum(TotalVarFTBS)
        TotalVarCTCS_sum[i-2] = sum(TotalVarCTCS)
        TotalVarLaxWendroff_sum[i-2] = sum(TotalVarLaxWendroff)
        
    return TotalVarFTBS_sum, TotalVarLaxWendroff_sum, TotalVarCTCS_sum
    
    