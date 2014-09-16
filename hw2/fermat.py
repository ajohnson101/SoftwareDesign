# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 23:04:43 2014

@author: anders
"""

def fermat(a,b,c,n):
    if(a**n + b**n == c**2 and n > 2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def user_input():
    a = input("Choose a value for 'a':")
    b = input("Choose a value for 'b':")
    c = input("Choose a value for 'c':")
    n = input("Choose a value for 'n':")
    return a,b,c,n
        
if __name__ == "__main__":
    var = user_input() 
    fermat(var[0],var[1],var[2],var[3])