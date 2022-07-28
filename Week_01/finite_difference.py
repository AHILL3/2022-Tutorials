# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:10:29 2022

@author: Artie Hill
"""

def forward_difference (f, x, h):
    approx = (f(x + h)-f(x)) / h
    return approx

def func_a(x):
    return x**3