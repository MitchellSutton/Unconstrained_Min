''' Fletcher-Reeves Conjugate Gradient Method for Approximating Minimizers to 2D Functions '''

#The Fletcher-Reeves conjugate gradient method for approximating minimizers to a given function relys on the following:
#   Give intial guess of minimizer
#   Compute initial search direction
#   Compute optimal initial step size
#   Update minimizer
#   Iterate over the following:
#       Compute gradient at current minimizer
#       Compute search direction parameter (unique to Fletcher-Reeves)
#       Update search direction
#       Compute optimal step size
#       Update minimizer
#       Compute error and check against given tolerance 

import numpy as np 
from scipy import optimize
from numpy import linalg as la
from CONT_FUNCS import f
from CONT_FUNCS import gradf 
from CONT_FUNCS import g


def FLETCHER_REEVES(U):
    #initialize necessary values
    D = np.zeros([1,2]) #array to store search directions
    DF = np.zeros([1,2]) #array to store gradients
    D[0] = gradf(U[0]) #set initial search direction
    p = optimize.newton(g,0,args=(U[0],D[0])) #set initial step size
    U = np.append(U,[U[0]-p*D[0]],axis=0) #store first approximation of minimizer
    k=1 #set iteration counter
    error = 1 #initialize error 
    #iterate method until tolerance is achieved
    while error > 10e-5:
        #calculate and store gradient at previous step
        DF = np.append(DF,[gradf(U[k])],axis=0)
        #calculate search direction parameter according to Fletcher-Reeves
        b = la.norm(gradf(U[k]))**2/la.norm(gradf(U[k-1]))**2
        #update and store search direction according to Fletcher-Reeves
        D = np.append(D,[gradf(U[k]) + b*D[k-1]],axis=0)
        #update step size
        p = optimize.newton(g,0,args=(U[k],D[k]))
        #update and store minimizer
        U = np.append(U, [U[k] -p*D[k]],axis=0)
        #calculate relative error
        error = la.norm(U[k+1]-U[k], ord=np.inf)
        #update iteration counter
        k=k+1
    return {'Total Iterations': k-1 , 'Error': error , 'Minimizer': U[k-1], 'Function Value': f(U[k-1]), 'Gradient at Minimizer': gradf(U[k-1])}