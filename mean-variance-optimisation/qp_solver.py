import cvxpy as cp; 
import numpy as np; 

def qp_solve(mu, Sigma, r):
    """
    Solve:
        min     w.T @ Sigma @ w
        s.t.    w.T @ mu    = r
                1.T @ w     = 1
    """

    mu = np.asarray(mu); 
    Sigma = np.asarray(Sigma); 
    n = len(mu); 

    w = cp.Variable(n); 
    objective = cp.Minimize(cp.quad_form(w, Sigma)); 
    constraints = [
        mu @ w == r,
        cp.sum(w) == 1
    ]; 

    problem = cp.Problem(objective, constraints); 
    problem.solve(); 

    return w.value; 