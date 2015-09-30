# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:36:14 2015

@author: claudio
"""

import numpy as np
from pint import UnitRegistry


ureg = UnitRegistry()
Q_ = ureg.Quantity


def computeLiftCoeff(weight_in, Sref_in, v_in, altitude_in, rho_in):
    """
    the funcion computes Cl in steady state conditions (W=L)
    after converting to SI units
    """
    weight = weight_in.to('kg*m/s**2')
    Sref = Sref_in.to('meter**2')
    Vinf = v_in.to('meter / second')
    alt = altitude_in.to('meter')
    rho = rho_in.to('kilogram / meter**3')

    Cl = weight/(0.5*rho*Vinf**2*Sref)

    return Cl
    
def computeMachRe(v_in, a_in, mu_in, lref_in, rho_in):
    """
    Computes Mach and Reynolds numbers
    after converting to SI units
    """
    Vinf = v_in.to('meter / second')
    Ainf = a_in.to('meter / second')
    rho = rho_in.to('kilogram / meter**3')
    mu = mu_in.to('kilogram / meter / second')
    lref = lref_in.to('meter')
    
    return Vinf/Ainf, rho*Vinf*lref/mu