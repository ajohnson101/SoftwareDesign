# -*- coding: utf-8 -*-
"""
Random_art.py

Anders Johnson
Software Design HW4
10/6/14
"""

# you do not have to use these particular modules, but they may help
from random import choice
from random import randint
from random import randrange
import math
from PIL import Image

def build_random_function(min_depth, max_depth, recursion):
   """ 
   This function builds a random equation from lists that contain certain
   building blocks for the random equation.  Once the equation is
   generated, it can be used in the other functions to evaluate the
   equation andmake art!
   """

   # your code goes here
   min_options = ["prod","cos_pi","sin_pi","cube","square"]
   options = ["prod","cos_pi","sin_pi","cube","square","x","y"]
   max_options = ["x","y"]
    
   if recursion < min_depth:
      func = choice(min_options)
      if func == "prod":
         return ["prod", [build_random_function(min_depth, max_depth, recursion+1), build_random_function(min_depth, max_depth, recursion+1)]]
      return [func , build_random_function(min_depth, max_depth, recursion+1)]
   elif recursion >= min_depth and recursion < max_depth:
      func2 = choice(options)
      if func2 == "x" or func2 == "y":
         return [func2]
      if func2 == "prod":
         return ["prod", [build_random_function(min_depth, max_depth, recursion+1), build_random_function(min_depth, max_depth, recursion+1)]]
      return [func2 , build_random_function(min_depth, max_depth, recursion+1)]
   else:
      func3 = choice(max_options)
      return [func3]

       
    
#    ["prod",["a"],["b"]]
#    ["cos_pi",["a"]]
#    ["sin_pi",["a"]]
#    ["a"]
#    ["b"]    
#    ["prod",["cos_pi",["x"]],"sin_pi"]
#    ["prod",["sin_pi",["x"]],"cos_pi"]
    
    

def evaluate_random_function(f, x, y):
   """
   This function is going to be used to call the random equation that was
   generated in the build_random_function equation and evaluate it by
   assigning a value for x and y.
   """

   # your code goes here
   if len(f) == 1:
      if f[0] == "x":
         return x
      else:
         return y



   if f[0] == "cos_pi":
      return math.cos(math.pi*evaluate_random_function(f[1],x,y))
   elif f[0] == "sin_pi":
      return math.sin(math.pi*evaluate_random_function(f[1],x,y))
   elif f[0] == "prod":
      return evaluate_random_function(f[1][0],x,y) * evaluate_random_function(f[1][1],x,y)
   elif f[0] == "cube":
      return evaluate_random_function(f[1],x,y)**3.0
   elif f[0] == "square":
      return evaluate_random_function(f[1],x,y)**2.0
   else:
      print "Invalid function"
      return None




def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
   """
   Maps the input value that is in the interval [input_interval_start, input_interval_end]
   to the output interval [output_interval_start, output_interval_end].  The mapping
   is an affine one (i.e. output = input*c + b).
    
   TODO: please fill out the rest of this docstring
   """
   # your code goes here
   magic = (val - input_interval_start) * (1.0 / (input_interval_end - input_interval_start)) * (output_interval_end - output_interval_start) - output_interval_start

   return magic


def pretty_pictures():
   
   im = Image.new("RGB",(350,350))

   red = build_random_function(2,6,0)
   green = build_random_function(2,6,0)
   blue = build_random_function(2,6,0)

   #print red
   #print green
   #print blue

   for row in range(350):
      for col in range(350):
         red1 = evaluate_random_function(red,remap_interval(row,0,349,-1,1), remap_interval(col,0,349,-1,1))
         green1 = evaluate_random_function(green,remap_interval(row,0,349,-1,1), remap_interval(col,0,349,-1,1))
         blue1 = evaluate_random_function(blue,remap_interval(row,0,349,-1,1), remap_interval(col,0,349,-1,1))

         red2 = remap_interval(red1,-1,1,0,255)
         green2 = remap_interval(green1,-1,1,0,255)
         blue2 = remap_interval(blue1,-1,1,0,255)
         #print red2

         im.putpixel((row,col), (int(red2), int(green2), int(blue2)))

   im.save("my_art"+".png")










    

if __name__=="__main__":
   f = build_random_function(2,6,0)
   #print evaluate_random_function(f,.2,.3)
   #pretty_pictures(f,.2,.3)
   pretty_pictures()
#your additional code and functions go here
