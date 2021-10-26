''' Continuous Functions '''

#Each of the below functions is a 'continuous' function related to the function which we wish to minimize

#   f() is the function we wish to find the minimizer of 
#   gradf() is the gradient of the function f
#   Df_x() is the partial derivative of f with respect to its first variable (labelled x)
#   Df_y() is the partial derivative of f with respect to its second variable (labelled y)
#   g() is a single variable auxillary function related to the derivative of f in a perturbed variable p

import numpy as np 

def f(u):
    #the function for which to find a minimizer
    #   u should be a 1x2 array
    return u[0]*u[0]*u[0]*u[0] + u[1]*u[1]*u[1]*u[1] + 10*u[0]*u[0] - u[0]*u[1] + u[1]*u[1] - 2*u[0] - 3*u[1]

def gradf(u):
    #gradient of f
    #   u should be a 1x2 array
    return np.array([4*u[0]*u[0]*u[0]+20*u[0]-u[1]-2, 4*u[1]*u[1]*u[1]-u[0]+2*u[1]-3])

def Df_x(x,y):
    #partial derivative of f in the first variable (x)
    #   x should be a real value
    #   y should be a real value
    return 4*x**3+20*x-y-2

def Df_y(y,x):
    #partial derivative of f in the second variable (y)
    #   x should be a real value
    #   y should be a real value
    return 4*y**3-x+2*y-3

def g(p,u,d):
    #g(p) := d/dp[f(u-pd)], the derivative of f(u-pd) with respect to p
    #   p must be a real number (int or float)
    #   u should be a 1x2 array
    #   d should be a 1x2 array

    return 2*d[0] + 3*d[1] - 2*d[1]*(u[1]-p*d[1]) - 20*d[0]*(u[0]-p*d[0]) + d[0]*(u[1] - p*d[1]) + d[1]*(u[0] - p*d[0]) - 4*d[0]*(u[0]-p*d[0])**3 - 4*d[1]*(u[1]-p*d[1])**3
