''' 2D Function Minimization '''


import numpy as np
from POLAK_RIBIERE import POLAK_RIBIERE
from RELAX import RELAX
from FLETCHER_REEVES import FLETCHER_REEVES


def main():
    #Give an initial guess for minimizer
    U = np.zeros([1,2])

    #Run three different minimization methods for a given function (see CONT_FUNCS.py to prescribe given function(s))
    #   RELAX() is the relaxation method for approximating the minimizer of a given function
    #   FLETCHER_REEVES() is the so-called Fletcher-Reeves Conjugate Gradient method for approximating the minimizer of a function
    #   POLAK_RIBIERE() is the so-called Polak-Ribiere Conjugate Gradient method for approximating the minimizer of a function 

    #   Each function returns a dictionary with the following labels:
    #   {'Total Iterations','Error','Minimizer','Function Value','Gradient at Minimizer'}

    a = RELAX(U) #assign the return dictionary to the label 'a'
    print('')
    print('--Relaxation Results--')
    #print(a)
    for item in a: 
        print(item,':', a[item])

    b = FLETCHER_REEVES(U) #assign the return dictionary to the label 'b'
    print('')
    print('--Fletcher-Reeves Results--')
    #print(b)
    for item in b: 
        print(item,':', b[item])


    c = POLAK_RIBIERE(U) #assign the return dictionary to the label 'c'
    print('')
    print('--Polak-Ribiere Results--')
    #print(c)
    for item in c: 
        print(item,':', c[item])



if __name__ == "__main__":
    main()