# Some Methods for Unconstrained Minimization

This project allows one to use (and compare) different methods to solve unconstrained minimization problems. The problem considered is of the form

Find (x^*,y^*) \in \R^{2} such that f(x^*,y^*) = inf_{(x,y) \in \R^2} f(x,y).

That is, we wish to find the minimizer of a given function using one of the following methods.
- Relaxation Method for Function Minimization
- Fletcher-Reeves Conjugate Gradient Metho for Function Minimization
- Polak-Ribiere Conjugate Gradient Mehtod for Function Minimization

## Dependencies
Running this project in its totality requires
- python 
- numpy
- scipy

## Quick Start
Using this project is relatively simple. Only two files should be interacted with. First, one will need to write the function which they wish to minimize, its gradient, each of its partial derivatives, and a related auxillary function in the corresponding python functions found in the file CONT_FUNCS.py. Specifications about the inputs and outputs of those functions are given within that file. 

Remark: A few examples of functions which one may wish to minimize have been included. When trying these (and any new functions) one must be very careful that each python function within CONT_FUNCS.py is calculating on the same function of interest.

Once the function of interest and its related functions are in order, everything is run from main.py. As it is set up, running main.py will run each of the above methods to solve the minimization problem and print all of the related results. If one wishes to only run a subset of these methods, simple comment out the undesired methods and their associated print commands from main.py. 

From within the directory, Unconstrained_Min, one may simple run "python main.py" at the terminal. All print commands will display in this terminal.  

## How it Works and Results
Running main.py will call whatever method(s) are indicated within the main() function. From within each of those, the necessary functions within CONT_FUNCS.py are called to compute the minimizer with respect to that method. Each method returns a dictionary of values of interest. Each dictionary is of the following form: {'Total Iterations':int, 'Error':numpy.float64, 'Minimizer':numpy.ndarray, 'Function Value':numpy.float64, 'Gradient at Minimizer':numpy.ndarray}. In its current set up, each of these values is printed for each method. This output can be controlled in main.py.

## Methods

### Relaxation Method for Function Minimization
The relaxation method, as it relates to finding the minimizer of a given function, essentially breaks a n-dimensional global optimization problem into n 1-dimensional global optimization problems. In this project, we only consider n=2. Like all of the methods in the project, it is an iterative method. Unlike the other two methods, it is not considered a member of the Cojugate Gradient family of methods. 

The relaxation method for approximating minimizers to a given 2D function (as presented by Ciarlet in Section 8.4 of Introduction to Numerical Linear Algebra and Optimisation) follows the below procedure.
-   Give intial guess of minimizer and a desired tolerance
-   Iterate over the following:
    - Find the zero/root of the partial derivative of interested function in the first coordinate
    - Update first coordinate of minimizer with this value
    - Find the zero/root of the partial derivative of interested function in the second coordinate
    - Update second coordinate of minimizer with this value 
    - Calculate error and check tolerance
    - If tolerance is achieved, exit iterations
- Output final minimizer

The method depends heavily on the zero/root finding of the partial derivatives in each coordinate in each iteration. This project uses Newton's method to do this zero/root finding step. One should be careful that their function of interest is sufficiently nice so that Newton's method will converge at each instance and that the relaxation method will converge. 


### Fletcher-Reeves Conjugate Gradient Method for Function Minimization
The Flethcer-Reeves Conjugate Gradient Method (F-R) is an example of a so-called gradient method. In particular, it is an example of a conjugate gradient (CG) method. Essentially, gradient methods are iterative methods where each successive estimate of the minimizer is given by the following rule: u_{k+1} = u_{k}-p_{k}*d_{k} where u_{k} is the previous estimate of the minimizer, p_{k} is the step-length, and d_{k} is the search direction which depends of the gradient of the function of interest. The F-R method is unique amongst this family of methods by the way it constructs d_{k}. The search direction in F-R depends explicitly on the quantity \|\nabla f(u_{k})\|^{2} / \|\nabla f(u_{k-1})\|^{2}, where \nabla f is the gradient of the function of interest. 

The Fletcher-Reeves Conjugate Gradient method for approximating minimizers to a given 2D function (as presented by Ciarlet in Section 8.5 of Introduction to Numerical Linear Algebra and Optimisation) follows the below procedure.
- Give intial guess of minimizer
- Compute initial search direction
- Compute optimal initial step size
- Update minimizer
- Iterate over the following:
    - Compute gradient at current minimizer
    - Compute search direction parameter (unique to F-R)
    - Update search direction
    - Compute optimal step size
    - Update minimizer
    - Calculate error and check tolerance
    - If tolerance is achieved, exit iterations
- Output final minimizer

Hidden within the method is a 1-D unconstrained optimization problem. Namely, solving for the optimal step size within each iteration. This is done by applying Newton's method to an auxilliary function which is related to the derivative of the function of interest. Note that a constant step size can be used. One must simply be wise in their choice of step size and understand than the total number of iterations before the tolerance is met may be significantly increased. 

### Polak-Ribiere Conjugate Gradient Method for Function Minimization
The Polak-Ribier Conjugate Gradient Method (P-R) is an example of a so-called gradient method. In particular, it is an example of a conjugate gradient (CG) method (see Fletcher-Reeves for more information). The search direction in P-R depends explicitly on the quantity (\nabla f(u_{k}), \nabla f(u_{k})-\nabla f(u_{k-1}))/\|\nabla f(u_{k-1})\|^{2}, where \nabla f is the gradient of the function of interest and (,) is the dot product. 

The Polak-Ribiere Conjugate Gradient method for approximating minimizers to a given 2D function (as presented by Ciarlet in Section 8.5 of Introduction to Numerical Linear Algebra and Optimisation) follows the same procedure as the Fletcher-Reeves method above. The only difference is how the search direction parameter is compute.

## Considerations
- For now, the project only considers functions of the form f:\R^{2} \rightarrow \R for which all partial derivatives exist.
- One should analyse their function of interest to ensure the existence and uniqueness of a global minimizer in order to interpret the results of these methods correctly. 
- Some methods compute the same values (i.e. initialize the same values). These computations are duplicated so that each method can be run independent of the others. 
- Visualization of the methods should be added.