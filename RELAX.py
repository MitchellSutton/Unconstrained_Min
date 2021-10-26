''' Relaxation Method for Approximating Minimizers to 2D Functions '''

#The relaxation method for approximating minimizers to a given function relys on the following:
#   Give intial guess of minimizer
#   Iterate over the following:
#       Find the zero/root of the partial derivative of interested function in the first coordinate
#       Update first coordinate of minimizer with this value
#       Find the zero/root of the partial derivative of interested function in the second coordinate
#       Update second coordinate of minimizer with this value 
#       Calculate relative error and check against given tolerance

import numpy as np 
from scipy import optimize
from numpy import linalg as la
from CONT_FUNCS import f
from CONT_FUNCS import gradf 
from CONT_FUNCS import Df_x
from CONT_FUNCS import Df_y

def RELAX(U):
    #initialize iteration counter and error
    k=1
    error = 1
    #loop until tolerance is achieved
    while error > 10e-5:
        #create row to write new minimizer estimate
        U = np.append(U,np.zeros([1,2]),axis=0)
        #update minimizer in first coordinate
        U[k,0] = optimize.newton(Df_x,0,args=([U[k-1,1]]))
        #update minimizer in second coordinate
        U[k,1] = optimize.newton(Df_y,0,args=([U[k,0]]))
        #compute relative error
        error = la.norm(U[k]-U[k-1], ord=np.inf)
        #update interation couter
        k = k+1
    return {'Total Iterations': k-1 , 'Error': error , 'Minimizer': U[k-1], 'Function Value': f(U[k-1]), 'Gradient at Minimizer': gradf(U[k-1])}