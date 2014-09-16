# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 21:58:31 2014

@author: anders
"""

def grid(size):
    rowA = size * ("+" + 4 * "-") + "+" + "\n"
    rowB = size * ("|" + 4 * " ") + "|" + "\n"
        
    print (size * (rowA + rowB * 4)) + rowA
    
grid(4)